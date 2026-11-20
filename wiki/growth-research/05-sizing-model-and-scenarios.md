# 5. Sizing model, 10x arithmetic and scenarios

[Back to wiki home](../README.md) · [Back to the main report](00-main-report.md)

Research compiled **20 November 2026**. This page shows the arithmetic behind "10x": what has to be true, what the leaders' numbers imply, and four scenario paths with their inputs.

## How to read the numbers

- Almost everything on this page is an **estimate**. Inputs are listed so each can be replaced with PureVPN's real data.
- **Sourced** inputs carry a link. **Assumption** marks an input with no public source.
- Ranges are deliberately wide. A single number here would be false precision.
- "Annual cycle" is used for growth arithmetic because churn and renewal are annual. These are illustrations of scale. They are not delivery schedules.

## 1. What counts as a customer

"Grow the customer base 10x" can mean three things. They differ by an order of magnitude in difficulty.

| Definition | Today | 10x | Comment |
|---|---|---|---|
| A. People the company calls "users" | 5 million (claim) | 50 million | Reachable only by counting free users and partner end users. Says little about the business |
| B. Paying direct subscribers | About 0.6M (estimate, range 0.3M to 1.2M) | About 6M | More than Surfshark has today. The hardest reading |
| C. Paying relationships: direct subscribers, plus end users a partner pays for, plus buyers of non-VPN products | About 0.6M plus an unknown number of partner users | About 6M | The reading this report recommends |

We recommend **definition C** as the scoreboard, with free monthly users tracked beside it and never added to it. Reasons:

- It counts only people for whom money changes hands, so it cannot be inflated with idle sign-ups.
- It recognises that a person protected through Samsung or a telco is a real customer of the service, though a less valuable one.
- It forces revenue to be reported next to the count, which keeps low-value seats visible.

Because today's partner-paid users are unknown, the baseline for definition C is taken as 0.6M. If PureWL already serves a large paid base, the true starting point is higher and the multiple needed is smaller. That number is the first [internal data request](06-validation-and-risks.md#internal-data-requests).

## 2. The leaders, for scale

