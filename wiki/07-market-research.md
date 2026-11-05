# 7. Market size, growth, players and the pain

[Back to wiki home](README.md)

Research compiled **5 November 2026**. This page answers the four questions the [financial model](02-financial-model.md) was carrying as assumptions, and it says which numbers are safe to plan on. The same findings are charted in [Private AI market conviction](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/aec17bb6-1105-47ee-a759-639826c83eff).

The [Venice note](competitor-research/venice-ai.md) sizes one company. It is not a market. Analyst reports titled "private AI" size on-premise enterprise software and hardware. They are not this product either.

## How to read the numbers

- **Sourced** figures have a link in Sources. They describe the market the publisher defined, which is often wider than ours.
- **Estimate** means our calculation. Each one states its inputs and confidence.
- **Clean private AI**, carried over from the Venice note: demand driven by confidentiality. No-logs, no-training, encrypted or attested inference, anonymity, and sensitive work (legal, health, finance, employer documents). It excludes adult, roleplay, "uncensored" and jailbreak demand, nudify and deepfakes.

## The four answers

| Question | Answer | Confidence |
|---|---|---|
| How big is the market we can sell into? | About **$40–80M a year** of paid clean consumer private AI in late 2026, centred near **$50M**. A second pool, private developer and enterprise inference, is about **$225M** in 2026. The $11B "private AI" figure is a different market. | Low–medium on the $50M; high that the $11B figure is the wrong market |
| How fast is it growing? | Plan on about **40% a year**, the growth rate of personal AI assistants. The only scaled player (Venice) grew about 10× in nine months of 2026; that is a launch spike, not a forecast. Bear **20%** (consumer VPN pace). Bull **70%** while the category is still new. | Medium for the planning rate; high that 10× will not persist |
| Who are the major players? | Habits sit with **ChatGPT** (58% of US users' primary assistant) and **Gemini** (25%). In clean private AI the scaled paid player is **Venice**. The clean brands with distribution are **Proton Lumo**, **Duck.ai**, **Brave Leo** and **ExpressVPN ExpressAI**. Local private use is **Ollama**. Enterprise attested inference is **Edgeless**, **Fortanix** and the hyperscalers. | High on who matters; low on everyone except Venice's revenue |
| What pain are they solving? | **A person might read what was typed.** US AI users value keeping humans out of their chats at **$11.20 a month** ($15.24 on highly sensitive tasks), against **$2.97** to stop training. Concern is above 80%. Only 18% have ever paid for better privacy. | High for the US choice experiment; medium that it travels to VPN buyers |

## 1. How big

Three layers. Only the middle one is the launch market.

### Layer A. Where people already pay for an assistant

This is the pond. A private product has to pull people out of it for the tasks they will not paste into ChatGPT.

| Market | 2026 size | Later | Growth | What it counts |
|---|---|---|---|---|
| Personal AI assistants | $4.84B, up from $3.4B in 2025 | $19.63B in 2030 | 42% a year | Consumer assistants. Research and Markets |
| AI assistants, wider cut | $7.11B | $26.75B in 2031 | 30% a year | Includes workplace assistants. MarketsandMarkets |
| ChatGPT | 1.2 billion weekly users (Oct 2026). 50 million+ paying subscribers (Feb 2026). About 6% of 800 million users paid at end-2025 | OpenAI run rate near $70B by Sep 2026, all products | Users from 900M weekly (Feb) to 1.2B (Oct) | The default habit, not a privacy product |

In a June 2026 US survey of 1,999 adult AI-assistant users, weighted to the AI-using public (Zou, 2026):

| Primary assistant | Share |
|---|---|
| ChatGPT | 58% |
| Gemini | 25% |
| Claude | 7% (about a third of coding tasks) |
| Copilot | 4% |
| Everyone else | about 5% |

Nobody in that ranking is a privacy product. Private AI is a second assistant for sensitive tasks, not a bid to replace ChatGPT for everyday questions.

### Layer B. The market this product sells into

**Clean consumer private AI, paid.** Bottom-up from companies that sell confidentiality as the product, with adult and "uncensored" revenue taken out using the Venice note.

| Piece | Late 2026 | Confidence |
|---|---|---|
| Venice, all revenue | $123M a year on-chain (1–17 Oct) to over $150M claimed (14 Oct) | High for the order of magnitude. See the [Venice note](competitor-research/venice-ai.md) |
| Venice, clean consumer and creator | **$30–50M a year** | Low–medium. Judgment on a revenue matrix |
| Proton Lumo, Duck.ai, Brave Leo, ExpressAI | Not disclosed. Lumo says more than 10 million people have tried it since July 2025. Treat their paid revenue as **smaller than Venice's clean slice**, not as zero | Users: company claims. Revenue: unknown |
| **Clean consumer pool** | **About $40–80M a year, point near $50M** | Low–medium |

**Clean developer and enterprise inference.** Separate product (the API and Teams tiers, from months 9 and 15).

| Piece | 2026 | 2031 | Confidence |
|---|---|---|---|
| Venice clean developer and coding API | About $32M a year | — | Medium. See the Venice note |
| Privacy-preserving AI inference, whole category | **$225M** | **$1.78B** | Medium. Knowledge Sourcing. Includes managed private-inference APIs, about $650M of the 2031 total |

Adding Venice's clean consumer slice to the $225M inference category double-counts nothing, but they are different buyers. Do not add them into one TAM and then compare the consumer plan to the sum.

**What Year 5 in the model means against this.**

The base case exits Year 5 at **$71M ARR** and **190,000 paying subscribers**, of which Pro and Max are about **$45M**. That consumer number is:

- about the **entire clean consumer pool as it stands in late 2026**, and
- roughly **15–30%** of a pool that starts at $50M and compounds at 40% a year for five years (about $150–400M by 2030–31, depending on the starting point inside $40–80M).

That is a category-leadership outcome. It is a reasonable plan only with a distribution advantage and a promise buyers can check. It is not "a small share of an $11 billion market."

**Attach-rate cross-check, using PureVPN.** PureVPN does not publish subscribers. Similarweb bands revenue at **$50–75M** (through September 2026). Another profile says **$10M** for 2025. The last company milestone in public is 1 million users in 2015–16.

Estimate, low confidence: take $60M of revenue and about $60 a year after discounts, which is about **1 million subscribers**. Five percent of them paying $18 a month is about **$11M** of AI ARR. Ten percent is about **$22M**. Fifteen percent is about **$32M**. The model's 190,000 consumer payers is larger than a 15% attach on today's base, so the plan also needs the VPN base to grow and some customers who do not already pay for PureVPN.

### Layer C. Real markets that are the wrong denominator

| Figure people reach for | Size | Why it is the wrong market |
|---|---|---|
| "Private AI" (Dimension Market Research) | $11.1B in 2025, $113.7B by 2034, 29.5% a year | On-premise and cloud software for data confidentiality: federated learning, differential privacy, on-device inference. On-premise is 58%. Large enterprises are 68%. Healthcare is 23%. Named players include IBM, Microsoft, Google, Palantir, Oracle. This is not a $18 chat subscription. |
| Private AI infrastructure (Technavio) | $33.7B in 2025, 18.7% a year to 2030 | Hardware, software and services. Hardware was $18.4B of an earlier cut. |
| Trusted execution for AI | $5.38B in 2026, $16B in 2030, 31% a year | Confidential computing hardware and cloud, plus software. Apple, NVIDIA, Intel, AWS and Microsoft dominate. Useful as a cost curve for TEE mode, not as revenue we can take. |
| All VPNs | $70–86B in 2026, growing about 15–21% a year | Enterprise remote access and SASE. Consumer VPN **apps** are the relevant neighbour: **$5.9B in 2024, up 15.6%**, about **150 million** users in 2025 (Business of Apps). |

Using Layer C makes a $71M Year-5 plan look easy. The binding constraint is Layer B.

## 2. How fast

Use a planning rate. Do not fit a curve through Venice's 2026 spike.

| Series | Rate | Use it for |
|---|---|---|
| Venice run rate, Jan to 14 Oct 2026 | $14M to over $150M, about 10× in nine months | Evidence the category can spike. Not a CAGR. Video credits, API and the token did much of this. |
| Venice clean consumer, mid-2026 to October | About 2.5× on burn counts | Same warning, narrower base. From the Venice note. |
| Personal AI assistants, 2026–2030 | **42% a year** | **Base case for clean consumer private AI.** Privacy is a feature battle inside this market. |
| Consumer VPN app revenue, 2024 | 15.6% | Bear case. A bundle sold to existing VPN buyers may grow like VPN, not like ChatGPT. |
| Privacy-preserving inference, 2026–2031 | 51% a year, from a $225M base | Base case for the API and Teams bet. Small base, so the percentage stays high longer. |
| Trusted execution for AI, 2026–2030 | 31% a year | Cost and supply of TEE capacity, not our revenue. |
| Ollama monthly developers, Jan to the 2026 Series B | Doubled, to 8.9 million | Demand for local private agents. Mostly unpaid, so it grows usage without growing the paid pool. |

**Planning stance**

- Clean consumer spend: **40% a year** base, **20%** bear, **70%** bull for the early years then back toward 40%.
- API and Teams: can follow the 50% inference category, but that revenue is not in the consumer price.
- Do not put Venice's 10× into the model. The model's own signup deceleration (12% month on month in Year 1 down to 2% in Year 5) is already a version of this. The missing check is whether Year-5 subscriber counts still fit inside Layer B after that deceleration. At 40% category growth they fit only as a leading share. At 20% they do not.

## 3. Who

Four groups. They do not compete for the same dollar.

### Default assistants (the habit to peel tasks off)

ChatGPT, Gemini, Claude, Copilot, Grok, Perplexity, Meta AI, DeepSeek. Quality bar and daily habit. Claude is the one users already call more trustworthy, and it takes a third of coding tasks from a 7% overall share. A private product that is worse at the job loses the sensitive task as well, because people route hard work to the tool they trust to be right.

### Clean private assistants (direct)

| Player | What they sell | Price signal | Scale we can cite | Gap versus us |
|---|---|---|---|---|
| Venice | "Private and unrestricted." No storage on the default path. TEE and E2EE on paid plans. Heavy API and credit revenue. Adult and video are a large estimated share. | Pro $18, average subscription about $23 | 5M users (19 Oct 2026). Over $150M run rate claimed. $65M Series A at $1B (Jul 2026) | Only scaled paid player. Much of the revenue is outside our content policy. See the [Venice note](competitor-research/venice-ai.md). |
| Proton Lumo | Zero-access encryption, no logs, open models on Proton-controlled servers in Europe. Proton says the model still sees cleartext; this is not an attested enclave. | Plus $12.99, or $9.99 a month yearly | More than 10 million have tried it since July 2025. Revenue not disclosed. | Closest clean brand. Cheaper. Distribution through Proton's privacy suite. |
| Duck.ai (DuckDuckGo) | Strips identity, then sends the prompt to GPT, Claude and others. Providers still see the text. Two open models run in a TEE. History on device. | Plus $9.99, bundled with a VPN. Cannot buy the AI alone. | About 19M monthly visits (third-party, low confidence). Revenue not disclosed. | Same "VPN plus private AI" bundle Express and PureVPN are walking into. |
| Brave Leo | In-browser. History on device. One model (GLM) routes into a TEE; the browser still trusts Brave's gateway for the check. | Premium $14.99 | Brave claims 128 million browser users. Leo's own usage is not disclosed. | Distribution inside a browser, not a destination site. |
| ExpressVPN ExpressAI | Sealed hardware, zero access, Cure53 audit, several models, web search, file vault. Included for Pro subscribers. | Bundle, not a standalone AI price. Launch promo cited the whole suite at $4.87 a month. Launched 31 Mar 2026. | No user or revenue split published. | A large VPN already shipping the product idea, with an audit we do not have. |

Smaller names using the "VPN for AI" phrase (Discrezo, Shield, AnonRouter, Antseed, Open Anonymity) had no scale in the October scan. Norton and Bitdefender use it for **agent network connections**, which hide the agent's IP and do not hide the prompt.

### Local and on-device (a habit, not a bill)

| Player | Scale | What it means |
|---|---|---|
| Ollama | 8.9 million monthly developers, doubled since January 2026. $65M Series B. In 85% of the Fortune 500, per the company. Revenue not disclosed. 14 people at the time of the round. | Developers will run private models themselves when the model is good enough, especially for coding agents. |
| LM Studio | About $1.8M estimated revenue (GetLatka, June 2025). | Confirms local apps are used and barely monetised. |
| Apple Private Cloud Compute | Default path for Apple Intelligence on Apple hardware. | Raises the bar for "prove the operator cannot read it" without charging an AI subscription. |

### Attested enterprise inference (the later API bet)

Edgeless Systems (Privatemode: OpenAI-shaped API, end-to-end encryption, remote attestation), Fortanix, Opaque, and confidential GPU offerings from Google, Microsoft, AWS and NVIDIA. Knowledge Sourcing puts private inference APIs and managed endpoints at about **$650M by 2031**, inside the $1.78B privacy-preserving inference market. This is the competitive set for Teams and the developer API, not for the $18 consumer plan.

## 4. The pain

The pain worth paying for is **a person reading the conversation**: an employee, a contractor, a model provider, or a government request that lands on stored chats.

A June 2026 discrete-choice experiment on the same US sample priced three data-handling features. Figures are the monthly price that offsets the feature. They are stated preference, not observed purchases.

| Feature users pay to avoid | All tasks | Highly sensitive tasks |
|---|---|---|
| A human reviews the conversation | **$11.20** | **$15.24** |
| Sponsored answers | $6.46 | $6.46 (flat) |
| The provider trains on the chats | **$2.97** | **$4.35** (about $7 among the most concerned) |

The rest of the pattern, from the same paper:

- More than **80%** are concerned about how conversation data is used.
- About **60%** do not know whether their assistant trains on their chats.
- Only **18%** have ever paid for a plan with better privacy protection.
- Knowing the training policy predicts protective behaviour better than how worried someone says they are.
- Price is the main reason in **38%** of the plan choices. Privacy differentiates a plan. It does not replace a tolerable price.
- Concern is flat across groups. Follow-through is not.

A UK survey of 211 users (PoPETs 2025) found the same gap from the other side: people are reluctant to share sensitive information and still do, because the useful answer requires the disclosure. Average protective actions were 1.4 out of 8. Deleting history (31%) and stripping sensitive details (27%) were the common ones. Only a minority had opted out of training.

**What this does to the product**

1. **"We do not train on you" is the cheap promise.** It is worth about $3 a month. Lumo at $9.99–12.99, Duck.ai bundled at $9.99 and Leo at $14.99 already occupy that shelf. An $18 plan has to sell the $11 promise: nobody stores the chat, and a human cannot read it. TEE, attestation and a published audit are the proof. A privacy policy is the $3 product.
2. **The buyer is routing one task, not changing assistants.** Sensitive work, health, money, legal and anything they would not want an employer to see. Everyday questions stay on ChatGPT. The free tier has to be good enough that the sensitive task is not the first time they open the product.
3. **Agent mode raises the same pain.** A stored agent trace includes pages visited, files and tool calls, not one prompt. Norton and Bitdefender cover the agent's IP. They do not cover the contents. That is the opening, and it is also the place a logging mistake does the most harm.
4. **"Uncensored" is a different pain, and it is not ours.** Venice's US search traffic leans on "uncensored AI" (about 40,500 searches a month in the September 2026 Semrush pull). The content policy keeps that demand out. Do not add it back into the TAM to make the plan look smaller as a share.

Secondary pains that show up in positioning, behind the human-review pain: refusals on lawful topics, history that locks the user into one vendor, and private models that are worse at the job than ChatGPT. Quality is the reason a privacy product stays a second tool. It is not, on this evidence, the reason people pay.

## 5. What would raise conviction

The page above is the enhancement: one market definition, a sourced scorecard, a growth rate the model can use, and a pain with a price. These measurements are still missing. Each one moves a planning number.

| Gap | What to collect | Which number it moves |
|---|---|---|
| PureVPN base | Paying subscribers, effective ARPU, renewal, country mix. Internal data. The public range is $10M versus $50–75M of revenue. | Whether 190,000 AI payers is a 5% attach or a 20% attach. |
| Intent on that base | A price test at $10, $13 and $18, for "no training" versus "no human can read this," on legal, health, finance and work-document tasks. Five hundred VPN customers is enough to beat the current guess. | Conversion (the model uses 2.5% of signups in month one, and 0.25% of the free base each month) and the $18 price. |
| Search demand | Semrush or Ahrefs for "private AI," "AI that does not save chats," "VPN for AI," against "uncensored AI." The Venice keyword table is from September 2026 and was not refreshed here. | Whether clean privacy has its own demand, or only rides Venice's brand and the uncensored queries we will not bid on. |
| Competitor revenue | Any disclosure or app-store panel for Lumo, Duck.ai, Leo and ExpressAI. | The $40–80M range. Today it is mostly Venice's clean slice plus a judgment that the others are smaller. |
| Paying subscribers at Venice | Still unpublished. On-chain burns miss a share of renewals. | How many people pay $18 for this job when the product is allowed to be "uncensored." An upper bound, not our forecast. |
| Proof as a purchase driver | Whether a Cure53-style audit (ExpressAI has one) or remote attestation changes willingness to pay in the same price test. | How much of the $11 human-review value we can actually capture at $18. |
| Churn | The model uses 6% a month on Pro and 5% on Max. No privacy-AI cohort has published this. A 6% monthly churn keeps about half of a cohort after a year. If sensitive-task use is occasional, churn can be worse. | Year-5 subscriber count more than signup count. |

Until the PureVPN price test exists, treat Year-5 consumer ARR of about $45M as the upside case in which this brand becomes one of the two or three clean private assistants, not as the base case implied by today's pool.

## Sources

| Source | Used for |
|---|---|
| [Zou, Platform Choice, Trust, and Privacy (Jul 2026)](https://arxiv.org/pdf/2607.15134) | US shares, concern, the 18% who have paid, willingness to pay |
| [Research and Markets, personal AI assistants](https://www.researchandmarkets.com/reports/6226037/personal-ai-assistant-market-report) | $3.4B (2025), $4.84B (2026), $19.63B (2030), about 42% a year |
| [MarketsandMarkets, AI assistants](https://www.marketsandmarkets.com/Market-Reports/ai-assistant-market-40111511.html) | $7.11B (2026) to $26.75B (2031), 30.4% a year |
| [Dimension Market Research, private AI](https://dimensionmarketresearch.com/report/private-ai-market/) | $11.1B definition and segment mix. Cited to reject it as our TAM |
| [Technavio, private AI infrastructure](https://www.technavio.com/report/private-ai-infrastructure-market-industry-analysis) | $33.7B infrastructure figure |
| [Knowledge Sourcing, privacy-preserving inference](https://www.knowledge-sourcing.com/report/privacy-preserving-ai-inference-market) | $225M (2026), $1.78B (2031), 51% a year, API slice |
| [The Business Research Company, trusted execution for AI](https://www.thebusinessresearchcompany.com/report/trusted-execution-for-artificial-intelligence-ai-market-report) | $5.38B (2026), $16B (2030), 31% a year |
| [Business of Apps, VPN apps](https://www.businessofapps.com/data/vpn-app-market/) | $5.9B consumer VPN app revenue in 2024, +15.6%, about 150M users |
| [TechCrunch, 900M weekly users](https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/) and later OpenAI remarks reported by [GPTOnline](https://gptonline.ai/chatgpt-search-queries-one-fifth-google/) | 50M subscribers (Feb 2026), 900M then 1.2B weekly users |
| [New York Times, 11 Feb 2026](https://www.nytimes.com/2026/02/11/technology/openai-revenue-challenge.html) | About 6% of users paying, 2025 revenue mix |
| [PoPETs 2025, UK conversational-agent privacy](https://doi.org/10.56553/popets-2025-0160) | Attitude versus behaviour, n = 211 |
| [Felloai, Lumo review (Oct 2026)](https://felloai.com/lumo-ai-review/) | Lumo price, 10 million tried, model sees cleartext |
| [ExpressVPN, ExpressAI launch](https://www.expressvpn.com/news-pr/expressai-private-ai-platform) | 31 Mar 2026 launch, Cure53, bundle |
| [Dealroom / TechCrunch on Ollama](https://app.dealroom.co/news/note/ollama-raises-65m-series-b-as-open-model-tool-hits-8-9m-monthly-users) | 8.9M monthly developers, $65M Series B |
| [Similarweb company page, PureVPN](https://www.similarweb.com/company/purevpn.com/) | $50–75M revenue band |
| Venice competitor note in this wiki | Venice revenue, clean split, search terms, "VPN for AI" landscape |

## Open gaps

- No company in the clean set except Venice has a usable revenue disclosure, and Venice's clean split is still a judgment.
- PureVPN subscriber count is not public. The attach-rate check is an estimate on top of a revenue band that itself conflicts ($10M versus $50–75M).
- Willingness-to-pay figures are a US choice experiment, not purchases, and not a VPN-customer sample.
- Search volumes were not re-pulled for this page. Semrush and Ahrefs were not available in the session that wrote it.
- Apple Private Cloud Compute has no public usage split that would show how many sensitive prompts never reach a third-party assistant.
