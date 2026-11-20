# Private AI Platform: Feasibility Wiki

Research and planning notes for a Venice.ai-style private AI platform (text chat, image generation and code on open-weight models, with no server-side conversation storage), extended with a Tab-style **agent mode** that plans multi-step tasks, browses the web, calls tools and runs code in sandboxes.

The company is assumed to be based in the UAE.

## Pages

| Page | What it covers |
|---|---|
| [1. Product overview](01-product-overview.md) | What we are building, tiers and pricing, privacy modes |
| [2. Financial model](02-financial-model.md) | 5-year model: assumptions, revenue, unit economics, costs, P&L, funding, sensitivities |
| [3. Hosting strategy](03-hosting-strategy.md) | Managed versus self-hosted inference, recommended stack and phased plan |
| [4. Provider comparison](04-provider-comparison.md) | Cost, content-policy limits and privacy terms for each provider |
| [5. Content policy and trust & safety](05-content-policy-and-trust-safety.md) | Handling sexual content and blocking child abuse material without breaking the privacy promise |
| [6. Legal risks](06-legal-risks.md) | UAE, international and product-level legal risks with mitigations |
| [7. Market size, growth, players and the pain](07-market-research.md) | How big the clean private-AI market is, how fast it is growing, who sells into it, and the pain buyers pay to remove |
| [8. Briefing for market research](08-researcher-brief.md) | Standalone brief: the product, the pains, the segments and the packaging, with each figure tagged as a decision, a model assumption or an estimate |
| [9. GPU cloud provider value research](09-gpu-cloud-provider-value-research.md) | 17 GPU/infra providers for self-host: AUP, H100 pricing, privacy posture, Primary/Secondary/Overflow/Avoid fit (15 Nov 2026) |
| [10. Provider value offering comparison](10-provider-value-offering.md) | Full value-offering matrix for every listed private/uncensored and GPU host (15 Nov 2026) |

## Competitor research

| Document | What it covers |
|---|---|
| [Venice.ai competitor analysis](competitor-research/venice-ai.md) | Venice's customer acquisition, adult-content exclusions, "VPN for AI" landscape, developer vs consumer revenue split and clean addressable market for PureVPN |

## Growth research

A separate, wider question: how PureVPN could grow its customer base ten-fold through product innovation. Compiled 20 November 2026. The private AI product above is one of 21 opportunities assessed.

| Page | What it covers |
|---|---|
| [Main report: growing PureVPN's customer base 10x](growth-research/00-main-report.md) | Executive summary, the 10x arithmetic in one table, recommended bets, and all eight sections in short form |
| [1. PureVPN baseline](growth-research/01-purevpn-baseline.md) | Ownership, estimated paying subscribers and revenue, products, pricing, audits, reviews, traffic and geography |
| [2. Market and demand structure](growth-research/02-market-and-demand.md) | Market size and why figures disagree, reasons to buy, regulatory shocks through 2026, platform threats, review-site and affiliate economics |
| [3. Competitor product strategy teardown](growth-research/03-competitor-teardown.md) | What Nord, Surfshark, Proton, ExpressVPN, Mullvad and others launched, the evidence it added customers, and what failed |
| [4. Product innovation opportunity catalog](growth-research/04-opportunity-catalog.md) | 21 opportunities sized and scored, split into those that add customers and those that add value per customer |
| [5. Sizing model, 10x arithmetic and scenarios](growth-research/05-sizing-model-and-scenarios.md) | What 10x requires, comparisons with the leaders, four scenario paths and sensitivities |
| [6. Validation plan, internal data requests and risks](growth-research/06-validation-and-risks.md) | Cheapest experiments with thresholds, 20 internal data requests, and the case against the recommendation |
| [7. Sources and method](growth-research/07-sources.md) | Every source by topic, tools that were and were not available, and claims resting on weak evidence |

## Interactive model

The full financial model is an interactive canvas where every assumption can be edited:
[Venice-style AI + Agent Mode: 5-Year Financial Model](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/1e8b646a-bc93-4ead-8979-f9cbca57dec3).
The numbers in this wiki are the canvas's base-case defaults.

Market size, growth, players and the priced pain are charted in [Private AI market conviction](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/aec17bb6-1105-47ee-a759-639826c83eff). The write-up is [page 7](07-market-research.md).

The document to send a market researcher is [page 8](08-researcher-brief.md). It collects the product, the pains, the segments and the packaging from the rest of the wiki.

Provider value offerings across confidential AI, open APIs, frontier ZDR and GPU clouds are in [page 10](10-provider-value-offering.md) and the [interactive matrix](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/51ed0eb0-5eaf-491e-819c-e0f54a868022).

## Status and caveats

- Prices and provider policies: short tables refreshed **15 November 2026** ([pages 4](04-provider-comparison.md), [9](09-gpu-cloud-provider-value-research.md), [10](10-provider-value-offering.md)). Both change often, so re-check before signing contracts.
- Interactive provider value matrix: [Private AI provider value offering](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/51ed0eb0-5eaf-491e-819c-e0f54a868022).
- Financial assumptions are planning estimates. [Page 7](07-market-research.md) replaces the market-size guess with sourced ranges: about $40–80M of clean consumer private AI today, planned at about 40% a year. Conversion, churn and the PureVPN attach rate are still unmeasured. Validate those, plus payment fees and token costs, before showing the model to investors.
- The [growth research](growth-research/00-main-report.md) estimates PureVPN's paying base at about 0.6 million (range 0.3 to 1.2 million), below the roughly 1 million assumed on [page 7](07-market-research.md). The attach-rate revenue there should be read 40% lower until PureVPN's own figure is known.
- Nothing here is legal advice. See [Legal risks](06-legal-risks.md) for the questions to take to counsel.

## Key decisions so far

1. **No sexual or obscene use cases.** The product will not be marketed for them, and generated images will block all nudity (see [page 5](05-content-policy-and-trust-safety.md)).
2. **Privacy means "nobody stores or reads your conversations"**, not "nothing checks them". Automated, in-memory safety checks are part of the design and disclosed to users.
3. **Hybrid hosting.** Start on managed zero-retention providers, then self-host the main models once spend justifies it (see [page 3](03-hosting-strategy.md)).
