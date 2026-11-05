# Briefing for market research

[Back to wiki home](README.md)

Compiled **5 November 2026** for a market researcher who needs the product, the pains, the segments and the packaging in one place. This document aggregates the feasibility wiki. It does not replace the source pages, and it does not add new research.

Read a number by its tag:

| Tag | Meaning |
|---|---|
| **Decided** | A product or policy choice already made in this wiki. |
| **Model assumption** | A planning input in the 5-year financial model. Not measured demand. |
| **Estimate** | Our calculation from public data. Confidence is stated. |
| **Sourced** | A published figure. The publisher's definition is stated, because several "private AI" figures describe a different market. |

Nothing here is legal advice. Company, brand name and final prices are not locked. The working assumption is a UAE company, and the commercial context in the competitor research is **PureVPN's private-AI plan**: a clean, confidentiality-led product distributed with a VPN brand, studied against Venice.ai.

Source pages: [product](01-product-overview.md), [financial model](02-financial-model.md), [hosting](03-hosting-strategy.md), [providers](04-provider-comparison.md), [content policy](05-content-policy-and-trust-safety.md), [legal risks](06-legal-risks.md), [market](07-market-research.md), [Venice](competitor-research/venice-ai.md). The model itself is editable: [5-year financial model](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/1e8b646a-bc93-4ead-8979-f9cbca57dec3). Market charts: [Private AI market conviction](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/aec17bb6-1105-47ee-a759-639826c83eff).

---

## 1. What the product is

### 1.1 The product in one description

**Decided.** A private AI platform in the style of Venice.ai, extended with a Tab-style agent.

The user can:

- chat,
- generate images,
- write and run code,

on open-weight models, through a service that does not keep the conversation.

On top of that, **agent mode** can:

- plan a multi-step task,
- browse the web inside a sandboxed browser,
- call tools (search, fetch, extract),
- run code inside a sandboxed environment.

Conversation history lives in the user's browser. Requests pass through our proxy and are not stored. Each model is labelled with the privacy mode it actually runs in, so the user can see what protection that request has.

The company is assumed to be based in the UAE. Users are expected to come from everywhere. A crypto token (Venice sells one, VVV) is **left out of the plan**.

### 1.2 The promise, in the words we are allowed to use

**Decided.** The promise is:

> We never store your conversations, and no human ever reads them. Automated safety checks run in real time and keep nothing.

That sentence is the product. Two boundaries sit inside it.

Privacy means nobody stores the conversation and no human reads it. It does not mean nothing checks the request. Classifiers run in memory, including inside the hardware enclave on the strongest modes, and they keep nothing. Users are told this. The wording to avoid is "we see nothing and check nothing." That claim is false, and a false privacy claim is a legal problem (US FTC, UAE consumer law, EU consumer law) if a provider in the path is in fact logging.

The one disclosed exception: if an uploaded image matches a database of **known** child-abuse material, we expect to have to block it, keep minimal evidence and report it. US providers report to NCMEC. UAE Federal Law No. 3 of 2016 ("Wadeema's Law") has reporting duties; counsel still has to confirm how they apply. The exception is stated in the privacy policy, the way encrypted messengers state theirs.

### 1.3 What the user can do, capability by capability

These are the capabilities. Section 4 is how they are packaged into paid plans. Several capabilities do not exist at launch. The month column is a **model assumption**, not a committed roadmap, but it is the only sequence the plan uses.

