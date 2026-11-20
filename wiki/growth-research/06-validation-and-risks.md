# 6. Validation plan, internal data requests and risks

[Back to wiki home](../README.md) · [Back to the main report](00-main-report.md)

Research compiled **20 November 2026**. This page says how to test each core bet cheaply, which internal numbers would replace the estimates in this report, and why the recommendation might be wrong.

## How to read this page

- Thresholds are **proposed decision rules**. Where a public benchmark exists it is linked. Where none exists the threshold is our judgment and is marked "proposed".
- Experiments are sized by sample (installs, conversations, partners), not by duration.
- "Stop" means stop spending on that bet and move the people elsewhere. It does not mean the idea is wrong for ever.

## The first step: establish the baseline

Nothing else in this report can be trusted until four numbers are known. They cost nothing to obtain.

| Number | Why it comes first |
|---|---|
| Paying direct subscribers | Our estimate is 0.6M with a range of 0.3M to 1.2M. The 10x target moves with it |
| Partner-paid active users through PureWL | If this is already in the millions, the starting point and the multiple both change |
| Annual churn by plan length | Decides how many new sign-ups any target needs |
| Network cost per gigabyte and per active user | Decides whether a free tier is affordable at all |

## Validation plan for the core bets

### Bet 1. Partner distribution platform

