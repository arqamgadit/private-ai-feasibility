# 2. Financial model

[Back to wiki home](README.md)

A 60-month model starting at month 1 of the build, in USD. The interactive version, with every assumption editable plus bear/base/bull scenarios and sensitivity charts, is here:
[Venice-style AI + Agent Mode: 5-Year Financial Model](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/1e8b646a-bc93-4ead-8979-f9cbca57dec3).

All figures below are the base case unless stated.

## Headlines

| Metric | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Revenue | $0.56M | $5.8M | $17.2M | $34.9M | $58.9M |
| Gross margin | 16% | 54% | 65% | 70% | 74% |
| Operating expenses | $2.7M | $6.6M | $12.5M | $19.7M | $28.1M |
| EBITDA | -$2.6M | -$3.5M | -$1.4M | +$4.7M | +$15.2M |
| Exit ARR | $1.7M | $9.6M | $23.8M | $44.2M | $71.0M |
| Paying subscribers (year end) | 6k | 28k | 67k | 122k | 190k |
| Monthly active users (year end) | 148k | 506k | 1.06M | 1.74M | 2.54M |
| Headcount (year end) | 16 | 33 | 54 | 77 | 98 |

- EBITDA turns positive for good in **month 33**.
- Cumulative losses peak at about **$7.8M**, so that is the capital needed to reach breakeven.
- Pre-launch build cost (months 1–4) is about **$0.65M**.
- At 8x ARR, Year 5 exit ARR implies a valuation of about $570M.

## Scenarios

| Metric | Bear | Base | Bull |
|---|---|---|---|
| Y5 revenue | $36.3M | $58.9M | $88.2M |
| Y5 exit ARR | $43.9M | $71.0M | $106.3M |
| Y5 paying subscribers | 102k | 190k | 305k |
| Y5 gross margin | 67% | 74% | 78% |
| Y5 EBITDA | -$3.8M | +$15.2M | +$40.3M |
| EBITDA breakeven | Beyond Y5 | Month 33 | Month 22 |
| Capital needed to breakeven | $24.6M | $7.8M | $4.0M |

- **Bear:** signups x0.6, conversion x0.75, churn x1.25, inference cost x1.2.
- **Bull:** signups x1.5, conversion x1.2, churn x0.85, inference cost x0.85.

## Revenue streams

1. **Pro subscriptions:** $18/month list price.
2. **Max subscriptions:** $49/month, includes agent mode. 25% of new paying users pick Max once agent mode launches.
3. **Agent credit top-ups:** 20% of Max users spend about $15/month extra.
4. **Developer API:** 0.1% of signups become API accounts, spending $60/month (growing 15% a year), with 4% monthly churn.
5. **Teams seats:** $40/seat/month from month 15; 150 new seats in the first month, with new-seat volume growing 4% a month.

In Year 5, Pro and Max subscriptions are about $22.5M each; API is $6.9M, Teams $5.4M and top-ups $1.6M.

## Key assumptions

### Acquisition and conversion

| Assumption | Value |
|---|---|
| Organic signups in launch month | 10,000 |
| Organic signup growth, month over month (Y1 to Y5) | 12%, 8%, 5%, 3%, 2% |
| Paid marketing spend per month (Y1 to Y5) | $40k, $120k, $250k, $420k, $650k |
| Paid cost per signup | $3.00 |
| Signup to paid in first month | 2.5% |
| Free base converting to paid each month | 0.25% |
| Free user monthly attrition | 15% |
| Pro / Max monthly churn | 6% / 5% |
| Share of paid users on annual plans | 35% (31% discount) |

### Inference and serving costs

| Assumption | Value |
|---|---|
| Open-model cost (self-hosted or cheap serverless) | $0.35 per 1M tokens |
| Premium closed-model cost | $4.00 per 1M tokens |
| Share of tokens on premium models | 10% |
| Unit cost decline | 30% a year |
| Usage per user growth | 15% a year |
| Tokens per month: free / Pro chat / Max chat | 0.15M / 1.5M / 3M |
| Agent tasks per month: Pro / Max | 10 / 60 |
| Tokens per agent task | 0.25M |
| Browser or code sandbox per task | $0.04 |
| Search and tool APIs per task | $0.02 |
| Images per month: free / Pro / Max | 30 / 300 / 500, at $0.004 each |
| Payment processing | 3% of revenue |
| Base infrastructure | $15k/month plus $0.03 per monthly active user |

### Team and operating costs

| Function | Today | Y1 | Y2 | Y3 | Y4 | Y5 | Loaded cost/yr |
|---|---|---|---|---|---|---|---|
| Engineering (ML, infra, agent, apps) | 4 | 8 | 16 | 26 | 36 | 45 | $170k |
| Product & design | 1 | 2 | 3 | 5 | 7 | 9 | $150k |
| Growth & marketing | 0 | 2 | 5 | 8 | 11 | 14 | $130k |
| Support & trust/safety | 0 | 2 | 5 | 9 | 14 | 18 | $70k |
| G&A (finance, legal, ops) | 1 | 2 | 4 | 6 | 9 | 12 | $140k |

Hires ramp linearly through each year. Salaries rise 4% a year, plus $500 per head per month for software and equipment.

| Other cost (per month) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Legal, compliance & content safety | $15k | $25k | $40k | $55k | $70k |
| R&D compute (fine-tuning, evals, staging) | $25k | $60k | $120k | $200k | $300k |
| Other G&A (office, insurance, audit) | $10k | $20k | $35k | $50k | $70k |

### Funding and tax

| Round | Month | Amount |
|---|---|---|
| Seed | 1 | $4M |
| Series A | 14 | $12M |
| Series B | 30 | $25M |

Total planned funding is $41M, enough to survive the bear case. Cash dips to about $1M just before the Series A, so raise that round earlier if possible.

Corporate tax is 9% (UAE), applied only after accumulated losses are used up.

## Unit economics (end of Year 2)

| Per user per month | Pro | Max |
|---|---|---|
| Effective price after annual discount | $16.05 | $43.68 |
| Total cost to serve | about $3.50 | about $14.40 |
| Gross margin | about 78% | about 67% |

Agent tokens are about 80% of a Max user's inference cost. Agent usage and the share of tokens sent to premium closed models are the biggest margin risks.

## What the model leaves out

- **Deferred revenue:** annual plans are billed upfront, so real cash is better than shown.
- **VAT:** 5% UAE VAT on B2C digital services is treated as a pass-through.
- **UAE 0% tax band** on the first AED 375k of profit.
- **A crypto token** like Venice's VVV.
- **GPU capex:** all GPU capacity is assumed rented.

## Validation notes from later research

- The $0.35 per 1M tokens default holds even at launch if traffic goes to DeepInfra-priced models (DeepSeek V4 Flash is about $0.14 input / $0.28 output per 1M tokens). See [page 4](04-provider-comparison.md).
- The $0.06 agent tool cost per task is conservative. Real figures come to about $0.02–0.03 (roughly $0.008 of browser time plus three searches at $0.005 each).
- The 3% payment fee is optimistic if a processor classes the business as high-risk (4–8%). Keeping marketing clean (see [page 5](05-content-policy-and-trust-safety.md)) is the main defence.
- Budget an extra one-time $30–60k for initial legal setup across jurisdictions (see [page 6](06-legal-risks.md)).
