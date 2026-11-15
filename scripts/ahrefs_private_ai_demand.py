#!/usr/bin/env python3
"""
Pull private-AI keyword volumes and month-on-month trends from the Ahrefs API v3.

Requires AHREFS_API_KEY in the environment (Bearer token from Ahrefs → API).

Example:
  export AHREFS_API_KEY='...'
  python3 scripts/ahrefs_private_ai_demand.py --country us
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

API_BASE = "https://api.ahrefs.com/v3/keywords-explorer"

# Seeds aligned with wiki "clean private AI" (confidentiality / self-host / secure).
SEED_KEYWORDS = [
    "private ai",
    "sovereign ai",
    "private ai chatbot",
    "private llm",
    "secure ai",
    "self hosted ai",
    "on premise ai",
    "local llm",
    "offline ai",
    "ai privacy",
    "vpn for ai",
    "encrypted ai",
    "anonymous ai",
    "no logs ai",
    "private chatgpt",
]

# Exclude NSFW / jailbreak demand (Venice competitor wiki).
EXCLUDE_PATTERN = re.compile(
    r"\b("
    r"uncensored|jailbreak|nsfw|porn|nude|nudify|undress|deepfake|"
    r"roleplay|character\.ai|abliterated|sex\b|xxx|hentai"
    r")\b",
    re.I,
)


@dataclass
class KeywordRow:
    keyword: str
    volume: int | None
    difficulty: int | None
    source: str


def api_get(path: str, params: dict[str, str], api_key: str) -> dict:
    q = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = f"{API_BASE}/{path}?{q}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"Ahrefs API {e.code} for {path}: {body}") from e


def discover_matching_terms(
    api_key: str, country: str, seed: str, limit: int
) -> list[KeywordRow]:
    data = api_get(
        "matching-terms",
        {
            "select": "keyword,volume,difficulty",
            "keywords": seed,
            "country": country,
            "match_mode": "terms",
            "terms": "all",
            "limit": str(limit),
            "order_by": "volume:desc",
            "where": "volume>=50",
        },
        api_key,
    )
    rows: list[KeywordRow] = []
    for item in data.get("keywords") or []:
        kw = item.get("keyword") or item.get("keywords")
        if isinstance(kw, list):
            kw = kw[0] if kw else None
        if not kw or EXCLUDE_PATTERN.search(kw):
            continue
        rows.append(
            KeywordRow(
                keyword=str(kw),
                volume=item.get("volume"),
                difficulty=item.get("difficulty"),
                source=f"matching:{seed}",
            )
        )
    return rows


def volume_history(
    api_key: str, country: str, keyword: str, date_from: str, date_to: str
) -> list[tuple[str, int]]:
    data = api_get(
        "volume-history",
        {
            "keyword": keyword,
            "country": country,
            "date_from": date_from,
            "date_to": date_to,
            "output": "json",
        },
        api_key,
    )
    out: list[tuple[str, int]] = []
    for m in data.get("metrics") or []:
        out.append((m["date"][:7], int(m["volume"])))
    return sorted(out)


def mom_changes(history: list[tuple[str, int]]) -> list[tuple[str, int, float | None]]:
    result: list[tuple[str, int, float | None]] = []
    prev: int | None = None
    for month, vol in history:
        mom = None if prev is None or prev == 0 else (vol - prev) / prev * 100
        result.append((month, vol, mom))
        prev = vol
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--country", default="us", help="ISO country code (default: us)")
    parser.add_argument("--months", type=int, default=24, help="History length in months")
    parser.add_argument("--discover-limit", type=int, default=200, help="Max ideas per seed")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("wiki/data/ahrefs"),
        help="Output directory for CSV/JSON",
    )
    parser.add_argument("--sleep", type=float, default=0.35, help="Seconds between API calls")
    args = parser.parse_args()

    api_key = os.environ.get("AHREFS_API_KEY", "").strip()
    if not api_key:
        print("Set AHREFS_API_KEY to your Ahrefs API Bearer token.", file=sys.stderr)
        return 1

    date_to = date.today().replace(day=1) - timedelta(days=1)
    date_from = (date_to.replace(day=1) - timedelta(days=30 * (args.months - 1))).replace(
        day=1
    )
    date_from_s = date_from.isoformat()
    date_to_s = date_to.isoformat()

    args.out_dir.mkdir(parents=True, exist_ok=True)

    # 1) Discover keywords from seeds
    by_kw: dict[str, KeywordRow] = {}
    for seed in SEED_KEYWORDS:
        by_kw[seed] = KeywordRow(keyword=seed, volume=None, difficulty=None, source="seed")
        try:
            for row in discover_matching_terms(
                api_key, args.country, seed, args.discover_limit
            ):
                existing = by_kw.get(row.keyword)
                if existing is None or (row.volume or 0) > (existing.volume or 0):
                    by_kw[row.keyword] = row
        except RuntimeError as e:
            print(f"warn: {e}", file=sys.stderr)
        time.sleep(args.sleep)

    # Keep seeds + top discovered by volume
    discovered = sorted(
        [r for r in by_kw.values() if r.source.startswith("matching")],
        key=lambda r: r.volume or 0,
        reverse=True,
    )[:80]
    track = list({r.keyword for r in ([by_kw[s] for s in SEED_KEYWORDS] + discovered)})

    # 2) Volume history per keyword
    history_dir = args.out_dir / "volume_history"
    history_dir.mkdir(exist_ok=True)
    summary_rows: list[dict] = []

    for kw in track:
        try:
            hist = volume_history(api_key, args.country, kw, date_from_s, date_to_s)
        except RuntimeError as e:
            print(f"warn: {kw}: {e}", file=sys.stderr)
            continue
        if not hist:
            continue

        path = history_dir / f"{kw.replace(' ', '_')}.csv"
        with path.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["month", "volume", "mom_pct"])
            for month, vol, mom in mom_changes(hist):
                w.writerow([month, vol, "" if mom is None else round(mom, 2)])

        latest_vol = hist[-1][1]
        first_vol = hist[0][1]
        yoy = None
        if len(hist) >= 13:
            yoy = (hist[-1][1] - hist[-13][1]) / hist[-13][1] * 100 if hist[-13][1] else None
        mom_last = mom_changes(hist)[-1][2]

        summary_rows.append(
            {
                "keyword": kw,
                "latest_month": hist[-1][0],
                "latest_volume": latest_vol,
                "first_month": hist[0][0],
                "first_volume": first_vol,
                "mom_latest_pct": mom_last,
                "yoy_pct": yoy,
                "source": by_kw.get(kw, KeywordRow(kw, None, None, "history")).source,
            }
        )
        time.sleep(args.sleep)

    summary_rows.sort(key=lambda r: r["latest_volume"], reverse=True)
    summary_path = args.out_dir / f"keyword_summary_{args.country}.json"
    summary_path.write_text(json.dumps(summary_rows, indent=2))

    md_path = args.out_dir / f"search_demand_report_{args.country}.md"
    lines = [
        f"# Private AI search demand ({args.country.upper()})",
        "",
        f"Ahrefs volume history {date_from_s} → {date_to_s}. Generated by `scripts/ahrefs_private_ai_demand.py`.",
        "",
        "## Top keywords by latest monthly volume",
        "",
        "| Keyword | Latest vol | MoM % | YoY % |",
        "|---------|------------|-------|-------|",
    ]
    for r in summary_rows[:40]:
        mom = r["mom_latest_pct"]
        yoy = r["yoy_pct"]
        mom_s = "—" if mom is None else f"{mom:+.1f}"
        yoy_s = "—" if yoy is None else f"{yoy:+.1f}"
        lines.append(
            f"| {r['keyword']} | {r['latest_volume']:,} | {mom_s} | {yoy_s} |"
        )
    md_path.write_text("\n".join(lines) + "\n")

    print(f"Wrote {summary_path}")
    print(f"Wrote {md_path}")
    print(f"Per-keyword CSVs in {history_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
