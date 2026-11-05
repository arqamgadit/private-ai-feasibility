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

## Competitor research

| Document | What it covers |
|---|---|
| [Venice.ai competitor analysis](competitor-research/venice-ai.md) | Venice's customer acquisition, adult-content exclusions, "VPN for AI" landscape, developer vs consumer revenue split and clean addressable market for PureVPN |

## Interactive model

The full financial model is an interactive canvas where every assumption can be edited:
[Venice-style AI + Agent Mode: 5-Year Financial Model](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/1e8b646a-bc93-4ead-8979-f9cbca57dec3).
The numbers in this wiki are the canvas's base-case defaults.

Market size, growth, players and the priced pain are charted in [Private AI market conviction](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/aec17bb6-1105-47ee-a759-639826c83eff). The write-up is [page 7](07-market-research.md).

## Status and caveats

- Prices and provider policies were checked on **26 October 2026**. Both change often, so re-check before signing contracts.
- Financial assumptions are planning estimates. [Page 7](07-market-research.md) replaces the market-size guess with sourced ranges: about $40–80M of clean consumer private AI today, planned at about 40% a year. Conversion, churn and the PureVPN attach rate are still unmeasured. Validate those, plus payment fees and token costs, before showing the model to investors.
- Nothing here is legal advice. See [Legal risks](06-legal-risks.md) for the questions to take to counsel.

## Key decisions so far

1. **No sexual or obscene use cases.** The product will not be marketed for them, and generated images will block all nudity (see [page 5](05-content-policy-and-trust-safety.md)).
2. **Privacy means "nobody stores or reads your conversations"**, not "nothing checks them". Automated, in-memory safety checks are part of the design and disclosed to users.
3. **Hybrid hosting.** Start on managed zero-retention providers, then self-host the main models once spend justifies it (see [page 3](03-hosting-strategy.md)).
