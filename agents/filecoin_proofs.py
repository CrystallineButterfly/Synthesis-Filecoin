"""Project-specific context for Proof Harbor Cloud."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "Proof Harbor Cloud",
    "track": "Filecoin Agentic Storage",
    "pitch": "A proof archive that writes impact artifacts, receipts, logs, and evidence bundles to Filecoin-ready manifests and retrieval receipts.",
    "overlap_targets": [
        "Octant",
        "YieldGuard",
        "Venice Private Agents",
        "ERC-8004 Receipts",
        "OpenServ",
        "Markee"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
