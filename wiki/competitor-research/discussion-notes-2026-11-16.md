# Competitor research: discussion notes

[Back to wiki home](../README.md)

**Research date:** 16 November 2026 (Asia/Dubai).

These notes supplement the full teardown documents for [Venice AI](venice-ai-teardown.md) and [Proton Lumo](proton-lumo-teardown.md). They capture analysis from the research discussion that is not duplicated in the main reports.

**Related teardowns**

- [Venice AI teardown and growth playbook](venice-ai-teardown.md) — company teardown, revenue mix, OpenRouter signal, Crusoe comparison, adult marketing inventory, PureVPN takeaways.
- [Proton Lumo teardown and growth playbook](proton-lumo-teardown.md) — suite bundling, privacy architecture, growth playbook including AI Paper Trail, Lumo vs Venice.

---

<a id="openrouters-role"></a>

## OpenRouter's role

OpenRouter is a marketplace/router: developers use one API key to reach many model providers (OpenAI, Anthropic, Google, Venice, and others). OpenRouter routes each request to a provider, bills the developer, and pays the provider. It publishes per-provider token volumes, which third parties (e.g. Vantage, [routers.vantage.sh](https://routers.vantage.sh)) convert into estimated spend. This gives an outside view of Venice developer demand, but it is only one channel: direct Venice API users and Venice consumer app usage are invisible there.

OpenRouter is roughly **15% or less** of Venice company tokens (versus ~500B tokens/day claimed by Voorhees in Oct 2026). Treat OpenRouter billings (~$970.6K trailing 30 days at list price) as a **floor and a trend signal**, gross of OpenRouter's take.

See also: [Who Venice sells to → OpenRouter](venice-ai-teardown.md#who-buys) in the Venice teardown.

---

<a id="api-billings-vs-subscription-revenue-quality-of-revenue"></a>

## API billings vs subscription revenue (quality of revenue)

- **API/credit revenue** is usage-based: COGS (GPU inference, plus per-token fees to frontier model vendors when reselling Claude/GPT) scales with revenue; margins thin to moderate; price-competitive across providers; revenue fluctuates with customer usage. Revenue via OpenRouter is gross of OpenRouter's cut.
- **Subscription revenue** is flat-fee: light users are high margin, heavy users can be loss-making; generally steadier, more predictable margins; churn is the risk.
- **Implication:** if 45–70% of Venice revenue is developer/metered (see the working range in the Venice teardown), the business is **lower-margin and less durable** than the $150M headline implies, warranting a lower valuation multiple. Venice has not disclosed margins; this is the general industry pattern.

See also: [Revenue mix: API vs subscriptions](venice-ai-teardown.md#revenue-mix) in the Venice teardown.

---

## Venice vs Crusoe (developer choice)

Crusoe offers managed inference with strong privacy. Verified: Crusoe Managed Inference terms (OpenRouter customers) say no training on and no on-disk storage of customer data, close to Venice's zero-retention claim. Crusoe's AUP is **not** uncensored (bans harmful use, prohibits evading filters). So **privacy is not a differentiator for Venice**; **uncensored is**.

Venice's remaining edges: consumer-plus-API brand, uncensored/NSFW as a product, TEE/E2EE options, crypto/DIEM/x402 payments, large multimodal catalog. Venice does not win on price or speed.

See also: [Competition and competitiveness](venice-ai-teardown.md#competition) in the Venice teardown.

---

## AI Paper Trail (switcher asset)

Proton's free tool ([proton.me/lumo/ai/ai-paper-trail](https://proton.me/lumo/ai/ai-paper-trail), Aug 2026): users upload a ChatGPT or Claude export and get a privacy exposure score showing personal info shared (health, money, work, relationships), then are pitched Lumo.

A **switcher asset** is a marketing tool designed to pull users from a competitor: high intent, makes privacy risk personal, cheap vs paid ads, shareable. PureVPN could build an equivalent ("what does ChatGPT know about you") ending in a PureVPN offer, without needing its own AI assistant first. It must process data **without storing it**, or it undermines the privacy message.

See also: [Growth playbook](proton-lumo-teardown.md#playbook) in the Proton Lumo teardown.