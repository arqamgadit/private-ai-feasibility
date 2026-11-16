# Proton Lumo teardown and growth playbook

[Back to wiki home](../README.md)

**Research date:** 16 November 2026 (Asia/Dubai).

A sourced teardown of Proton's privacy AI assistant, how it is monetized inside the Proton suite, and what PureVPN should copy or avoid. Lumo is a consumer and business product, not a developer API business. Estimates are labeled. Research as of 16 November 2026, Asia/Dubai.

> **The lesson for PureVPN** Lumo is not a Venice-style standalone AI company. It is a privacy-suite feature designed to raise switching costs and ARPU inside Proton, which already competes with PureVPN on VPN. The copyable moves are the bundle design, honest privacy architecture, and cross-sell to an existing base. Buying or partnering with Proton is not realistic. Building a weak assistant would hurt the brand more than having none.


<a id="key-facts"></a>

## Contents

- [Key facts](#key-facts)
- [Product, models, and platforms](#product)
- [Privacy architecture](#privacy)
- [Pricing and bundling](#pricing)
- [Who Lumo sells to](#who-buys)
- [Revenue model](#revenue)
- [Timeline](#timeline)
- [Growth playbook](#playbook)
- [Reception and criticism](#reception)
- [Competition](#competition)
- [Lumo versus Venice](#versus-venice)
- [What PureVPN should take](#purevpn)
- [Sources](#sources)

## Key facts

*Research as of 16 November 2026, Asia/Dubai. User and revenue figures are company or secondary statements from the cited dates, not independently audited.*

#### Overview

| Item | Fact |
| --- | --- |
| What it is | Lumo is Proton's privacy-first AI assistant for chat, web search, files, images, memory, and projects. Public site lumo.proton.me, with marketing at proton.me/lumo. |
| Launch | 23 July 2025. Major rebuild as Lumo 2.0 on 30 June 2026. |
| Owner | Proton AG, Geneva. Controlled since June 2024 by the nonprofit Proton Foundation. No traditional VC investors. |
| Users, company claims | Proton said more than 10 million people had started using Lumo by the 30 June 2026 Lumo 2.0 post. A 17 September 2026 Apertus post used looser language, tens of millions of Lumo users. Neither is a dated census of monthly active or paying users. |
| Who it sells to | By design, consumers and Proton account holders first, then businesses through Lumo Professional and Workspace Premium. There is no generally available public developer API as of this research. |
| Revenue | No Lumo-specific revenue, subscriber count, or conversion rate has been disclosed. Proton-wide revenue is discussed in the Revenue model section. |
| Monetization | Free tier plus standalone Lumo Plus, a Plus add-on on most paid Proton plans, and Plus included in Visionary, Lifetime, and Workspace Premium. |
| VPN overlap | Proton VPN is in the same suite. Lumo is part of Proton's bundle strategy against other VPN and privacy brands, including PureVPN. |

#### Product

| Item | Fact |
| --- | --- |
| Current models, official privacy page | Qwen 3.5, GLM 5.3, Image-Turbo, FireRed-Image-Edit-1.1, and Apertus 1.5. Proton says these run on servers it controls. |
| Launch models, The Verge | Mistral Nemo, Mistral Small 3, Nvidia OpenHands 32B, and Ai2 OLMo 2 32B, with routing by task. |
| Privacy claim | No server-side conversation logs, zero-access encryption for saved history, no training on chats by default, European hosting and Swiss company. Live prompts are decrypted on Proton's GPU servers. |
| Open source | Web and mobile clients are open source, GPLv3. Server-side routing and system prompts are not. This is a documented point of criticism. |
| Platforms | Web, iOS, and Android. Guest use is allowed, including over Tor. A desktop app was described as in development in April 2026; a public desktop launch was not confirmed in this pass. |
| iOS, 16 Nov 2026 | Lumo AI by Proton, 4+, Productivity. 3.82 average from 582 ratings. Version 2.1.2, current version dated 21 October 2026, 12:38 AM Asia/Dubai. |
| Android, 16 Nov 2026 | Lumo by Proton, package me.proton.android.lumo. Play Store listing showed 3.8 stars from 3.44K reviews, updated 21 October 2026. |
| Content stance | Privacy-first, not uncensored. Official getting-started page says Proton has implemented safeguards against harmful or offensive responses. |

Switch the table for a compact view of the product, the company behind it, or the commercial facts. All numbers are attributed in later sections.


<a id="product"></a>

## Product, models, and platforms

Lumo is a consumer and business chat assistant inside Proton's encrypted suite, not a model lab and not, today, a public inference marketplace. It launched on 23 July 2025 as a text assistant with optional web search, file uploads, Proton Drive integration, and Ghost mode. Lumo 2.0, announced 30 June 2026, added Fast and Thinking modes, image analysis, generation, and editing, stronger cited web search, user-controlled memory, a larger context window, Projects, and Custom Lumos. Later 2026 updates added data visualizations, a visual redesign, the Apertus 1.5 model option, and a canvas for documents, code, and web pages.

Proton's current privacy article lists the models as Qwen 3.5, GLM 5.3, Image-Turbo, FireRed-Image-Edit-1.1, and Apertus 1.5. At launch, The Verge, citing Proton spokesperson Betsy Jones, named Mistral Nemo, Mistral Small 3, Nvidia OpenHands 32B, and the Allen Institute's OLMo 2 32B, with programming questions routed to OpenHands. On 21 September 2026, @asklumo said Lumo runs the 70B version of Apertus 1.5, that it is not the default model, and that Lumo Lite is a much more capable model. Official pages say the models run exclusively on servers Proton controls, so prompts are not sent to OpenAI or other US or Chinese model vendors.

Lumo 2.0 is Proton's capability pitch against ChatGPT and Claude. The company said Lumo 2.0 Lite scored 127% higher than Lumo 1.4 on the Artificial Analysis Intelligence Index, Lumo 2.0 Max scored 240% higher, and everyday queries were up to 76% faster. Those are Proton's readings of a third-party index, not a head-to-head market-share result. App Store and Play Store reviews, discussed later, still describe a quality and reliability gap with the frontier assistants.

The product is available on the web at lumo.proton.me, on iOS as Lumo AI by Proton, and on Android as Lumo by Proton. Guest access works without an account, and the marketing site says users can connect through Tor. Saved history requires a Proton account. Business users get Lumo Professional, either standalone or inside Proton Workspace. An official public developer API was not generally available as of this research.


<a id="privacy"></a>

## Privacy architecture

*Claims below are quoted or paraphrased from Proton's own pages. The live-inference caveat is one Proton states itself.*

Lumo's privacy story has two layers, and they are not the same. Saved chat history is zero-access encrypted in the same family of design as Proton Mail and Drive: only the user's device, unlocked with the account password, can read it. Live prompts are different. Proton encrypts them on the device with a per-request AES key, wraps that key to a Lumo PGP public key, and sends the payload over TLS. Only the Lumo GPU server can decrypt the prompt, run the model, and encrypt the response. Proton calls this user-to-Lumo, or U2L, encryption, and it says this is not the regular definition of end-to-end encryption, because the model server must see cleartext.

> We acknowledge this is not the regular definition of end-to-end encryption, which is why we prefer to call it user-to-Lumo (U2L) encryption to avoid any misunderstanding.
>
> — Marc Dupont, Lumo security model, 4 August 2025

Two marketing phrases need care. Proton often says even Proton cannot read conversations. That is true of stored history, and not true of the live GPU step. And Proton often says Lumo is fully open source. The clients are. The European Open Source AI Index, as quoted on Wikipedia, called Lumo the least open open AI assistant, because Proton had not open-sourced the system prompt or the routing methods that choose a model. Wikipedia also records the license split: web and mobile clients GPLv3, server proprietary.


<a id="pricing"></a>

## Pricing and bundling

*Plan features are from official Proton support and pricing pages checked on 16 November 2026, Asia/Dubai. Exact Plus and Professional dollar prices come from contemporaneous press, because the live pricing pages did not render list prices in this fetch.*

The bundle design is the commercial heart of Lumo. Proton did not give Lumo Plus away inside Unlimited, its flagship consumer suite that already includes Proton VPN. It put a limited free assistant in almost every account, sold Plus as an add-on or standalone plan, and reserved included Plus for the top consumer tier and the top business suite. That keeps GPU costs off the mid-tier VPN bundle while still letting Proton advertise a private AI assistant to more than 100 million accounts.


<a id="who-buys"></a>

## Who Lumo sells to

*No official customer-mix, paid-subscriber, or API-revenue split has been disclosed. The read below is from product packaging, traffic, and store listings.*

- **Verdict:** Lumo sells to end users, especially existing Proton customers, and is building a secondary business channel. It is not, today, a developer platform in the Venice or OpenRouter sense.
- **Confidence:** High on the customer type, because the official packaging is consumer and business, and a public API has been promised but not generally launched. Low on any split of dollars, because Proton has not published Lumo revenue or paid-user counts.
- **Trend:** From a consumer ChatGPT alternative in July 2025, to a business SKU in October 2025, to a Workspace Premium inclusion in March 2026, with an API still described as upcoming in 2026 community and roadmap material.

### Consumers and Proton cross-sell

The default path is a Proton account. Guest chat exists to cut first-session friction, but history, favorites, and Projects want a login. Free Lumo is already listed on Proton Free, Mail Plus, Unlimited, Duo, and Family, so the main acquisition engine is cross-sell into a base Proton has long described as over 100 million accounts. The 10 million people who had started using Lumo by 30 June 2026, if taken at face value, would be a large trial slice of that base, but started using is not monthly active, and it is not paying.

Consumer traffic is real and still small next to ChatGPT. Similarweb's October 2026 figures, compiled by Momentic, put ChatGPT at 6.05 billion visits, Gemini at 2.64 billion, Claude at 1.25 billion, Grok at 203.8 million, and Perplexity at 88.3 million. Lumo is not in that seven-assistant set, which only includes properties above roughly 50 million monthly visits. A stale HypeStat page for lumo.proton.me, with source data that appears to date from spring 2026, estimated about 1.5 million monthly visits. Treat that as a rough, outdated third-party figure, not an October 2026 census, and note that Lumo marketing also lives on proton.me, whose 77.8 million October visits are dominated by Mail, account, and VPN traffic.

### Business

Lumo for Business launched on 30 October 2025 and is now sold as Lumo Professional, with admin controls, and as part of Workspace Premium. Official pages pitch law firms, nonprofits, research, media, and other teams that cannot put client files into ChatGPT. Proton said in the 31 March 2026 Workspace post that more than 100,000 businesses already used Proton services. That is a company-wide business-customer claim, not a count of Lumo Professional seats.

### Developers, and the missing API

There is a client-side Lumo API inside Proton's open-source web client, used by the official apps, and an unofficial Python client, pyLumo, that speaks the same encrypted consumer endpoint. That is not a supported product API for third-party apps. On 24 April 2026, @ProtonPrivacy said an upcoming Lumo API would let organizations add a secure assistant to their product, and that a desktop app was in development. As of this research, no official public API documentation or generally available developer billing page was found. UserVoice and Reddit threads still asked Proton to launch API access. Until that ships, Lumo should not be valued as a developer-inference business.


<a id="revenue"></a>

## Revenue model

Proton has not disclosed Lumo revenue, paying Plus or Professional subscribers, or the attach rate of the Plus add-on on Unlimited. Any dollar figure for Lumo alone would be an invention, so none is offered here. The business model is still clear from the packaging.

- Standalone Lumo Plus is a conventional consumer subscription, cheaper than ChatGPT Plus at the commonly cited $12.99 versus $20 list prices, with a 30-day money-back guarantee on official pages.
- The add-on on Unlimited, Duo, Family, and single-service Plus plans is an ARPU lift on customers Proton has already acquired, which is the low-CAC path.
- Including Plus in Visionary, Lifetime, and Workspace Premium is a reason to stay on the top tiers, not a mass-market giveaway of GPU time.
- Free Lumo, including the teaser inside Unlimited, is a marketing and retention cost. It supports the privacy-suite story and creates a natural upgrade to Plus.
- Lumo Professional and Workspace Premium are the business monetization path, sold on confidentiality and European jurisdiction rather than on model quality alone.

Proton-wide, Dealroom wrote in July 2026 that Yen had said the company generates more than $100 million in annual revenue, and a November 2026 Dealroom interview summary called Proton profitable and still without venture capital. Those are secondary reports of founder remarks, not audited accounts, and they describe Proton as a whole. Lumo is one product inside a subscription company that also sells Mail, VPN, Drive, Pass, Wallet, Meet, and Workspace. It is safer to treat Lumo as a bundle and attach-rate story than as a hidden $100 million AI line.

Unit economics should follow the subscription pattern described in the Venice work: a Plus dollar is a flat fee, so light users are high margin and heavy users can be expensive, especially once image generation and large files are in the plan. Proton has not published Lumo COGS or margins.


<a id="timeline"></a>

## Timeline

### 23 Apr 2025 — @asklumo created

The official Lumo account existed about three months before launch.

### 23 Jul 2025 — Public launch

Web, iOS, and Android. No-account chat, zero-access history, no-logs and no-training pitch, European models on Proton servers. Plus listed at $12.99 a month in launch coverage.

### 4 Aug 2025 — Security model published

Proton explains U2L versus zero-access history, and admits live inference is not classical E2EE.

### 21 Aug 2025 — Lumo 1.1

Faster, smarter models and performance improvements.

### 16 Oct 2025 — Lumo 1.2

Dark mode and customized chats.

### 30 Oct 2025 — Lumo for Business

Confidential AI for teams, later packaged as Lumo Professional and folded into Workspace.

### 13 Jan 2026 — Lumo 1.3, Projects

Dedicated encrypted workspaces for multi-session tasks.

### 31 Mar 2026 — Proton Workspace

Business suite launch. Lumo included in Workspace Premium, not Standard. Proton cites more than 100,000 business customers company-wide.

### 24 Apr 2026 — Roadmap: API and desktop

Proton says a Lumo API for organizations and a desktop app are coming. The API was not found as generally available in this pass.

### 30 Jun 2026 — Lumo 2.0

Reasoning modes, images, stronger search, memory, Custom Lumos, and a claim that more than 10 million people had started using Lumo.

### Aug 2026 — AI Paper Trail and data visuals

A free switcher tool analyzes ChatGPT or Claude exports. Lumo also gains in-chat data visualizations.

### 17 Sep 2026 — Apertus 1.5 partnership

Switzerland's open academic model is added as an opt-in choice, with optional anonymized feedback to researchers.

### 22 Oct 2026 — Canvas

Lumo can create documents, code, and web pages in an encrypted canvas.

### 30 Oct 2026 — AI workplace controversy

After reporting that Proton would re-interview staff about AI use, The Verge and 404 Media wrote that Yen canceled the interviews and said there would be no loss of jobs from AI. @ProtonPrivacy also said Proton does not install tracking software to measure AI-generated code.


<a id="playbook"></a>

## Growth playbook

Venice grew as a standalone destination. Lumo grows as a new surface on a brand people already pay for. The loop looks like this.

### Cross-sell the existing base

Free Lumo is in ordinary Proton accounts. The first session can start from Mail, VPN, or account settings rather than from a cold ad. That is the structural CAC advantage PureVPN should pay most attention to.

### Launch PR as category design

The July 2025 launch landed in The Verge, TechCrunch, PCMag, TechRadar, and others as the privacy ChatGPT alternative, with Yen attacking surveillance capitalism. Lumo 2.0 got another cycle in June 2026.

### Privacy and EU sovereignty messaging

Copy stresses zero-access encryption, no logs, no training, no ads, open-source clients, GDPR, and independence from US jurisdiction. Lumo's launch post tied the product to a EuroStack investment and a shift of infrastructure into the EU.

### Founder and brand distribution

@ProtonPrivacy, with about 378,000 followers, carries most of the reach. @asklumo amplifies product news. This is quieter than Erik Voorhees's personal audience, but it is still a owned channel into privacy-minded users.

### Switcher tools, not only ads

AI Paper Trail, at proton.me/lumo/ai/ai-paper-trail, is a free diagnostic that reads a ChatGPT or Claude export and shows an exposure score, then pitches Lumo. That is a high-intent acquisition asset. Official Meta or Google ad creatives for Lumo were not independently enumerated from official ad libraries in this pass, so paid social is unquantified here.

### SEO and comparison pages

Official Lumo pages answer queries such as the best AI chat assistant for privacy and compare Lumo with Gemini, Copilot, OpenAI, and Claude on training, logs, ads, jurisdiction, and open source. The comparison table is first-party marketing, not a third-party audit.

### Tight freemium, then an add-on

Seven-day free history, one Project, and limited messages and images force a decision without giving away unlimited GPU use. Plus can be bought alone or bolted onto a plan the user already has.

### Business and compliance expansion

ISO 27001, SOC 2, and GDPR and HIPAA language support a second motion into teams, especially where ChatGPT is a data-policy problem.

### Feature velocity as marketing

1.1, 1.2, 1.3, Business, 2.0, visuals, Apertus, and canvas each created a reason to post and to re-engage existing Proton users.

### Low-friction start

No account, Tor access, and mobile apps lower the cost of a first chat. Login then makes history portable across devices.

Proton's main site traffic mix supports this read. Similarweb, for October 2026 on proton.me, put Direct first at 63.18% of desktop visits, with Mail and Organic Search next, and called Paid Social the most underutilized channel. That is Proton as a whole, not Lumo alone, but it fits a brand that lives on existing accounts and PR more than on performance ads.


<a id="reception"></a>

## Reception and criticism

Launch coverage was broadly sympathetic on privacy and cautious on capability. PCMag and TechRadar framed Lumo as a ChatGPT alternative for confidential work. That framing has stuck. The sharper criticisms are technical and, more recently, cultural.

### Not classical E2EE

Critics argued that Proton's early marketing leaned on end-to-end language while the model server must decrypt prompts. Proton's own 4 August 2025 security post already grants the point and introduces the U2L label. The honest formulation is: history is E2EE; live inference is encrypted to Proton's GPU, then forgotten, by policy.

### Not fully open source

The European Open Source AI Index, as quoted in Wikipedia's Lumo article, called Lumo the least open open AI assistant and compared Proton's claim to calling Windows open source because Windows Terminal has a GitHub repository. What is public is the web and mobile clients, including https://github.com/ProtonLumo/ios-lumo, cited in the App Store listing, and the Lumo code in Proton's WebClients repository. The server, router, and system prompt are not in that set.

### Quality and store ratings

The iOS app had a 3.82 average from 582 US App Store ratings when checked, and the Play Store listing showed 3.8 stars from 3.44K reviews. Sampled reviews praise privacy and criticize outdated or inaccurate answers, broken search, and app bugs, including reports after the 2.0 release that queries failed on the first attempt or that the Android app was slow or unstable. MacRumors commenters on the 2.0 announcement also described weak non-English performance. Proton's getting-started page itself warns that the model can produce inaccurate responses and that users should verify anything they use outside Lumo.

### Workplace AI controversy, October 2026

In late October 2026, 404 Media reported that Proton planned to re-interview staff about how they use AI at work, with jobs potentially at stake, as part of a broader AI push associated with Yen. The Verge, on 30 October 2026, 11:55 PM Asia/Dubai, reported that Yen then canceled the interviews, that a reorganization would still happen, and that Yen said there will be no loss of jobs from AI. The official @ProtonPrivacy post at 2:54 AM on 31 October, Asia/Dubai, began a statement on AI strategy and culture by saying Proton does not install tracking software on employees' laptops to measure AI-generated code. That episode is about Proton's internal AI adoption, not about Lumo's product privacy, but it is part of the current brand context around the company's AI strategy.


<a id="competition"></a>

## Competition

*Prices and privacy wording are from official pages or cited press as of 16 November 2026, Asia/Dubai, unless labeled otherwise. Traffic figures are third-party estimates.*

#### Privacy peers

| Product | Paid plan | Privacy, from its own pages | Models and features | Traffic or reach |
| --- | --- | --- | --- | --- |
| Proton Lumo | Plus about $12.99 a month or $119.88 a year, per launch and June 2026 press. Professional about $14.99 per user per month, per MacRumors. | Zero-access encrypted history; U2L encryption in transit; no server-side chat logs; no training except optional Apertus feedback. Official privacy page: https://proton.me/support/lumo-privacy | Open-source models on Proton servers: currently Qwen 3.5, GLM 5.3, image models, and optional Apertus 1.5. Chat, search, files, images, memory, Projects. Safeguards against harmful content. No generally available public API. | Company: more than 10 million had started using it by 30 June 2026. Not in Momentic's 50 million-plus visit table. Stale third-party estimate for lumo.proton.me was about 1.5 million monthly visits in spring 2026. |
| Venice AI | Pro $18 a month, or $216 a year, from venice.ai/pricing on 16 November 2026. | Device-side history and several privacy modes. Default Private mode is contractual zero retention. Anonymous mode still sends prompts to frontier providers. Docs: https://docs.venice.ai/overview/privacy | Consumer app plus a large OpenAI-compatible API, including uncensored and NSFW models. This is a different product thesis. | Company-reported registered users over 4 million on the about page at the Venice research date, with much higher third-party visit estimates. Founder-stated run rate above $150 million as of 14 October 2026. |
| Duck.ai | A DuckDuckGo subscription page exists. An official current Plus dollar price was not extracted in this pass, so it is not listed here. | Recent chats saved locally by default. Optional encrypted Sync and Backup that DuckDuckGo cannot decrypt. Identifying metadata is stripped before prompts go to model providers, which agree not to train on them and to delete data within 30 days, with safety and legal exceptions. Policy: https://duckduckgo.com/duckai/privacy-terms | Routes to third-party providers such as Anthropic, OpenAI, Azure OpenAI, and Together. Not a Proton-style self-hosted model stack. Usage policies of those providers apply, including a ban on sexually explicit use. | Not in the seven-assistant traffic table. Embedded in DuckDuckGo, so web-domain comparisons understate it. |
| Brave Leo | Leo AI Premium $14.99 a month or $149.99 a year, official page https://brave.com/premium/ | Leo does not retain or share chats or use them for additional model training. No account is required for free use. Premium billing is described as unlinkable from Leo usage. Product page: https://brave.com/leo/ | Built into the Brave browser. Models from Mixtral, Claude, and Llama, plus bring-your-own-model. Brave Search grounding. | Not separable as a large standalone domain in the Momentic set. Distribution is the Brave browser. |

Switch the table for privacy-positioned assistants or for the mainstream bots Lumo uses as foils. Lumo's real peer set is Venice, Duck.ai, and Brave Leo. ChatGPT, Le Chat, and Perplexity are the products it wants to replace for privacy-sensitive work, not the ones it currently matches on usage or features.

### Where Lumo wins, and where it is weak

- **Wins:** The strongest mainstream-brand privacy architecture among hosted consumer assistants: U2L plus zero-access history, no-training by default, self-hosted open models, a Swiss nonprofit-controlled parent, and a real suite that already includes a VPN. The add-on bundle is elegant. AI Paper Trail is a smart switcher. Business compliance language is further along than Venice's consumer-and-crypto story.
- **Weak:** Capability and polish still trail ChatGPT and Claude, which shows up in 3.8-level store ratings. No public API, no uncensored niche, and no standalone growth engine on the scale of Venice's usage or revenue claims. Open-source and E2EE wording has been contested. Unlimited customers must still pay extra for Plus. Traffic is tiny next to the frontier assistants.
- **Versus Duck.ai and Brave Leo:** Lumo is more opinionated about keeping models on its own European servers. Duck.ai and Leo often route to third-party model providers under contracts. Lumo also has a fuller standalone app and business SKU. Leo wins on being inside a browser with no account. Duck.ai wins on using frontier vendor models while stripping identity.
- **Versus Venice:** Covered in the next section. Short version: Lumo wins on brand safety, suite fit, and encryption of saved history. Venice wins on feature breadth, uncensored demand, API and credits, and disclosed AI-native revenue scale.


<a id="versus-venice"></a>

## Lumo versus Venice

These are two different answers to private AI, and they imply two different PureVPN strategies.

If the goal is inorganic growth in a privacy suite, Lumo is the product pattern to copy and Venice is the cautionary tale about competing in commodity inference. If the goal is a high-growth AI asset, Venice is the larger economic object, and it is also the one PureVPN is least likely to buy or to brand as its own.


<a id="purevpn"></a>

## What PureVPN should take

Proton is not a friendly case study that happens to sell AI. It is a direct VPN competitor using a private assistant to make the Proton bundle harder to leave. Lumo's job, commercially, is to help Proton Unlimited, Visionary, and Workspace win against single-product VPNs. PureVPN should read this as both a playbook and a competitive threat.

Plot the recommended moves by effort and impact. These are judgment calls from the teardown, not a forecast of lift.

### What to copy

- Bundle design: put a limited free private assistant in the main VPN or suite plan, sell a Plus add-on, and include the paid assistant only in the top tier. Do not give unlimited GPU use away inside the mid-tier VPN plan. That is exactly how Proton kept Plus out of Unlimited.
- Privacy positioning: lead with architecture, not a footnote. Explain what is encrypted, what the server can see during inference, and what is not logged. Borrow Proton's honesty on U2L rather than its occasional shorthand that even we cannot read conversations, which is easy to over-read.
- Cross-sell before cold ads. The cheapest Lumo user is someone who already paid for Mail or VPN. PureVPN should productize private AI as an upgrade path for current subscribers, not as a standalone app that has to buy all of its demand.
- A switcher asset in the spirit of AI Paper Trail: help people see what ChatGPT already knows about them, then offer a no-logs path. That is a privacy-brand move, and it does not require shipping a frontier model first.
- Tight freemium: short history, limited messages, and one workspace or project. Generous free usage will not convert and will run up inference cost.
- Jurisdiction and open clients, if they are true. If PureVPN ships an assistant, publish the client code and be precise about where inference runs. Do not copy the fully open source claim unless the server side is public too.

### Build, partner, or buy

- Do not try to buy Proton or Lumo. The company is Foundation-controlled, mission-driven, and a direct VPN competitor. There is no practical acquisition path in the public facts.
- Partner, but not with Proton, and be careful with Venice. A co-brand with Proton would advertise a rival VPN. A co-brand with Venice can work for a narrow anti-censorship or crypto segment if NSFW and the token are ring-fenced, as the Venice report already argued.
- The best long-term model for PureVPN is Lumo's, not Venice's: a private assistant inside a privacy suite, sold as an add-on, with no adult hook. That can be built, or assembled with a privacy-respecting inference partner that does not sell a competing VPN.
- If PureVPN builds, ship quality or do not ship. Lumo's 3.8 store ratings show the risk. A clumsy assistant attached to a VPN brand will be reviewed as the VPN, and it will be compared with ChatGPT from day one.
- A thinner product is acceptable at first: private routing for existing AI tools, a no-logs policy page, and a small self-hosted or contracted open-model chat, then a Plus add-on. That is closer to Proton's original 2025 launch than to Lumo 2.0.
- Skip a utility token, and skip uncensored or adult positioning. Those are Venice's growth hacks, and they conflict with a mainstream VPN brand and with app stores.

**Strengths**

- Clear, copyable bundle logic that raises ARPU without giving the mid-tier plan away.
- Brand-safe private AI, which fits PureVPN better than Venice's uncensored hook.
- A reminder that the real asset is an existing subscriber base, not a new AI destination site.
- An honest technical story, if PureVPN is willing to distinguish live inference from stored history.

**Weaknesses**

- Proton can now sell VPN plus private AI in one account, which raises the bar for a VPN-only brand.
- PureVPN does not have Proton's 100 million accounts, Mail and Drive lock-in, or nonprofit-controlled European legal story.
- Inference is expensive, and Lumo has not published the economics that would make a copy easy to underwrite.
- Overclaiming encryption or open source will be called out, as Proton itself was.

> Big Tech is using AI to supercharge the collection of sensitive user data to accelerate the world's transition to surveillance capitalism. Our vision for Lumo is AI that puts people ahead of profits.
>
> — Andy Yen, quoted by The Verge, 23 July 2025


<a id="sources"></a>

## Sources

*Primary Proton pages, contemporaneous press, store listings, Similarweb via Momentic, and public X posts. Third-party traffic tools are estimates. Lumo revenue was not disclosed.*

1. [Introducing Lumo](https://proton.me/blog/lumo-ai) (Proton, 23 Jul 2025)
2. [Lumo 2.0, including the 10 million started-using claim](https://proton.me/blog/lumo-2) (Proton, 30 Jun 2026)
3. [Lumo security model, U2L versus zero-access history](https://proton.me/blog/lumo-security-model) (Proton, 4 Aug 2025)
4. [Lumo privacy, current models and no-training exception](https://proton.me/support/lumo-privacy) (Proton)
5. [Getting started, including 7-day free history](https://proton.me/support/lumo-getting-started) (Proton)
6. [Lumo consumer pricing page](https://proton.me/lumo/pricing) (Proton)
7. [Proton plans, including Unlimited and Visionary Lumo treatment](https://proton.me/support/proton-plans) (Proton)
8. [Add-ons, including where Lumo Plus is included or sold extra](https://proton.me/support/proton-add-ons) (Proton)
9. [Lumo for Business product page](https://proton.me/business/lumo) (Proton)
10. [Lumo for Business announcement](https://proton.me/business/blog/lumo-business) (Proton, 30 Oct 2025)
11. [Proton Workspace launch, including Premium prices and 100,000 businesses](https://proton.me/business/blog/proton-workspace) (Proton, 31 Mar 2026)
12. [Apertus 1.5 partnership](https://proton.me/blog/lumo-apertus-partnership) (Proton, 17 Sep 2026)
13. [Apertus in Lumo, feedback steps](https://proton.me/support/apertus-lumo) (Proton)
14. [AI Paper Trail](https://proton.me/lumo/ai/ai-paper-trail) (Proton)
15. [Lumo product updates index](https://proton.me/blog/proton-updates/lumo) (Proton)
16. [Proton Foundation ownership change](https://proton.me/blog/proton-non-profit-foundation) (Proton, 16 May 2024)
17. [Sustaining Proton's mission, funding stance](https://proton.me/blog/sustaining-mission-over-time) (Proton)
18. [The Verge launch report, models and early limits](https://www.theverge.com/news/711860/proton-privacy-focused-ai-chatbot) (The Verge, 23 Jul 2025)
19. [PCMag launch report, Plus price and Unlimited add-on](https://uk.pcmag.com/ai/159256/protons-new-lumo-ai-chatbot-puts-privacy-first-with-its-chatgpt-alternative) (PCMag, 23 Jul 2025)
20. [MacRumors on Lumo 2.0, Plus and Professional prices](https://www.macrumors.com/2026/06/30/proton-lumo-version-2-new-features/) (MacRumors, 30 Jun 2026)
21. [Wikipedia Lumo article, including open-source criticism](https://en.wikipedia.org/wiki/Lumo_(AI_assistant)) (Wikipedia)
22. [Dealroom, Yen on $100 million-plus Proton revenue](https://app.dealroom.co/news/note/proton-100m-revenues-still-no-valuation-on-file) (Dealroom, Jul 2026)
23. [The Verge, Proton cancels AI staff re-interviews](https://www.theverge.com/news/1023707/proton-now-wont-re-interview-staff-actually) (The Verge, 30 Oct 2026)
24. [Proton, AI strategy and culture statement](https://x.com/ProtonPrivacy/status/2116302824577405320) (X, 31 Oct 2026)
25. [Proton roadmap mention of an upcoming Lumo API](https://x.com/ProtonPrivacy/status/2047686263067586746) (X, 24 Apr 2026)
26. [@asklumo, Apertus 70B is not the default model](https://x.com/asklumo/status/2102047665731031523) (X, 21 Sep 2026)
27. [ChatGPT Plus official price](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) (OpenAI)
28. [Brave Leo Premium pricing](https://brave.com/premium/) (Brave)
29. [Brave Leo privacy claims](https://brave.com/leo/) (Brave)
30. [Duck.ai privacy policy](https://duckduckgo.com/duckai/privacy-terms) (DuckDuckGo)
31. [Mistral official pricing, including Le Chat / Vibe Pro](https://mistral.ai/pricing/) (Mistral)
32. [Momentic, Similarweb visits for leading assistants, October 2026](https://momenticmarketing.com/blog/top-ai-chatbots) (Momentic, 5 Nov 2026)
33. [Similarweb, proton.me October 2026 traffic](https://www.similarweb.com/website/proton.me/) (Similarweb)
34. [iOS App Store listing, Lumo AI by Proton](https://apps.apple.com/us/app/lumo-ai-by-proton/id6746714949) (Apple)
35. [Google Play listing, Lumo by Proton](https://play.google.com/store/apps/details?id=me.proton.android.lumo) (Google Play)

