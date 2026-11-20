# Growing PureVPN's customer base 10x through product innovation

[Back to wiki home](../README.md)

Research compiled **20 November 2026**. This is a strategy report for PureVPN's leadership. It asks whether the customer base can grow ten-fold, which product moves would do it, and how to find out cheaply. It is wider than the private AI work in the rest of this wiki and connects to it in [section 5](#5-product-innovation-opportunity-space).

| Deep-dive page | What it covers |
|---|---|
| [1. PureVPN baseline](01-purevpn-baseline.md) | Ownership, subscriber estimate, products, pricing, audits, reviews, traffic |
| [2. Market and demand structure](02-market-and-demand.md) | Market size, reasons to buy, regulatory shocks, platform threats, affiliate economics |
| [3. Competitor product strategy teardown](03-competitor-teardown.md) | What each rival launched, what added customers, what failed |
| [4. Product innovation opportunity catalog](04-opportunity-catalog.md) | 21 opportunities, each sized and scored |
| [5. Sizing model, 10x arithmetic and scenarios](05-sizing-model-and-scenarios.md) | The arithmetic, four scenario paths, sensitivities |
| [6. Validation plan, internal data requests and risks](06-validation-and-risks.md) | Experiments with thresholds, 20 data requests, the case against |
| [7. Sources and method](07-sources.md) | Every source by topic, tools that worked and did not |

## Executive summary

### Headline answer

1. **Ten times the direct paying subscribers is not a credible plan.** We estimate PureVPN has about 0.6 million paying subscribers (range 0.3 to 1.2 million; the company publishes only "5 million users"). Six million would need about 8 million new sign-ups in total and more than 3 million in the final annual cycle. PureVPN's US brand search volume is one fifty-sixth of NordVPN's, and buying that many customers would cost roughly $330M to $740M against estimated revenue of $21M to $36M a year.
2. **Ten times the paying relationships is reachable, but only through partners.** If "customer" includes people whose access a telco, bank, device maker or app pays for, the central case of our recommended strategy reaches about 5.7 million, or 9.5x. We put the chance of reaching 6 million at about 25% to 35%, and of reaching 3 million at about 60%. These odds are judgment.
3. **Revenue would grow three to five times in that case, not ten.** Partner-paid users are worth a few dollars a year each.
4. **The constraint is not the feature list.** PureVPN already sells a password manager, data removal, dark web monitoring, a travel eSIM, residential IPs, a business VPN and a ChatGPT app. None has moved the customer count. The innovations that add customers are in distribution, trust and price, not in more features.

### The 10x arithmetic in one table

Paying relationships at a mature steady state, in millions. All figures are estimates; inputs are in the [sizing page](05-sizing-model-and-scenarios.md).

| Line | Today | Low | Centre | High | What drives it |
|---|---|---|---|---|---|
| Direct subscribers | 0.6 | 0.9 | 1.5 | 2.2 | Trust reset, emerging-market offer, staged free tier, clearer bundle |
| Partner-paid active users | Unknown, counted as 0 | 1.0 | 3.5 | 6.0 | Partner distribution platform |
| Buyers of new products | About 0 | 0.2 | 0.7 | 1.5 | Travel eSIM, private AI, short passes |
| **Total paying relationships** | **0.6** | **2.1** | **5.7** | **9.7** | |
| **Multiple of today** | 1x | **3.5x** | **9.5x** | **16x** | |
| Revenue a year | $21M to $36M | About $45M | About $110M | About $210M | |
| Multiple of today's revenue | 1x | 1.3x to 2.1x | 3x to 5x | 6x to 10x | |
| Free monthly users, not counted above | 0 | 2 | 5 | 10 | Staged free tier |

For comparison, the same exercise for direct subscribers alone:

| To reach 6.0M direct subscribers | Requirement |
|---|---|
| Growth each annual cycle, if done in five | 58%. Nord Security's billings grew 29% in the year to June 2026 |
| New sign-ups in total, at 30% annual churn | About 8.2M |
| New sign-ups in the final cycle | About 3.4M, roughly a third of what the whole Nord group needs |
| Cost at $40 to $90 per sign-up | $330M to $740M |

### Recommended bets

| Bet | What it is | Contribution in the centre case | Strongest evidence |
|---|---|---|---|
| **Core 1. Partner distribution platform** | Turn the white-label arm into a kit of privacy modules that partners include in their own plans | 3.5M partner-paid users | F-Secure earns 82% of revenue through about 200 partners. Gen Digital's partner revenue is $863M. PureVPN already powers Samsung Secure Wi-Fi |
| **Core 2. Trust and quality reset** | Named auditor, open-source apps, fair billing, an Android app rated 4.5 | About 0.2M direct, and the entry ticket for bets 1 and 4 | The auditor's name has gone from PureVPN's own page. PCMag rates it 2.5 of 5. Google Play rating is 3.8 against 4.6 to 4.7 for rivals |
| **Core 3. Emerging-market offer** | Local prices, local payments, a light Android app, protocols that survive blocking | About 0.5M direct, together with bet 4 | VPN use is about 55% of internet users in Indonesia and 43% in India. The market leader earns little there |
| **Core 4. Free tier, staged and gated** | A limited free plan in selected markets, started only after bet 2 | Included in the 0.5M above; up to 2.4M alone in the high case | Proton VPN has 140 million Android downloads. Median freemium apps convert 2.1% of installs |
| Supporting | Clearer three-tier bundle with scam protection; travel eSIM with its own front door; day and week passes; readiness for age-verification events; the private AI assistant as a premium tier and partner module; a small developer and AI-agent API; buying small VPN brands | 0.7M new-product buyers and about 0.2M direct | Saily reached about 4 million users in two years. Half of Nord's new web subscribers take two or more products |