| Company | Paying customers | Revenue per paying customer per year | Source |
|---|---|---|---|
| Nord Security | More than 22M (June 2026); more than 15M (September 2025) | About $58 (estimate: $878M of 2024 billings over about 15M) | [Fitch](https://www.fitchratings.com/research/corporate-finance/fitch-affirms-cyberspace-bv-nord-security-idr-at-bb-outlook-stable-20-10-2026), [S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953) |
| Kape (ExpressVPN, CyberGhost, PIA) | 7.4M (end of 2022) | About $85 (estimate: $623.5M over 7.4M, including non-VPN revenue) | [Kape 2022 results](https://pdf.dfcfw.com/pdf/H22_AN202303211584441241_1.pdf) |
| Surfshark | 4M (February 2026) | About €37 (estimate: €149M of 2024 revenue over 4M) | [LinkedIn post](https://www.linkedin.com/posts/regimantasurbanas_if-you-invest-in-stocks-would-you-consider-activity-7434851400632868864-xOYF) |
| Aura (identity protection) | 1.1M direct | About $199 ($16.61 a month) | [Aura Q3 2026](https://www.aura.com/press/release/third-quarter-2026-financial-results), [Software & Capital](https://softwareandcapital.com/articles/aura-digital-safety-subscription-economics) |
| Mullvad | About 0.57M (estimate) | €60 (flat price) | [rating.se](https://www.rating.se/info1/detail/numbers/5592384001), [Mullvad](https://mullvad.net/en/help/no-logging-data-policy) |
| Proton | Not disclosed | Not disclosed. More than $100M of revenue | [Dealroom](https://app.dealroom.co/news/note/proton-100m-revenues-still-no-valuation-on-file) |
| PureVPN | About 0.6M (estimate) | $35 to $60 (estimate) | [Baseline page](01-purevpn-baseline.md) |

- Total paying consumer VPN users: 60 to 120 million (estimate, [market page](02-market-and-demand.md#how-many-people-pay)).
- PureVPN's share today: 0.5% to 1%. At 6 million direct subscribers it would be 5% to 10%.
- Six million direct subscribers would make PureVPN larger than Surfshark, close to the whole Kape group at its last disclosure, and more than a quarter of Nord Security.

## 3. What 10x of direct subscribers would require

A subscriber base follows one rule: next year's base equals this year's base, less the share that leaves, plus new sign-ups.

| Input | Value | Source |
|---|---|---|
| Starting base | 0.6M | Estimate |
| Target | 6.0M | 10x |
| Annual churn | 30% in the centre; 21% and 40% as bounds | Assumption. Nord retains 79% of users ([Fitch](https://www.fitchratings.com/research/corporate-finance/fitch-affirms-cyberspace-bv-nord-security-idr-at-bb-outlook-stable-20-10-2026)); the median subscription app retains 27% to 28% of yearly subscribers after 12 months ([RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)). PureVPN's own rate is unknown |

| If 10x takes this many annual cycles | Growth needed each cycle | New sign-ups needed in total (30% churn) | New sign-ups needed in the final cycle |
|---|---|---|---|
| 4 | 78% | 7.5M | 3.6M |
| 5 | 58% | 8.2M | 3.4M |
| 7 | 39% | 9.6M | 3.0M |

At 21% churn the five-cycle total is 7.3M. At 40% it is 9.1M. Once at 6 million, standing still takes 1.3M to 2.4M new sign-ups a year.

**How that compares.**

- Nord Security's net billings grew 29% in the year to June 2026, and Fitch forecasts 21% a year for 2025 to 2028 ([Fitch](https://www.fitchratings.com/research/corporate-finance/fitch-affirms-cyberspace-bv-nord-security-idr-at-bb-outlook-stable-20-10-2026)). The consumer VPN market grows about 15% to 16% ([market page](02-market-and-demand.md)). PureVPN would need to grow about two to four times faster than the leader is forecast to grow, for several cycles in a row.
- Kape added 791,000 net subscribers in 2022 across three large brands while paying $233M for marketing ([Kape 2022 results](https://pdf.dfcfw.com/pdf/H22_AN202303211584441241_1.pdf)). The plan above needs about 3 million gross sign-ups in its last cycle from one mid-sized brand.
- Nord Security needs roughly 9 to 11 million gross sign-ups a year (estimate: 21% churn on about 18.5M, plus 5M to 7M of net growth). PureVPN would have to reach a third of that while its US brand search volume is one fifty-sixth of NordVPN's (5,400 against 301,000, [baseline page](01-purevpn-baseline.md#7-traffic-and-acquisition-mix)).

**What it would cost through paid channels.**

| Cost per new subscriber | Basis | Total for 8.2M sign-ups | Final cycle (3.4M sign-ups) |
|---|---|---|---|
| $40 | 40% affiliate commission on a $93.87 five-year order is $37.55 ([affiliates](https://www.purevpn.com/affiliates), [order page](https://www.purevpn.com/order)) | $330M | $135M |
| $90 | Our estimate for Kape in 2022 ([market page](02-market-and-demand.md#6-review-sites-and-affiliate-economics)) | $740M | $300M |

The $40 row is a floor, not a forecast. Commission-only channels cap out at the number of buyers who click a PureVPN link, and the review sites that send most of those clicks rank better-known brands first. Buying the rest through search and sponsorships costs more. Against estimated revenue of $21M to $36M a year, neither row can be financed from the business.

**Conclusion.** Ten times the direct subscriber base, reached by doing what Nord, Surfshark and Kape did, is not a credible plan for PureVPN. This is a statement about channel capacity and capital. It is not a statement about product quality.

## 4. Four scenario paths

Each path is described at a mature steady state. "Paying relationships" follows definition C.

### Path A. Freemium-led

A free tier drives installs; a share converts to paid.

| Input | Low | Centre | High | Source |
|---|---|---|---|---|
| Free-tier installs a year | 10M | 25M | 40M | Assumption. 50 tracked VPN apps had 412M downloads in 2025 ([Cybernews](https://cybernews.com/best-vpn/vpn-usage-by-country/)) |
| Installs that pay within five weeks | 0.7% | 1.5% | 2.1% | [RevenueCat via The Social Outline](https://thesocialoutline.com/blog/download-to-paid-conversion-rate-benchmarks): 0.7% is the median in India and South East Asia, 2.1% the median freemium app |
| New payers a year | 70,000 | 375,000 | 840,000 | Calculated |
| Annual churn of those payers | 35% | 35% | 35% | Assumption |
| Payers sustained by the free tier | 0.2M | 1.1M | 2.4M | New payers divided by churn |
| Plus today's base, held flat | 0.6M | 0.6M | 0.6M | Estimate |
| **Paying relationships** | **0.8M** | **1.7M** | **3.0M** | |
| **Multiple of today** | **1.3x** | **2.8x** | **5.0x** | |
| Free monthly users | 5M | 10M | 20M | Assumption |
| Cost of free users a year | $3M | $12M | $48M | Assumption: $0.05, $0.10 and $0.20 per free user per month |

Reaching 10x through the free tier alone would need 390 to 820 million installs in total (8.2M sign-ups at 2.1% and 1% conversion). Proton VPN has 140 million Android downloads after years as the best-known free VPN ([Chrome-Stats](https://chrome-stats.com/a/NzY3MjQ3OTcwNjU1ODUyNjY0Nw)).

**Verdict.** Freemium gets to 10x on definition A (users). It gets to about 3x on paying customers, with real cost and risk.

### Path B. Partner-led (B2B2C)

Partners include PureVPN's service in their own plans and pay per active user.

| Input | Low | Centre | High | Source |
|---|---|---|---|---|
| Anchor partners and active users each | 1 at 0.6M | 3 at about 0.9M | 4 at about 1.2M | Assumption. One white-label deal of about 1M users is on record ([Pulse 2.0](https://pulse2.com/point-wild-profile-neill-feather-interview/)) |
| Mid-sized and small partners, total active users | 0.4M | 0.8M | 1.2M | Assumption. PureWL claims 150+ partners ([PureWL](https://www.purewl.com/white-label-vpn-business/)) |
| Partner-paid active users | 1.0M | 3.5M | 6.0M | Calculated |
| Plus today's direct base, held flat | 0.6M | 0.6M | 0.6M | Estimate |
| **Paying relationships** | **1.6M** | **4.1M** | **6.6M** | |
| **Multiple of today** | **2.7x** | **6.8x** | **11x** | |
| Wholesale revenue a year | $4M | $21M | $48M | Assumption: $0.33, $0.50 and $0.67 per active user per month |

The [catalog](04-opportunity-catalog.md#1-partner-distribution-platform) shows the same shape before any shortfall: three anchors at 1.0M, 20 mid-sized partners at 40,000 and 150 small ones at 2,000 give 4.1M.

**Verdict.** This is the only single path on which the high case passes 10x. It does so with low revenue per customer and heavy dependence on a handful of contracts.

### Path C. Category-expansion-led

New products with their own front doors (travel eSIM, private AI, short passes) bring in people who did not come for a VPN. A stronger bundle improves retention.

| Input | Low | Centre | High | Source |
|---|---|---|---|---|
| Direct VPN subscribers after bundle and retention gains | 0.6M | 0.9M | 1.2M | Estimate |
| eSIM buyers a year | 0.1M | 0.4M | 1.0M | [Catalog, item 9](04-opportunity-catalog.md#9-travel-esim-with-its-own-front-door) |
| Private-AI subscribers who are not VPN subscribers | 0.03M | 0.1M | 0.2M | The wiki's year-five base case is 190,000 in total ([financial model](../02-financial-model.md)) |
| Short-pass buyers and developer accounts | 0.07M | 0.2M | 0.3M | Assumption |
| **Paying relationships** | **0.8M** | **1.6M** | **2.7M** | |
| **Multiple of today** | **1.3x** | **2.7x** | **4.5x** | |

For comparison, Saily reached about 4 million users in two years, but with Nord's marketing engine behind it ([PEGN](https://revistapegn.globo.com/startups/noticia/2026/02/como-este-app-nascido-dentro-de-um-unicornio-cresceu-4x-em-um-ano.ghtml)).

**Verdict.** Useful, and the best route to revenue per customer. Not a route to 10x.

### Path D. Combined, distribution first (recommended)

Partners carry the count. A trust reset, an emerging-market offer and a staged free tier grow the direct base. New products add buyers and revenue.

| Line | Low | Centre | High | How the centre is built |
|---|---|---|---|---|
| Direct subscribers | 0.9M | 1.5M | 2.2M | 0.6M today, plus 0.2M from lower churn and better ratings, plus 0.5M from the emerging-market offer and free tier, plus 0.2M from bundle and affiliate gains |
| Partner-paid active users | 1.0M | 3.5M | 6.0M | Path B |
| New-product buyers | 0.2M | 0.7M | 1.5M | Path C: eSIM 0.4M, private AI 0.1M, passes and developers 0.2M |
| **Paying relationships** | **2.1M** | **5.7M** | **9.7M** | |
| **Multiple of today (0.6M)** | **3.5x** | **9.5x** | **16x** | |
| Revenue a year | $45M | $110M | $210M | Direct at $40, $45 and $50 a year; partner users at $4, $6 and $8; new-product buyers at $25, $30 and $35. All assumptions |
| Multiple of today's revenue ($21M to $36M) | 1.3x to 2.1x | 3x to 5x | 6x to 10x | |
| Free monthly users, not counted above | 2M | 5M | 10M | Assumption: roughly half of Path A's figures, because the tier is staged by market. At $0.10 per user per month that costs about $2M, $6M and $12M a year |

Notes on the centre:

- The free tier contributes about half of its stand-alone centre here, because it launches only after the trust reset and only in selected markets.
- Direct subscribers grow 2.5 times. Mullvad grew revenue about four-fold in four years on trust alone ([rating.se](https://www.rating.se/info1/detail/numbers/5592384001)), so growth of that order has a precedent.
- Sixty per cent of the centre's count is partner-paid. If no anchor partner is won, the path delivers the low case.

## 5. Which path we believe

**Path D, with the partner line as the deciding variable.**

| Outcome | Our judgment of likelihood | What has to happen |
|---|---|---|
| 10x or more paying relationships (6M+) | About 25% to 35% | At least three anchor partners that include the service in their plans, plus the direct base more than doubling |
| 5x or more (3M+) | About 60% | One or two anchor partners, or a free tier that converts near the median |
| Under 3x | About 25% | No anchor partner and a free tier that does not convert or is too costly to run |
| 10x direct subscribers (6M) | Under 5% | Would need Nord-scale marketing capital and brand |

These likelihoods are judgment, not calculation. They are stated so they can be challenged.

Why we believe it:

1. It is the only path whose high case reaches 10x without assuming PureVPN outspends or outgrows the market leader.
2. It rests on an asset PureVPN already has and most rivals of its size do not: a working white-label platform with a named device-maker customer.
3. Its failure mode is tolerable. If partners do not come, the trust reset and the emerging-market offer still improve the direct business.

Why it might be wrong is set out in the [risks page](06-validation-and-risks.md#risks-and-counterarguments).

## 6. Sensitivities

| If this input changes | Effect on the Path D centre (5.7M) |
|---|---|
| Baseline is 0.3M, not 0.6M | The count falls to about 5.4M, but the multiple rises to 18x because the starting point is smaller |
| Baseline is 1.2M, not 0.6M | The count rises to about 6.3M and the multiple falls to about 5x |
| PureWL already has 1M partner-paid users | The honest baseline is 1.6M and the centre is about 3.6x |
| Only one anchor partner is won | Partner users fall to about 1.7M; the total is about 3.9M, or 6.5x |
| Free-tier conversion is 0.7%, not 1.5% | Direct subscribers fall by about 0.3M; the total is about 5.4M |
| Annual churn is 40%, not 30% to 35% | Direct subscribers fall by about 0.3M |
| Wholesale price is $0.30 a month, not $0.50 | The count is unchanged; revenue falls by about $8M |

The baseline matters more than any other input. Establishing it is the first action in the [validation plan](06-validation-and-risks.md).

## 7. Link to the private AI model

The [private AI financial model](../02-financial-model.md) plans for 190,000 paying AI subscribers and $71M of recurring revenue in year five. Set against this page:

- By count, private AI is about 3% of a 6 million target. It is not a 10x lever.
- By revenue, it could be the largest single line: $71M against the $110M centre of Path D for everything else.
- The two plans share a dependency. Both assume PureVPN's base can be cross-sold. A base of 0.6M rather than 1M cuts the attach-rate revenue on [the market research page](../07-market-research.md) by 40%. Partner distribution could restore it, if the AI assistant is offered as a module in the partner kit.

## Open gaps

- PureVPN's paying base, churn, revenue per subscriber and partner-paid users would replace most assumptions on this page.
- There is no public benchmark for wholesale VPN price per user.
- Free-user serving cost is an assumption that swings Path A from affordable to ruinous.
