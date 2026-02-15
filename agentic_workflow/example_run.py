from __future__ import annotations

import json
import os
from pathlib import Path

from workflow_orchestrator import AgenticWorkflowOrchestrator, ClauseResult
from supabase_store import build_store_from_env


def main() -> None:
    orchestrator = AgenticWorkflowOrchestrator()

    # Example data aligned with your pilot style (multi-condition HS clause)
    sample = [
        ClauseResult(
            clause_id="TRHS-2.10",
            compliance_label="conditional_pass",
            confidence=0.84,
            uncertainty=0.31,
            risk_tier="A",
            evidence_refs=["drawing_sheet_A1", "jsonl_rule_2_10"],
            assumptions=["staircase boundary inferred from annotation layer"],
        ),
        ClauseResult(
            clause_id="TRHS-2.2.2a",
            compliance_label="pass",
            confidence=0.96,
            uncertainty=0.12,
            risk_tier="A",
            evidence_refs=["section_view_S2"],
            assumptions=[],
        ),
    ]

    results = orchestrator.run_batch(sample)

    out_path = Path(__file__).resolve().parent / "outputs" / "pilot_run_trace.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(f"Saved: {out_path}")
    print(f"auto_approved={results['auto_approved']}, abstain_escalate={results['abstain_escalate']}")

    store = build_store_from_env()
    if store is None:
        print("Supabase upload skipped (set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY).")
        return

    source = os.getenv("WORKFLOW_SOURCE", "agentic_workflow_example")
    uploaded = store.save_batch(results, source=source)
    print(f"Supabase uploaded run_id={uploaded['run_id']} traces={uploaded['uploaded_traces']}")


if __name__ == "__main__":
    main()
