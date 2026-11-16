#!/usr/bin/env python3
"""Convert grok/canvas JSX exports to Markdown."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def strip_wrapper(text: str) -> str:
    text = re.sub(r"^<cursor_untrusted_data[^>]*>\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"</cursor_untrusted_data_1337>\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r'^Canvas "[^"]+" \([^)]+\):\s*\n', "", text)
    return text


def unescape(s: str) -> str:
    return s.replace('\\"', '"').replace("\\n", "\n")


def parse_string_list(blob: str) -> list[str]:
    return [unescape(x) for x in re.findall(r'"((?:\\.|[^"\\])*)"', blob)]


def table_md(block: str) -> str:
    cm = re.search(r"columns=\{(\[[\s\S]*?\])\}", block)
    rm = re.search(r"rows=\{(\[[\s\S]*?\])\s*\}", block)
    if not cm or not rm:
        return ""
    cols = parse_string_list(cm.group(1))
    rows_raw = rm.group(1)
    row_blocks = re.findall(r"\[([\s\S]*?)\]", rows_raw)
    lines = [
        "| " + " | ".join(cols) + " |",
        "| " + " | ".join("---" for _ in cols) + " |",
    ]
    for rb in row_blocks:
        cells = re.findall(r'"((?:\\.|[^"\\])*)"', "[" + rb + "]")
        cells = [unescape(c) for c in cells]
        while len(cells) < len(cols):
            cells.append("")
        lines.append("| " + " | ".join(cells[: len(cols)]) + " |")
    return "\n".join(lines) + "\n\n"


def bullet_md(block: str) -> str:
    im = re.search(r"items=\{(\[[\s\S]*?\])\s*\}", block)
    if not im:
        return ""
    items = parse_string_list(im.group(1))
    return "\n".join(f"- {i}" for i in items) + "\n\n"


def properties_md(block: str) -> str:
    items = re.findall(
        r'label:\s*"([^"]+)",\s*value:\s*"((?:\\.|[^"\\])*)"',
        block,
    )
    return "\n".join(f"- **{l}:** {unescape(v)}" for l, v in items) + "\n\n"


def rows_md(block: str) -> str:
    chunks = re.findall(
        r"\{\s*meta:\s*\"([^\"]*)\",\s*title:\s*\"([^\"]*)\",\s*detail:\s*\"((?:\\.|[^\"\\])*)\"\s*\}",
        block,
    )
    if not chunks:
        chunks = [
            ("", t, unescape(d))
            for t, d in re.findall(
                r"\{\s*title:\s*\"([^\"]*)\",\s*detail:\s*\"((?:\\.|[^\"\\])*)\"\s*\}",
                block,
            )
        ]
    out = []
    for meta, title, detail in chunks:
        detail = unescape(detail)
        if meta:
            out.append(f"### {meta} — {title}\n\n{detail}\n")
        else:
            out.append(f"### {title}\n\n{detail}\n")
    return "\n".join(out) + "\n"


def quote_md(block: str) -> str:
    cite = re.search(r'cite="([^"]+)"', block)
    body = re.search(r">\s*([\s\S]*?)\s*</Quote>", block)
    if not body:
        return ""
    q = body.group(1).strip()
    c = cite.group(1) if cite else ""
    return f"> {q}\n>\n> — {c}\n\n"


def pros_cons_md(block: str) -> str:
    out = []
    pm = re.search(r"pros=\{\[([\s\S]*?)\]\}", block)
    cm = re.search(r"cons=\{\[([\s\S]*?)\]\}", block)
    if pm:
        out.append("**Strengths**\n")
        out.extend(f"- {unescape(p)}" for p in parse_string_list(pm.group(1)))
        out.append("")
    if cm:
        out.append("**Weaknesses**\n")
        out.extend(f"- {unescape(c)}" for c in parse_string_list(cm.group(1)))
        out.append("")
    return "\n".join(out) + "\n"


def line_chart_md(block: str) -> str:
    lm = re.search(r"labels=\{\[\"([^\"]+)\"\]\}", block)
    label = lm.group(1) if lm else "Series"
    pts = re.findall(r'label:\s*"([^"]+)",\s*value:\s*([\d.]+)', block)
    lines = [f"*{label} (data table):*", "", "| Period | Value |", "| --- | --- |"]
    for pl, pv in pts:
        lines.append(f"| {pl} | {pv} |")
    return "\n".join(lines) + "\n\n"


def link_cards_md(block: str) -> str:
    links = re.findall(
        r"title:\s*\"([^\"]*)\"[^}]*?(?:site:\s*\"([^\"]*)\",\s*)?(?:date:\s*\"([^\"]*)\",\s*)?href:\s*\"([^\"]*)\"",
        block,
    )
    out = []
    n = 1
    for title, site, date, href in links:
        meta = ", ".join(x for x in (site, date) if x)
        suffix = f" ({meta})" if meta else ""
        out.append(f"{n}. [{title}]({href}){suffix}")
        n += 1
    return "\n".join(out) + "\n\n"


def matrix_venn_md(block: str) -> str:
    out = []
    if "Matrix2x2" in block:
        pts = re.findall(r'label:\s*"([^"]+)"', block)
        if pts:
            out.append(
                "*Recommended moves (effort vs impact matrix from canvas):* "
                + "; ".join(pts)
                + "\n\n"
            )
    if "Venn" in block:
        sets = re.findall(r'label:\s*"([^"]+)"', block)
        overlap = re.search(r'overlap="([^"]+)"', block)
        item_blocks = re.findall(r"items:\s*\[([\s\S]*?)\]", block)
        out.append("**Audience overlap**\n\n")
        for i, s in enumerate(sets[:2]):
            out.append(f"- **{s}:**")
            if i < len(item_blocks):
                for it in parse_string_list(item_blocks[i]):
                    out.append(f"  - {it}")
        if overlap:
            out.append(f"- **Overlap:** {overlap.group(1)}")
        out.append("")
    return "\n".join(out) + "\n"


SEGMENT_LABELS = {
    "overview": "Overview",
    "scale": "Scale",
    "token": "Token",
    "product": "Product",
    "company": "Proton (company)",
    "privacy": "Privacy peers",
    "mainstream": "Mainstream assistants",
}


def segmented_tables_md(body: str) -> str:
    if "<Segmented" not in body and "facts ===" not in body and "comp ===" not in body:
        return ""
    out = []
    seen_tables: set[str] = set()
    for key, label in SEGMENT_LABELS.items():
        marker = f'=== "{key}"'
        if marker not in body:
            continue
        idx = body.index(marker)
        chunk = body[idx : idx + 15000]
        tm = re.search(r"<Table[\s\S]*?/>", chunk)
        if tm:
            tmd = table_md(tm.group(0))
            if tmd not in seen_tables:
                seen_tables.add(tmd)
                out.append(f"#### {label}\n\n{tmd}")
    return "".join(out)


COMPONENT_PATTERNS: list[tuple[str, str]] = [
    ("section", r'<Section heading="([^"]+)"(?:\s+id="([^"]*)")?(?:\s+caption="([^"]*)")?\s*>'),
    ("text", r"<Text>\s*([\s\S]*?)\s*</Text>"),
    ("table", r"<Table[\s\S]*?/>"),
    ("bullet", r"<BulletList[\s\S]*?/>"),
    ("props", r"<Properties[\s\S]*?/>"),
    ("rows", r"<Rows[\s\S]*?/>"),
    ("quote", r"<Quote[\s\S]*?</Quote>"),
    ("proscons", r"<ProsCons[\s\S]*?/>"),
    ("linechart", r"<LineChart[\s\S]*?/>"),
    ("linkcards", r"<LinkCards[\s\S]*?/>"),
    ("matrix", r"<Matrix2x2[\s\S]*?/>"),
    ("venn", r"<Venn[\s\S]*?/>"),
]


def find_components(body: str, skip_nested_sections: bool = True) -> list[tuple[int, str, re.Match]]:
    found: list[tuple[int, str, re.Match]] = []
    for kind, pat in COMPONENT_PATTERNS:
        if kind == "section" and skip_nested_sections:
            continue
        for m in re.finditer(pat, body):
            found.append((m.start(), kind, m))
    found.sort(key=lambda x: x[0])
    # dedupe overlapping (prefer longer matches at same pos - not needed with distinct tags)
    return found


def render_component(kind: str, m: re.Match) -> str:
    if kind == "text":
        return m.group(1).strip() + "\n\n"
    block = m.group(0)
    handlers = {
        "table": table_md,
        "bullet": bullet_md,
        "props": properties_md,
        "rows": rows_md,
        "quote": quote_md,
        "proscons": pros_cons_md,
        "linechart": line_chart_md,
        "linkcards": link_cards_md,
        "matrix": matrix_venn_md,
        "venn": matrix_venn_md,
    }
    return handlers.get(kind, lambda b: "")(block)


def render_block(body: str, depth: int = 3) -> str:
    out: list[str] = []
    if depth == 3 and segmented_tables_md(body):
        out.append(segmented_tables_md(body))

    pos = 0
    while pos < len(body):
        if body[pos:].startswith("</Section>"):
            pos += len("</Section>")
            continue

        sec_m = re.match(
            r'<Section heading="([^"]+)"(?:\s+id="([^"]*)")?(?:\s+caption="([^"]*)")?\s*>',
            body[pos:],
        )
        if sec_m:
            h = "#" * min(6, depth)
            out.append(f"{h} {sec_m.group(1)}\n\n")
            if sec_m.group(3):
                out.append(f"*{sec_m.group(3)}*\n\n")
            inner, end = take_balanced_section(body, pos + sec_m.end())
            out.append(render_block(inner, depth + 1))
            pos = end
            continue

        matched = False
        for kind, pat in COMPONENT_PATTERNS:
            if kind == "section":
                continue
            m = re.match(pat, body[pos:])
            if m:
                out.append(render_component(kind, m))
                pos += m.end()
                matched = True
                break

        if not matched:
            nxt = re.search(
                r"(<Text>|<Table |<BulletList|<Properties|<Rows|<Quote|<ProsCons|<LineChart|<LinkCards|<Section |</Section>)",
                body[pos + 1 :],
            )
            pos = pos + 1 + nxt.start() if nxt else len(body)

    return "".join(out)


def take_balanced_section(text: str, start: int) -> tuple[str, int]:
    depth = 1
    i = start
    inner_start = start
    while i < len(text) and depth > 0:
        open_m = re.search(r"<Section\s", text[i:])
        close_m = re.search(r"</Section>", text[i:])
        if not close_m:
            break
        if open_m and open_m.start() < close_m.start():
            depth += 1
            i += open_m.end()
        else:
            close_pos = i + close_m.start()
            depth -= 1
            if depth == 0:
                return text[inner_start:close_pos], i + close_m.end()
            i += close_m.end()
    return text[inner_start:], len(text)


def find_page_bounds(content: str) -> str:
    m = re.search(r"<Page[\s\S]*?>", content)
    if not m:
        return content
    start = m.end()
    end = content.rfind("</Page>")
    return content[start:end] if end > start else content[start:]


def convert(content: str, back_link: str) -> str:
    content = strip_wrapper(content)
    title_m = re.search(r'title="([^"]+)"', content)
    summary_m = re.search(r'summary="([^"]+)"', content)
    title = title_m.group(1) if title_m else "Report"
    summary = unescape(summary_m.group(1)) if summary_m else ""

    lines = [
        f"# {title}",
        "",
        f"[Back to wiki home]({back_link})",
        "",
        "**Research date:** 16 November 2026 (Asia/Dubai).",
        "",
        summary,
        "",
    ]

    callout = re.search(
        r'<Callout lead="([^"]+)">\s*([\s\S]*?)\s*</Callout>', content
    )
    if callout:
        lines.append(
            f"> **{callout.group(1)}** {callout.group(2).strip()}\n"
        )
        lines.append("")

    toc_m = re.search(r"<TableOfContents\s+items=\{(\[[\s\S]*?\])\s*\}", content)
    if toc_m:
        items = re.findall(r'label:\s*"([^"]+)",\s*id:\s*"([^"]+)"', toc_m.group(1))
        lines.append("## Contents\n")
        for label, sid in items:
            lines.append(f"- [{label}](#{sid})")
        lines.append("")

    page_body = find_page_bounds(content)
    sec_re = re.compile(
        r'<Section heading="([^"]+)"\s+id="([^"]+)"(?:\s+caption="([^"]*)")?\s*>'
    )
    pos = 0
    while True:
        m = sec_re.search(page_body, pos)
        if not m:
            break
        heading, sid, caption = m.group(1), m.group(2), m.group(3)
        inner, end = take_balanced_section(page_body, m.end())
        lines.append(f'<a id="{sid}"></a>\n\n## {heading}\n')
        if caption:
            lines.append(f"*{unescape(caption)}*\n")
        lines.append(render_block(inner))
        pos = end

    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: canvas_to_markdown.py <input> <output.md>")
        sys.exit(1)
    inp, outp = Path(sys.argv[1]), Path(sys.argv[2])
    back = "../README.md"
    outp.parent.mkdir(parents=True, exist_ok=True)
    md = convert(inp.read_text(encoding="utf-8"), back)
    outp.write_text(md, encoding="utf-8")
    print(f"Wrote {outp} ({len(md)} chars, {md.count(chr(10))} lines)")


if __name__ == "__main__":
    main()