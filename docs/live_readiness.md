# Live readiness

- **Project:** Proof Harbor Cloud
- **Track:** Filecoin Agentic Storage
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:12+00:00`

## Trust boundaries

- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **Octant** — `rest_json` — Publish scored public-goods signals and DPI artifacts.
- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **OpenServ** — `rest_json` — Dispatch jobs and expose swarm service endpoints.
- **Markee** — `rest_json` — Publish GitHub-adjacent build stories and repo messages.

## Offline-ready partner paths

- **Filecoin** — prepared_filecoin_bundle
- **ERC-8004 Receipts** — prepared_contract_call

## Live-only partner blockers

- **Octant**: OCTANT_SIGNAL_URL — https://octant.app/
- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **OpenServ**: OPENSERV_API_KEY, OPENSERV_AGENT_URL — https://docs.openserv.ai/
- **Markee**: MARKEE_API_KEY, MARKEE_MESSAGE_URL — https://markee.xyz/

## Highest-sensitivity actions

- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for ProofHarborRegistry.
- Run python3 scripts/run_agent.py to produce a dry run for filecoin_proofs.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
