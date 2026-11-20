# 4. Product innovation opportunity catalog

[Back to wiki home](../README.md) · [Back to the main report](00-main-report.md)

Research compiled **20 November 2026**. This page lists every product idea considered, says what kind of growth each one produces, and scores them. The [main report](00-main-report.md) turns the scores into a portfolio.

## How to read this page

- **Net-new** means the idea brings in people who are not PureVPN customers today. **Value per customer** means it raises price paid or retention among people who would have bought anyway. Only the first kind moves the customer count directly.
- **Sourced** figures carry an inline link. **Estimate** means our calculation with inputs shown. **Assumption** means a planning input with no public source; each one appears in the [internal data request list](06-validation-and-risks.md#internal-data-requests).
- "Customers" means paying relationships: direct subscribers, people whose access a partner pays for, and buyers of a non-VPN product. Free users are counted separately. The definition is argued in the [sizing page](05-sizing-model-and-scenarios.md#1-what-counts-as-a-customer).
- All sizes describe a mature steady state, not a date.

## Summary

| # | Opportunity | Kind of growth | Paying customers it could add (estimate) | Score | Verdict |
|---|---|---|---|---|---|
| 1 | Partner distribution platform | Net-new | 1.0M to 6.0M, centre 3.5M | 4.10 | Core bet |
| 2 | Trust and quality reset | Enabler; retention | 0.15M to 0.3M directly | 3.55 | Core bet |
| 3 | Emerging-market offer | Net-new | 0.2M to 0.4M | 3.50 | Core bet |
| 4 | Free tier, staged by market | Net-new | 0.2M to 2.4M, centre 1.1M | 3.00 | Core bet, gated on 2 |
| 5 | Censorship-resistant protocols | Enabler for 3 and 4 | Mostly free users | 2.90 | Part of 3 and 4 |
| 6 | Super-bundle repackaging | Value per customer | None directly | 3.40 | Supporting |
| 7 | Scam and phishing protection | Value per customer | None directly | 2.90 | Supporting, inside 6 |
| 8 | Identity protection and data removal as a standalone line | Value per customer | Under 0.1M | 2.40 | Do not pursue standalone |
| 9 | Travel eSIM with its own front door | Net-new, per trip | 0.1M to 1.0M buyers, centre 0.4M | 3.35 | Supporting |
| 10 | Private AI assistant | Value per customer; some net-new | 0.03M to 0.2M | 2.55 | Supporting |
| 11 | AI-agent egress and developer API | Net-new, niche | Thousands | 2.60 | Low-cost option |
| 12 | Family and parental controls | Value per customer | Small | 2.20 | Do not build |
| 13 | Age-verification event playbook | Net-new, in bursts | Tens of thousands per event | 2.85 | Supporting |
| 14 | Streaming and sports features | Retention | None directly | 3.00 | Maintain; stop piracy-keyword reliance |
| 15 | Gaming-specific product | Net-new, niche | Small | 2.30 | Do not pursue |
| 16 | Dedicated and residential IP | Value per customer | None directly | 3.10 | Maintain |
| 17 | Router, smart TV and hardware | Retention | None | 1.65 | Do not pursue hardware |
| 18 | PureDome for small business | Net-new, in organisations | Thousands of firms | 2.65 | Maintain, not a count bet |
| 19 | Crypto-native or decentralised VPN | Net-new, niche | Small | 1.55 | Do not pursue |
| 20 | Micro-plans: day pass and build-a-plan | Net-new | Unknown; cheap to test | 3.25 | Supporting |
| 21 | Roll-up of small VPN brands | Net-new, by purchase | Depends on targets | 2.90 | Option, not a product |

## Core candidates in detail

### 1. Partner distribution platform

Turn PureWL from "a VPN you can rebrand" into a kit of privacy modules that a telco, device maker, bank, security vendor or travel app can include in its own product: VPN, scam and leak alerts, travel eSIM and, later, the private AI assistant.

| Question | Answer |
|---|---|
| Target customer and job | A company with millions of end users that wants a privacy or safety benefit to raise its plan value or reduce churn, without building one |
| Why now | Subscription bundling through carriers and banks is growing fast. Bango's platform managed 24 million active subscriptions in 2025, up almost 60%, and serves 7 of the top 8 US telcos ([Bango results](https://www.globenewswire.com/news-release/2026/04/27/3281314/0/en/Full-Year-Results-for-the-year-ended-31-December-2025.html)). 44% of US subscribers get at least one subscription through a bundle ([Bango survey report](https://bango.com/wp-content/uploads/2025/09/Bango_Gravity_Shift_Report_2.pdf), a vendor-commissioned survey). Revolut includes NordVPN in its top plan ([Bango](https://bango.com/partner-spotlight-nord-security/)) |
| Evidence of demand | F-Secure earns 81.6% of revenue through about 200 partners ([F-Secure annual report 2025](https://ir-cdn.inderes.com/assets/fsecure/calendar-event-attachments/ab83d5ee-f36d-4062-aa21-0d0fb7d3ab45/f-secure-annual-report-2025.pdf)). Gen Digital's partner revenue is $863M ([Gen](https://newsroom.gendigital.com/2026-05-07-Gen-Crosses-5B-in-FY26-Revenue-with-Growth-Accelerating-to-Double-Digits)). A rival white-label supplier took over VPN service for about 1 million users of one security vendor ([Pulse 2.0](https://pulse2.com/point-wild-profile-neill-feather-interview/)). PureVPN already powers Samsung Secure Wi-Fi ([TechRadar](https://www.techradar.com/news/pure-vpn-joins-forces-with-samsung-to-build-a-safer-online-world)) |
| How it grows customer count | Each partner brings an installed base. PureVPN pays no acquisition cost per person. One large partner can equal PureVPN's whole direct base |
| Rough size | **Estimate: 3.5M partner-paid active users, range 1.0M to 6.0M.** Illustrative build: three anchor partners at 1.0M active users each, 20 mid-sized partners at 40,000, and 150 small partners at 2,000 gives 4.1M. The centre allows for a shortfall. Confidence: low. It depends on winning two to four anchor deals |
| Build, buy or partner | Build on what exists: the PureWL SDK and API, per-active-user billing and the Samsung reference. New work: a multi-module kit, activation tooling, partner reporting, compliance documents. Depends on the trust reset (bet 2), because large partners run security due diligence |
| Unit economics | **Assumption: $0.30 to $1.00 per active user per month wholesale.** No public price was found. At $0.50, 3.5M users is about $21M a year. The partner carries marketing and first-line support. PureVPN carries network cost, integration work and long sales cycles |
| Moat | Moderate. PureVPN has a working SDK, a named device-maker reference and low cost. Rivals (Pango, WLVPN, Nord's reseller programme) have stronger brands or broader kits ([Pango](https://www.pango.co/demo), [WLVPN](https://wlvpn.com/about-wlvpn/), [NordVPN reseller programme](https://nordvpn.com/reseller-program/)) |
| Main risks | Concentration in a few partners. Thin margins. The partner owns the customer. An optional upsell inside a host app attaches poorly: Brave's VPN reaches about 0.1% of its users ([Brave](https://brave.com/blog/100m-mau/)). The VPN has to be included in the partner's plan to produce volume |

### 2. Trust and quality reset

Make the product provably trustworthy and pleasant to use: a named top-tier auditor on a fixed schedule, open-source apps with reproducible builds, post-quantum protection on by default, an Android app rated 4.5 or better, and billing that does not generate complaints.

| Question | Answer |
|---|---|
| Target customer and job | Every prospective buyer and every prospective partner. The job is "let me believe the no-logs claim and not regret the purchase" |
| Why now | The auditor's name has disappeared from PureVPN's own audit page ([PureVPN blog](https://www.purevpn.com/blog/kpmg-validates-purevpn-no-log-claims/)). PCMag rates the product 2.5 out of 5 ([PCMag](https://uk.pcmag.com/vpn/4500/purevpn)). The Android app is at 3.8 against 4.6 to 4.7 for rivals ([baseline page](01-purevpn-baseline.md#app-store-ratings)). Rivals have made verifiable trust standard ([Mullvad](https://mullvad.net/en/blog/mullvad-review-of-2025), [ExpressVPN](https://www.expressvpn.com/lightway)) |
| Evidence of demand | 62% of US adults rate no-logs as very or extremely important ([Security.org](https://www.security.org/resources/vpn-consumer-report-annual/)). Mullvad grew revenue about four-fold in four years on trust alone ([rating.se](https://www.rating.se/info1/detail/numbers/5592384001)) |
| How it grows customer count | Indirectly. It lifts conversion on every channel, improves ranking on review sites, reduces churn and refunds, and unlocks partner deals and a credible free tier |
| Rough size | **Estimate: 0.15M to 0.3M more direct subscribers at steady state.** Illustration: 210,000 gross additions a year sustain 0.6M subscribers at 35% annual churn and 0.75M at 28%. Both churn rates are assumptions. The larger effect is on bets 1, 3 and 4 |
| Build, buy or partner | Build and commission. Components: audit contract with a named firm, open-sourcing the apps, build pipeline changes, an app-quality programme focused on Android and Windows, changes to trial, renewal and refund terms |
| Unit economics | A cost with no direct revenue. Fairer billing will reduce some short-term cash from trial conversions and silent renewals |
| Moat | None. This is catching up. It removes a disadvantage rather than creating an advantage |
| Main risks | The 2017 logging case stays in every review regardless. Open-sourcing exposes code quality. Short-term revenue falls when billing practices change |

### 3. Emerging-market offer

Sell a plan built for the countries where VPN use is highest: local-currency prices at a fraction of the US price, local payment methods, a small Android app that works on weak connections, and local-language support.

| Question | Answer |
|---|---|
| Target customer and job | Internet users in Indonesia, India, Pakistan, Turkey, Brazil, the Gulf and similar markets who already use a free VPN and want one that is faster and safer at a price they can pay |
| Why now | VPN use is about 55% of internet users in Indonesia and 43% in India ([Browsec summary of GWI](https://browsec.com/en/blog/vpn-usage-statistics)). The market leader earns little there ([S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953)). Few providers accept local payment methods such as UPI in India ([vpnandprivacy.com](https://vpnandprivacy.com/vpn/india), a review site) |
| Evidence of demand | NordVPN already prices at 35% of the US level in India and 36% in Turkey ([EasyPPP](https://www.easyppp.com/ppp-tracker/nordvpn)). Proton VPN added Hindi, Malay, Swahili, Urdu and Yoruba ([Google Play listing](https://play.google.com/store/apps/details?id=ch.protonvpn.android&hl=en&gl=US)). In Iran, two thirds of internet users rely on free circumvention tools ([ISPA survey](https://sabt.it/archive/1784709827.529048/output.pdf)) |
| How it grows customer count | Opens countries where the current price excludes most people |
| Rough size | **Estimate: 0.2M to 0.4M paying subscribers.** Inputs: 10 million installs a year in target markets, 0.7% to 1.5% of installs paying within five weeks, 35% annual churn. The lower conversion rate is the median for India and South East Asia across subscription apps ([RevenueCat data via The Social Outline](https://thesocialoutline.com/blog/download-to-paid-conversion-rate-benchmarks)). Confidence: low |
| Build, buy or partner | Partner for payments (local wallets, carrier billing). Build the light app and price localisation. Group staff in Pakistan and the UAE are an advantage for South Asia and the Gulf |
| Unit economics | Low revenue per customer: about $10 to $20 a year at 30% to 40% of US prices (estimate). Acquisition must be nearly free, through app-store search, referrals and the free tier |
| Moat | Low to moderate. Local knowledge and low cost base. Proton's free tier is the incumbent in most of these markets |
| Main risks | Sanctions and payment restrictions (Russia, Iran). Local licensing rules that conflict with no-logs promises (Pakistan, India). Price arbitrage by buyers in rich countries. Low revenue per customer |

### 4. Free tier, staged by market

Offer a free plan with limits, starting in a few markets, to build an audience that the paid plans can convert.

| Question | Answer |
|---|---|
| Target customer and job | People who will not pay before trying, and people responding to a sudden block or age check |
| Why now | Free VPN use among US VPN users rose to 43% in 2026 ([Security.org](https://www.security.org/resources/vpn-consumer-report-annual/)). Browsers now give VPNs away: Firefox passed 1 million sign-ups in two months ([Mozilla](https://blog.mozilla.org/en/firefox/more-control-firefox/)) and Opera 400,000 activations in one ([Opera](https://blogs.opera.com/mobile/2026/03/vpn-pro-opera-for-android-pilot/)). Free apps capture most of each regulatory spike ([Reuters](https://www.reuters.com/world/asia-pacific/vpns-up-porn-websites-down-australia-brings-new-online-age-restrictions-2026-03-09/)) |
| Evidence of demand | Proton VPN has 140 million Android downloads ([Chrome-Stats](https://chrome-stats.com/a/NzY3MjQ3OTcwNjU1ODUyNjY0Nw)). A free app, Turbo VPN, has 537 million ([AppCurves](https://appcurves.com/app/turbo-vpn)). Eighteen popular free VPN apps with more than 900 million combined downloads share hidden owners and security flaws ([Tom's Guide](https://www.tomsguide.com/computing/vpns/these-seemingly-independent-free-vpns-are-all-connected-and-they-pose-a-threat-to-your-data)), which leaves room for a safe free option |
| How it grows customer count | Free users are not customers until they pay. Freemium apps convert a median 2.1% of installs to paid within 35 days; the top quarter exceed 4.5%; Google Play converts at 0.9% against 2.6% on the App Store ([RevenueCat State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps), [summary](https://thesocialoutline.com/blog/download-to-paid-conversion-rate-benchmarks)) |
| Rough size | **Estimate: 1.1M paying subscribers from the free tier at steady state, range 0.2M to 2.4M, with 5 to 20 million free monthly users.** Centre: 25 million installs a year at 1.5% conversion gives 375,000 new payers a year; at 35% annual churn that sustains 1.07M. Low: 10 million installs at 0.7%. High: 40 million at 2.1%. For scale, 50 tracked VPN apps had 412 million downloads worldwide in 2025 ([Cybernews](https://cybernews.com/best-vpn/vpn-usage-by-country/)), so the centre needs a 6% share. Confidence: low |
| Build, buy or partner | Build. Components: capacity and abuse controls, a no-account start, upgrade prompts, country gating. Depends on the trust reset, the Android app rating and blocking-resistant protocols |
| Unit economics | **Assumption: $0.05 to $0.20 per free monthly user per month** in network and support cost, so 10 million free users cost $6M to $24M a year. No public figure exists; PureVPN's own cost per gigabyte decides this. Windscribe earned about $3M on 43 million registered users in 2022 ([founder interview](https://blog.jasonsherman.org/2022/07/20/zero-to-ceo-how-to-crush-your-competition-in-tech-with-a-small-team-with-yegor-sak/)), which shows how badly it can go |
| Moat | Low. Proton's free tier has a trust lead and an ecosystem to sell into. PureVPN's advantages are cost base and regional focus |
| Main risks | Cost without conversion. Abuse traffic that damages IP reputation for paying customers. Cannibalising paid plans. A free product from a brand with a logging controversy attracts scrutiny |

### 5. Censorship-resistant protocols and distribution

Obfuscated protocols, automatic fallback routes and app distribution outside the stores, as Proton offers ([Proton VPN 2025 report](https://protonvpn.com/blog/eoy-report-2025)). NordVPN and Surfshark have equivalents ([TechRadar](https://www.techradar.com/vpn/vpn-privacy-security/pakistan-begins-blocking-unregistered-vpn-apps-and-this-popular-service-is-among-the-casualties)). PureVPN lists obfuscated servers ([homepage](https://www.purevpn.com/)).

- **Demand.** Russia: more than 9 million VPN downloads in March 2026 ([Carnegie](https://carnegieendowment.org/russia-eurasia/politika/2026/05/russia-vpn-usage-political)). Iran: 74% of internet users ([ISPA survey](https://sabt.it/archive/1784709827.529048/output.pdf)).
- **Customer-count effect.** Mostly free users. Payment from Russia and Iran is restricted, so few of them can become paying customers.
- **Verdict.** A technical requirement for bets 3 and 4 and for holding existing customers in Pakistan, Turkey and the Gulf. Not a growth bet by itself.
- **Risks.** Sanctions law, app-store removal, and retaliation against staff or infrastructure in blocking countries.

## Supporting candidates

### 6. Super-bundle repackaging

- **What.** Present Standard, Plus and Max as a clear ladder with fewer add-ons at checkout. PCMag criticised confusing pricing and constant upsell prompts ([PCMag](https://uk.pcmag.com/vpn/4500/purevpn)).
- **Evidence.** About half of Nord's new web subscribers take two or more products, and non-VPN products are over 20% of its billings ([S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953), [Fitch](https://www.fitchratings.com/research/corporate-finance/fitch-affirms-cyberspace-bv-nord-security-idr-at-bb-outlook-stable-20-10-2026)).
- **Customer-count effect.** None directly. Max costs 65% more than Standard on a two-year plan ($3.55 against $2.15, [pricing](https://www.purevpn.com/pricing)). If 30% of new buyers chose Max, revenue per new customer would rise about 20% (estimate). That pays for higher affiliate bids and so helps acquisition indirectly.
- **Risk.** Every large rival already sells the same bundle.

### 7. Scam and phishing protection

- **What.** Warnings on scam calls, texts and links inside the app.
- **Why now.** US consumers reported $15.9B of fraud losses in 2025, up from about $12B ([FTC testimony](https://search.ftc.gov/system/files/ftc_gov/pdf/ftc-testimony-jec-hearing-on-the-rising-scam-economy.pdf)). NordVPN shipped call protection on 1 June 2026 ([NordVPN](https://nordvpn.com/blog/call-protection/)) and Surfshark in October and November 2026 ([TechRadar](https://www.techradar.com/vpn/vpn-services/surfshark-updates-its-iphone-vpn-app-to-filter-out-scam-callers-but-you-need-a-premium-plan)).
- **Customer-count effect.** A retention feature inside the bundle, and a module partners will ask for. Already standard at the two largest rivals.
- **Path.** License a number-reputation and link-reputation feed. Do not build one.
- **Risk.** Low. The main risk is spending effort to reach parity.

### 9. Travel eSIM with its own front door

- **What.** Sell the existing Truely-powered eSIM ([PureVPN eSIM](https://esim.purevpn.com/)) as a product people can find and buy without wanting a VPN, then cross-sell the VPN.
- **Why now.** Travel eSIM spending rose from $989M in 2024 to $1.8B in 2025. 12% of travellers used one in 2025, forecast to reach 31% by 2030 ([eSIM Compare, citing Juniper and Kaleido](https://esimcompare.co/blog/travel-esim-statistics-2026), a comparison site).
- **Evidence.** Saily reached about 4 million users in two years ([PEGN](https://revistapegn.globo.com/startups/noticia/2026/02/como-este-app-nascido-dentro-de-um-unicornio-cresceu-4x-em-um-ano.ghtml)). Airalo passed 30 million customers ([Airalo](https://www.airalo.com/about-us/press-releases/airalo-surpasses-30-million-users)).
- **Customer-count effect.** Net-new buyers, but they pay per trip. **Estimate: about 0.4M buyers a year, range 0.1M to 1.0M.** Inputs: 0.5% of $1.8B is $9M of sales; at $15 an order and 1.5 orders per buyer a year (assumptions) that is 400,000 buyers. Confidence: low.
- **Unit economics.** A median week of data sells for $8.54 ([eSIM Compare](https://esimcompare.co/blog/travel-esim-statistics-2026)). PureVPN resells, so it keeps a margin set by its Truely contract (not public).
- **Moat.** None. Airalo is building its own network ([BusinessWire](https://www.businesswire.com/news/home/20261109079390/en/Airalo-Rolls-out-a-Single-Install-eSIM-Experience-on-Its-Own-Network)). Saily ranks first in the US for "esim" ([Semrush](https://www.semrush.com/website/saily.com/overview/)).
- **Risk.** Thin margins, strong specialists, and one-off buyers who never return.

### 10. Private AI assistant

This is the subject of the rest of the wiki. Here it is assessed only as a customer-count lever.

- **Customer-count effect.** Small. The wiki's base case is 190,000 paying subscribers in year five ([financial model](../02-financial-model.md)). That is about 3% of a 6 million target. Attach rates of 5%, 10% and 15% on a base of 0.6M subscribers give 30,000, 60,000 and 90,000 AI subscribers.
- **Revenue effect.** Large per customer. The Pro tier at $18 a month ([product overview](../01-product-overview.md)) is several times a VPN plan. Those attach rates are worth about $6.5M, $13M and $19M a year (estimate: subscribers multiplied by $216). The wiki's earlier figures of $11M, $22M and $32M assumed 1 million PureVPN subscribers ([market research page](../07-market-research.md)).
- **Evidence.** US AI users value keeping humans out of their chats at $11.20 a month ([market research page](../07-market-research.md)). ExpressVPN lists its AI assistant in every tier ([plan list](https://www.expressvpn.com/support/manage-account/available-subscriptions/)) and Proton's Lumo has been tried by more than 10 million people ([IntelligentHQ](https://www.intelligenthq.com/proton-launches-lumo-2-0-can-privacy-first-ai-finally-compete-with-chatgpt-and-claude/)), so the window to be first is closing.
- **Role in this strategy.** A reason to choose and stay with PureVPN, a higher-priced tier, and a module in the partner kit. Not a route to ten times the customers.
- **Risk.** As set out in the wiki: compute cost, safety obligations, and rivals who bundle it free.

### 11. AI-agent egress and developer API

- **What.** Give AI agents and developers programmatic access to PureVPN's network: per-task tunnels and residential exits. PureVPN already has a residential network, an IP-per-tab extension and a ChatGPT app ([pricing](https://www.purevpn.com/pricing), [IP Per Tab](https://www.purevpn.com/blog/introducing-ip-per-tab-chrome-extension/), [ChatGPT app](https://www.purevpn.com/blog/purevpn-chatgpt-integration/)).
- **Why now.** Norton and Bitdefender both launched VPNs for AI agents in 2026 ([Gen](https://newsroom.gendigital.com/2026-04-30-Gen-Accelerates-Agentic-Security-and-Privacy-for-the-AI-Era), [Bitdefender](https://www.bitdefender.com/en-us/news/bitdefender-unveils-vpn-for-ai-agents-giving-autonomous-assistants-their-own-path-to-privacy)). 1Password credits AI-agent tooling for its recent acceleration ([1Password](https://1password.com/press/2026/october/1password-surpasses-500-million-arr)).
- **Evidence of demand.** Thin. Neither Norton nor Bitdefender has published usage. PureVPN's site received 462 visits from ChatGPT in October 2026 ([Semrush](https://www.semrush.com/website/purevpn.com/overview/)).
- **Customer-count effect.** Thousands, not millions. Tailscale, the most successful developer networking product, has 20,000 paying customers ([The Globe and Mail](https://www.theglobeandmail.com/business/article-tailscale-tech-vpn-avery-pennarun/)).
- **Verdict.** A cheap option because the infrastructure exists, and a natural companion to the private AI product. Keep it small.
- **Risk.** Residential exits attract scraping and fraud. That can damage the network's reputation for everyone.

### 13. Age-verification event playbook

- **What.** Be ready before each new age-check law or platform block: store listings, local pages, server capacity, a short trial and a low-friction plan.
- **Evidence.** UK daily VPN app use went from 650,000 to more than 1.4 million and settled near 900,000 ([Ofcom](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf?v=409837)). The top five apps' UK revenue rose about five-fold at the peak ([Appfigures](https://appfigures.com/resources/insights/20250808/amp?f=2)). Australian downloads tripled in March 2026 ([Cybernews](https://cybernews.com/security/age-verification-laws-drive-surge-in-bypass-discussions-and-vpn-downloads/)).
- **Customer-count effect.** **Estimate: tens of thousands per event at PureVPN's current visibility.** The UK market kept about 250,000 extra daily users. A 2% to 5% share of that is 5,000 to 12,500 people. The winners were the best-known brands and free apps.
- **Risk.** Marketing a VPN as a way round age checks invites the bans that legislators have so far declined to pass. The UK government says it is "prepared to take further action" ([UK government](https://www.gov.uk/government/consultations/growing-up-in-the-online-world-a-national-consultation/outcome/growing-up-in-the-online-world-government-response-july-2026)). Readiness is sensible. Campaigning on circumvention is not.

### 20. Micro-plans: day pass and build-a-plan

- **What.** A day or week pass, or a low-priced plan limited to a few locations, for people who need a VPN for one event or one trip.
- **Evidence.** 18% of US non-users say VPNs are too expensive ([Security.org](https://www.security.org/resources/vpn-consumer-report-annual/)). PureVPN's monthly price is $12.95 against $2.15 a month on two years ([pricing](https://www.purevpn.com/pricing)), so the only short-term option costs six times the long-term rate. Windscribe sells locations at $1 a month each with a $3 minimum ([Windscribe](https://windscribe.com/knowledge-base/articles/how-much-does-it-cost-to-use-windscribe)).
- **Customer-count effect.** Unknown. No public data shows how many people buy short passes. It is the cheapest idea here to test.
- **Risk.** Buyers who would have prepaid two years choose a pass instead, which reduces upfront cash.

### 21. Roll-up of small VPN brands

- **What.** Buy the subscriber bases of sub-scale VPN brands and migrate them, as with Ivacy in 2024 ([TechNadu](https://www.technadu.com/ivacy-merges-with-purevpn/546417/)).
- **Evidence.** Kape reached 7.4 million subscribers largely by acquisition ([Kape 2022 results](https://pdf.dfcfw.com/pdf/H22_AN202303211584441241_1.pdf)).
- **Customer-count effect.** Depends entirely on targets and price. Not a product innovation, so it sits outside the brief, but it is a real lever and the group has done it once.
- **Risk.** Migration damages trust if terms change. Ivacy "lifetime" plans became five-year plans, according to user reports ([vpnfin](https://vpnfin.com/ivacy-review/), an affiliate-style site).

## Candidates not recommended

| # | Opportunity | Evidence | Why not |
|---|---|---|---|
| 8 | Identity theft protection and data removal as a standalone line | The identity-protection market is about $8.8B in 2026 ([DIResearch via MarketResearch.com](https://www.marketresearch.com/Deep-Insights-Research-Co-DIR-v4285/Global-Identity-Theft-Fraud-Protection-43868937/)). Aura pays $171 to $192 to win a subscriber who pays $16.61 a month ([Aura overview](https://qoria.com/hubfs/Qoria/Corporate/ASX-Announcements%20(KEEP)/2026/2026-03-26_Merger%20Update%20and%20Aura%20Business%20Overview.pdf), [Software & Capital](https://softwareandcapital.com/articles/aura-digital-safety-subscription-economics)) | A US-centred market that needs insurance, credit-bureau links and heavy marketing. PureVPN's brand is weakest where this category is strongest. Keep data removal inside the Max tier |
| 12 | Family and parental controls | The parental-control market is about $1.57B. Bark covers 7.5 million US children. Aura bought Qoria in July 2026 ([MIT Technology Review](https://www.technologyreview.com/2026/08/19/1141623/child-monitoring-apps-need-reboot/), [Aura](https://www.aura.com/press/release/aura-completes-qoria-acquisition)) | Specialists with school channels own it. PureVPN has no assets here, and monitoring children sits badly with a privacy brand. Source a module from a partner if the partner kit needs one |
| 14 | Streaming and sports as a growth bet | 41% of subscribers use a VPN for streaming ([Tom's Guide](https://www.tomsguide.com/features/more-than-40-of-vpn-subscribers-use-them-for-streaming-heres-why)). TechRadar gives PureVPN a near-perfect streaming score ([TechRadar](https://www.techradar.com/vpn/best-vpn)) | Keep streaming quality high; it is a strength. Stop relying on piracy and free sports-stream keywords for traffic ([baseline page](01-purevpn-baseline.md#7-traffic-and-acquisition-mix)). They bring visitors who do not pay and they are a liability in partner due diligence |
| 15 | Gaming-specific product | The gaming VPN market is put at $567M for 2024 ([Valuates](https://reports.valuates.com/market-reports/QYRE-Auto-12N12605/global-gaming-vpn)). ExitLag claims 30 million users ([CriticNest](https://criticnest.com/gearup-vs-exitlag/), claims not verified) | Specialists own it. The group spun out a gaming product, Kill Ping, once before ([Uzair Gadit bio](https://www.disrupt.com/team/uzair-gadit)) |
| 16 | Dedicated and residential IP as a growth bet | Reviewers list dedicated IP and port forwarding among PureVPN's strengths ([TechRadar](https://www.techradar.com/reviews/pc-mac/software/utilities/purevpn-1325640/review)) | A good add-on that raises revenue per customer. It serves existing enthusiasts and does not widen the audience |
| 17 | Routers and hardware | ExpressVPN retired its own routers in September 2026 and now relabels a partner's ([ExpressVPN](https://www.expressvpn.com/news-pr/expressvpn-fortify-glinet-router)) | Capital, inventory and support cost for a niche. TV apps are worth maintaining; hardware is not |
| 18 | PureDome as a customer-count bet | Nord earns under 5% of revenue from businesses ([S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953)). PureDome has 37 reviews on G2 ([G2](https://www.g2.com/it/products/purevpn-puredome/reviews)) | A sound business line measured in firms and seats, not millions of consumers. Run it for profit |
| 19 | Crypto-native or decentralised VPN | Twelve decentralised VPN apps total about 3.5 million installs. Nym has about 10,000 paying users ([IPinfo](https://ipinfo.io/blog/decentralized-vpns), [Nym](https://nym.com/press)) | Tiny demand, token and regulatory risk, no fit with PureVPN's assets. PureVPN already accepts cryptocurrency |

## Other ideas considered

- **No-account instant start.** Proton, Opera and Firefox all let people start without signing up. This belongs inside the free tier and the trial, not as a separate bet.
- **Free exposure scans as lead generation.** Already live ([PureVPN blog](https://www.purevpn.com/blog/introducing-digital-privacy-protection-by-purevpn/)). Their conversion to paid is an [internal data request](06-validation-and-risks.md#internal-data-requests).
- **Employers and insurers as a channel.** Aura serves about 2,300 employers ([Aura](https://www.aura.com/press/release/third-quarter-2026-financial-results)). This is a segment of bet 1.
- **Distribution inside AI assistants.** The ChatGPT app is live and brings a few hundred visits a month. Too early to size.
- **Referral loops.** Windscribe gives data for referrals and social posts ([Windscribe](https://windscribe.com/knowledge-base/articles/can-i-use-windscribe-for-free)). Worth building into the free tier.

## Scoring

Each idea is scored from 1 to 5 on six criteria. A higher score is always better, so a 5 on cost means cheap and a 5 on risk means safe.

| Criterion | Weight | What a 5 means |
|---|---|---|
| Customer-count impact | 30% | Could add more than 2 million paying relationships |
| Confidence in evidence | 20% | Demand and mechanism are shown by audited or first-party numbers |
| Fit with PureVPN assets | 15% | Uses something PureVPN already has and rivals lack |
| Cost and complexity | 15% | Few components change; little new infrastructure |
| Speed to learn | 10% | A small experiment gives a clear answer |
| Strategic risk | 10% | Failure would not damage the brand, margins or legal standing |

| Opportunity | Impact | Confidence | Fit | Cost | Speed | Risk | Weighted score |
|---|---|---|---|---|---|---|---|
| Partner distribution platform | 5 | 4 | 5 | 3 | 3 | 3 | **4.10** |
| Trust and quality reset | 3 | 4 | 4 | 3 | 3 | 5 | **3.55** |
| Emerging-market offer | 3 | 3 | 4 | 4 | 5 | 3 | **3.50** |
| Super-bundle repackaging | 2 | 4 | 4 | 4 | 4 | 4 | **3.40** |
| Travel eSIM with its own front door | 3 | 3 | 3 | 4 | 4 | 4 | **3.35** |
| Micro-plans | 2 | 2 | 4 | 5 | 5 | 4 | **3.25** |
| Dedicated and residential IP | 1 | 3 | 5 | 5 | 4 | 3 | **3.10** |
| Streaming and sports features | 2 | 3 | 4 | 4 | 4 | 2 | **3.00** |
| Free tier, staged by market | 4 | 3 | 2 | 2 | 4 | 2 | **3.00** |
| Roll-up of small VPN brands | 3 | 3 | 4 | 2 | 2 | 3 | **2.90** |
| Censorship-resistant protocols | 3 | 3 | 3 | 3 | 3 | 2 | **2.90** |
| Scam and phishing protection | 2 | 3 | 3 | 3 | 4 | 4 | **2.90** |
| Age-verification event playbook | 2 | 3 | 3 | 4 | 4 | 2 | **2.85** |
| PureDome for small business | 1 | 3 | 4 | 3 | 3 | 4 | **2.65** |
| AI-agent egress and developer API | 1 | 2 | 4 | 4 | 4 | 3 | **2.60** |
| Private AI assistant | 2 | 3 | 3 | 2 | 3 | 3 | **2.55** |
| Identity protection and data removal, standalone | 2 | 3 | 2 | 2 | 3 | 3 | **2.40** |
| Gaming-specific product | 1 | 2 | 3 | 3 | 3 | 4 | **2.30** |
| Family and parental controls | 2 | 2 | 2 | 2 | 3 | 3 | **2.20** |
| Router and hardware | 1 | 2 | 2 | 1 | 2 | 3 | **1.65** |
| Crypto-native or decentralised VPN | 1 | 2 | 1 | 2 | 3 | 1 | **1.55** |

The scores are our judgment. They are shown so that a reader who disagrees with one number can see what it changes. Three places where the portfolio departs from the ranking are explained in the [main report](00-main-report.md#6-prioritised-strategy).

## Open gaps

- Wholesale price per partner user and the number of active partner users are assumptions.
- The cost of serving a free user is an assumption. It decides whether bet 4 is affordable.
- PureVPN's churn rate is an assumption throughout.
- No public data exists on day-pass demand, on Saily's repeat purchase rate, or on use of VPNs for AI agents.