| Capability | What the user gets | When it exists in the plan | What "private" means for this capability |
|---|---|---|---|
| Text chat | Open-weight models. Low refusal on lawful topics. History in the browser. | Public launch, month 5, on Free and Pro | Depends on the mode label. Default is Private. |
| Image generation | Open image models (launch path is fal.ai; later Flux or SDXL on our own GPUs). | Launch, month 5 | The launch provider scans every image request (hash match plus OpenAI's moderation model), so fal.ai sees prompts. Full control arrives when images are self-hosted. All nudity is blocked on output. |
| Code | Code-capable open models, same chat surface. | Launch, month 5 | Same as text. |
| Agent mode | Multi-step plan, sandboxed browser, search/fetch/extract, sandboxed code. | Month 7, with the Max tier. Pro then gets a small monthly task allowance. | The prompt is under the same privacy mode as chat. The browser vendor (Browserbase at launch) sees every page the agent opens, so a data-processing agreement is required. Code sandboxes (E2B) are short-lived and can be self-hosted later because the software is open source. |
| Frontier models | OpenAI, Anthropic, Google, reached through our proxy. | Available as a labelled option, not the default. | Always labelled **Anonymous**. The provider sees the prompt and may keep it. We do not attach the user's identity. |
| Developer API | OpenAI-compatible endpoints. Priced as a markup on inference. | Month 9 | The caller's traffic uses the same mode labels. There is no published per-token price card yet. |
| Teams | Shared workspaces, SSO, admin controls, private deployments. | Month 15 | "Private deployments" is specified as a feature and is not separately costed. This is the enterprise motion. |

### 1.4 The four privacy modes

**Decided.** Copied from Venice's published architecture. Every model is labelled with one mode. The label is part of the product, because the modes do not offer the same protection and pretending they do would make the privacy claim false.

| Mode | How it works | Who can see the prompt | What the user still has to trust | Web search and memory |
|---|---|---|---|---|
| Anonymous | The request is relayed to a frontier provider (OpenAI, Anthropic or Google) without the user's identity. | The provider sees the text and may keep it. | That we really stripped the identity, and whatever the provider's retention policy is. | The frontier product's own tools, if we pass them through. Not specified in detail. |
| Private (default) | Runs on our GPUs, or on a partner contractually bound to zero data retention and no training. | The operator of the GPU can see it in the clear. The contract says they do not keep it or train on it. | Us, and the partner, honouring the contract. This is a promise, not a hardware proof. | Allowed. This is the normal product. |
| TEE (paid) | Runs inside a hardware-isolated confidential-computing enclave. Each response can carry remote attestation. | The GPU operator cannot read the prompt. Our proxy still sits in front. | The attestation, and that our proxy is not copying the prompt before it enters the enclave. A confidential VM for the proxy (Phala is the candidate) is how users could verify the proxy itself keeps no logs. | Allowed, subject to the enclave design. |
| E2EE (paid) | The prompt is encrypted on the device and decrypted only inside a verified enclave. | Nobody, including us, can see the prompt. | The user's own device, and that the enclave they attested is the one that decrypted it. | **No web search and no memory.** The server cannot see the prompt, so it cannot search or recall on the user's behalf. |

Safety classifiers run in every mode. In TEE and E2EE they run **inside** the enclave, so the check does not require us or the GPU provider to see the prompt. The strongest privacy mode is still moderated.

**What this means for research.** Buyers are not choosing one privacy product. They are choosing a labelled level. Most usage is designed to sit on Private, which is only as strong as a contract. The paid distinction is TEE and E2EE, which are the modes that match the sentence "no human can read this" with a mechanism rather than a policy. E2EE gives up agent-style tools (search and memory). A respondent who wants both "the model browses for me" and "nobody can see the prompt" is asking for something the E2EE mode does not do. Those are two segments, or two modes of one user, and the research should separate them.

### 1.5 How the service is actually run, because it changes the claim

**Decided direction.** Hybrid hosting. Start on managed zero-retention APIs. Move the steady traffic onto GPUs we rent once volume justifies it. Keep managed providers for spikes, niche models and overflow.

The privacy reason: every managed provider we route through sees the prompt in the clear. Self-hosting is the only setup with full control. The cost reason points the other way at the start. Serverless open models are cheap (DeepSeek V4 Flash about $0.14 input / $0.28 output per 1M tokens, checked 26 October 2026). An H100 at about $3 an hour, serving about 2,500 tokens a second at 60% utilisation, costs about $0.55–0.56 per 1M tokens. Below about 50% utilisation, serverless is usually cheaper. Self-hosting is chosen for privacy, policy control and our own fine-tunes, then for cost once the machines are busy.

| Phase | When | What runs where |
|---|---|---|
| Launch | First 6–12 months, or until inference spend is roughly $50–100k a month | Pay-per-token APIs, plus a few dedicated endpoints. No GPU operations team. |
| Hybrid | Once usage is steady | Reserved GPUs for the main 2–3 models. Managed providers for overflow and the long tail. |
| Scale | Year 3 onward | Mostly self-hosted, possibly partly in the UAE for residency and Gulf latency. Managed providers stay as backup. |

Launch stack the plan assumes:

| Job | Launch | Later |
|---|---|---|
| No-logging proxy | Our gateway (LiteLLM or a custom router). Optionally on a Phala confidential VM. | Same |
| Default Private text | DeepInfra. Zero retention is in their terms. Some models run at FP4; the plan is to pin FP8. | Our own serving (vLLM, SGLang, or TensorRT-LLM) on CoreWeave or Nebius. DeepInfra for overflow. |
| Fast agent steps | Groq, with zero retention switched on. Abuse logs can be kept up to 30 days unless Data Controls opts out. | Same, or self-hosted. |
| TEE / E2EE | NEAR AI Cloud, per token. A Venice partner. Hardware enclaves, signed proof on each response. Acceptable-use policy not yet checked. | Phala confidential GPUs on a reservation. Phala's acceptable-use policy is also not yet checked. |
| Images | fal.ai. Sees prompts. Safety filter on by default. | Flux or SDXL on our GPUs. |
| Frontier | Direct OpenAI, Anthropic, Google APIs, labelled Anonymous. They see and may keep prompts. About $2–25 per 1M tokens. | Same |
| Code sandbox | E2B, about $0.17 an hour for 2 CPUs and 4 GB, Pro plan $150 a month. Terms not yet checked. | Self-hosted E2B. |
| Browser sandbox | Browserbase, about $0.10–0.12 per browser-hour, Startup plan $99 a month. Sees every page. | Not yet decided. |
| Web search | Brave Search API, $5 per 1,000 searches, privacy-positioned, no user profiling. | Same |
| Safe-for-work overflow, especially Teams and coding | Fireworks or Together, only with zero retention actually switched on. Together stores prompts by default. Fireworks' Responses API stores 30 days unless `store=false`. | Same |

Prices and policies were checked on **26 October 2026**. They move. The researcher does not need to re-price GPUs. The researcher does need to know that "private" at launch is a contract with DeepInfra, Groq and fal.ai, and that verifiable privacy is a separate, more expensive mode.

### 1.6 What the product refuses, on every mode

**Decided.** Low refusal on lawful topics. A fixed list is refused even in E2EE, because the classifier sits inside the enclave.

Refused everywhere:

- Sexual content involving minors.
- Non-consensual intimate imagery and sexual deepfakes of real people.
- Meaningful help with weapons, especially chemical, biological, radiological or nuclear weapons.
- Malware and attacks on systems the user does not own.

Also designed out, so the product cannot be used or marketed this way:

- No erotica-tuned or "abliterated" models. System prompts decline explicit sexual content. Some explicit text will still slip through on open models. That is accepted only if the default product does not produce it and the terms ban it.
- Every generated image passes an in-memory nudity classifier. All nudity is blocked, not only illegal nudity.
- No "undress" tools. No editing of an uploaded photo of a real person. No user-uploaded LoRAs or custom checkpoints. No public gallery and no sharing at launch.
- Named real people are blocked in image prompts. There is a takedown process for likeness and trademark claims.
- 18+ with an age check at signup.
- Accounts that keep tripping blocks are suspended. We store a counter, not the conversation, and we say so.
- Marketing does not say "NSFW", "no limits" or "uncensored".

Child-abuse controls, all in memory except the known-image exception above:

| Layer | What it does |
|---|---|
| Prompt classifier | Blocks requests that combine minors with sexual content, in text and in image prompts. |
| Output classifiers | Nudity detector plus an age estimator on every generated image. Flagged images are discarded. |
| Hash matching on uploads | Microsoft PhotoDNA, Thorn Safer, NCMEC hash list, Internet Watch Foundation list. Only a fingerprint is compared. |
| Model choice | Base image models trained on filtered data. No community checkpoints tuned for explicit content. |
| Agent blocklist | The agent cannot open known abuse URLs (IWF and Thorn lists). |
| Reporting channel | A user-facing "report a problem" control. Text-only abuse roleplay cannot be blocked completely on open models. |

This policy is also the payment strategy. Card networks shut accounts that generate prohibited content. Clean marketing and the image controls are what keep a normal merchant account. If a processor instead classes the business as high-risk, payment fees move from the model's 3% to something like 4–8%.

### 1.7 The legal frame that shapes who we can talk to and what we can claim

The company needs UAE counsel plus US, EU and UK coverage. These are the constraints that change research stimuli. They are risks with proposed mitigations, not finished legal opinions.

| Constraint | What it does to the product and the pitch |
|---|---|
| UAE content law | Cybercrime law (Federal Decree-Law 34 of 2021) and media regulation (Federal Decree-Law 55 of 2023) criminalise obscene content, insults to religion, content harming national unity, and "rumours". Pornography is illegal. An "uncensored" AI is exposed even when generation is private. The working mitigation is a free zone (DIFC or ADGM are the candidates), conservative model defaults, no "no limits" marketing, and a question to counsel on geo-restriction. |
| UAE data protection | PDPL (Federal Decree-Law 45 of 2021), or DIFC/ADGM rules, still applies to accounts, email and payments. Conversations are not the store of personal data. Accounts are. |
| EU AI Act | Users must be told they are talking to an AI. Generated images need labels, including machine-readable watermarks. In force for this purpose from August 2026 in the competitor research's legal table. |
| UK Online Safety Act | Chatbots are in scope once users can share content or the product behaves like search. Age checks are strict for pornography. Mitigation: no explicit images, no sharing at launch. |
| US state companion and minor laws | California SB 243 and similar laws cover self-harm and minors. The mitigation is an 18+ gate, crisis-resource responses, and no romantic companion aimed at minors. |
| US non-consensual imagery | Take It Down Act: 48-hour takedown duties for non-consensual intimate imagery were already on the clock for May 2026. Mitigation: no real-person sexual edits, no public gallery. |
| GDPR | Applies to account and payment data of EU users. Needs an EU representative, processing agreements and a transfer mechanism. |
| Law enforcement | We can hand over what we hold, which is mostly account and payment data. The plan is a published request process and, later, a transparency report. We do not promise to resist lawful orders. |
| Agent liability | An agent that browses, fills forms or buys things can break a site's terms, scrape illegally, or be used for fraud. Mitigation: confirmation before purchases and logins, rate limits, a domain blocklist, terms that put the user's instructions on the user. |
| Sanctions | Sanctioned countries are blocked at signup and payment. |
| Model licences | Some weights are non-commercial (Flux "dev") or need a separate licence at very high scale (Llama, above 700 million monthly users). A licence register is part of the product, not a side task. |

### 1.8 What this product is, relative to the tools people already use

**Sourced and decided together.** In a June 2026 US survey of 1,999 adult AI-assistant users, weighted to people who already use an assistant (Zou, 2026):

| Primary assistant | Share |
|---|---|
| ChatGPT | 58% |
| Gemini | 25% |
| Claude | 7%, and about a third of coding tasks |
| Copilot | 4% |
| Everyone else | about 5% |

No privacy product appears in that ranking. The product is designed as the place a person sends the task they will not paste into that primary assistant. It is not designed as the assistant they use for ordinary questions.

The clean competitive set, as of late 2026:

| Product | Position against us |
|---|---|
| Venice.ai | The only private-AI product with scale. Privacy plus an "unrestricted" brand, a large estimated adult and video business, and an API that is most of its revenue. Direct comparison on the privacy mechanic. Poor comparison on who the buyer is, because we will not take the uncensored and adult demand. |
| Proton Lumo | Closest clean brand. Zero-access history, no logs, open models on Proton's own servers. Proton says the model still sees cleartext. There is no enclave. Cheaper than our Pro. |
| Duck.ai | DuckDuckGo strips identity and forwards the prompt to GPT, Claude and others. The provider sees the text. Two open models run in a TEE. Sold only as part of a VPN bundle. |
| Brave Leo | Inside the Brave browser. History on the device. One model routes into a TEE, and the browser still trusts Brave's gateway for the check. |
| ExpressVPN ExpressAI | The precedent of a VPN brand shipping this. Sealed hardware, Cure53 audit, several models, web search, a file vault, included for Pro subscribers. Launched 31 March 2026. |
| Ollama, LM Studio, Apple Private Cloud Compute | Local or on-device. They take the user who will not send the prompt anywhere. Ollama reported 8.9 million monthly developers in 2026, doubled since January, mostly unpaid. |
| Edgeless Privatemode, Fortanix, Opaque, confidential GPUs at Google, Microsoft, AWS, NVIDIA | Enterprise attested inference. This is the later competitor for the API and for Teams, not for the consumer subscription. |

Norton and Bitdefender sell a "VPN for AI agents" that gives each agent task its own network connection. That hides the agent's IP. It does not hide the prompt.

### 1.9 The business the packaging has to pay for

**Model assumption**, base case, so the researcher can see the scale the packages are being asked to reach. USD. The model starts at month 1 of a build, and revenue starts after launch in month 5.

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Revenue | $0.56M | $5.8M | $17.2M | $34.9M | $58.9M |
| Exit ARR | $1.7M | $9.6M | $23.8M | $44.2M | $71.0M |
| Paying subscribers, year end | 6k | 28k | 67k | 122k | 190k |
| Monthly active users, year end | 148k | 506k | 1.06M | 1.74M | 2.54M |

Year-5 revenue split: Pro about $22.5M, Max about $22.5M, API $6.9M, Teams $5.4M, agent credit top-ups $1.6M.

Bear / base / bull at Year 5: revenue $36.3M / $58.9M / $88.2M; paying subscribers 102k / 190k / 305k. The bear multiplies signups by 0.6, conversion by 0.75, churn by 1.25 and inference cost by 1.2. The bull multiplies signups by 1.5, conversion by 1.2, churn by 0.85 and inference cost by 0.85.

EBITDA turns positive in month 33 in the base case. Capital to get there is about $7.8M. Planned funding is larger ($4M seed in month 1, $12M Series A in month 14, $25M Series B in month 30) so the bear case, which needs $24.6M and does not break even inside five years, can survive.

These are not market facts. Section 3 says how they sit against the market that exists.

---

## 2. The pains it is solving

The pains are listed in the order of what buyers will pay, not in the order of what the public debate talks about. Evidence is from a June 2026 discrete-choice experiment on 1,999 US adult AI-assistant users, weighted to the AI-using public (Zou, "Platform Choice, Trust, and Privacy in the Consumer AI Assistant Market", July 2026), unless another source is named. The dollar figures are the monthly price that offsets the feature. They are stated preference, not receipts.

### 2.1 A person might read what was typed

**This is the pain the price has to match.**

| | All tasks | Highly sensitive tasks |
|---|---|---|
| Value of avoiding a human reviewing the conversation | **$11.20 / month** | **$15.24 / month** |

The human in that fear is an employee of the vendor, a contractor, a model provider, an employer who can demand the log, or a government request that lands on stored chats. It is not "the model saw the words in order to answer."

How the product answers it:

- History is in the browser. The server is not the system of record for the conversation.
- The proxy is designed not to store the request.
- Private mode puts a no-retention, no-training contract on the path.
- TEE mode puts the prompt in an enclave the GPU operator cannot read, with attestation.
- E2EE mode encrypts on the device. We cannot read it either.
- The published wording is "no human ever reads them."
- A law-enforcement request can only return what we hold. The plan holds account and payment data, plus the known-abuse-image exception.

What it does not answer:

- On Private mode, a human at the GPU operator *can* read the prompt. The protection is the contract. Marketing that says "nobody can" while the default mode is Private is the false claim the legal page warns about.
- On Anonymous mode, the frontier provider can read and may keep the prompt. The label has to do that work in the interface.
- Launch image traffic is visible to fal.ai.
- Launch browser traffic is visible to Browserbase.
- Groq may keep abuse logs for up to 30 days unless the opt-out is on.
- Together stores prompts unless zero retention is switched on at organisation level. It is not the default path for that reason.
- E2EE cannot search the web or keep memory. The strongest reading protection and the agent are in tension.
- We do not promise to ignore a lawful order for the data we do hold.

**Packaging consequence.** $18 a month is above this $11–15 range by a little and far above the next pain. The feature that earns $18 is the one a buyer can check: attestation, no server-side history, and an independent audit. ExpressAI already has a Cure53 audit and bundles the AI into the VPN. A privacy policy alone does not capture this willingness to pay.

### 2.2 The vendor might train on the chats

| | All tasks | Highly sensitive tasks | Most concerned users |
|---|---|---|---|
| Value of avoiding training | **$2.97 / month** | **$4.35 / month** | about **$7 / month** |

This is the pain press coverage and product marketing usually lead with. In the choice experiment it is worth about a quarter of "no human reads this."

How the product answers it:

- Private, TEE and E2EE paths are specified as no-training.
- Partner contracts have to say no-training in writing, not only on a settings page.
- We do not train on conversations. The only neighbouring case is still unspecified in our own policy; Proton, for comparison, will share anonymised feedback on one open model if the user opts in.

What it does not answer:

- Anonymous mode is the frontier provider's training policy, which we do not control. The label is the mitigation.
- About 60% of US AI users do not know whether their current assistant trains on them. A no-training toggle they cannot see will not be valued at even $2.97.

**Packaging consequence.** Lumo Plus is $12.99, or $9.99 a month on an annual plan. Duck.ai's bundle starts at $9.99 and cannot be bought as AI alone. Brave Leo Premium is $14.99. Those prices already cover a $3 promise. We should not brief research as if "no training" is the reason to pay $18.

### 2.3 Sponsored answers and a product that is working for someone else

Value of avoiding sponsored answers: **$6.46 a month**, and it does not rise on sensitive tasks.

ChatGPT has an ads business (reported past $1 billion annualised within 200 days of launch). Our plan has no advertising product and no crypto incentive. The financial model is subscriptions, usage credits, an API and seats.

This pain matters in research as a reason people leave a free assistant, and as a reason a paid private plan can be compared with "the free one, with ads." It is not a feature we are building. It is an absence.

### 2.4 People are worried and still do not move

Same US study:

- More than **80%** are concerned about how conversation data is used.
- Concern is flat across demographic groups.
- About **60%** do not know whether their assistant trains on their chats.
- Only **18%** have ever paid for a plan with better privacy protection.
- Knowing the training policy predicts protective behaviour more than the level of worry does. Policy literacy is associated with 0.34 more protective tools adopted. A point of concern on a five-point scale is associated with 0.17.
- Price is the primary reason in **38%** of the hypothetical plan choices. Privacy can differentiate a plan. It does not replace a tolerable price.
- Protective behaviour falls with age. Literacy about training also falls with age. Higher education and lower income are associated with more protective actions.

A UK survey of 211 conversational-agent users (PoPETs 2025) finds the same gap from the other direction. People are reluctant to put sensitive information into the tool and still do, because the useful answer requires the disclosure. They reported 1.4 protective behaviours out of 8 on average. The common ones were deleting history (31%) and stripping sensitive details out of the prompt (27%). About a quarter had read the privacy policy. Beliefs about what deletion and training opt-out actually do were often wrong.

**What this means for the product.** The job is not to persuade a worried person that privacy matters. They already think it matters. The job is to make the protection legible at the moment they are about to paste something sensitive, and to make the paid step small. The mode label, a no-account way to try one chat, and a price near the $10–15 neighbours are the product responses. Whether that closes an 18% "have ever paid" gap is unmeasured. It is the main conversion question in section 5.

### 2.5 The sensitive task is stuck on a tool they do not trust with it

The tasks named across the market work are legal, health, finance, and documents a person would not want an employer to see. Valuations rise with stakes: human-review protection goes from $9.45 on non-sensitive tasks to $15.24 on highly sensitive ones, and training protection from $2.42 to $4.35.

Users already split tasks across tools. Claude is the primary assistant for 7% of US users and takes about a third of coding tasks. Trust in that study is earned by using a product, not by its reputation. Claude is ranked most trustworthy in every head-to-head among people who have used both tools, and it has the widest gap between how its users and its non-users rate it.

How the product answers it:

- A separate place, with a different data handling story, for the prompt they are currently self-censoring or not sending.
- Open-weight models on the private path, so the answer does not require a frontier provider.
- Anonymous mode when they want a frontier model and will accept that the provider sees the text, as long as their identity is not attached.
- Premium models inside Max, for the quality gap. The model assumes 10% of tokens go to premium closed models at about $4 per 1M tokens, against about $0.35 per 1M for the open path.

What it does not answer:

- If the private model is worse at the job, the user keeps the sensitive task on ChatGPT and self-censors, which is what the UK study already sees. Quality is why a privacy product stays a second tool. Research should test the task with the actual model, not with a privacy slogan.
- We do not have memory on E2EE, so a long-running legal or medical thread that depends on server memory cannot use the strongest mode.
- We are not a system of record. A lawyer or clinician who needs a retained file for their own professional duty is a different buyer from a person who wants no file to exist. Teams' "private deployments" is the closest feature, and it is month 15, lightly specified.

### 2.6 An agent trace is worse than a chat log

**Decided product, inferred pain.** Agent mode is in the product because multi-step work is where assistants are going (the personal-assistant market's own write-ups put autonomous agents at the centre of the next leg of growth). The privacy pain gets sharper when the stored object is not one prompt.

A stored agent trace can include the plan, the pages opened, the files touched, the code that ran, and the tool calls. Norton's and Bitdefender's agent VPNs cover the network identity of that session. They do not cover the contents. That is the opening.

How the product answers it:

- The same no-storage rule as chat.
- Browser and code execution happen in sandboxes (Browserbase and E2B at launch), not on our application servers as a retained workspace.
- Search goes through Brave, which is positioned as search without a profile of the user.
- Confirmation is required before the agent buys something or logs in. Rate limits and a domain blocklist are part of the design. The terms put the user's instructions on the user.
- The agent cannot open known child-abuse URLs.

What it does not answer:

- Browserbase sees the pages at launch. E2B's terms have not been checked.
- Tool use and web search are incompatible with E2EE as specified.
- Pro includes only 10 agent tasks a month after launch of the feature. Max includes 60. A heavy agent user is a Max buyer, or a top-up buyer. Someone who needs an agent every day and also needs E2EE is not served by the current spec.

The model thinks this is where the money and the cost both sit. Once Max exists, 25% of new paying users take it. Agent tokens are about 80% of a Max user's inference cost. A Max user costs about $14.40 a month to serve by the end of Year 2, against about $3.50 for Pro.

### 2.7 Lawful questions come back refused

**Decided, and narrower than Venice's version of this pain.**

Venice's acquisition language is "private and unrestricted," and its US search demand includes "uncensored ai" (about 40,500 searches a month) and "uncensored artificial intelligence" (about 33,100) in a September 2026 Semrush pull. Its comparison pages market adult roleplay. The clean-versus-adult split of Venice's revenue is an estimate: at a $150M base, about 31% adult, 16% uncensored-but-not-adult, 53% clean.

Our product's version of the refusal pain is: a competent adult asking a lawful question should get an answer, including questions that are frank, technical, or uncomfortable. The product will not be the place that removes safety to attract the uncensored and adult audience.

Research should test refusal on lawful sensitive topics (a health question, a legal hypothetical, a security explanation the user is allowed to hear). It should not test, or recruit for, NSFW generation, jailbreaks, companion roleplay, or nudify. Those buyers are out of the market we are sizing. Putting them in will make willingness to pay look larger and will describe a product we will not ship. It also collides with UAE content law and with the payment-processor strategy.

### 2.8 Identity is attached to the prompt, even when the vendor is well behaved

Some buyers are less worried about a human at the lab and more worried that the prompt is tied to their account, their IP, or their employer.

| Mode | What happens to identity |
|---|---|
| Anonymous | Identity is stripped. The text is not. |
| Private | The user is our customer. The inference partner is not supposed to receive identity. The contract has to be checked per provider. |
| TEE / E2EE | The prompt is unbound from operator visibility. Account and payment records still exist for a paying user. |
| Free, no account | Specified for the start of a Venice-style funnel in the competitor note's recommendations ("no-sign-up AI trial"), and history-in-the-browser makes a no-account session possible. Our own tier table does not yet say whether Free requires an account. Age check is specified "at signup", which implies an account exists before the gate. This is unresolved. |

Duck.ai's entire product is the identity-stripping version. If research finds that "don't attach my name" is the whole job, Duck's bundle at $9.99 is the relevant package, and our TEE work is over-built for that buyer.

### 2.9 Pains we are not solving

Stated so a screener can exclude them.

| Pain | Why it is out |
|---|---|
| "I want adult, NSFW, or erotic generation." | Not designed, not marketed, images blocked, terms ban it. |
| "I want a companion or a character that remembers me." | No companion product. E2EE has no memory. US companion-chatbot laws are a reason to stay out, on top of the content decision. |
| "I want to edit a photo of a real person, or remove their clothes." | Feature is not built. Named real people are blocked in image prompts. |
| "I want an uncensored model with the refusals stripped." | We will not serve abliterated models. Lawful frank answers are in scope. Refusal-free models are not. |
| "I want the vendor to keep my archive and produce it for a lawsuit, a medical record, or a regulator." | We are built to have nothing to produce except account and payment data. A retention buyer needs a different product. Teams' private deployments might become that, and today they are a line on a tier, not a spec. |
| "I want local AI on my laptop and I will not send a prompt." | Ollama and LM Studio already do this, mostly for free. We are a hosted product. |
| "I want a token, yield, or airdrop." | No token. Venice uses VVV, staking and burns as retention. We do not copy that. Dubai's VARA regime is the other reason. |

---

## 3. The segments

The wiki does not contain a finished segmentation study. What follows is every cut the product, the model and the market work actually use, with the tag that says whether it is a decision or a hypothesis. The researcher should treat section 3.2 and 3.3 as the segments to go and measure, and section 3.4 as people to exclude from the sample.

### 3.1 Cuts that are already decided

**Adults only.** 18+, age check at signup. The product is not for minors, and it is not a romantic companion.

**Clean confidentiality, worldwide, from a UAE company.** The buyer is someone whose reason is confidentiality: no logs, no training, encrypted or attested inference, anonymity, sensitive work. The company is assumed to sit in the UAE, likely a free zone. Users are expected from many countries. Sanctioned countries are blocked. Counsel may add geo-restrictions. Gulf users are a later hosting consideration (in-region capacity, UAE law, so the local deployment is safe-for-work only), not a decided beachhead.

**Four commercial motions, in this order.**

| Motion | Who | Opens |
|---|---|---|
| Consumer free and Pro | An individual who will try chat and images and may pay $18. | Month 5 |
| Consumer Max | An individual whose usage, or whose agent use, does not fit Pro. | Month 7 |
| Developer API | A developer or agent product calling an OpenAI-compatible endpoint. | Month 9 |
| Teams | A company buying seats, SSO, admin, and a private deployment. | Month 15 |

Research that mixes a developer API buyer with a consumer chat buyer will average two willingness-to-pay figures into a useless one. They are specified as different products, different months, and different competitors.

### 3.2 Consumer job segments to test

These are the jobs named by the market definition and the pain evidence. None of them has a measured size inside PureVPN's base or in the general population. They are the screener.

**Segment A. Sensitive-task individuals.**

The person already uses ChatGPT, Gemini, Claude or Copilot. They have at least one recurring task they consider highly sensitive: a legal question, a health question, a financial question, or a work document they would not want an employer, a platform reviewer, or a government request to see. They either self-censor the prompt, strip names out of it, delete the thread afterwards, or avoid the tool for that task.

What we need to learn:

- Which of those four task types they actually have, and how often. Frequency decides whether they need Pro every month or a tool they open twice a quarter. The model assumes Pro churn of 6% a month and Max churn of 5% a month. Occasional use can be worse than that.
- Whether the fear is a human reading it ($11–15) or training ($3–7) or both.
- Whether they need web search and memory. If they do, E2EE is the wrong mode to show them, and Private or TEE is the concept.
- What quality they will tolerate relative to their primary assistant, on that exact task.
- Whether they will pay $10, $13 or $18. The price test is the single most useful study. $10 sits with Duck.ai's bundle and Lumo's annual price. $13 sits with Lumo monthly. $18 is our Pro list price and Venice Pro.
- Whether an audit or an attestation demo moves them between those prices. This is the difference between capturing the $3 pain and the $11 pain.

This segment is the core of the consumer plan. Year-5 Pro plus Max is about $45M and 190,000 paying subscribers in the base case.

**Segment B. Existing privacy subscribers, especially PureVPN.**

The distribution idea in the competitor work is that a VPN buyer already paid to keep their traffic from being tied to them, and a private assistant is the same instinct applied to prompts. ExpressAI has already shipped a version of this to ExpressVPN Pro subscribers. Duck.ai sells the AI only inside a VPN bundle.

PureVPN facts the researcher can and cannot use:

| Fact | Status |
|---|---|
| Public revenue band $50–75M through September 2026 (Similarweb) | Sourced, and it conflicts with a separate 2025 profile at $10M. Do not pick one silently. |
| Last company-published user milestone is 1 million users, in 2015–16 | Sourced. Not a current subscriber count. |
| Working estimate used in the market page: about 1 million current subscribers if revenue is $60M and effective price is about $60 a year | **Estimate, low confidence.** |
| 5% of that base on an $18 plan is about $11M of AI ARR. 10% is about $22M. 15% is about $32M. | Arithmetic on the estimate above. |
| The model's 190,000 paying subscribers is larger than a 15% attach on today's estimated base | So the plan also needs the VPN base to grow, and some buyers who are not current subscribers. |

What we need to learn, from PureVPN's own customers if the researcher can field there:

- How many would add private AI at $10, $13 and $18, as a bundle line versus a separate subscription. ExpressAI is included in the VPN subscription. Duck.ai cannot be bought alone. Our plan currently prices AI as its own subscription. Those are three different packages and they should all be in the test.
- Which job they think it is. A VPN buyer who wants "hide my IP from the model vendor" is segment B's version of pain 2.8. A VPN buyer who pastes contracts into ChatGPT is segment A, reached through a VPN login. The product work is different.
- Country and language. Venice's traffic is heaviest in the US (Similarweb about 40%, Semrush about 25% in the September 2026 pulls), then India, Mexico, Canada and Germany, with Semrush also showing Bangladesh at about 9%. The competitor note suggested Hindi, Bengali and Portuguese pages because Venice publishes in English, German and Spanish only. That is a channel hypothesis, not a decision to target those countries.

**Segment C. The agent user.**

Someone whose work is multi-step: research across sites, pull facts into a draft, run code, repeat. They are in the plan as Max, plus a thin allowance on Pro, plus credit top-ups.

Model assumptions that describe this person, and that research should try to falsify:

| Assumption | Value |
|---|---|
| Share of new paying users who pick Max once agents exist | 25% |
| Agent tasks included | 10 a month on Pro, 60 on Max |
| Extra spend | 20% of Max users buy about $15 a month of top-up credits |
| Tokens per agent task | 0.25 million |
| Max chat tokens | 3 million a month, against 1.5 million on Pro and 0.15 million on Free |
| Max images | 500 a month in the cost model. The product tier table does not state an image cap for Max. |

The privacy question for this person is pain 2.6. The commercial question is whether 60 tasks a month is the right fence between Pro and Max, or whether agent users want a meter they can buy by the task from day one. Venice sells that meter as credits (100 credits = $1) and makes most of its revenue there. Our top-up is a side line ($1.6M of Year-5 revenue), not the business.

**Segment D. The quality-seeking private user.**

A person who will pay inside Max for "premium models" because the open model failed a task they care about. The model sends 10% of tokens down that path. In the product, those requests are Anonymous unless we have a premium model that can run inside Private or TEE. Today the frontier providers only fit Anonymous.

Research should show the mode label next to the premium model and ask whether the person still sends the sensitive document. If they will not, then "premium models" do not belong in the sensitive-task segment. They belong to a less sensitive, higher-willingness-to-pay usage segment, and the two should not share one Max story.

### 3.3 Business segments to test later

These are in the plan. They are the wrong sample for a consumer concept test.

**Segment E. Developers and agent products on the API.**

Opens month 9. OpenAI-compatible. Usage-based markup on inference. There is no rate card yet.

The model assumes 0.1% of signups become API accounts, spending $60 a month at the start, that spend growing 15% a year, and 4% monthly churn. Year-5 API revenue is $6.9M. That is a small developer business.

The market context is larger and is mostly not ours to claim:

- Venice's clean developer and coding API is estimated at about $32M a year, inside a company whose credits and API are roughly 65–81% of revenue (about $95–105M). A large share of Venice's API demand is entangled with uncensored and video use. The clean coding portion is the part that overlaps us.
- Privacy-preserving inference as a category is **sourced** at $225M in 2026 and $1.78B in 2031, 51% a year (Knowledge Sourcing). Managed private-inference APIs are projected at about $650M of the 2031 total. Competitors are Edgeless, Fortanix, and the hyperscalers' confidential GPUs.
- Ollama's 8.9 million monthly developers show that a large technical audience will self-host rather than pay an API, once the open model is good enough for agents and coding.

What a later study needs: will a developer pay a markup, and how much, for an OpenAI-compatible endpoint with a contractual no-retention mode versus an attested TEE mode. Our consumer price test does not answer that.

**Segment F. Teams and regulated buyers.**

Opens month 15. $40 per seat per month. Shared workspace, SSO, admin controls, private deployments.

The model assumes 150 new seats in month 15 and new-seat volume growing 4% a month. Year-5 Teams revenue is $5.4M.

The buyer in the enterprise "private AI" reports (healthcare, finance, government, on-premise, 68% large enterprise in the Dimension Market Research cut) is this segment's neighbour and is easy to confuse with it. Those reports size software and hardware those companies buy from IBM, Microsoft, Palantir, Oracle and NVIDIA. A $40 seat with SSO is a small product next to that. Research for Teams should be framed as "a hosted assistant your staff can use on sensitive internal text, with admin control and a deployment you can diligence," and the willingness to pay should be allowed to come back as "we will only buy this if it runs in our tenant." The spec's phrase "private deployments" is where that answer has to land. It is not designed yet.

Regulated individual professionals (a lawyer, a clinician, an adviser) may look like segment A in a survey and like segment F in procurement, because their firm has to sign. Ask who pays and who signs.

### 3.4 People who are not a segment

Exclude from screening, from paid acquisition concepts, and from market-size builds.

| Group | Reason |
|---|---|
| Under 18 | Age gate. Companion-chatbot legal exposure. |
| NSFW, erotic roleplay, companion, character apps | Content policy. A large piece of Venice, Character.ai and Janitor AI demand. Out. |
| "Uncensored", jailbreak, abliterated-model seekers | Venice sells this. We do not. US search demand is real and is not our TAM. |
| Undress, nudify, real-person sexual edits, deepfakes | Feature ban and the law. |
| Buyers who need a retained archive for professional or legal duty | Conflicts with the no-storage promise, until and unless private deployments are specified as a retention product. |
| Sanctioned countries | Blocked at signup and payment. |
| Token and airdrop audiences | No token. |

Venice's own estimated mix is the illustration of how large the excluded part is. At a claimed base above $150M a year (October 2026), the clean portion is about $80M (range about $55–100M) and the clean consumer and creator portion is about $30–50M. The rest is adult, uncensored, or developer API. Our consumer market is that $30–50M slice plus the smaller clean brands, together about **$40–80M a year**, not Venice's headline number and not the $11.1B enterprise "private AI" market.

### 3.5 What the model assumes about how segments convert

These are the funnels the packages are built on. They are **model assumptions**. The researcher is being asked to replace them, not to confirm them by default.

| Step | Assumption |
|---|---|
| Organic signups in the launch month | 10,000 |
| Organic signup growth, month on month, Years 1 to 5 | 12%, 8%, 5%, 3%, 2% |
| Paid marketing per month, Years 1 to 5 | $40k, $120k, $250k, $420k, $650k |
| Paid cost per signup | $3 |
| A signup pays in the first month | 2.5% |
| The free base converts each month | 0.25% |
| Free users leave each month | 15% |
| Pro churn per month | 6% |
| Max churn per month | 5% |
| Paid users on an annual plan | 35% |
| Annual discount | 31% |
| New payers who take Max after month 7 | 25% |
| Max users who buy top-ups | 20%, at about $15 a month |
| Signups who become API accounts | 0.1% |

A 6% monthly Pro churn keeps roughly half a cohort after a year. If segment A uses the product only when a sensitive task appears, churn is the assumption most likely to be wrong, and it moves Year-5 subscribers more than the signup forecast does.

Context the researcher should hold next to the 2.5% conversion assumption:

- At the end of 2025, about 6% of ChatGPT's then 800 million users paid. That is a mature default assistant, not a second tool.
- Only 18% of US AI users have *ever* paid for better privacy, which is a lifetime action, not a first-month conversion, and it includes people whose "privacy plan" is ChatGPT Plus rather than a separate product.
- Venice's average subscription, measured by Spartan Group, is $23.06, against a Pro price of $18. Most payers take Pro. Venice also has the uncensored and adult audience we are excluding, so its conversion is an upper reference, not a target to copy.

### 3.6 Where the Year-5 plan sits, so segment targets stay honest

| Comparison | Figure |
|---|---|
| Clean consumer private AI, late 2026 | About $40–80M a year. **Estimate**, low–medium confidence. |
| Our Year-5 Pro + Max revenue | About $45M. **Model assumption.** |
| That $45M as a share of today's clean pool | The whole pool, at the middle of the range. |
| If the pool grows at 40% a year (personal-assistant rate) | A $50M start is on the order of $150–400M by 2030–31, depending on the start inside $40–80M. $45M is a leading share. |
| If it grows at about 20% (consumer VPN pace) | The Year-5 subscriber count does not fit. |
| Venice's 2026 run rate | $14M in January to over $150M by 14 October. A spike. Do not use it as the segment growth rate. |
| Privacy-preserving inference, for segments E and F | $225M in 2026, 51% a year. Our Year-5 API plus Teams is about $12.3M, which is a small share of that category and does not require heroic assumptions. The consumer plan is the one that requires a leading share. |

---

## 4. Products and packaging

Two layers get confused in conversation. **Capabilities** are chat, image, code, agent, API and Teams (section 1.3). **Packages** are the things a person or a company can buy. This section is the packages: price, what is in the box, what is metered, how they step up, and how the neighbours package the same job.

### 4.1 The range

**Decided prices and inclusions, except where a cell is marked as only a model assumption.** Blank cells are unspecified. Do not invent them in a survey stimulus. Ask, or leave them out.

| | Free | Pro | Max | API | Teams |
|---|---|---|---|---|---|
| Price | $0 | $18 / month | $49 / month | Usage-based markup on inference. No rate card. | $40 / seat / month |
| Annual option | None stated | About 31% off if the buyer pays annually. See 4.2. | Same discount. | Not stated. The model treats API as monthly usage. | Not stated. |
| When it exists | Month 5 | Month 5 | Month 7 | Month 9 | Month 15 |
| Chat | Rate-limited. The message cap is **not specified**. The model provisions 0.15M tokens a month. | Higher limits. Message cap not specified. Model provisions 1.5M tokens a month. | Higher still. Model provisions 3M chat tokens a month. | OpenAI-compatible endpoint. | Seats inside a shared workspace. Per-seat usage caps not specified. |
| Images | About 30 a month | 300 a month | Not on the product tier table. The cost model uses 500 a month. | Not specified. | Not specified. |
| Code | Included in chat | Included in chat | Included in chat | Included if the endpoint serves a code model | Included |
| Agent | None | 10 tasks a month, only after agent mode exists (month 7) | 60 tasks a month | A caller can build their own agent on the API. Our hosted agent is a consumer feature. | Not specified |
| Premium / frontier models | Not included. Default path is open-weight Private. | Not listed as a Pro feature. | Included, under the name "premium models." Share and which models are not set. Model assumes 10% of tokens at premium rates across the business. | Whatever the rate card eventually lists, each endpoint labelled with its mode. | Not specified. Teams traffic is the one place the hosting note names Fireworks or Together as a safe-for-work backup. |
| Privacy modes | Private by default. Anonymous only if we choose to expose frontier models on Free, which is not decided. TEE and E2EE are marked Pro. | Private, plus TEE and E2EE. | The spec does not say Max adds a privacy mode that Pro lacks. Treat TEE and E2EE as paid features, available from Pro upward, until that is written down. | Mode is a property of the endpoint, not a line item. | Private deployments are named and not specified. SSO and admin are named. |
| Top-ups | No | Not the plan. Pro's overage path is not specified. | Credit top-ups. Model assumes 20% of Max users spend about $15 a month. | Usage-based already. | Not specified |
| Admin, SSO, shared workspace | No | No | No | No | Yes |
| Age | 18+ at signup. Whether Free can be tried before signup is unresolved. | 18+ | 18+ | 18+ / business terms not drafted | Business terms not drafted |

Effective price after the annual mix, **model assumption**, end of Year 2, used for margin maths: Pro **$16.05** a month, Max **$43.68** a month. That blend assumes 35% of paid users take the annual plan.

Cost to serve at that point, same model: Pro about $3.50 (gross margin about 78%), Max about $14.40 (gross margin about 67%). Max is the thinner package because agent tokens dominate its cost. A packaging change that raises Max agent use, or pushes more tokens to frontier models, hits margin before it hits Pro.

### 4.2 Annual billing

**Model assumption, and it does not match Venice as cleanly as the product page says.**

The product page says annual plans are discounted about 31%, "matching Venice Pro's annual pricing." The model uses a 31% discount and 35% of paid users on annual plans.

Venice's published Pro price, in the competitor research, is $18 a month or $216 a year. That annual price is 18 × 12. It is not a 31% discount. The same research says Venice's yearly billing saves up to about 16.7%. Spartan measured Venice's average subscription at $23.06, with most payers on Pro.

So:

- Our list prices for monthly Pro ($18) match Venice Pro.
- Our annual discount is deeper than Venice Pro's published annual price.
- The "matching Venice" phrase in the product page should not be repeated to respondents as a fact about Venice.

Cash timing: annual plans are billed upfront. The profit-and-loss model does not show that deferred-revenue benefit. For a packaging study, the relevant point is simpler. Annual is how we ask a 6% monthly churn cohort to prepay. If segment A is an occasional user, annual prepay will be a hard sell, and the 35% annual mix will be high.

UAE VAT of 5% on B2C digital services is treated as a pass-through. Prices above are before that conversation with the user. Do not show a VAT-inclusive and a VAT-exclusive price as if both were the plan.

### 4.3 What each package is for

**Free.** The trial of Private-mode chat and a small image allowance, so the sensitive task is not the first time someone opens the product. No agent. The model needs a large free base (148,000 monthly active users by the end of Year 1, 2.54 million by Year 5) because first-month conversion is only 2.5% and the free base converts at 0.25% a month. Free is therefore a distribution package, not a revenue package. Venice's free tier, for comparison, is 10 text prompts and 15 images a day, base models, and no signup to start. Ours is specified as about 30 images a **month**, which is a much tighter image allowance, and the daily or monthly chat cap is unwritten. That gap should be closed before anyone tests "is the free tier generous enough to form a habit."

**Pro, $18.** The main consumer product. Higher chat limits, 300 images, and, from month 7, 10 agent tasks. TEE and E2EE live here. This is the package aimed at segment A. It is the package that has to earn the human-review willingness to pay, because the training-only willingness to pay does not reach $18.

**Max, $49.** The heavy package. 60 agent tasks, premium models, and a top-up path. Aimed at segment C, and at segment D if premium models survive the mode-label test. In Venice's range the steps above Pro are much higher and are credit bundles: Pro+ is $68 with 7,500 credits, Max is $200 with 22,500 credits. Our Max is a usage tier at $49, not a credit bundle. That is a deliberate shape only if we want a simple subscription. It is a weak shape if the research shows agent users want to buy tasks one at a time. The top-up ($15, taken by 20% of Max) is the current answer, and it is a small one.

**Top-ups.** Not a standalone product. A Max add-on. Price per credit, expiry and rollover are not specified. Venice's credits roll over (two months on Pro+, three on Max) and are the majority of Venice's revenue. If the researcher tests overage, they should test three mechanics: a hard stop at the allowance, an automatic top-up, and a cheaper "buy a pack of agent tasks" that does not require Max. We do not have a preference written down beyond "Max users can buy credits."

**API.** A developer product, not a consumer fair-use tier. OpenAI-compatible so an existing agent or coding tool can point at us. Price is a markup on what inference costs us. There is no credit currency. The model's $60 a month average spend is a placeholder for a small account, not a price. Positioning against Venice's API (100 credits = $1, and a large share of Venice's $100M-plus credit run rate) and against Edgeless's attested OpenAI-shaped API should wait until we know whether the buyer is paying for compatibility, for no-retention, or for attestation. Those are three markups.

**Teams, $40 a seat.** A company package: shared workspace, SSO, admin, private deployments. It is not "Pro, times n." The $40 price is below Max and above Pro, per person, and it buys administration rather than more agent tasks. Per-seat allowances are not set, so a concept test can describe the controls and should not invent a usage bundle. Private deployment is the feature a regulated buyer will interrogate. Until it has a one-paragraph definition (whose GPU, which country, who can read prompts, whether chats are retained for the company), it should be described as "available, details in discovery" rather than demonstrated.

### 4.4 How the modes sit on the packages

The mode is not a sixth product. It is a property of a request, and it is how Pro justifies a higher price than a no-training chatbot.

| Request the user is making | Mode we should be selling them | Package |
|---|---|---|
| Everyday question, quality first, identity detached is enough | Anonymous, if we offer it | Any tier we choose to put frontier models on. Cost sits in the 10% premium-token assumption. |
| Sensitive draft, user accepts a contractual promise | Private, the default | Free and Pro |
| Sensitive draft, user wants hardware proof and still wants search | TEE | Pro and, by assumption, Max |
| Sensitive draft, user wants nobody, including us, to be able to read it, and does not need search or memory | E2EE | Pro and, by assumption, Max |
| Multi-step research or code | Private or TEE. E2EE cannot do this as specified. | Pro for a light user (10 tasks), Max for 60, top-up past that |
| A company that must diligence the deployment | Not a mode. A Teams private deployment. | Teams, month 15 |

Showing all four modes to every respondent will produce a preference for E2EE and a complaint when search disappears. The concept test should attach the limitation to the mode in the same sentence as the benefit.

### 4.5 Neighbour packaging, so our boxes are not tested in a vacuum

Prices checked in October 2026 from the pages cited in the market and Venice notes.

| Product | Free | Paid | What the paid step actually buys | Privacy they can honestly claim |
|---|---|---|---|---|
| **Ours, planned** | Rate-limited chat, ~30 images a month, no agent | Pro $18; Max $49; API usage; Teams $40/seat | Allowances, TEE/E2EE, agents, premium models on Max, admin on Teams | "No human reads, we don't store," with mode labels. Private is contractual. TEE/E2EE are the proof. Launch images and launch browsing have extra parties in the path. |
| Venice | 10 text and 15 images a day, base models, can start with no signup | Pro $18 ($216/year). Pro+ $68. Max $200. API: 100 credits = $1. Average subscription $23.06 | Unlimited text, a large image allowance (1,000 a day on Pro), credits, TEE/E2EE on Pro. Higher tiers are credit bundles with rollover. | Same four-mode architecture, which we copied. Also an unrestricted and adult brand we are not copying. No independent no-logs audit found. |
| Proton Lumo | Usable without an account, tight limits on the better model, history and images | Plus $12.99, or $9.99 a month yearly ($119.88). Professional about $11.99–14.99 per user. A wider Proton bundle exists. | More of the better model, history, images, projects | Zero-access encrypted history, no logs, no training, models on Proton's servers. Proton's own writing says the model sees cleartext. Not an enclave. |
| Duck.ai | Free daily cap, unpublished, no account | Plus $9.99 or $99.99 a year. Pro $19.99 or $199.99 a year. Both include a VPN, personal-information removal and identity-theft restoration. AI cannot be bought alone. | Larger models (Claude and GPT tiers), plus the VPN bundle | Identity stripped. Providers see the text, agree not to train, and delete within a stated window that DuckDuckGo describes differently on different pages. Two open models in a TEE the user cannot verify themselves. |
| Brave Leo | Inside Brave, no account, "reasonable" rate limits | Premium $14.99, or $149.99 a year | Higher limits and model choice | History on device. Most models: the inference host sees the prompt. One model in a TEE, gateway still trusted. |
| ExpressAI | Not a public free tier. Included for ExpressVPN Pro. | The VPN subscription. A launch promotion framed the whole Express suite at $4.87 a month. 500 daily credits, 2 GB vault, 50 MB file cap in the launch description. | Several models, web search, file vault, included rather than sold | Sealed hardware, zero access, no training, Cure53 audit. The strongest "a VPN brand already did this" package. |
| Ollama | The desktop app is free | A cloud subscription for larger models was described around the 2026 round, from free up to about $100 a month, billed on GPU time. Revenue not disclosed. | Hosted capacity, not a privacy upgrade. Local is already private. | On-device for the local product. |

Reading the column of paid prices: the clean no-training products cluster at **$10–15**. Venice Pro, which adds TEE/E2EE and an unrestricted brand, is **$18**. Our Pro copies the $18 and the TEE/E2EE and refuses the unrestricted brand. ExpressAI's lesson is that a VPN brand can choose not to charge for the AI separately at all.

A useful conjoint, if only one study is fielded, is therefore:

- Price: $0 bundled into a VPN plan the respondent already pays, $10, $13, $18, $49.
- Proof: "we don't train," "we don't store and no human reads, by policy," "hardware attestation," "independent audit."
- Tools: chat only, chat plus images, chat plus a metered agent.
- Limit: the E2EE option shown once with search, and once without, so the trade is visible.

That design covers segments A, B and C without pretending Teams and the API are the same purchase.

### 4.6 Allowances the model uses, and that a stimulus should not exceed

If a concept describes "unlimited," the model does not. These are the planning allowances. They are also the costed product. A research concept that promises unlimited agents will test a product the model does not believe it can afford. Max's margin is about 67% at the allowances below, and agent tokens are 80% of that user's inference cost.

| Meter | Free | Pro | Max |
|---|---|---|---|
| Chat tokens a month | 0.15 million | 1.5 million | 3 million |
| Images a month | 30 | 300 | 500 in the cost model only |
| Agent tasks a month | 0 | 10 | 60 |
| Tokens per agent task | — | 0.25 million | 0.25 million |
| Image cost assumption | $0.004 | $0.004 | $0.004 |
| Sandbox plus search, per agent task | — | about $0.06 in the model, and closer to $0.02–0.03 on the later check | same |

Usage per user is assumed to grow 15% a year, and unit token cost to fall 30% a year. Those two assumptions are why margins recover. They are not features.

Open-model serving is costed at $0.35 per 1M tokens blended. Premium closed models at $4 per 1M, on 10% of tokens. Payment processing at 3%, with a stated risk that it becomes 4–8% if the content stance is judged high-risk. That risk is why the exclusions in section 3.4 are a packaging decision and not only a brand decision.

### 4.7 What is not for sale

- No token, staking, or burn mechanic.
- No advertising tier.
- No per-mode surcharge written down. TEE costs us more (NEAR's published token prices are far above DeepInfra for several models) but the user pays for it inside Pro and Max, not as a line item.
- No family or household plan. Duck.ai's terms, for comparison, are personal and non-shareable. We have not said.
- No student, NGO, or regional price.
- No on-premise appliance. "Private deployments" on Teams is the only gesture at it.
- GPU capacity is rented in the model. We are not packaging hardware.
- Free does not include the agent, and Pro's agent allowance does not exist before month 7. A launch study in the first two months of the product should not show agent mode as a current Pro feature.

### 4.8 Launch sequence, because packaging research has a clock

| Month | What a respondent can actually be sold |
|---|---|
| 1–4 | Nothing public. Build. Pre-launch cost in the model is about $0.65M. |
| 5 | Free and Pro. Chat, image, code. Private mode. TEE/E2EE if the NEAR path is ready; the tier table includes them on Pro, the hosting plan treats them as a provider choice that may lag. |
| 7 | Agent mode, the 10-task Pro allowance, and Max at $49. |
| 9 | API. |
| 15 | Teams at $40 a seat. |

A study run for a launch campaign should use month-5 packaging only, and can use month-7 packaging as a "coming" concept if the question is whether agent mode is why someone picks this over Lumo. It should not use Teams as a launch message.

---

## 5. What the research is for

The four sections above are the brief. These are the measurements that would change a decision, in the order they change the plan. Sample frames follow from the segments.

| # | Question | Segment | Decision it feeds |
|---|---|---|---|
| 1 | At $10, $13 and $18, what share of PureVPN subscribers add a private assistant, bundled versus billed separately? | B, and A inside B | Whether 190,000 payers is a plausible attach, and whether AI is a product or a VPN feature. |
| 2 | On a real sensitive task, does "no training," "no human reads, by policy," attestation, or an audit move the same person between those prices? | A | Whether Pro at $18 has a reason to exist above Lumo and Duck.ai. |
| 3 | Does that person still send the document when the better model is labelled Anonymous? | A and D | Whether premium models belong in the sensitive-task product. |
| 4 | How often does the sensitive task happen, and do they want search and memory on it? | A | E2EE versus TEE, and whether 6% monthly churn is credible. |
| 5 | Is the agent a reason to pay $49, or a meter they want to buy by the task? | C | Max versus a credit pack. Pro's 10 included tasks. |
| 6 | Will a developer pay a markup for no-retention, for attestation, or only for a cheap OpenAI-compatible endpoint? | E | Whether the API is a business. Not required before the consumer test. |
| 7 | Who signs for a professional user, the person or the firm, and do they require retention? | A versus F | Whether Teams is a seat product or a deployment product. |

Until question 1 and question 2 have answers, the Year-5 consumer revenue of about $45M is the case in which this brand becomes one of two or three clean private assistants. It is not a base case the current market measures support on their own.
