# AIsa Doc Reality Audit

- **Target:** https://aisa.one
- **Run (UTC):** 2026-06-26T02:11:08.920504+00:00
- **Result:** 3 blockers · 1 warnings · 4 ok

| Sev | Check | Finding |
|-----|-------|---------|
| 🔴 | `discovery_endpoint` | Discovery endpoint unusable: /openapi.yaml (Consolidated OpenAPI spec (cited by guide + ai-plugin)) |
| 🔴 | `count_drift_skills` | Skill count drift: guide says 13, live agent card advertises 45 |
| 🔴 | `localization_zh` | Chinese doc coverage is 1.3% (10/773 indexed pages). China is the gateway's headline model-supply market. |
| 🟡 | `count_drift_paths` | Guide promises one consolidated spec with 111+ paths, but the live index ships 30 separate per-service OpenAPI files and no consolidated spec. |
| 🟢 | `discovery_endpoint` | Discovery endpoint OK: /.well-known/agent-card.json |
| 🟢 | `discovery_endpoint` | Discovery endpoint OK: /.well-known/ai-plugin.json |
| 🟢 | `discovery_endpoint` | Discovery endpoint OK: /.well-known/mcp.json |
| 🟢 | `discovery_endpoint` | Discovery endpoint OK: /docs/llms.txt |

## Blockers — detail & remediation

### Discovery endpoint unusable: /openapi.yaml (Consolidated OpenAPI spec (cited by guide + ai-plugin))

```json
{
  "url": "https://aisa.one/openapi.yaml",
  "http_status": 404,
  "returned_html_shell": false
}
```
**Fix:** Either publish the resource at this exact URL or update every reference (ai-plugin.json `api.url`, agent-discovery guide) to the real location. Agents following the published contract currently hit a dead link here.

### Skill count drift: guide says 13, live agent card advertises 45

```json
{
  "claimed": 13,
  "live": 45,
  "claimed_source": "https://aisa.one/docs/guides/agent-discovery.md",
  "live_source": "https://aisa.one/.well-known/agent-card.json"
}
```
**Fix:** The skill catalogue is generated; the guide's number is hand-typed. Replace the literal with a build-time injection from the agent card so it can never drift.

### Chinese doc coverage is 1.3% (10/773 indexed pages). China is the gateway's headline model-supply market.

```json
{
  "zh_pages": 10,
  "total_pages": 773,
  "zh_share_pct": 1.3,
  "examples": [
    "https://aisa.one/docs/agent-skills/last30days-zh.md",
    "https://aisa.one/docs/agent-skills/prediction-market-arbitrage-zh.md",
    "https://aisa.one/docs/agent-skills/prediction-market-data-zh.md",
    "https://aisa.one/docs/guides/chinese-llms.md",
    "https://aisa.one/docs/guides/chinese-llms/bytedance.md",
    "https://aisa.one/docs/guides/chinese-llms/deepseek.md",
    "https://aisa.one/docs/guides/chinese-llms/glm.md",
    "https://aisa.one/docs/guides/chinese-llms/kimi.md"
  ]
}
```
**Fix:** Stand up a zh-CN docs tree mirroring the EN tree. Prioritise the first-success path: quickstart + chinese-llms + auth. Drive it from the same source via an automated translate-and-PR agent.
