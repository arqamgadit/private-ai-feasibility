# Venice AI teardown and growth playbook

[Back to wiki home](../README.md)

**Research date:** 16 November 2026 (Asia/Dubai).

A company teardown of Venice AI, plus the growth tactics PureVPN could copy. Includes a sourced read on who Venice sells to, a competition analysis, and an inventory of adult and uncensored marketing surfaces. Contractual no-training privacy is not unique among inference hosts such as Crusoe, but Venice's uncensored consumer product, TEE and E2EE modes, and multimodal bundle are. Estimates are labeled. Research as of 16 November 2026, Asia/Dubai.

> **The lesson for PureVPN** Venice reached profitability and a $1 billion valuation by making no-logs the product, not a footnote, then closing the feature gap with ChatGPT. The crypto token helped distribution, but the CEO told TechCrunch only about 8% of users pay with crypto. The copyable moves are positioning, founder-led distribution, tight freemium, and a privacy-AI bundle — not launching a token.


<a id="key-facts"></a>

## Contents

- [Key facts](#key-facts)
- [Product and privacy](#product)
- [Pricing and API](#pricing)
- [Revenue mix: API vs subscriptions](#revenue-mix)
- [Who Venice sells to](#who-buys)
- [Competition and competitiveness](#competition)
- [Adult content marketing](#adult-marketing)
- [VVV and DIEM](#token)
- [Team, funding, and scale](#company)
- [Timeline](#timeline)
- [Competitors, strengths, and weaknesses](#swot)
- [Growth playbook](#playbook)
- [What PureVPN should take](#purevpn)
- [Sources](#sources)

## Key facts

*Live market data as of 16 November 2026, Asia/Dubai. User and revenue figures are company or founder statements from the cited dates, not independently audited.*

#### Overview

| Item | Fact |
| --- | --- |
| Company | Venice.ai, Inc. Public site venice.ai. Founded 2024. Legal address in Sheridan, Wyoming. |
| What it is | Privacy-first, uncensored multi-model AI for text, image, video, audio, code, search, characters, and a developer API. |
| Founders | Erik Voorhees, CEO (ShapeShift). Jesse Proudman, president and CTO (Blue Box / IBM). Teana Baker-Taylor has been described as co-founder and COO (former Circle). |
| Funding | $65 million Series A, 1 July 2026, $1 billion valuation, first outside capital. Led by Dragonfly. Previously bootstrapped. |
| Revenue | Voorhees told TechCrunch the company was already profitable with annualized run-rate revenue above $70 million as of July 2026. He later said it crossed $100 million on 17 August and was above $150 million on 14 October. GeekWire reported profitability in Q1 2026. |
| Revenue mix | No official API-versus-subscription split has been disclosed. See the Revenue mix and Who Venice sells to sections. |
| Who it sells to | By customer count, end users. By usage and, likely, a rising share of revenue, developers and agents. Working range and caveats are in Who Venice sells to. |
| Competitiveness | Default no-training privacy on open models is not unique (see Crusoe and other hosts). Venice's sharper edges are the uncensored consumer app, TEE and E2EE, and the multimodal bundle. Details in Competition and competitiveness. |
| Monetization | Consumer subscriptions plus API and credit sales. Voorhees said about 8% of users pay with crypto. |
| Team | About 45 employees as of July 2026, remote, no office, six in Seattle. Up from roughly 15 a year earlier and about 20 in 2025 coverage. |

#### Scale

| Item | Fact |
| --- | --- |
| Users, Jul 2026 | 3.5 million registered users (company Series A post). TechCrunch also cited more than 3 million active users. |
| Users, Nov 2026 | About page now says join over 4 million users. Not a dated census. KR1, citing an October community update, later said 5 million. |
| Usage, Jul 2026 | 1.3 trillion tokens per month; 2 million API calls per day, peaking above 2.1 million; 300,000 inference requests per hour at peak. |
| Company web traffic, Jul 2026 | 1.3 million to 1.6 million site visits per month from roughly 850,000 to 1 million unique visitors. |
| Third-party traffic, Oct 2026 | Similarweb and AlphaMoat estimate 25.1 million visits, +23.8% month over month. This is far above the company's July figure. Treat as an estimate only. |
| Engagement estimate, Oct 2026 | Similarweb: 10 minutes 52 seconds average visit, 7.61 pages per visit, 32.79% bounce rate. Direct traffic 58.16% of desktop visits. United States 37.5% of visits. |
| 2025 recap | Voorhees on 1 January 2026: 1.7 million registered users, +400% year-over-year Pro subscriber growth, +20% compound monthly revenue growth, 323 million LLM requests, 137 million images, 1.4 million videos, 170 million API calls. |

Switch the table for a compact view of the company, its scale, or the token. All numbers are attributed in later sections.


<a id="product"></a>

## Product and privacy

Venice is a consumer app and developer API that aggregates frontier and open-source models in one place, with a privacy and free-speech positioning against ChatGPT, Claude, and Gemini. It is available on web, iOS, and Android. The about page still emphasizes that people can start without an account. Docs listed 414 models as of this research: 142 text, 82 image, 144 video, plus speech, music, and embeddings. Featured defaults on the about page included DeepSeek V4.1 Flash 1017 Uncensored, Z-Image Turbo, Grok 4.7, Kimi K3, DeepSeek V4 Pro 0813, Qwen 3.8 27B, Venice Uncensored 1.2, and Lustify v7 and v8.

Product surface includes chat, web search with citations, document uploads, image generation and editing (including NSFW on paid tiers), video, music, text-to-speech, custom characters, agents, and an OpenAI-compatible API at https://api.venice.ai/api/v1. Integrations called out on the API site include OpenClaw, MCP, a CLI, and Agent Skills. Models are added quickly and used as launch marketing.

Privacy is sold as four modes, all of which pass through a Venice proxy. Conversation history is kept on the user's device, not on Venice servers. The distinction that matters for a PureVPN reader is that not every mode is equally private.

Venice also says it does not add content restrictions to models, and that it uses system prompts that tell models to speak more freely. Proudman has said there are still safeguards against abuse and illegal activity. The uncensored and NSFW image positioning is a real acquisition hook and a brand risk.


<a id="pricing"></a>

## Pricing and API

*Plan prices and credit rules from venice.ai/pricing as of 16 November 2026, Asia/Dubai.*

100 credits equal $1. Credits buy video, music, frontier image and text models, and API usage. Video is marketed at under 80 credits for a short clip from models such as Seedance 2.5, Wan 3.0, Kling V3, and Grok Imagine 2.0. API users can pay as they go, use bundled Plus or Max spend, spend staked DIEM, or pay per request from a USDC wallet through x402. Staking at least 100 VVV is also described as unlocking Pro features.


<a id="revenue-mix"></a>

## Revenue mix: API vs subscriptions

*Researched 16 November 2026, Asia/Dubai. Venice has not published a split. The table is an independent on-chain reading, not a company disclosure.*

For discussion notes on **API vs subscription revenue quality** (margins, durability), see [Competitor research discussion notes (16 Nov 2026)](discussion-notes-2026-11-16.md#api-billings-vs-subscription-revenue-quality-of-revenue).

Venice has not disclosed how much revenue comes from consumer Pro, Pro Plus, and Max subscriptions versus the API or other credit sales. The Series A blog, the TechCrunch interview, GeekWire, and Voorhees's public posts all describe both channels and give company-wide totals. None of them gives a percentage. Paying subscriber counts have also not been disclosed, so Pro price times subscribers cannot be computed from official figures. Bluecoin Capital, in an August 2026 note, stated the split as its own assumption and wrote that Venice does not disclose the mix.

The only public, payment-level series is Tokenomist's 20 October 2026 reading of programmatic VVV burns on Base. Venice publishes fixed burn amounts: $2 per Pro month, $5 per Pro Plus, $10 per Max, and 5% of credit purchases. Tokenomist counted USDC transfers from burn wallet 0xe315…82e7 from 1 to 17 October 2026 and backed out the underlying sales.

Tokenomist annualized that window at about $336,000 a day, or about $123 million a year, and called the mix the surprise: about four-fifths credit purchases and one-fifth subscription payments. That is not the same thing as an official API-versus-Pro split, for several reasons.

- Credits are a shared currency. The pricing page says they are used for video, music, frontier models, and API access, so a credit purchase can be an in-app consumer upsell rather than a developer API invoice. Tokenomist's label of these sales as API credits bought by developers overstates how cleanly they map to the API.
- Pro Plus and Max already bundle $75 and $225 a month of credits inside the subscription price. That bundled usage is subscription revenue, not a separate credit purchase.
- The April 15 burn post triggers burns on every new subscription. The July 17 post refers to a share of every Pro, Pro Plus, and Max payment. A secondary report of a 22 July community call said renewals were still a future trigger, not an active one. Tokenomist itself flagged this. If only new signups burn, the 19% figure is new-subscription sales, not subscription ARR, and understates the installed Pro base.
- Annual plans, if they burn only one month's amount, would also undercount subscription revenue. Tokenomist noted this bias.
- Staked DIEM can fund API use at $1 a day per token without a fresh credit purchase. The 40,000 DIEM supply target implies up to about $14.6 million a year of daily credit capacity, which may not appear in the burn-wallet credit line.
- Voorhees's above-$150 million figure in mid-October sits above Tokenomist's $123 million burn-implied pace. The gap could be uncounted renewals, annual plans, DIEM-settled usage, timing, or fees. It is not a disclosed reconciling item.

Other third-party takes should be kept in their own lane. Apollo Crypto, on 18 August, wrote that independent estimates put the split at roughly half subscriptions and half API at the $100 million stage, and that half of $100 million at an $18 Pro price would imply on the order of 230,000 paying subscribers. That is Apollo's arithmetic, not a disclosed count, and Apollo disclosed that it holds VVV. Sacra wrote that subscriptions were the vast majority of revenue in 2024 and, by mid-2026, were likely a minority of the run rate. The next section uses OpenRouter, docs traffic, published API stats, and DIEM capacity to go further than credits versus subscriptions, and to ask who actually pays: end users or developers.


<a id="who-buys"></a>

## Who Venice sells to

*Analysis as of 16 November 2026, Asia/Dubai. No official customer-mix or API-versus-in-app credit split has been disclosed. Ranges below are labeled estimates with assumptions shown.*

For **OpenRouter's role** as one visible API channel (limits of the signal), see [discussion notes](discussion-notes-2026-11-16.md#openrouters-role).

Credits mix API invoices and in-app spend on video, music, and premium models, so the burn-wallet 81% credit share cannot be read as developer revenue. The more useful question is who Venice sells to. The public evidence splits cleanly by metric, and less cleanly by dollars.

- **Verdict:** By customer count, Venice sells to end users. By token consumption, and likely by a rising share of revenue, it sells to developers and agents. End-user subscriptions remain a real franchise, and some credit dollars are in-app media, not API.
- **Working range:** As of October 2026, a sourced but unverified working range is about 45% to 70% of revenue from developers, agents, and other metered API-like usage, and about 30% to 55% from end-user subscriptions plus in-app credits. This is not a company figure.
- **Confidence:** Medium on the direction, toward developers and agents. Low to medium on any percentage. The range would move if subscription renewals are missing from burns, or if in-app video and premium models are a large part of credit sales.
- **Trend:** Toward developers and agents through 2026. Company-wide tokens grew much faster than registered users, OpenRouter volume rose several times from July to November, and third-party commentary shifted from subscription-majority in 2024 toward credits and API later.

### Assumptions behind the range

- Start from Tokenomist's October payment reading: about 19% subscription payments and 81% credit purchases on a $123 million annualized pace, versus Voorhees's above-$150 million total. If the gap is mostly uncounted renewals, subscriptions could be around one-third of $150 million. That sets a floor-to-mid range for end-user plans.
- The remaining two-thirds or more is metered credits and other items. Those credits are used for API and for in-app video, music, and frontier models. Spartan Group wrote in August that video generates outsized credit revenue despite a tiny share of requests, so a slice of credits is consumer, not developer.
- Developer and agent demand is independently visible: 2 million API calls a day from developers at the 1 July raise, OpenRouter volume in the 70 to 85 billion token a day range by mid-November, and token intensity at an early-August peak of about 12,500 tokens per request, which is hard to produce with ordinary consumer chat.
- The range would be too high for developers if most credit dollars are in-app media, and too low if almost all credit dollars are API and if subscription burns omit the renewal base.

### OpenRouter, one visible API channel

Vantage's OpenRouter provider page, as of the last complete UTC day on 15 November 2026, showed Venice at 78.7 billion observed tokens that day, a 30-day average of 75.2 billion, a 0.3% token share, and rank 48 among providers, on 38 hosted models. Trailing 30-day estimated billings at listed prices were $970,600, which annualizes to about $12 million if that pace held. That is an estimated OpenRouter-attributable billing figure, not Venice's net receipts after any OpenRouter take-rate, and one-day estimates are jumpy, so the 30-day trailing total is the better number.

*OpenRouter tokens through Venice, billions per day (data table):*

| Period | Value |
| --- | --- |
| 1 Jul | 11.9 |
| 1 Aug | 22.4 |
| 1 Sep | 40 |
| 1 Oct | 57.8 |
| 9 Oct | 113.5 |
| 1 Nov | 51.1 |
| 15 Nov | 69.1 |

The series rose from about 12 billion tokens a day at the start of July, when Venice itself reported 1.3 trillion tokens a month company-wide, or about 43 billion a day, to a 30-day average near 75 billion by mid-November. Voorhees, on 14 October, said daily token demand was then above 500 billion. KR1, citing an October community update, said daily inference exceeded one trillion tokens during October, versus about 250 billion at the end of September. Those company-wide figures are much larger than OpenRouter alone. A simple ratio, labeled as such: 75 billion OpenRouter tokens versus Voorhees's 500 billion is about 15% of company tokens on this one gateway, and less than that if the trillion-token October reading is right. Most Venice tokens, and most of the post-July explosion, are off OpenRouter, on the direct API, the consumer app, or both.

The OpenRouter mix is also not the consumer uncensored niche. On 15 November, Vantage's model table was led by DeepSeek V4.1 Flash, DeepSeek V4 Flash variants, GLM 5.3 Flash, and Xiaomi MiMo Flash, which are the sorts of cheap, long-context models agents use. Venice Uncensored, the flagship uncensored model placed on OpenRouter in July 2025, is a small slice: the public app list on its OpenRouter page was led by KLOUT Prompt Engineering at 95.1 million tokens, and Venice is the sole host. That 2025 partnership also let OpenRouter stake VVV and offer the model free through OpenRouter, so Uncensored volume there should not be treated as cash API revenue.

### Direct API and the developer ecosystem

The company itself, in the 1 July Series A post, reported 2 million API calls per day from developers, peaking above 2.1 million, alongside 300,000 inference requests per hour at peak. TechCrunch cited 1.7 million API calls a day on average at the same time. Apollo wrote that API users had passed 25,000 in March 2026. Voorhees's 1 January 2026 recap already included 170 million API calls for 2025. Those are company or close-to-company figures, and they show a real developer channel well before the autumn token spike.

Official developer packaging is still small. On 16 November 2026 the veniceai GitHub organization showed 172 stars on Skills, 79 on the MCP server, 71 on api-docs, 53 on the CLI, and smaller repos for x402, community showcases, and an IronClaw experiment. npm, for the week of 9 to 15 November, recorded 1,970 downloads of @veniceai/mcp-server and 224 of veniceai-cli. A community Vercel AI SDK wrapper, venice-ai-sdk-provider by npm user dpuyosa, had 186,693 downloads that week and 680,562 in the prior 30 days. That is not an official package, and weekly npm counts can be inflated by CI, so it is a signal of interest, not a census of API customers. The unofficial PyPI package venice-ai, now redirecting to venice-py, had only 55 downloads in the last week. An authenticated GitHub code search for api.venice.ai was not available in this pass.

Integrations are real but still more about routing than about a huge self-serve SDK business: OpenClaw lists Venice as a built-in provider, the API site pushes MCP, a CLI, Agent Skills, x402, and OpenAI-compatible migration, and Apollo also named Fleek, Cursor via bring-your-own-model, and community VS Code extensions. Founder posts through 2026 lean heavily on agents. That marketing mix matters, and it does not by itself prove agents are the majority of revenue.

### On-chain API capacity

CoinGecko, on 16 November 2026, listed 37,255 DIEM as both circulating and total supply. Each staked DIEM is designed to yield $1 per day of Venice API credit. If every token were staked and fully used, that would be about $37,000 a day, or about $13.6 million a year, against a 40,000-token target ceiling of $14.6 million a year. That is a capacity ceiling, not recognized revenue: unused daily credit does not roll over, and the staked share of circulating DIEM was not published in the sources checked. It can also sit outside the credit-purchase burn line. Even at the ceiling, DIEM is a meaningful but not dominant slice of a $150 million run rate.

### The consumer franchise is still large

Registered users are a consumer story: 3.5 million at the July raise, over 4 million on the about page at this research date, and 5 million in a KR1 note that cited an October community update. Proudman told GeekWire he wants the app on the phone next to ChatGPT and Claude. Similarweb, for October 2026, estimated 25.1 million visits to venice.ai with a 10-minute 52-second average visit and 7.61 pages per visit, which is app-like engagement, not documentation browsing. The same vendor estimated only 80,800 visits to docs.venice.ai, up 19.19% month over month, with a 1-minute 21-second visit and 1.81 pages. Even if Similarweb overstates the consumer site, the gap between the marketing site and the docs is wide. The company's own July web figures, 1.3 to 1.6 million visits, are still an order of magnitude above the docs estimate.

The iOS app, listed as Venice AI in Productivity, had a 4.2 rating from 1,500 App Store ratings when checked, a Similarweb US Productivity rank of 173 as of 13 November 2026, and a third-party download estimate of 500,000 or more. The store listing emphasizes private chat, image generation, a social feed, and no sign-up, and claims more than 1 million users have chosen Venice. Reviews mention privacy, uncensored use including NSFW, and the $18 Pro plan, including complaints that video burns credits quickly. Pricing still leads with consumer tiers. Feature launches in 2025 and 2026 added both consumer media, such as video, music, and characters, and developer surfaces, such as the API, OpenClaw, TEE, and x402.

### What this means for API versus in-app credits

A clean API-versus-in-app split of the credit line is still not in the public data. The weight of the evidence is that developers and agents explain most of the token growth, and therefore a large share of metered usage, while end users explain most of the headcount, the web and app sessions, and a substantial but smaller share of revenue through Pro plans and some in-app credit spend. Apollo's line, that the users are consumers and the tokens are agents, fits the public series, even though that wording is Apollo's, not a quoted company disclosure.

### Next steps that would sharpen the split

- Build or buy a Dune query on burn wallet 0xe315…82e7 to keep the $2, $5, $10, and 5% credit lots current, and on the DIEM staking contract to get staked versus circulating supply and large agent-like wallets.
- Pay for Similarweb, Semrush, or equivalent path-level data on venice.ai top pages, and compare /chat and the marketing site with /settings/api, venice.ai/venice-api, and docs.venice.ai.
- Ask Venice, or a well-placed investor, for two numbers: paying Pro, Plus, and Max subscribers, and API or credit revenue versus subscription revenue, ideally with in-app credit spend broken out.
- Use an authenticated GitHub code search for api.venice.ai and VENICE_API_KEY, and inspect OpenRouter's app breakdown for the Venice provider, not only for Venice Uncensored.
- Talk to visible API consumers such as KR1, which has said it resells Venice inference, and to OpenClaw or other agent-framework operators about spend.
- Check data.ai or equivalent for iOS and Android downloads, active users, and in-app purchase mix, which would bound the consumer side independently of web-traffic estimates.


<a id="competition"></a>

## Competition and competitiveness

*Researched 16 November 2026, Asia/Dubai. Prices are official list rates or OpenRouter provider rates checked that day. Privacy and content claims are quoted from each company's own pages. Traffic figures are third-party estimates unless labeled as company-reported.*

Arqam's pushback is the right one to test first. If Crusoe already sells managed inference with strong privacy and open models, then privacy and uncensored may not be a moat. The official pages support the first half of that point and not the second.

### Does Crusoe already offer what Venice sells?

Crusoe's own marketing for Managed Inference, at https://www.crusoe.ai/cloud/solutions/model-inference, is an enterprise and developer inference product: OpenAI-compatible APIs, a curated gallery plus bring-your-own models, MemoryAlloy caching, pay-per-token or provisioned throughput, and a stated audience of app developers, startups, and enterprise API consumers. The pricing page at https://www.crusoe.ai/cloud/pricing lists serverless inference for open models including DeepSeek V4.1 Flash, DeepSeek V4 Flash 0731, DeepSeek V4 Pro, GLM-5.3 and GLM-5.3 Flash, Gemma 4 31B, GPT-OSS 120B, Qwen3.8 27B, and several NVIDIA Nemotron variants, plus GPU rental. Crusoe does not present a consumer chat app, characters, or an uncensored brand.

On privacy, Crusoe's Managed Inference Terms of Service for OpenRouter customers are explicit: Crusoe will only use Customer Data for inference, will not use it to train models, and will not store it on disk or use it for any other purpose than the inference process. The same terms say Crusoe generally does not log Customer Data, but does log metadata, and may observe and log a small portion of Customer Data when necessary for debugging, security, or as required by law. That is very close to Venice's Private mode, which the docs describe as zero data retention, contract-enforced: prompt and response content is processed for inference only and is not retained after the request completes. Venice, like Crusoe, still processes operational metadata. This OpenRouter-customer ToS was the cleanest no-disk, no-training quote found. Crusoe's general Cloud Platform Terms say Customer Data is used only to provide the Services and not for other Crusoe products or advertising, but they do not repeat the no-disk sentence. Treat the no-disk language as verified for OpenRouter-routed Managed Inference, and not independently quoted from a separate direct-customer inference ToS in this pass.

On uncensored, Crusoe's own Acceptable Use Policy is not a free-speech product. It prohibits illegal activity including child sexual exploitation, non-consensual explicit imagery, harassment, hate, and self-harm, and it separately prohibits testing or reverse-engineering the Services in order to evade filtering capabilities. Model-specific EULAs also apply. Venice also bans illegal use and child sexual abuse in its Terms of Service, and Proudman has said there are still safeguards against abuse, but Venice markets uncensored and NSFW generation as a feature, ships models named Uncensored and Lustify, and says it does not add content restrictions to models. Crusoe's public pages checked for this research do not make that claim.

- **Arqam's point:** Holds on managed open-model inference and on contractual no-training, no-disk privacy for Crusoe's OpenRouter Managed Inference terms. Those are not unique to Venice.
- **Where it does not hold:** Crusoe is not an uncensored consumer product. It has an AUP that includes evading filters, a smaller serverless catalog, no consumer app, and no TEE or E2EE offering found on the pages checked.
- **Confidence:** High on the policy comparison, because both quotes come from each company's own legal or docs pages. Medium on catalog completeness, because Crusoe also sells dedicated deployments that can host other models.

### Developer and API comparison

### Same-model list prices

Prices below are per 1 million tokens, input then output, then cache read where published. Venice figures are from https://docs.venice.ai/pricing. Crusoe figures are from https://www.crusoe.ai/cloud/pricing, parsed from the serverless inference rows on 16 November 2026. Together's DeepSeek V4.1 Flash rate was confirmed on OpenRouter as $0.30 / $1.20, matching its listed provider price. Groq is omitted because it was not a listed provider on these overlapping DeepSeek and GLM pages.

On the models that can be compared cleanly, Venice is not the cheap host. It is a few cents below Crusoe on DeepSeek V4 Flash 0731 and V4 Pro, a cent above Crusoe on V4.1 Flash input, and well above DeepInfra's discounted V4.1 Flash. Crusoe is cheaper than Venice on Qwen 3.8 27B and GPT-OSS 120B in the official rows above. GLM 5.3 Flash is the same price at both.

### OpenRouter head-to-head, DeepSeek V4.1 Flash

This is the fairest public latency comparison, because OpenRouter measures the same model across providers. Figures are from https://openrouter.ai/deepseek/deepseek-v4.1-flash as checked on 16 November 2026, Asia/Dubai. Token share is OpenRouter's 1-day effective-price table, not a company-wide market share.

Together was the speed leader on this page's standard endpoints. DeepInfra had the most token share at a lower list price. Venice and Crusoe sat in the same mid-pack price band, with Crusoe slightly faster to first token and a slightly larger 1-day share. Venice's Ultrafast SKU can win on throughput, but at ten times the list price. AutoExacto quality scores on the same page put Crusoe at 89.2% GPQA Diamond and 75.2% TAU-Bench, and Venice at 89.2% and 70.8%. That is close on GPQA and a gap on TAU-Bench; it is a benchmark, not a billing result.

### Consumer comparison

Consumer plan prices below are from each company's pricing page as commonly published, and should be rechecked before any purchase decision because those pages are updated often. Venice prices are from https://venice.ai/pricing on 16 November 2026. ChatGPT Plus is listed at https://chatgpt.com/pricing/, Claude Pro at https://claude.com/pricing, Grok-related X plans at https://x.ai/pricing, and Perplexity Pro at https://www.perplexity.ai/hub/pricing and https://www.perplexity.ai/pro. Proton Lumo's live page at https://proton.me/lumo/pricing describes Free and Plus, with zero-access encryption and a claim that chats are never used to train AI; the exact Plus dollar price was not extracted from that page in this pass. Dollar prices for Duck.ai, Brave Leo, Le Chat, Character.AI, Janitor AI, SpicyChat, and Kindroid were also not reliably extracted from their live pages in this pass.

Even if one uses Similarweb's 25.1 million October visits for Venice, that is still a small consumer web footprint next to ChatGPT, Gemini, Claude, Grok, and the larger companion apps. Venice's own July visit count is an order of magnitude smaller still. The consumer franchise is real, and it is not in the same traffic league as the frontier assistants.

### Where Venice wins, where it is a commodity, and what that means

- **Wins:** The consumer-plus-API bundle; uncensored and NSFW as a product, not just open weights; TEE and E2EE on top of contractual retention; crypto, DIEM, and x402 payments; a very wide multimodal catalog in one app; and founder-led distribution in crypto and privacy communities.
- **Commodity:** OpenAI-compatible access to DeepSeek, GLM, Qwen, Llama, and similar open models; mid-pack per-token list prices; mid-pack OpenRouter latency; and contractual no-training or no-disk privacy, which Crusoe, Fireworks, and DeepInfra also offer in some form.
- **Moat, as of this research:** Brand and community, not unique GPUs or unique base models. The consumer funnel can feed API demand. OpenRouter helps distribution and also makes it easy to switch away. The token and DIEM loop helps crypto-native agents, but Voorhees has said most users still pay in fiat.
- **Threats:** Price competition from DeepInfra, Fireworks, and many OpenRouter hosts; production features at Together, Crusoe, and Fireworks such as dedicated endpoints, fine-tuning, and GPU rental; TEE suppliers that can sell around Venice; much larger consumer incumbents; companion apps in the uncensored niche; and regulatory or brand risk from NSFW.
- **Revenue durability:** The consumer subscription is a real but smaller franchise. A large and rising share of tokens, and likely of revenue, sits in metered inference, where switching costs are low and prices are already mid-pack. Durability depends more on keeping the bundle and the uncensored brand than on winning a pure price or speed war. Confidence on this read is medium.

For PureVPN, the implication is sharper than it was before this comparison. Do not treat Venice's default privacy mode as a unique technical asset that Crusoe-class clouds lack. The copyable lesson is still to make no-logs the product, not a footnote. If the interest is a private consumer assistant, Proton Lumo, Duck.ai, and Brave Leo are closer brand-fit peers, because they sell privacy without an uncensored or NSFW hook. A commercial bundle with Venice can still make sense for crypto-adjacent and anti-censorship customers, but the NSFW and token layers should stay ring-fenced from a mainstream VPN brand. An acquisition thesis at a $1 billion valuation after a fresh primary round is even harder to justify if the API layer is a commodity and the remaining differentiation is brand, distribution, and a controversial content niche.


<a id="adult-marketing"></a>

## Adult content marketing

*Inventory researched 16 November 2026, Asia/Dubai. Only pages and ads actually found are listed. Marketing copy is paraphrased in neutral terms. No explicit imagery was downloaded, stored, or described.*

Uncensored is a core Venice brand word, not a side campaign. Adult and NSFW messaging is real, but it is concentrated in programmatic SEO blogs, comparison pages against Character.ai and Janitor AI, and model names such as Lustify and Venice Role Play Uncensored. Paid social landing pages found in this pass use softer language: unfiltered, unrestricted, no filter, or does not censor. They do not say NSFW or AI girlfriend on the page titles or meta descriptions that were fetched.

- **Scope:** venice.ai/sitemap.xml listed 574 URLs on 16 November 2026. A keyword pass for nsfw, uncensored, adult, roleplay, companion, girlfriend, lustify, and related terms hit 38 URLs. A broader pass added unfiltered, unrestricted, no-filter, and Character.ai or Janitor comparison posts. Paid landing pages under /lp/meta2026, /lp/reddit2026, /lp/x2026, /lp/tiktok2026, and /lp/landing-page-meta returned 200 but were not in the sitemap.
- **How big it is:** Qualitative only. Path-level traffic was not available, so this is not a share of visits or paid spend. Uncensored and no-filter language appears on product hubs, app listings, official X, and paid social LPs, so it is a primary acquisition theme. Explicit adult, NSFW, girlfriend, and roleplay wording is mostly an organic SEO cluster, not the wording on the paid LPs that were found.
- **Keywords:** Highest-intent SEO terms found: uncensored AI chatbot, uncensored or unrestricted image generator, AI image generator adult, no adult restrictions, adult creative writing, roleplay and fiction, AI girlfriend, Character.ai alternative, Janitor AI comparison, uncensored LLM API, no-filter chat, furry art, and romance writing. Paid LPs target unfiltered or unrestricted AI chat.
- **Pro upsell:** Custom Characters are described as a Pro feature at $18 a month. The Mature Filter can be turned off only on Pro or higher. Pro raises the image cap from 15 a day to 1,000, and Lustify or frontier image and video models spend credits. The iOS FAQ tells users that App Store policies limit model behavior and to install a PWA for the full uncensored experience.
- **Age gating:** Weak on the marketing site. Terms require users to be at least 13, and under 18 to have parent or guardian consent and not disable the mature content filter. No identity age check was found on the landing pages fetched. The iOS app is rated 17+. Seedance has a separate face-consent flow for real likenesses.

### What this implies for PureVPN

- Do not copy the adult SEO cluster or model names such as Lustify. That is a brand, app-store, and partnership risk for a mainstream VPN, and it is already flagged in What PureVPN should take as a move to skip.
- Ring-fence any commercial bundle: share a referral path or a privacy-AI offer, not a joint campaign that lands on NSFW image, AI girlfriend, or Janitor AI comparison pages.
- The copyable lesson is the broader uncensored-as-free-speech and no-logging hook, which is also what the paid Meta, Reddit, X, and TikTok landing pages emphasize. One Meta campaign was tagged utm_campaign=vpn1, which suggests Venice is already buying against VPN-adjacent audiences. That is a distribution overlap, not a reason to inherit adult creative.
- If a bundle is considered, diligence the weak age gate (13+ self-attestation, mature filter unlocks at Pro) and the official admission that store apps are more limited than the web or PWA. Those are partner and compliance issues, not just tone issues.

### Paid and product landing pages

### Ads

Paid uncensored acquisition is real. The full creative set was not independently enumerated from official ad libraries in this pass, so the rows below are only items that could be verified from a page or a third-party ad-library extract. Google Ads Transparency search in this pass did not turn up a Venice advertiser page. Reddit Ads Library creatives were not retrieved; the reddit2026 landing is the evidence that Reddit is a paid channel. No official affiliate landing was found: https://venice.ai/affiliates, /affiliate, and /partners all returned 404. The first-party referral program, described at https://venice.ai/faqs/all, pays both sides $10 in API credits when a referred user upgrades to Pro. That program is not adult-specific.

### Programmatic SEO and comparison blogs

These are first-party venice.ai/blog posts that were fetched. Many are 2026 listicles that rank Venice first for adult or uncensored queries, then pitch Pro or Studio. Earlier 2024 and 2025 posts introduce the uncensored claim, characters, and an AI girlfriend guide.

Related uncensored-but-not-primarily-adult posts were also in the sitemap, including the OpenRouter partnership and the incentive-fund announcement. They use uncensored as a company-wide brand word for developers and agents, not as adult creative SEO, so they are not repeated row by row here.

### Model pages, app listings, docs, and official posts

Official X was sampled with full-archive search of @AskVenice and @ErikVoorhees for NSFW, Lustify, girlfriend, roleplay, uncensored, and related terms. That is not a complete archive of every post. The pattern in the returned 2025 and 2026 posts is that uncensored and unrestricted are frequent launch adjectives, while explicit adult or girlfriend wording is much more common on the website SEO cluster than on the official accounts in this sample.

### Limits of this inventory

- No path-level traffic or ad-spend figures were available, so the size of this channel is a qualitative read, not a percentage of acquisition.
- The official Meta Ad Library was not fully scraped. One creative and a third-party count of 68 live ads are recorded, not the complete set of 68.
- X, Reddit, and TikTok ad creatives were not retrieved from those networks' ad libraries. Their landings were found by probing predictable /lp/ paths.
- A Google Ads presence was not found in the public Transparency Center results checked, and may still exist.
- https://venice.ai/blog/what-is-an-uncensored-ai-model was confirmed in the sitemap but not fully re-fetched for a complete paraphrase in the later pass, and is labelled as such.
- Featurebase's mature-filter article URL was found in search results but failed to load in this environment; the same policy is documented on the official FAQ.


<a id="token"></a>

## VVV and DIEM

VVV launched on 27 January 2025 as an ERC-20 on Base, with no presale. Genesis supply was 100 million: 50% airdropped (25 million to more than 100,000 Venice users who met an activity threshold, 25 million to crypto-AI communities on Base such as Virtuals, AIXBT, and others), 35% to Venice.ai including a 10 million team grant vesting through January 2027, 10% incentive fund, and 5% liquidity. The airdrop was explicitly aimed at users and at AI agents.

The live utility loop is: stake VVV to receive sVVV and emissions; lock sVVV at a mint rate to mint DIEM; stake DIEM so that each token yields $1 of API credit per day, refreshed at 00:00 UTC with no rollover. Unused DIEM credit does not bank. A portion of subscription and credit revenue is used to buy and burn VVV ($5 of every $100 of credit purchases, plus subscription burns). Emissions have been cut in stages and were set to fall to 2 million VVV per year from 1 October 2026. The DIEM supply target was raised in August 2026 from 38,000 to 40,000.

CoinGecko on 16 November 2026, Asia/Dubai, showed VVV at $20.05, a $982 million market cap, and a $1.63 billion fully diluted valuation. That is a liquid, high-visibility asset, and also a regulatory and volatility overlay the core SaaS business does not need. Voorhees has said most users are not crypto people, and that revenue comes from Pro subscriptions and credit sales.


<a id="company"></a>

## Team, funding, and scale

- **CEO:** Erik Voorhees, founder. Former ShapeShift CEO, early Bitcoin advocate, based in Panama per his X profile. About 997,000 X followers as of this research.
- **President and CTO:** Jesse Proudman, co-founder. University of Puget Sound classmate of Voorhees. Founded Blue Box (sold to IBM in 2015) and Strix Leviathan (sold to Parataxis in 2025). Seattle-based.
- **Other leaders:** Teana Baker-Taylor has been named co-founder and COO (former Circle, Crypto.com, Binance). July 2026 GeekWire photo also listed Austin Virts (VP marketing), Jonathan Shapiro (strategy), Tim Shakarian (engineering), and Johanna Tseng (VP business operations).
- **Series A:** $65 million at a $1 billion valuation, announced 1 July 2026. Dragonfly led. Disclosed participants across the company post and GeekWire: Coinbase Ventures, F-Prime, North Island Ventures, Archetype, Morgan Creek, Liquid2 Ventures, and Founders' Co-op.
- **Use of proceeds:** Scale the consumer app and API, and buy GPUs / build data-center capacity to improve gross margins instead of leasing compute.

Company-reported registered users rose from 450,000 at the January 2025 token launch, to 1.7 million at year-end 2025, 3 million in April 2026, 3.5 million at the July 2026 raise, and "over 4 million" on the about page at the time of this research. That is the series to trust for scale. Third-party web-traffic estimates are much higher than Venice's own July 2026 visit numbers and should not be mixed with them.

*Registered users, company-reported, millions (data table):*

| Period | Value |
| --- | --- |
| Jan 2025 | 0.45 |
| Jan 2026 | 1.7 |
| Feb 2026 | 2 |
| Apr 2026 | 3 |
| Jul 2026 | 3.5 |
| Nov 2026 | 4 |

The gap between 1.3–1.6 million company-reported monthly visits in July and 15.3 million third-party estimated visits for that same month (AlphaMoat) is too large to ignore. Use Venice's own figures for planning; use the third-party series only as a directional growth trend, not as a traffic forecast.


<a id="timeline"></a>

## Timeline

### May 2024 — Public launch

Private, uncensored AI on open-source models. No-account use is part of the original hook.

### Jul 2024 — Live web search

Citations added, a step toward assistant parity.

### Nov 2024 — Developer API

Sets up the later token and agent strategy.

### 27 Jan 2025 — VVV token generation

50% airdrop to users and crypto-AI communities. Staking for inference access. Listings later include Coinbase and Kraken.

### Apr 2025 — Image generation

Broadens the product beyond chat.

### 14 Jul 2025 — OpenRouter partnership

Venice Uncensored listed on OpenRouter. OpenRouter staked VVV to offer the model free through that gateway.

### Aug 2025 — DIEM launch

1 staked DIEM = $1 per day of API credit. VVV inflation cuts begin.

### Oct 2025 — Video and Venice V2

Text-to-video and image-to-video, first for beta and Pro, then wider.

### 1 Jan 2026 — Year recap

Voorhees posts 1.7 million users, 400% Pro growth, 20% compound monthly revenue growth.

### 18 Mar 2026 — TEE and E2EE

Hardware-attested private inference with NEAR and Phala. Pro feature.

### 24 Mar 2026 — Referral program

Referrer and referee each get $10 in credits when the friend upgrades to Pro. Open even to anonymous users.

### 9 Apr 2026 — Pro Plus and Max

Credits become the upsell currency. ARPU expansion after a simple $18 Pro plan.

### 1 Jul 2026 — Series A unicorn round

$65 million at $1 billion. First outside capital, already profitable at a $70 million-plus run rate per Voorhees. 2 million API calls a day from developers.

### 17 Aug 2026 — Revenue milestone

Voorhees posts that Venice has crossed $100 million annualized revenue.

### Aug–Oct 2026 — Token tightening

Credit-purchase burns, DIEM target to 40,000, emissions down to 2 million VVV per year.

### 14 Oct 2026 — Revenue milestone

Voorhees posts that annual revenue is now above $150 million and daily token demand is above 500 billion.

### Nov 2026 — Site claim

About page: over 4 million users and more than 200 leading models in marketing copy; docs listed 414 models.


<a id="swot"></a>

## Competitors, strengths, and weaknesses

A fuller side-by-side, including Crusoe's own terms and OpenRouter prices for the same models, is in Competition and competitiveness. In short, Venice competes up-market with ChatGPT, Claude, Gemini, and Grok on one app for all models, and sideways with OpenRouter, Together, Fireworks, DeepInfra, Groq, and Crusoe on API inference. The uncensored and character niche overlaps Janitor AI, Character.AI, and similar sites. Privacy alternatives include Proton Lumo, Duck.ai, Brave Leo, local models, and TEE hosts such as NEAR and Phala. Voorhees has said the aim is for Venice to sit on the phone next to ChatGPT and Claude.

**Strengths**

- Clear wedge: private by default and less censored, in a market where people now put health, legal, and relationship questions into chatbots.
- Bootstrapped to profitability and a $1 billion raise, which implies strong unit economics relative to frontier-model labs.
- Founder distribution: Voorhees has a large X audience; the company account had about 114,000 followers as of this research.
- Fast model shipping and near feature parity, which Voorhees called the strongest growth driver.
- OpenAI-compatible API plus agent integrations, so developers can switch with a base-URL change.
- Layered monetization: tight free limits, a popular $18 Pro, higher Plus and Max tiers, credits, and a crypto access path without making crypto mandatory.

**Weaknesses**

- Anonymous mode still sends prompts to frontier providers that may store them. The headline privacy claim is easy to over-read.
- Default contractual zero retention on open models is also offered by Crusoe, Fireworks, and others, so it is not a unique API moat.
- Uncensored and NSFW positioning wins a loud cohort and can cap mainstream, family, and enterprise brand fit.
- Token narrative, listings, and volatility add regulatory and communications risk even though most revenue is fiat.
- Safety and misuse questions are already in the press; Voorhees frames the product as a neutral tool, which will not satisfy every partner or regulator.
- Growth is concentrated in a founder brand and in crypto-adjacent channels that can fade with the cycle. Third-party traffic estimates also conflict with company-reported visits.

> When we launched, we were very far away from what ChatGPT could do, but people would use us because it was private. And today, we're very close to what ChatGPT can do, so as we've closed that gap, it's become an increasingly compelling alternative.
>
> — Erik Voorhees, to TechCrunch, 1 July 2026


<a id="playbook"></a>

## Growth playbook

Venice did not buy its way to 3.5 million registered users with a classic affiliate machine. Similarweb, for October 2026, put direct traffic first at 58.16% of desktop visits, then organic search, then organic social, and called affiliate the most underutilized channel. The loop looks like this.

### Category design

Lead with private and uncensored, not with model names. Privacy is the reason to switch; model breadth is why people stay. The site copy attacks logging, censorship, and corporate or government access to thoughts.

### Founder-led X and crypto community

Voorhees posts product, token, and usage numbers in his own voice. The company account amplifies launches and referrals. This is low-CAC distribution into an audience that already distrusts Big Tech.

### Airdrop as acquisition, not just speculation

Half of genesis supply went to active users and to Base AI-agent communities. That seeded a holder base, API demand, and ongoing social talk. Eligibility required real product usage, which rewarded early habit.

### Token as retention and API prepay

Staking for Pro and DIEM for daily credits turns some users into owners. It is powerful for agents and crypto-native developers, and secondary for the mass of fiat subscribers.

### Tight freemium

Ten text prompts a day is a conversion throttle, not a generous trial. Pro at $18 undercuts many AI plans while feeling unlimited for core chat. Later Plus and Max tiers raise ARPU without abandoning the hero price.

### Credits, welcome bonuses, and rollover

Credits make video, music, and frontier models metered upsells. Welcome credits and banking reduce churn anxiety. Annual discounts of 10% to 16.7% pull cash forward.

### Referral on paid conversion

Both sides get $10 in credits only when the friend upgrades to Pro, not merely on signup. That pays for a subscriber, not a tire-kicker, and still works for anonymous visitors.

### Feature velocity as marketing

New models ship in days and become posts. Video, music, TEE, E2EE, and OpenClaw each created a news cycle without a big ad budget.

### Low-friction start, then account and app

No-account chat lowers first-session cost. Mobile apps, encrypted backup, characters, and referrals then give people a reason to register and stay.

### PR around a clean story

The Series A landed in TechCrunch and GeekWire as a profitable privacy unicorn. The story was product and thesis, then the raise, not the raise alone.

### Partnerships that extend the claim

Base and Coinbase for token and payments; NEAR and Phala for verifiable privacy; OpenClaw and MCP for agents. Each partner puts Venice inside another ecosystem.

### SEO and high-intent terms

The site targets private AI and uncensored AI. Combined with strong direct and social traffic, search is a support channel, not the only engine.


<a id="purevpn"></a>

## What PureVPN should take

The audience overlap is real, and so is a brand-fit limit. Venice buyers care about surveillance, logging, and permissionless access — the same instincts as a no-logs VPN customer, especially in crypto and anti-censorship segments. Venice also leans into uncensored and NSFW generation, which is a poorer fit for a mainstream VPN brand and for app-store or partnership risk. Treat Venice as a privacy-suite peer and a possible partner, not as a company whose entire tone should be copied. The competition section adds an important caution: default no-training inference privacy is not unique to Venice, so a partnership should be sold on the consumer bundle and distribution, not on a claim that only Venice can offer private open-model APIs.

Plot the recommended moves by effort and impact. These are judgment calls from the teardown, not a forecast of lift.

### Quick wins

- Rewrite the core offer so architecture, not a policy footnote, is the reason to buy: no central log to breach or subpoena, explained in plain language the way Venice explains device-side history and proxy modes.
- Put a named executive voice on X and in privacy communities, consistently, with product proof and numbers. Voorhees is a distribution channel, not just a CEO.
- Audit whether PureVPN's free or trial limits actually force a paid decision. Venice's 10 prompts a day is blunt, and it converts. A tighter trial beats a generous one that never hurts.
- Pay referrals on paid conversion, in account credit both sides can spend, not only on a percentage off first purchase. Venice's $10 / $10 on a Pro upgrade is the pattern.
- Keep a simple hero price, then add higher tiers and metered extras (credits, extra devices, dedicated IPs, business) to raise ARPU the way Pro Plus and Max did in April 2026.
- Build search and content for private AI, AI that does not log prompts, and VPN for ChatGPT or other AI tools. That demand is rising, and Venice does not own the VPN-adjacent queries.
- Cut first-session friction: fewer form fields, guest access, and a faster path to a working connection, analogous to Venice's no-account start.

### Partnership and longer bets

- A bundle is the most direct inorganic-adjacent move: annual PureVPN with a term of Venice Pro, or a co-branded private internet plus private intelligence offer. Share a referral code, not a full brand merger, so NSFW and token risk stay ring-fenced.
- Productize AI leak protection: a one-click mode or landing page that routes AI-app traffic through PureVPN, with a clear explanation of what a VPN does and does not hide from the model provider. That is honest, and it complements Venice's own warning about Anonymous mode.
- If inorganic growth is the brief, diligence a commercial partnership first, then a minority investment or acquisition in a privacy-preserving AI utility, not a bid for Venice itself at a $1 billion mark after a fresh primary round.
- A longer suite bet is VPN plus private DNS plus a private assistant plus encrypted storage, sold as one sovereignty stack. That is how Venice talks about intelligence; PureVPN can talk about the network layer of the same life. Proton Lumo is a closer brand-fit assistant peer than Venice if the goal is privacy without NSFW.
- Do not copy the token. It worked for Venice because of Voorhees, Base, and an agent-API story, and it still accounts for a small share of payments. The legal, listing, and brand cost for a VPN company is likely worse than the distribution gain.
- Do not lead with uncensored or adult generation. Steal the privacy and permissionless-access language, not the NSFW hook.


<a id="sources"></a>

## Sources

*Primary company pages, contemporaneous press, market data, and public X posts. Third-party traffic tools, OpenRouter billing estimates, and burn-wallet readings are estimates.*

1. [Venice about page](https://venice.ai/about) (venice.ai)
2. [Pricing](https://venice.ai/pricing) (venice.ai)
3. [Venice API pricing](https://docs.venice.ai/pricing) (docs.venice.ai)
4. [Venice privacy docs, four modes and zero retention](https://docs.venice.ai/overview/privacy) (docs.venice.ai)
5. [Venice Terms of Service](https://venice.ai/legal/tos) (venice.ai, 8 Jun 2026)
6. [Crusoe Cloud pricing, including serverless inference](https://www.crusoe.ai/cloud/pricing) (crusoe.ai)
7. [Crusoe Managed Inference product page](https://www.crusoe.ai/cloud/solutions/model-inference) (crusoe.ai)
8. [Crusoe Managed Inference ToS for OpenRouter customers, no training and no disk storage](https://crusoeenergy.pactsafe.io/versions/67abf52567a1197c3e81df8c.pdf) (Crusoe Legal)
9. [Crusoe Acceptable Use Policy](https://crusoeenergy.pactsafe.io/versions/6a763aa330efed65d371105d.pdf) (Crusoe Legal)
10. [OpenRouter, DeepSeek V4.1 Flash providers, prices, and latency](https://openrouter.ai/deepseek/deepseek-v4.1-flash) (OpenRouter, 16 Nov 2026)
11. [OpenRouter, Venice-hosted models](https://openrouter.ai/provider/venice) (OpenRouter)
12. [OpenRouter, Crusoe-hosted models](https://openrouter.ai/provider/crusoe) (OpenRouter)
13. [Together AI zero data retention, opt-in not default](https://docs.together.ai/docs/zero-data-retention) (Together docs)
14. [Fireworks privacy policy](https://fireworks.ai/privacy-policy) (fireworks.ai)
15. [DeepInfra privacy policy](https://deepinfra.com/privacy) (deepinfra.com, 15 Aug 2026)
16. [ChatGPT plans and pricing](https://chatgpt.com/pricing/) (OpenAI)
17. [Claude plans and pricing](https://claude.com/pricing) (Anthropic)
18. [xAI and Grok plans](https://x.ai/pricing) (x.ai)
19. [Perplexity Pro](https://www.perplexity.ai/pro) (Perplexity)
20. [Proton Lumo pricing and privacy claims](https://proton.me/lumo/pricing) (Proton)
21. [Momentic, Similarweb web visits for leading assistants, October 2026](https://momenticmarketing.com/blog/top-ai-chatbots) (Momentic, 5 Nov 2026)
22. [$65 million Series A post, including 2 million developer API calls a day](https://venice.ai/blog/venice-raises-65-million-series-a) (venice.ai, 1 Jul 2026)
23. [TechCrunch Series A interview](https://techcrunch.com/2026/07/01/venice-ai-becomes-a-unicorn-with-65m-series-a-as-its-privacy-first-ai-platform-takes-off/) (TechCrunch, 1 Jul 2026)
24. [GeekWire Series A, including Proudman on the consumer app](https://www.geekwire.com/2026/private-ai-venice-ai-led-by-crypto-vet-erik-voorhees-and-seattles-jesse-proudman-raises-65m/) (GeekWire, 1 Jul 2026)
25. [Voorhees, annual revenue above $150 million and token demand above 500 billion a day](https://x.com/ErikVoorhees/status/2110436081581879460) (X, 14 Oct 2026)
26. [Tokenomist, October burn-wallet sales mix](https://tokenomist.ai/research/venice-earns-150-million-vvv-gets-about-a-tenth) (Tokenomist, 20 Oct 2026)
27. [OpenRouter Venice provider tokens and estimated billings](https://routers.vantage.sh/providers/venice?pricing=listed) (Vantage, 15 Nov 2026)
28. [Similarweb, venice.ai consumer-site estimates](https://www.similarweb.com/website/venice.ai/) (Similarweb, Oct 2026)
29. [NEAR AI Cloud pricing](https://near.ai/pricing) (NEAR AI)
30. [Phala confidential model catalog](https://phala.com/models) (Phala)
31. [RedPill confidential AI](https://redpill.ai/) (RedPill)
32. [Apollo Crypto, users versus tokens, 25,000 API users in March](https://apollocrypto.com/a-pound-of-inference/) (Apollo Crypto, 18 Aug 2026)
33. [DIEM supply](https://www.coingecko.com/en/coins/diem) (CoinGecko, 16 Nov 2026)
34. [VVV and DIEM docs](https://docs.venice.ai/overview/vvv-diem) (docs.venice.ai)
35. [API product page](https://venice.ai/venice-api) (venice.ai)
36. [Voorhees, crossed $100 million annualized](https://x.com/ErikVoorhees/status/2089375845425287610) (X, 17 Aug 2026)
37. [VVV market data](https://www.coingecko.com/en/coins/venice-token) (CoinGecko, 16 Nov 2026)
38. [Uncensored product hub](https://venice.ai/uncensored) (venice.ai)
39. [Characters landing, private uncensored alternative to Character.ai](https://venice.ai/characters) (venice.ai)
40. [Meta ads landing, unrestricted creative freedom](https://venice.ai/lp/landing-page-meta) (venice.ai)
41. [Reddit ads landing, an AI that does not censor you](https://venice.ai/lp/reddit2026) (venice.ai)
42. [X ads landing, unrestricted AI](https://venice.ai/lp/x2026) (venice.ai)
43. [TikTok ads landing, the AI with no filter](https://venice.ai/lp/tiktok2026) (venice.ai)
44. [Venice versus Character.ai, uncensored comparison](https://venice.ai/blog/venice-vs-character-ai) (venice.ai, 4 Sep 2026)
45. [Venice versus Janitor AI, uncensored comparison](https://venice.ai/blog/venice-vs-janitor-ai) (venice.ai, 4 Sep 2026)
46. [Creating your own AI girlfriend guide](https://venice.ai/blog/creating-your-own-ai-girlfriend-a-comprehensive-guide) (venice.ai, 30 Jan 2025)
47. [Best AI image generator for adult content](https://venice.ai/blog/best-ai-image-generator-adult) (venice.ai, 3 Sep 2026)
48. [Official FAQ, Mature Filter and App Store or PWA uncensored split](https://venice.ai/faqs/all) (venice.ai)
49. [Terms of Service, age 13-plus and mature filter rules](https://venice.ai/legal/tos) (venice.ai, 8 Jun 2026)
50. [NSFW best practices, consenting adults only](https://learn.venice.ai/video/guides/nsfw) (learn.venice.ai)
51. [Consent and responsible use](https://learn.venice.ai/video/guides/consent) (learn.venice.ai)
52. [iOS App Store listing, Venice AI, 17-plus](https://apps.apple.com/us/app/venice-ai/id6742061900) (Apple)
53. [Google Play listing, Venice AI](https://play.google.com/store/apps/details?id=com.ai.venice) (Google Play)
54. [Third-party record of a Meta unfiltered-answers ad and vpn1 campaign tags](https://adlibraryspy.com/ad/c3deab0380c056c1ae2e3c827e888e6d/venice-ai) (AdLibrarySpy)
55. [Voorhees, uncensored models in the app and API](https://x.com/ErikVoorhees/status/2121286556334031298) (X, 13 Nov 2026)

