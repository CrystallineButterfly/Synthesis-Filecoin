# Proof Harbor Cloud

- **Repo:** `Synthesis-Filecoin`
- **Primary track:** Filecoin Agentic Storage
- **Category:** storage
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

A proof archive that writes impact artifacts, receipts, logs, and evidence bundles to Filecoin-ready manifests and retrieval receipts.

## Selected concept

A storage agent writes impact artifacts, receipts, logs, and evaluation bundles to Filecoin-ready manifests. A registry contract stores content commitments, access policy hashes, and retrieval receipts so the repo is ready to attach live CID proofs later.

## Idea shortlist

1. Impact Proof Archive
2. Private Evidence Vault
3. Agentic Storage Control Plane

## Partners covered

Filecoin, Octant, Venice, ERC-8004 Receipts, OpenServ, Markee

## Architecture

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[ProofHarborRegistry policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> filecoin[Filecoin]
    Contract --> octant[Octant]
    Contract --> venice[Venice]
    Contract --> erc_8004_receipts[ERC-8004 Receipts]
    Contract --> openserv[OpenServ]
    Contract --> markee[Markee]
```

## Repository layout

- `src/`: shared policy contracts plus the repo-specific wrapper contract.
- `script/`: Foundry deployment entrypoint.
- `agents/`: Python runtime, partner adapters, and project metadata.
- `scripts/`: CLI utilities for running the loop and rendering submissions.
- `docs/`: architecture, credentials, demo script, and security notes.
- `submissions/`: generated `synthesis.md` snippet for this repo.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `filecoin_proof_store` | Filecoin | Use Filecoin for a bounded action in this repo. | $20 | medium |
| `octant_signal_publish` | Octant | Use Octant for a bounded action in this repo. | $25 | medium |
| `venice_private_analysis` | Venice | Use Venice for a bounded action in this repo. | $5 | high |
| `erc_8004_receipts_receipt_anchor` | ERC-8004 Receipts | Use ERC-8004 Receipts for a bounded action in this repo. | $1 | medium |
| `openserv_job_dispatch` | OpenServ | Use OpenServ for a bounded action in this repo. | $10 | medium |
| `markee_repo_message` | Markee | Use Markee for a bounded action in this repo. | $5 | low |

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| Filecoin | FILECOIN_API_TOKEN, FILECOIN_UPLOAD_URL | https://docs.filecoin.cloud/ |
| Octant | OCTANT_SIGNAL_URL | https://octant.app/ |
| Venice | VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL | https://docs.venice.ai/ |
| ERC-8004 Receipts | RPC_URL | https://eips.ethereum.org/EIPS/eip-8004 |
| OpenServ | OPENSERV_API_KEY, OPENSERV_AGENT_URL | https://docs.openserv.ai/ |
| Markee | MARKEE_API_KEY, MARKEE_MESSAGE_URL | https://markee.xyz/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for ProofHarborRegistry.
3. Run python3 scripts/run_agent.py to produce a dry run for filecoin_proofs.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