| Experiment | What it costs | Metric | Proposed threshold | Stop signal |
|---|---|---|---|---|
| Audit the existing PureWL book | Analyst effort only | Active users per partner; revenue per active user; share of users with the top five partners; whether the VPN is included in the partner's plan or sold as an extra | Know all four | None. This is a fact-finding step |
| Structured conversations with 20 prospective partners across five types: telcos and internet providers, neobanks, device makers, security vendors, travel and eSIM apps | A one-page module kit, an indicative price list, senior sales time | Partners that ask for a security questionnaire or technical evaluation | At least 5 of 20 proceed to evaluation, including at least one with more than 1 million end users on the relevant plan | Fewer than 2 of 20 proceed, or every refusal cites trust or jurisdiction |
| Inclusion pilot with one existing partner: give the VPN to a cohort as part of the plan instead of as an extra | Integration support; a discounted pilot rate | Share of eligible users who connect at least once a month | 10% or more (proposed). For comparison, an optional VPN inside Brave reaches about 0.1% of users ([Brave](https://brave.com/blog/100m-mau/)) | Under 3%. Per-active-user pricing then yields too little |
| List the service with one subscription-bundling platform | Listing and integration cost | Operators that select the product from the catalogue | One operator launch | No selection after being offered to the platform's operator customers |

Leading indicators once the bet is running: security questionnaires passed without remediation, partner-paid monthly active users, revenue per active user, and the share of partner users held by the largest partner.

Why inclusion matters: Google closed its bundled VPN because "people simply weren't using it" ([9to5Google](https://9to5google.com/2024/04/11/google-one-vpn-discontinued/)), and Microsoft ended its Defender VPN in February 2025 ([Microsoft](https://support.microsoft.com/en-us/defender/end-of-support-privacy-protection-vpn-in-microsoft-defender-for-individuals)). A bundled VPN that nobody activates produces neither revenue nor customers.

### Bet 2. Trust and quality reset

| Experiment | What it costs | Metric | Proposed threshold | Stop signal |
|---|---|---|---|---|
| Publish a no-logs audit with the auditor's name and full report, then test the checkout page with and without it | Audit fee; page test | Checkout conversion | A measurable lift. Any lift pays, because the audit is needed for bet 1 regardless | None. The audit is required for partner due diligence |
| Billing fairness test: reminder before a trial converts, trial covered by the refund guarantee, renewal price shown at purchase | Some lost conversions | Refund rate, chargeback rate, billing tickets, share of one-star reviews that mention billing, net revenue per trial start | Billing complaints fall by half. Net revenue per trial start falls by less than 10% (proposed) | Net revenue per trial start falls by more than 25% with no change in reviews |
| Android and Windows quality programme | Engineering focus; no new features on those apps while it runs | Crash-free sessions, connection success rate, time to connect, average rating of new reviews | New Google Play reviews average 4.5 or more, against 3.8 overall today ([Google Play](https://play.google.com/store/apps/details?id=com.gaditek.purevpnics&hl=en&gl=US)) | New reviews still average under 4.2 after the main defects are fixed |
| Ask the five most-read reviewers what would change their score | Conversations | A written list of blockers | A list exists and is worked through | None |
| Open-source one client app | Code clean-up; legal review | Independent security findings; press and reviewer response | No critical findings unresolved | Critical findings that cannot be fixed before publication |

Leading indicators: first-renewal rate, share of support contacts about billing, number of new Trustpilot reviews (only 481 of 18,006 were written in the last 12 months, per the search-engine copy of the [Trustpilot page](https://www.trustpilot.com/review/purevpn.com)), and position on the main review sites' lists.

### Bet 3. Emerging-market offer

| Experiment | What it costs | Metric | Proposed threshold | Stop signal |
|---|---|---|---|---|
| Local-currency price test in two or three countries at 30% to 40% of the US price, using app-store regional pricing | Configuration only | Share of installs that pay within 35 days; revenue per install against the current price | 0.7% or more, the median for India and South East Asia ([RevenueCat via The Social Outline](https://thesocialoutline.com/blog/download-to-paid-conversion-rate-benchmarks)), and revenue per install no lower than before | Revenue per install falls and conversion does not at least double |
| Add one local payment method in one country through a payment partner | Partner integration | Conversion by payment method | Local method carries more than a third of purchases (proposed) | Under 10% |
| Price-arbitrage check | Analysis | Share of discounted purchases made from outside the target country | Under 5% (proposed) | Over 15% |
| Connection test from inside blocking countries (bet 5) | Testers or probes in Pakistan, Turkey, the Gulf | Connection success with automatic fallback | 90% or more (proposed) | Under 70% after protocol work |

Leading indicators: organic installs from store search in target countries, month-two retention of monthly plans, and refund rate.

### Bet 4. Free tier, staged by market

This bet does not start until bet 2 has a named audit published and new Android reviews at 4.3 or better. A free product from a brand with a logging controversy will be examined closely.

| Experiment | What it costs | Metric | Proposed threshold | Stop signal |
|---|---|---|---|---|
| Desk calculation of the cost of a free user, using trial users' data volumes and network cost per gigabyte | Analyst effort | Cost per free monthly user per month | $0.10 or less (proposed) | Over $0.20. The centre case then costs more than $24M a year for 10 million users |
| Country-gated free plan on Android in one or two markets, on a separate pool of servers and addresses | Capacity; abuse tooling; upgrade prompts | Share of installs that pay within 35 days | 1.5% or more. The Google Play median is 0.9% and the freemium median is 2.1% ([RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)) | Under 0.7% after 100,000 installs |
| Same pilot | Same | First-year revenue from a cohort against first-year cost of serving it | Revenue exceeds cost | Revenue under half of cost |
| Same pilot | Same | Abuse complaints per 1,000 free users; block rate of paid servers by streaming and payment sites | No rise in paid-server block rate | Paid customers' block rate rises |
| Same pilot | Same | New paid sign-ups from the same country through other channels | No fall | A fall larger than the free tier's own conversions |

Leading indicators: day-30 retention of free users, upgrade-prompt click rate, and cost per free user.

### Supporting bets: one cheap test each

| Bet | Test | Signal to continue |
|---|---|---|
| Super-bundle repackaging | Checkout test: a three-step ladder with no add-on prompts against today's flow | Higher revenue per order with no fall in conversion |
| Travel eSIM front door | A stand-alone landing page and store listing; measure buyers who are not VPN subscribers | Repeat purchase within a second trip, and 5% or more of buyers taking a VPN plan (proposed) |
| Micro-plans | Offer a day or week pass only to visitors who abandon checkout | Passes add buyers without reducing two-year plan sales in the control comparison |
| Age-verification event playbook | Prepare pages, store listings and capacity for the next jurisdiction with a dated age-check law | Share of store search impressions during the event above PureVPN's normal share |
| Private AI assistant | The attach-rate test already called for in the [wiki](../README.md): offer it to a sample of existing subscribers | Attach of 5% or more at the planned price, the low case in the [sizing page](05-sizing-model-and-scenarios.md#7-link-to-the-private-ai-model) |
| AI-agent egress | Publish developer documentation and a connector for agent tools; count sign-ups | Paying developer accounts in the hundreds from organic discovery alone |

## Internal data requests

Each item replaces an estimate or assumption in this report.

| # | Data needed | Estimate or assumption it replaces |
|---|---|---|
| 1 | Paying direct subscribers, by plan length, tier, platform and country | Baseline of 0.6M (range 0.3M to 1.2M) |
| 2 | Revenue and billings for the last three years, split into direct VPN, add-ons, PureWL, PureDome and eSIM | Revenue estimate of $21M to $36M. Similarweb's band is $50M to $75M ([Similarweb](https://www.similarweb.com/website/purevpn.com/)) |
| 3 | First-renewal rate by plan length; monthly-plan churn; share of the base on five-year plans and when those cohorts renew | Churn of 30% to 35% |
| 4 | New sign-ups a year by channel: affiliates, organic search, paid search, app stores, direct, partners | Channel capacity; the share of sales that depends on affiliates |
| 5 | Commission paid per order, the ten largest affiliates' share of sales, and payback by channel | Acquisition-cost floor of about $40 |
| 6 | PureWL: active partners, partner-paid monthly active users, revenue per active user, concentration in the top five, whether each partner includes the VPN or sells it as an extra, and the status and term of the Samsung contract | Partner seat counts and the wholesale price of $0.30 to $1.00 a month. The partner count is given as "150+" in one place and "600+" in another ([PureWL](https://www.purewl.com/white-label-vpn-business/), [PureVPN white label](https://www.purevpn.com/white-label)) |
| 7 | Network cost per gigabyte, average gigabytes per paying user, idle capacity | Free-user cost of $0.05 to $0.20 a month |
| 8 | The $0.99 seven-day trial: starts, conversion to paid, refunds, chargebacks, support contacts | The cash at stake in the billing fairness test |
| 9 | Refund and chargeback rates overall; share of support contacts about billing | Trust reset sizing |
| 10 | Crash-free rate, connection success rate and time to connect, by platform; rating of new store reviews over time | App-quality gap |
| 11 | Who performs the always-on audit today, why the auditor's name was removed from the public page, and what can be published | The trust reset's first component |
| 12 | Share of new orders on Standard, Plus and Max; attach rates for dedicated IP, port forwarding and the residential network | Revenue per subscriber of $35 to $60; the bundle test |
| 13 | Free exposure-scan funnel: scans, email addresses captured, conversion to paid | Whether lead-generation tools already work |
| 14 | eSIM: orders, buyers, repeat rate, margin under the Truely contract, share of buyers who are not VPN subscribers | eSIM sizing of 0.4M buyers |
| 15 | Paying subscribers, price points and payment methods by country, especially Pakistan, India, Indonesia, Turkey, Brazil and the Gulf; paying users in Russia against Russia's 8% share of desktop visits | Emerging-market sizing |
| 16 | Share of organic visits landing on pages that rank for piracy and free sports-stream keywords, and their conversion | What is lost if that traffic is given up |
| 17 | Usage of the ChatGPT app and the IP-per-tab extension | Demand for AI-related features |
| 18 | Ivacy migration: subscribers moved and their retention since | The roll-up option |
| 19 | Legal entity map, where staff and data sit, the position on Pakistan's VPN licensing regime, and the history of law-enforcement requests | Jurisdiction risk in partner due diligence |
| 20 | Engineering headcount by product line | Execution capacity |

## Risks and counterarguments

This section argues against the recommendation. Each row gives the strongest form of the objection, the evidence for it, and what we would do about it. Some objections are not fully answered.

### "Partner-paid users are not customers. This is 10x by redefinition."

- **The objection.** In the central scenario, 3.5M of 5.7M paying relationships are people a partner pays about $6 a year for. Revenue rises three to five times, not ten. The partner owns the relationship. One lost contract removes a million "customers" in a day.
- **Evidence for it.** Google and Microsoft both closed bundled VPNs because people did not use them ([9to5Google](https://9to5google.com/2024/04/11/google-one-vpn-discontinued/), [Microsoft](https://support.microsoft.com/en-us/defender/end-of-support-privacy-protection-vpn-in-microsoft-defender-for-individuals)). F-Secure's partner-led model produces €146M of revenue from "tens of millions" of subscribers, which is a few euros each at most ([F-Secure annual report 2025](https://ir-cdn.inderes.com/assets/fsecure/calendar-event-attachments/ab83d5ee-f36d-4062-aa21-0d0fb7d3ab45/f-secure-annual-report-2025.pdf)).
- **Our answer.** The objection is largely right, and the report says so in its summary. We recommend counting only active partner users, reporting revenue beside the count, and capping any one partner at a third of partner users. If leadership means "10x revenue" or "10x direct subscribers", no path in this report gets there.

### "PureVPN will lose partner deals to stronger suppliers."

- **The objection.** Nord has Revolut and a reseller programme. Pango and WLVPN sell broader kits. Gen and F-Secure already own the telco channel. A large partner's security team will find the 2017 case, the unnamed auditor and the Pakistan operations.
- **Evidence for it.** [Bango](https://bango.com/partner-spotlight-nord-security/), [Pango](https://www.pango.co/demo), [WLVPN](https://wlvpn.com/about-wlvpn/), [Gen](https://newsroom.gendigital.com/2026-05-07-Gen-Crosses-5B-in-FY26-Revenue-with-Growth-Accelerating-to-Double-Digits).
- **Our answer.** This is why the trust reset comes first. PureVPN's realistic targets are mid-sized partners and emerging-market operators that the leaders serve poorly; S&P notes Nord earns little in emerging markets ([S&P](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101636953)). The 20-conversation test is designed to find out quickly whether trust blocks deals.

### Brand trust

- **The objection.** In a 2017 FBI cyberstalking case, PureVPN records helped identify a suspect even though the service was marketed as "zero log" ([Wikipedia](https://en.wikipedia.org/wiki/PureVPN)). Every review still mentions it. No audit removes it. Mullvad's trust-led growth does not transfer, because Mullvad has no such history.
- **Evidence for it.** PCMag rates the product 2.5 out of 5 ([PCMag](https://uk.pcmag.com/vpn/4500/purevpn)). CNET France names privacy history as the weak point ([CNET France](https://fr.cnet.com/vpn/4985/purevpn-ce-vpn-historique-tient-il-encore-ses-promesses)). The auditor's name is gone from PureVPN's own page ([PureVPN blog](https://www.purevpn.com/blog/kpmg-validates-purevpn-no-log-claims/)).
- **Our answer.** Partly conceded. The reset is sized at only 0.15M to 0.3M direct subscribers for this reason. Its main value is as an entry ticket for partners. If reviewers and partners do not respond to a named audit and open-source apps, a new brand for the partner kit should be considered.

### Jurisdiction

- **The objection.** The operating company is registered in the British Virgin Islands, the Android developer entity is in Cyprus, and the parent group is listed with its headquarters in Karachi ([Wikipedia](https://en.wikipedia.org/wiki/PureVPN), [Google Play](https://play.google.com/store/apps/details?id=com.gaditek.purevpnics&hl=en&gl=US), [The Org](https://theorg.com/org/disrupt-com)). Pakistan began licensing VPN providers in November 2025 and has restricted unlicensed ones ([PTA](https://www.pta.gov.pk/category/pta-commences-licensing-of-vpn-service-providers-under-cvas-data-regime-1566349483-2025-11-13), [TechRadar](https://www.techradar.com/vpn/vpn-privacy-security/pakistan-begins-blocking-unregistered-vpn-apps-and-this-popular-service-is-among-the-casualties)). A provider with staff in a licensing country can be pressured in ways a Swiss or Swedish provider cannot.
- **Our answer.** Not answered by product work. It needs a legal structure that partners can inspect: where keys, data and decision rights sit. An emerging-market offer in Pakistan or India may require a choice between a licence and the no-logs promise. If so, do not sell there under the PureVPN brand.

### Margin dilution from free users

- **The objection.** Ten million free users would cost $6M to $24M a year on our assumptions, against estimated revenue of $21M to $36M. Windscribe earned about $0.07 per registered user in 2022 ([founder interview](https://blog.jasonsherman.org/2022/07/20/zero-to-ceo-how-to-crush-your-competition-in-tech-with-a-small-team-with-yegor-sak/)). Proton can afford a free VPN because it sells mail and storage to the same people. PureVPN has nothing comparable to sell.
- **Our answer.** This is why the free tier is staged, gated and has a hard stop at 0.7% conversion. It is also why it scores only 3.00. If the desk calculation of cost per free user comes back above $0.20, the bet should not start.

### Abuse and trust-and-safety cost

- **The objection.** Free tiers and residential exits attract fraud, scraping, spam and worse. Abuse gets shared addresses blocked, which damages streaming access, the thing reviewers praise most about PureVPN ([TechRadar](https://www.techradar.com/vpn/best-vpn)). Handling abuse without logs is hard. The 2017 case was itself an abuse investigation.
- **Our answer.** Separate address pools for free users, rate limits, no free residential exits, and a published abuse policy. These reduce the problem and do not remove it. The cost belongs in the free-tier economics.

### Cannibalisation

- **The objection.** A free tier, day passes and regional prices all give existing buyers a cheaper option. Fairer billing reduces trial-conversion cash. PureVPN's cash flow leans on multi-year prepayment ([order page](https://www.purevpn.com/order)).
- **Our answer.** Every experiment above has a control group and a revenue-per-visitor metric for this reason. Expect some loss. The question the tests answer is whether new buyers outweigh it.

### Affiliate dependence

- **The objection.** The sites that rank VPNs are owned by, or paid by, competitors. Kape owns vpnMentor and two sister sites; Ziff Davis owns IPVanish, PCMag and CNET ([vpnMentor](https://www.vpnmentor.com/about-us/), [The New York Times](https://www.nytimes.com/2024/08/06/business/media/cnet-ziff-davis.html)). Rankings follow payouts as much as quality, so a trust reset may not move them. PureVPN already pays 40% of the first order and 35% of renewals ([affiliate programme](https://www.purevpn.com/affiliates)).
- **Our answer.** Agreed, and it is the reason this strategy does not rely on outbidding rivals in that channel. The risk runs the other way too: if affiliates produce most of today's sales, anything that annoys them (lower prices, a free tier that cuts commission) could shrink the base before new channels work. Data request 4 sizes this.

### Regulatory risk

- **The objection.** Legislators are starting to treat VPNs as a loophole. Utah passed a VPN provision in 2026, Wisconsin and Michigan attempted them, and the UK government says it is "prepared to take further action" ([Biometric Update](https://www.biometricupdate.com/202611/utah-separates-adult-site-age-checks-from-blocked-vpn-provision), [EFF](https://www.eff.org/deeplinks/2025/12/year-states-chose-surveillance-over-safety-2025-review), [UK government](https://www.gov.uk/government/consultations/growing-up-in-the-online-world-a-national-consultation/outcome/growing-up-in-the-online-world-government-response-july-2026)). Russia restricts 469 VPN services ([RIA Novosti](https://ria.ru/20260226/roskomnadzor-2076790707.html)). An age-gated VPN market would end no-account free tiers and reverse the demand spikes.
- **Our answer.** Do not market circumvention of age checks. Build the ability to verify age where the law requires it. Keep the partner channel, which is less exposed because the partner already knows its customer.

### Platform risk

- **The objection.** Browsers now give VPNs away. Firefox's built-in VPN is unlimited until the end of January 2027 ([Mozilla](https://blog.mozilla.org/en/firefox/built-in-vpn-unlimited-data/)). A free tier from PureVPN competes with free products from brands people already trust.
- **Our answer.** Browser VPNs cover one browser and offer few locations. The free tier is aimed at markets and uses (whole-device protection, blocked apps) they do not serve. This answer weakens if Apple or Google ship a system-wide free VPN.

### Execution capacity

- **The objection.** PureVPN already ships a VPN, a password manager, data removal, an eSIM, a business product, a white-label platform and a ChatGPT app, and reviewers describe the result as unpolished ([PCMag](https://uk.pcmag.com/vpn/4500/purevpn), [TechRadar](https://www.techradar.com/reviews/pc-mac/software/utilities/purevpn-1325640/review)). Five core bets plus a private AI product repeats the mistake.
- **Our answer.** The strategy only works with the stop list enforced. Two bets (partners and trust) run first. The others wait for their gates. If the private AI build goes ahead, something on this list should be dropped rather than run in parallel.

### "The goal itself is wrong."

- **The objection.** Ten times the customers at a fifth of the revenue per customer is a worse business than three times the revenue from better customers. A plan built on trust, the bundle and private AI might create more value with a 2x to 3x customer count.
- **Our answer.** We have sympathy with this. The brief asked for customer count, so the report optimises for it. The revenue column in every scenario is there so that leadership can choose with both in view.

## What would change our recommendation

| If we learned that | We would |
|---|---|
| PureWL already has more than 2 million partner-paid active users | Treat partners as the existing engine, restate the baseline, and move emphasis to direct growth |
| PureWL revenue per active user is under $0.15 a month | Lower the partner bet's revenue case and require inclusion in paid plans only |
| Fewer than 2 of 20 partner conversations proceed, citing trust | Pause partner sales, finish the trust reset, and test a separate brand for the kit |
| Network cost per free user is above $0.20 a month | Drop the free tier and rely on trials and regional pricing |
| Annual churn is above 45% | Put retention ahead of every acquisition bet |
| Affiliates supply more than 60% of new sales | Protect that channel first and stage every price change |
| The paying base is above 1.2M | Raise the direct targets; 10x direct remains out of reach but 3x becomes the centre |

## Open gaps

- No public benchmark exists for activation of a VPN included in a partner plan. The 10% threshold is our judgment.
- The thresholds for billing changes are proposals. PureVPN's finance team should set the acceptable revenue loss.
- We could not interview partners, customers or staff. Every qualitative judgment here rests on public material.
