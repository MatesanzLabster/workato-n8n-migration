# Workato to n8n Migration Project

## Purpose

This project is used to migrate Workato recipes to n8n workflows for the company.

## Main ideas for upcoming sessions

- Use the configured alternate server `n8n-mcp`, not the separate local `n8n` server.
- The remote n8n endpoint requires the user VPN to be connected.
- Verify the connection with `n8n-revops-mcp` MCP before declaring it working.
- Perform MCP actions directly in the current session; do not use subagents unless the user explicitly asks.

## Migration in progress

- First recipe being migrated: "Callable - Create Customer in NetSuite" (source description in `recipes/Callable - Create Customer in Netsuite.md`).
- Draft n8n Workflow SDK code written to `workflows/create-customer-in-netsuite.workflow.ts` (not yet created in n8n — validated with `validate_workflow`, valid with only cosmetic warnings).
- Salesforce Sandbox `labster--partialsb.sandbox.my.salesforce.com`, Connected App "N8N Connected App" using OAuth2 Client Credentials flow (Run As: asingla@labster.com.partialsb, scope `api`). Configured in n8n as a generic "OAuth2 API" credential (Grant Type: Client Credentials) and verified working via an HTTP Request node (e.g. `GET /services/data/v60.0/sobjects/Account/describe` returns 200). Use this same credential for all Salesforce HTTP Request calls; no native Salesforce node needed since Client Credentials isn't supported by it.

## Working rules

- Keep only stable, high-level context and main ideas in this file.
- Do not create or maintain separate conversation-log or ideas files unless the user explicitly requests one.
- Do not record every message, command, or result.
- Keep secrets out of this file: redact tokens, passwords, API keys, cookies, and private URLs.
- Use the project directory as the working directory unless the user explicitly asks otherwise.
- User may use his/her mothertongue, but you always document in English.