**Not to do:** own hardware, a decentralised or crypto VPN, a standalone identity-theft product for the US, a gaming product, home-built parental controls, growth through piracy and free sports-stream search terms, enthusiast features, deeper discounts or lifetime plans, and treating the business VPN (PureDome) as a customer-count bet.

### What we are least sure of

- **The baseline.** Subscribers, revenue and churn are all estimated from public signals. PureVPN's own numbers could move the starting point by a factor of two either way.
- **The partner channel's price and activation.** No public source gives a wholesale price per user or the share of bundled users who activate. Both are assumptions.
- **The cost of a free user.** It decides whether a free tier is affordable. It is an assumption.
- **Whether trust can be rebuilt.** The 2017 logging case appears in every review. An audit may not change that.

## How to read the numbers

- **Sourced** figures carry an inline link to a page that was opened during this research. Each data point carries its date where the source gives one.
- **Claim** means a company's statement about itself that nobody independent has confirmed.
- **Estimate** means our own calculation. Inputs are shown here or in the linked deep-dive page.
- **Assumption** means a planning input with no public source. Each appears in the [internal data request list](06-validation-and-risks.md#internal-data-requests).
- **Tool data** names the tool, metric, database and pull date. The paid Semrush and Ahrefs interfaces were not available, so traffic and keyword figures come from the free public overview pages those tools publish.
- Review sites that earn commission or belong to a VPN group are flagged in the deep-dive pages where they are used.
- "Customers" means **paying relationships**: direct subscribers, people whose access a partner pays for, and buyers of a non-VPN product. Free users are counted separately.
- Sizes describe a mature steady state. This report gives no delivery dates. Work is sequenced by dependency in [section 6](#6-prioritised-strategy).

## 1. PureVPN baseline

Full detail: [baseline page](01-purevpn-baseline.md).

| Item | Finding | Status |
|---|---|---|
| Ownership | GZ Systems Limited (British Virgin Islands), inside the PureSquare group, owned by Disrupt.com, a self-funded venture builder based in the UAE ([Wikipedia](https://en.wikipedia.org/wiki/PureVPN), [PureSquare](https://www.puresquare.com/), [Disrupt.com](https://www.disrupt.com/)) | Sourced |
| Stated users | "5 million" on 2 July 2026 ([PureSquare on LinkedIn](https://www.linkedin.com/posts/puresquarecom_purevpn-5millionstrong-activity-7478384222622253056-53vM)). The parent says PureSquare serves "10M+ users" ([Disrupt.com](https://www.disrupt.com/)). Neither says how many pay | Claim |
| Paying direct subscribers | **About 0.6M, range 0.3M to 1.2M** | Estimate, low to medium confidence |
| Direct revenue | **$21M to $36M a year** (0.6M at $35 to $60). Similarweb's modelled band is $50M to $75M ([Similarweb](https://www.similarweb.com/website/purevpn.com/), pulled 20 Nov 2026) | Estimate, low confidence |
| Products | VPN in three tiers (Standard, Plus with a password manager, Max with data removal and dark web monitoring), paid add-ons, travel eSIM run by Truely, PureDome for business, PureWL white label, a ChatGPT app ([pricing](https://www.purevpn.com/pricing), [eSIM](https://esim.purevpn.com/), [white label](https://www.purevpn.com/white-label)) | Sourced |
| Price | $2.15 a month on two years and $1.49 a month on five years for Standard, read 20 Nov 2026 ([pricing](https://www.purevpn.com/pricing), [order page](https://www.purevpn.com/order)). Cheapest of the large brands | Sourced |
| Audit | KPMG assessed the no-logs claim in February 2023 ([KPMG letter](https://www.purevpn.com/wp-content/uploads/2023/07/KPMG_PureVPN_TPA_Letter_2023-04-FINAL-2.pdf)). PureVPN's own page now says "well known audit firm" ([PureVPN blog](https://www.purevpn.com/blog/kpmg-validates-purevpn-no-log-claims/)) | Sourced |
| Reviews | PCMag 2.5 of 5 (9 Jul 2025, [PCMag](https://uk.pcmag.com/vpn/4500/purevpn)). TechRadar lists it as a budget pick with strong streaming and "kinks" in the apps (12 Nov 2026, [TechRadar](https://www.techradar.com/vpn/best-vpn)). Google Play 3.8 from 42.9K reviews ([Google Play](https://play.google.com/store/apps/details?id=com.gaditek.purevpnics&hl=en&gl=US), pulled 20 Nov 2026) | Sourced |
| Traffic | 1.31M visits in October 2026; 362 paid-search visits; top organic keywords are free sports-stream and piracy terms; "purevpn" has 5,400 US searches a month ([Semrush free overview](https://www.semrush.com/website/purevpn.com/overview/), US database, pulled 20 Nov 2026) | Tool data |
| Partner reach | Samsung Secure Wi-Fi runs on PureWL ([TechRadar, 26 Sep 2022](https://www.techradar.com/news/pure-vpn-joins-forces-with-samsung-to-build-a-safer-online-world)). "150+" or "600+" partners depending on the page ([PureWL](https://www.purewl.com/white-label-vpn-business/), [white label](https://www.purevpn.com/white-label)) | Sourced relationship; claimed counts |

**How the subscriber estimate was made.** Surfshark disclosed 4 million paying users in February 2026 ([LinkedIn post](https://www.linkedin.com/posts/regimantasurbanas_if-you-invest-in-stocks-would-you-consider-activity-7434851400632868864-xOYF)). PureVPN's size relative to Surfshark is 13% on Google Play reviews, 6% on iOS ratings, 12% on website visits and 5% on brand searches. Those imply 0.2M to 0.5M. We set the centre at 0.6M because five-year plans and the 2024 Ivacy migration both hide subscribers from these signals. The earlier assumption in this wiki of about 1 million subscribers looks high.

**What the baseline says about strategy.** PureVPN is a low-price, mid-reputation brand with a full feature list, weak app ratings, a trust problem it has not closed, little brand demand, and one unusual asset: a working white-label platform with a global device maker as a customer.

## 2. What "10x" means

Full detail: [sizing page](05-sizing-model-and-scenarios.md).

| Definition of customer | Today | 10x | Our view |
|---|---|---|---|
| "Users" as the company uses the word | 5 million (claim) | 50 million | Reachable only by counting free and partner end users. A weak measure |
| Paying direct subscribers | About 0.6M | About 6M | Not credible. See below |
| Paying relationships | About 0.6M plus unknown partner users | About 6M | The measure we recommend, reported with revenue beside it |

**Scale of the target.**

- Six million direct subscribers is more than Surfshark's 4 million, close to the 7.4 million the whole Kape group last disclosed (end of 2022, [Kape results](https://pdf.dfcfw.com/pdf/H22_AN202303211584441241_1.pdf)), and over a quarter of Nord Security's 22 million (June 2026, [Fitch](https://www.fitchratings.com/research/corporate-finance/fitch-affirms-cyberspace-bv-nord-security-idr-at-bb-outlook-stable-20-10-2026)).
- We estimate 60 to 120 million people pay for a consumer VPN worldwide. PureVPN holds 0.5% to 1% of them. Six million would be 5% to 10%.

**New sign-ups needed.** A subscriber base loses a share each year and has to replace it before it grows.

| Annual cycles to reach 6M | Growth each cycle | Total new sign-ups at 30% churn | New sign-ups in the final cycle |
|---|---|---|---|
| 4 | 78% | 7.5M | 3.6M |
| 5 | 58% | 8.2M | 3.4M |
| 7 | 39% | 9.6M | 3.0M |

Churn of 30% is an assumption. Nord retains 79% of users a year ([Fitch](https://www.fitchratings.com/research/corporate-finance/fitch-affirms-cyberspace-bv-nord-security-idr-at-bb-outlook-stable-20-10-2026)); the median subscription app keeps 27% to 28% of yearly subscribers after 12 months ([RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)).

**Channel capacity.** Kape paid $233M for marketing in 2022 and added 791,000 net subscribers across three large brands ([Kape results](https://pdf.dfcfw.com/pdf/H22_AN202303211584441241_1.pdf)). We estimate that at $85 to $95 per new subscriber. PureVPN's affiliate commission implies a floor near $40. At those prices 8.2 million sign-ups cost $330M to $740M. Review sites rank brands by earnings per click, and several belong to competitors ([market page](02-market-and-demand.md#6-review-sites-and-affiliate-economics)), so more commission does not buy proportionally more volume.

**Revenue per customer.** Nord earns about $58 a year per subscriber and Surfshark about €37 (estimates from disclosed figures). PureVPN earns an estimated $35 to $60. A partner-paid user is assumed to be worth $4 to $8 a year. That is why the count can rise 10x while revenue rises 3x to 5x.

## 3. Market and demand structure

Full detail: [market page](02-market-and-demand.md).

| Question | Finding | Source |
|---|---|---|
| Market size | Consumer VPN apps earned $5.9B in 2024, up 15.6%. That implies about $7.8B in 2026 (estimate). Figures of $60B to $90B include enterprise networking | [Business of Apps](https://www.businessofapps.com/data/vpn-app-market/), [Axis Intelligence roundup](https://axis-intelligence.com/vpn-statistics/) |
| Leader's growth | Nord Security: more than 15M payers in September 2025 and more than 22M in June 2026; billings up 29% | [S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953), [Fitch](https://www.fitchratings.com/research/corporate-finance/fitch-affirms-cyberspace-bv-nord-security-idr-at-bb-outlook-stable-20-10-2026) (read from the search-engine copy) |
| US adoption | 42% of US adults used a VPN in August 2026, up from 32%. 43% of users use a free one | [Security.org survey](https://www.security.org/resources/vpn-consumer-report-annual/) (a review site's own survey, 1,008 adults) |
| Reasons to use | Privacy 56%, security 51%, foreign media 27%, less tracking 27%, age-restricted content over 10% | Same survey |
| Where users are | Indonesia about 55% of internet users, India about 43%. The leader earns "limited" revenue in emerging markets | [Browsec summary of GWI](https://browsec.com/en/blog/vpn-usage-statistics), [S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953) |

**Regulatory shocks through 2026.**

- **United Kingdom.** After age checks began on 25 July 2025, daily VPN app users rose from about 650,000 to more than 1.4 million and settled near 900,000 ([Ofcom](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf?v=409837)). About a third of the spike stayed. Parliament rejected a VPN ban for under-18s on 9 March 2026, and the government said in July 2026 it "will not ban or age-gate VPNs" but is "prepared to take further action" ([UK government](https://www.gov.uk/government/consultations/growing-up-in-the-online-world-a-national-consultation/outcome/growing-up-in-the-online-world-government-response-july-2026)).
- **Australia.** VPN downloads roughly tripled when adult-content age checks began on 9 March 2026. Free apps were among the biggest winners ([Cybernews](https://cybernews.com/security/age-verification-laws-drive-surge-in-bypass-discussions-and-vpn-downloads/), [Reuters](https://www.reuters.com/world/asia-pacific/vpns-up-porn-websites-down-australia-brings-new-online-age-restrictions-2026-03-09/)).
- **United States.** About half the states require age checks for some sites. Attempts to restrict VPNs directly have mostly failed, though Utah passed a provision in 2026 ([EFF](https://www.eff.org/deeplinks/2025/12/year-states-chose-surveillance-over-safety-2025-review), [Biometric Update](https://www.biometricupdate.com/202611/utah-separates-adult-site-age-checks-from-blocked-vpn-provision)).
- **Blocking countries.** Russia restricts 469 VPN services and still saw more than 9 million VPN downloads in March 2026 ([RIA Novosti](https://ria.ru/20260226/roskomnadzor-2076790707.html), [Carnegie](https://carnegieendowment.org/russia-eurasia/politika/2026/05/russia-vpn-usage-political)). Pakistan began licensing VPN providers in November 2025 and has disrupted unlicensed ones ([PTA](https://www.pta.gov.pk/category/pta-commences-licensing-of-vpn-service-providers-under-cvas-data-regime-1566349483-2025-11-13)).

**Platform threats.** Firefox added a free built-in VPN in March 2026 and passed 1 million sign-ups in two months ([Mozilla](https://blog.mozilla.org/en/firefox/more-control-firefox/)). Opera recorded 400,000 activations of a no-sign-up trial in a month ([Opera](https://blogs.opera.com/mobile/2026/03/vpn-pro-opera-for-android-pilot/)). Google and Microsoft both closed bundled VPNs that offered no choice of location ([9to5Google](https://9to5google.com/2024/06/21/vpn-by-google-one-shutdown/), [Microsoft](https://support.microsoft.com/en-us/defender/end-of-support-privacy-protection-vpn-in-microsoft-defender-for-individuals)). Telcos, banks and device makers increasingly bundle subscriptions: Revolut includes NordVPN in its top plan ([Bango](https://bango.com/partner-spotlight-nord-security/)).

**Commoditisation and affiliates.** Entry prices have converged at $2 to $4 a month. Every large brand bundles. S&P says Nord's growth came from "relatively expensive" channels: affiliates, influencers and pay-per-click ([S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953)). Kape owns vpnMentor and sister review sites; Ziff Davis owns PCMag, CNET and the IPVanish VPN ([vpnMentor](https://www.vpnmentor.com/about-us/), [The New York Times](https://www.nytimes.com/2024/08/06/business/media/cnet-ziff-davis.html)).

**What this means.** Demand is growing and event-driven. The paying market is concentrated in rich countries, where it is sold through channels PureVPN cannot afford to win. The largest pools of users are in countries where the leaders earn little and free apps dominate. Bundling through partners is growing and PureVPN already has a foothold.

## 4. Competitor product strategy: what added customers

Full detail: [competitor teardown](03-competitor-teardown.md).

| Company | What it launched | Evidence | Lesson for PureVPN |
|---|---|---|---|
| Nord Security | Four-tier bundle, NordPass, Incogni, Saily eSIM (March 2024), scam-call protection (June 2026), reseller and bank bundles | More than 15M payers in September 2025 and more than 22M in June 2026. Half of new web subscribers take two or more products. Saily reached about 4M users ([PEGN, Feb 2026](https://revistapegn.globo.com/startups/noticia/2026/02/como-este-app-nascido-dentro-de-um-unicornio-cresceu-4x-em-um-ano.ghtml)) | The engine is paid marketing. New products with their own front door add customers. Bundle features add revenue per customer |
| Surfshark | Lowest price of the large brands, unlimited devices, Alternative ID | 4M payers, €149M revenue in 2024 | A low-price challenger can scale, with a clear hook, good apps and paid acquisition |
| Proton | Free VPN with unlimited data, anti-censorship tools, an ecosystem, Lumo private AI | More than 100M accounts, more than $100M revenue ([fDi Intelligence](https://www.fdiintelligence.com/content/f3d9fb74-b947-41df-ac19-26c2a4716151)). 140M Android downloads ([Chrome-Stats](https://chrome-stats.com/a/NzY3MjQ3OTcwNjU1ODUyNjY0Nw), 16 Nov 2026) | A free tier reaches tens of millions when the brand is trusted and the apps are good |
| ExpressVPN | Three tiers (September 2025), bundled AI assistant, identity cover, eSIM; retired its own routers (September 2026) | No subscriber figure since 2022 | Every PureVPN bundle feature now has a counterpart at a better-known brand. Hardware did not last |
| Mullvad | One product, one price, no affiliates, verifiable builds | Revenue up about four-fold from 2021 to 2025, to SEK 380.9M, with 53 staff ([rating.se](https://www.rating.se/info1/detail/numbers/5592384001)) | Trust builds a profitable business of PureVPN's size. It has not produced 10x |
| Windscribe | Generous free tier, referral rewards, build-a-plan pricing | More than 100M registered users; about $3M revenue in 2022 ([founder interview](https://blog.jasonsherman.org/2022/07/20/zero-to-ceo-how-to-crush-your-competition-in-tech-with-a-small-team-with-yegor-sak/)) | Free users can be many and worth almost nothing |
| Gen Digital, F-Secure | Security sold through telcos, retailers, banks and employers | Gen: 79M paid customers and $863M partner revenue ([Gen](https://newsroom.gendigital.com/2026-05-07-Gen-Crosses-5B-in-FY26-Revenue-with-Growth-Accelerating-to-Double-Digits)). F-Secure: 81.6% of revenue through about 200 partners ([F-Secure](https://ir-cdn.inderes.com/assets/fsecure/calendar-event-attachments/ab83d5ee-f36d-4062-aa21-0d0fb7d3ab45/f-secure-annual-report-2025.pdf)) | Partners reach customer counts that direct marketing cannot, at lower revenue each |
| Brave | Paid VPN offered inside the browser | Nearly 100,000 subscribers on about 100M users ([Brave](https://brave.com/blog/100m-mau/)) | An optional upsell attaches to about 0.1%. Inclusion is what produces volume |

**Products that failed or stalled:** Google One VPN and Microsoft Defender VPN (shut for low use), NordVPN Meshnet (1% of subscribers used it), ExpressVPN's own routers, decentralised VPNs (about 3.5M installs across twelve apps, [IPinfo](https://ipinfo.io/blog/decentralized-vpns)), and Windscribe's free tier as a source of revenue.

**Growth engines ranked by evidence:**

1. Paid acquisition at scale, financed by prepaid plans. Strong evidence. Not open to PureVPN without large capital.
2. A free tier backed by trust. Strong evidence on users, weak on conversion.
3. Partner distribution. Strong evidence on count, lower revenue per customer.
4. A new product with its own front door. Good evidence, helped by Nord's marketing.
5. Trust-led word of mouth. Good evidence of profitable growth, none of 10x.
6. Bundle features. Good evidence for revenue and retention. None for customer count.

## 5. Product innovation opportunity space

Full detail, with all nine questions answered for each core candidate: [opportunity catalog](04-opportunity-catalog.md).

"Net-new" means the idea brings in people who are not customers today. "Value per customer" means it raises price or retention among people who would have bought anyway.

| # | Opportunity | Kind of growth | Paying customers it could add (estimate) | Score | Verdict |
|---|---|---|---|---|---|
| 1 | Partner distribution platform | Net-new | 1.0M to 6.0M, centre 3.5M | 4.10 | Core |
| 2 | Trust and quality reset | Enabler; retention | 0.15M to 0.3M directly | 3.55 | Core |
| 3 | Emerging-market offer | Net-new | 0.2M to 0.4M | 3.50 | Core |
| 4 | Free tier, staged by market | Net-new | 0.2M to 2.4M, centre 1.1M | 3.00 | Core, gated on 2 |
| 5 | Censorship-resistant protocols | Enabler for 3 and 4 | Mostly free users | 2.90 | Part of 3 and 4 |
| 6 | Super-bundle repackaging | Value per customer | None directly | 3.40 | Supporting |
| 7 | Scam and phishing protection | Value per customer | None directly | 2.90 | Supporting, inside 6 |
| 8 | Identity protection and data removal, standalone | Value per customer | Under 0.1M | 2.40 | No |
| 9 | Travel eSIM with its own front door | Net-new, per trip | 0.1M to 1.0M buyers, centre 0.4M | 3.35 | Supporting |
| 10 | Private AI assistant | Value per customer; some net-new | 0.03M to 0.2M | 2.55 | Supporting |
| 11 | AI-agent egress and developer API | Net-new, niche | Thousands | 2.60 | Low-cost option |
| 12 | Family and parental controls | Value per customer | Small | 2.20 | No |
| 13 | Age-verification event playbook | Net-new, in bursts | Tens of thousands per event | 2.85 | Supporting |
| 14 | Streaming and sports features | Retention | None directly | 3.00 | Maintain |
| 15 | Gaming-specific product | Net-new, niche | Small | 2.30 | No |
| 16 | Dedicated and residential IP | Value per customer | None directly | 3.10 | Maintain |
| 17 | Router and hardware | Retention | None | 1.65 | No |
| 18 | PureDome for small business | Net-new, in organisations | Thousands of firms | 2.65 | Maintain |
| 19 | Crypto-native or decentralised VPN | Net-new, niche | Small | 1.55 | No |
| 20 | Micro-plans: day pass, build-a-plan | Net-new | Unknown; cheap to test | 3.25 | Supporting |
| 21 | Roll-up of small VPN brands | Net-new, by purchase | Depends on targets | 2.90 | Option |

### The core candidates in brief

**1. Partner distribution platform.**

- **Customer and job.** A company with millions of end users that wants a privacy benefit in its plan without building one.
- **Why now and evidence.** Bango's bundling platform managed 24 million active subscriptions in 2025, up almost 60% ([Bango results](https://www.globenewswire.com/news-release/2026/04/27/3281314/0/en/Full-Year-Results-for-the-year-ended-31-December-2025.html)). A rival white-label supplier took over VPN service for about 1 million users of one vendor ([Pulse 2.0](https://pulse2.com/point-wild-profile-neill-feather-interview/)).
- **How it adds customers.** Each partner brings an installed base at no acquisition cost to PureVPN.
- **Size.** 3.5M partner-paid active users in the centre (range 1.0M to 6.0M). Low confidence. It needs two to four anchor deals.
- **Path.** Build on the PureWL SDK, per-active-user billing and the Samsung reference. Add a multi-module kit, activation tooling and partner reporting. Depends on bet 2.
- **Economics.** Assumed $0.30 to $1.00 per active user per month. About $21M a year at the centre.
- **Moat and risk.** Moderate moat: working platform, named reference, low cost base. Risks: concentration, thin margin, stronger rivals, and low activation unless the VPN is included in the partner's plan.

**2. Trust and quality reset.**

- **Customer and job.** Every prospective buyer and partner: "let me believe the no-logs claim and not regret the purchase."
- **Evidence.** 62% of US adults rate no-logs as very or extremely important ([Security.org](https://www.security.org/resources/vpn-consumer-report-annual/)). Billing complaints recur; PureVPN confirmed its $0.99 trial is excluded from the refund guarantee ([Reddit thread, 26 Oct 2026](https://www.reddit.com/r/PureVPNcom/comments/1xdtx12/purevpns_riskfree_trial_cost_me_4795_refund/)).
- **How it adds customers.** Indirectly: conversion, review rank, churn, and access to partners and a credible free tier.
- **Size.** 0.15M to 0.3M direct subscribers from lower churn (estimate).
- **Path.** Named auditor on a fixed schedule, open-source apps with reproducible builds, an Android and Windows quality programme, fair trial and renewal terms.
- **Economics and risk.** A cost. Some short-term cash is lost when billing terms change. It creates no advantage; it removes a disadvantage. The 2017 case will still be cited.

**3. Emerging-market offer** (with **5. censorship-resistant protocols** as a dependency).

- **Customer and job.** People in Indonesia, India, Pakistan, Turkey, Brazil and the Gulf who use a free VPN and want a safer, faster one at a price they can pay.
- **Evidence.** NordVPN prices at 35% of the US level in India ([EasyPPP, 31 Oct 2026](https://www.easyppp.com/ppp-tracker/nordvpn)). Proton VPN added Hindi, Urdu, Malay, Swahili and Yoruba ([Google Play](https://play.google.com/store/apps/details?id=ch.protonvpn.android&hl=en&gl=US)).
- **Size.** 0.2M to 0.4M paying subscribers (estimate: 10 million installs a year, 0.7% to 1.5% paying, 35% churn).
- **Path.** Partner for local payments. Build regional prices and a light Android app. Requires protocols that survive blocking.
- **Economics and risk.** About $10 to $20 a year per customer, so acquisition must be nearly free. Risks: licensing rules that conflict with no-logs promises, sanctions, and price arbitrage.

**4. Free tier, staged by market.**

- **Customer and job.** People who will not pay before trying, and people reacting to a sudden block or age check.
- **Evidence.** Free VPN use among US VPN users rose to 43% in 2026 ([Security.org](https://www.security.org/resources/vpn-consumer-report-annual/)). Freemium apps convert a median 2.1% of installs within 35 days, and 0.9% on Google Play ([RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)). Eighteen popular free VPN apps share hidden owners and security flaws ([Tom's Guide](https://www.tomsguide.com/computing/vpns/these-seemingly-independent-free-vpns-are-all-connected-and-they-pose-a-threat-to-your-data)), which leaves room for a safe one.
- **Size.** 1.1M paying subscribers alone at the centre (25 million installs a year, 1.5% paying, 35% churn), with a range of 0.2M to 2.4M. Low confidence.
- **Economics.** Assumed $0.05 to $0.20 per free user per month, so 10 million free users cost $6M to $24M a year.
- **Moat and risk.** Low moat; Proton leads. Risks: cost without conversion, abuse that damages the network for paying customers, cannibalisation.

### How the private AI work fits

The rest of this wiki plans a private AI assistant with 190,000 paying subscribers in year five ([financial model](../02-financial-model.md)). Against a 6 million target that is about 3% of the count. It is not a 10x lever. It may be the largest revenue line, because its price is several times a VPN plan. In this strategy it has three roles: a premium tier that gives people a reason to choose PureVPN, a retention feature, and a module in the partner kit. One correction follows from the baseline: the attach-rate cross-check on the [market research page](../07-market-research.md) assumed 1 million PureVPN subscribers. At 0.6 million it is 40% lower.

## 6. Prioritised strategy

### Scoring rubric

Each idea is scored 1 to 5 on six criteria. A higher score is always better.

| Criterion | Weight | What a 5 means |
|---|---|---|
| Customer-count impact | 30% | Could add more than 2 million paying relationships |
| Confidence in evidence | 20% | Demand and mechanism are shown by audited or first-party numbers |
| Fit with PureVPN assets | 15% | Uses something PureVPN has and rivals lack |
| Cost and complexity | 15% | Few components change; little new infrastructure |
| Speed to learn | 10% | A small experiment gives a clear answer |
| Strategic risk | 10% | Failure would not damage the brand, margins or legal standing |

The individual scores are in the [catalog](04-opportunity-catalog.md#scoring). They are our judgment, shown so a reader who disagrees can see what changes.

### Portfolio

| Tier | Bets | Role |
|---|---|---|
| **Core** | 1. Partner distribution platform. 2. Trust and quality reset. 3. Emerging-market offer, with censorship-resistant protocols. 4. Free tier, staged and gated on bet 2 | Carry the customer count |
| **Supporting** | Super-bundle repackaging with scam protection. Travel eSIM with its own front door. Micro-plans. Age-verification event readiness. Private AI assistant. AI-agent and developer API, kept small. Roll-up of small VPN brands when a target appears | Add revenue per customer, retention, and modest numbers of new buyers |
| **Maintain** | Streaming quality. Dedicated and residential IP. PureDome | Keep working; do not expand |
| **Not to do** | Own hardware. Decentralised or crypto VPN. Standalone identity-theft product in the US. Gaming product. Home-built parental controls. Piracy and sports-stream search traffic as a growth source. Enthusiast features. Deeper discounts or lifetime plans | Each costs focus and has weak evidence of adding customers |

**Three places where the portfolio departs from the ranking.**

1. **The free tier scores 3.00 and is still a core bet.** It is the second-largest count lever and the only proven way to reach tens of millions of users without Nord's budget. Its low score comes from fit, cost and risk. Those are the reasons it is gated behind the trust reset and staged by market, not reasons to leave it out. Censorship-resistant protocols (2.90) are included for the same reason: bets 3 and 4 do not work without them.
2. **Four cheap, safe ideas outscore the free tier and are not core.** Super-bundle repackaging (3.40), travel eSIM (3.35), micro-plans (3.25) and dedicated IP (3.10) score well because they are easy and low-risk. None could add more than a few hundred thousand customers. For a 10x goal, impact has to count for more than a 30% weight allows.
3. **Private AI scores 2.55 and stays in the portfolio.** The rubric scores customer count. Private AI is weak on count and strong on revenue per customer, it is already under evaluation in this wiki, and it strengthens the partner kit.

### Scenario paths to 10x

Paying relationships at a mature steady state. Inputs and arithmetic are in the [sizing page](05-sizing-model-and-scenarios.md#4-four-scenario-paths).

| Path | Low | Centre | High | Reaches 10x? |
|---|---|---|---|---|
| A. Freemium-led: a free tier drives installs and a share converts | 0.8M (1.3x) | 1.7M (2.8x) | 3.0M (5.0x) | No, on paying customers. Yes, on "users" |
| B. Partner-led: partners include the service and pay per active user | 1.6M (2.7x) | 4.1M (6.8x) | 6.6M (11x) | Only in the high case |
| C. Category-expansion-led: eSIM, private AI and passes bring new buyers | 0.8M (1.3x) | 1.6M (2.7x) | 2.7M (4.5x) | No |
| **D. Combined, distribution first (recommended)** | **2.1M (3.5x)** | **5.7M (9.5x)** | **9.7M (16x)** | Centre is just short; high case exceeds |

How each centre is built:

- **A.** 25 million installs a year at 1.5% conversion gives 375,000 new payers a year. At 35% churn that sustains 1.07M, plus today's 0.6M. Free users cost about $12M a year at $0.10 each per month.
- **B.** Three anchor partners at about 0.9M active users each, plus 0.8M across smaller partners, gives 3.5M, plus today's 0.6M. Wholesale revenue is about $21M a year at $0.50 per user per month.
- **C.** Direct subscribers rise to 0.9M on a better bundle. eSIM adds 0.4M buyers, private AI 0.1M, passes and developer accounts 0.2M.
- **D.** Direct 1.5M (today's 0.6M, plus 0.2M from the trust reset, 0.5M from the emerging-market offer and free tier, 0.2M from bundle and affiliate gains). Partner-paid 3.5M. New-product buyers 0.7M. Revenue about $110M: direct at $45, partner users at $6, new-product buyers at $30.

**Which path we believe.** Path D, with the partner line as the deciding variable.

- It is the only path whose high case reaches 10x without assuming PureVPN outgrows the market leader several times over.
- It rests on an asset PureVPN has and most rivals of its size lack.
- If partners do not come, the trust reset and the emerging-market offer still improve the direct business. The path then delivers its low case of about 3.5x.

Our judgment of the odds: about 25% to 35% for 6 million or more paying relationships, about 60% for 3 million or more, and under 5% for 6 million direct subscribers.

### Scope of each core bet

| Bet | Components that change | How invasive | Depends on | Main delivery risk |
|---|---|---|---|---|
| 1. Partner platform | SDK and API packaging into modules; partner activation and reporting tools; billing per active user; security and compliance documentation; a senior partner sales function | Moderate. Mostly additive to PureWL. Little change to consumer apps | Trust reset (audit, entity map); scam-alert and eSIM modules from supporting bets | Long, uncertain sales cycles; integration effort per partner |
| 2. Trust reset | Audit contract; app source publication and build pipeline; Android and Windows app defects; trial, renewal and refund terms; checkout | High in the apps and billing system. Touches every customer | Nothing | Short-term revenue dip; code quality exposed by open-sourcing |
| 3. Emerging-market offer | Regional price lists; local payment integrations through a partner; a lighter Android build; obfuscated protocols with automatic fallback; local-language support | Moderate. Mostly configuration and one app variant | Protocol work; legal review per country | Licensing conflicts; payment fraud; arbitrage |
| 4. Free tier | Separate server and address pools; abuse controls; no-account start; upgrade prompts; country gating; capacity planning | High in network operations. New abuse-handling workload | Trust reset gates; cost-per-user calculation; protocols | Cost overrun; abuse damaging paid service |

### Sequence, by dependency and learning

The order below is set by what unlocks what. It makes no statement about duration.

1. **Establish the facts.** Pull the four baseline numbers: paying subscribers, partner-paid users, churn, and network cost per user. Nothing depends on anything else here, and every later decision depends on this.
2. **Start the two bets that have no prerequisites.** The trust reset (audit, billing terms, app quality) and partner discovery (the existing PureWL book and 20 structured conversations). Run the configuration-only tests alongside: regional prices, a bundle ladder at checkout, a day pass shown to abandoning visitors.
3. **Gate A: trust.** A named audit is published and new Android reviews average 4.3 or more. Passing unlocks anchor-partner due diligence and the free-tier pilot.
4. **Build what the first tests justify.** The multi-module partner kit and an inclusion pilot with an existing partner. The emerging-market offer in the countries where the price test passed. The eSIM front door.
5. **Gate B: economics.** The inclusion pilot shows 10% or more monthly activation, at least one anchor partner is in contracting, and a free user costs $0.10 a month or less.
6. **Pilot the free tier in one or two markets.** Expand only if 1.5% of installs pay within 35 days and paid servers are not blocked more often.
7. **Scale what passed.** Add the private AI module to the partner kit when that product exists. Consider buying small VPN brands once migration can be done without breaking terms.

If the private AI build proceeds in parallel, it competes for the same engineers as steps 2 and 4. One of them should yield.

## 7. Validation plan

Full detail, including stop signals: [validation page](06-validation-and-risks.md).

| Core bet | Cheapest experiments | Metric and proposed threshold | Leading indicators |
|---|---|---|---|
| 1. Partner platform | Audit the PureWL book. Hold 20 structured partner conversations with a one-page kit and price list. Run an inclusion pilot with one existing partner | 5 of 20 partners proceed to evaluation, one with more than 1M end users. 10% or more of eligible users active monthly | Security questionnaires passed; partner-paid active users; revenue per active user; share held by the largest partner |
| 2. Trust reset | Publish a named audit and test checkout with and without it. Test fairer trial and renewal terms against today's. Fix the top Android and Windows defects | Billing complaints halve while net revenue per trial start falls less than 10%. New Google Play reviews average 4.5 | First-renewal rate; billing share of support contacts; new Trustpilot reviews; review-site rank |
| 3. Emerging-market offer | Local-currency prices at 30% to 40% of US levels in two or three countries. One local payment method in one country. Connection tests from inside blocking countries | 0.7% or more of installs pay within 35 days and revenue per install does not fall. Under 5% of discounted purchases from outside the country | Organic store installs; month-two retention; refund rate |
| 4. Free tier | Desk calculation of cost per free user. Country-gated Android pilot on separate servers | Cost of $0.10 a month or less. 1.5% of installs pay within 35 days. First-year cohort revenue exceeds cohort cost. No rise in paid-server blocking | Day-30 retention; upgrade-prompt clicks; abuse complaints per 1,000 users |

The 0.7% and 1.5% thresholds sit against public benchmarks: 0.7% is the median for subscription apps in India and South East Asia, 0.9% the Google Play median and 2.1% the freemium median ([RevenueCat](https://www.revenuecat.com/state-of-subscription-apps), [summary by The Social Outline](https://thesocialoutline.com/blog/download-to-paid-conversion-rate-benchmarks)). The other thresholds are proposals.

**Internal data that would replace estimates.** The full list of 20 items is [here](06-validation-and-risks.md#internal-data-requests). The ten that matter most:

1. Paying direct subscribers by plan, tier, platform and country.
2. Revenue for three years, split into direct, add-ons, PureWL, PureDome and eSIM.
3. First-renewal rate by plan length and monthly churn.
4. New sign-ups a year by channel, and the affiliate share.
5. PureWL: active partners, partner-paid active users, revenue per active user, concentration, and whether each partner includes or upsells the VPN.
6. Network cost per gigabyte and average use per subscriber.
7. Trial starts, conversion, refunds and chargebacks.
8. Who audits PureVPN now and what can be published.
9. Tier and add-on mix on new orders.
10. Subscribers, prices and payment methods by country.

## 8. Risks and counterarguments

Full detail: [risks section](06-validation-and-risks.md#risks-and-counterarguments). This section argues against the recommendation.

| Objection | Why it has force | Our answer |
|---|---|---|
| Partner-paid users are not customers; this is 10x by redefinition | 60% of the centre case is people worth about $6 a year whom a partner owns. Google and Microsoft closed bundled VPNs for lack of use | Largely right. Count only active users, report revenue beside the count, cap any partner at a third of partner users. If leadership means revenue or direct subscribers, no path here reaches 10x |
| PureVPN will lose partner deals to Nord, Pango, WLVPN, Gen and F-Secure | They have stronger brands and broader kits | Target mid-sized and emerging-market partners. Use the 20-conversation test to find out early |
| Brand trust cannot be repaired | The 2017 FBI case is in every review. Mullvad's path does not transfer | Partly conceded. The reset is sized small for direct sales. If partners still refuse, give the kit a separate brand |
| Jurisdiction | A British Virgin Islands entity with operations linked to Pakistan, where VPNs are now licensed and unlicensed ones disrupted | Not solved by product work. Needs a legal structure partners can inspect. Do not sell under this brand where a licence conflicts with no-logs |
| Free users dilute margins | 10 million free users would cost $6M to $24M a year against $21M to $36M of revenue. Windscribe earned about seven cents per registered user | Hence the gates, the staging and a hard stop at 0.7% conversion |
| Abuse and trust-and-safety cost | Free tiers and residential exits attract fraud and scraping; blocked addresses hurt paying customers | Separate pools, rate limits, no free residential exits. Reduces the problem; does not remove it |
| Cannibalisation | Free plans, passes and regional prices give current buyers cheaper options. Fairer billing costs trial cash | Every test has a control group and a revenue-per-visitor measure |
| Affiliate dependence | Review sites are owned or paid by rivals; rankings may not respond to a trust reset. Changes could annoy the affiliates who supply today's sales | The strategy avoids outbidding rivals there. Measure the affiliate share first and stage price changes |
| Regulation | Legislators increasingly treat VPNs as a loophole. An age-gated VPN market would end no-account free tiers | Do not market circumvention. Build age verification where required. Partners already know their customers |
| Execution capacity | PureVPN already ships many products at uneven quality. This adds more | Enforce the stop list. Start with two bets. Gate the rest |
| The goal is wrong | Three times the revenue from better customers may be worth more than ten times the count | We have sympathy with this. The revenue row in every scenario is there so leadership can choose with both in view |

**What would change the recommendation:** PureWL already serving more than 2 million paid users (restate the baseline and shift emphasis to direct growth); fewer than 2 of 20 partner conversations proceeding (pause and fix trust, or rebrand the kit); a free user costing more than $0.20 a month (drop the free tier); churn above 45% (put retention before every acquisition bet).

## Method and limits

- **What was used.** Web search and page fetches for company pages, rating-agency notes, regulatory documents, filings and press. Free public Semrush and Similarweb overview pages for traffic and keywords. Google Play listings and Apple's public iTunes Search API for app ratings. All pulled on 20 November 2026.
- **What was not available.** The Semrush, Ahrefs, Synapse, SuperMe and conqueror connectors all required authentication that this research did not have. No keyword-level, backlink or historical data from paid tools is in this report.
- **Pages read from search-engine copies.** The Fitch note on Nord Security and PureVPN's Trustpilot page did not return content when fetched directly. They are flagged where used.
- **No interviews.** No customers, partners, staff or competitors were spoken to.
- **Sources.** The full list is on the [sources page](07-sources.md).

## Open gaps

- PureVPN's paying base, revenue, churn, channel mix and partner-paid users. These would replace the largest estimates in the report.
- Wholesale price per partner user and activation rates for bundled VPNs. No public benchmark was found.
- The cost of serving a free user.
- How many of Nord's 22 million paying users are Saily buyers. If many are, Nord's subscriber growth is smaller than it looks and a travel eSIM matters more.
- Conversion from free to paid at Proton, and subscriber counts for Incogni, DeleteMe and Kape's brands after 2022. None is published.
