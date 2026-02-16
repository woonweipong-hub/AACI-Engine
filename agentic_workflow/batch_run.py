from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
from typing import Any, Dict, List

from supabase_store import build_store_from_env
from workflow_orchestrator import AgenticWorkflowOrchestrator, ClauseResult


REQUIRED_FIELDS = {"clause_id", "compliance_label", "confidence", "uncertainty"}


def _load_json(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("JSON input must be a list of clause records.")
    return data


def _load_csv(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            records.append(dict(row))
    return records


def _to_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned:
            return []
        try:
            parsed = json.loads(cleaned)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except json.JSONDecodeError:
            pass
        return [part.strip() for part in cleaned.split(";") if part.strip()]
    return [str(value)]


def _normalize(record: Dict[str, Any]) -> ClauseResult:
    missing = REQUIRED_FIELDS - set(record.keys())
    if missing:
        raise ValueError(f"Missing required fields: {sorted(missing)} in record={record}")

    return ClauseResult(
        clause_id=str(record["clause_id"]),
        compliance_label=str(record["compliance_label"]),
        confidence=float(record["confidence"]),
        uncertainty=float(record["uncertainty"]),
        risk_tier=str(record.get("risk_tier", "A") or "A"),
        evidence_refs=_to_list(record.get("evidence_refs")),
        assumptions=_to_list(record.get("assumptions")),
    )


def run(input_path: Path, output_path: Path, upload: bool) -> Dict[str, Any]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() == ".json":
        raw = _load_json(input_path)
    elif input_path.suffix.lower() == ".csv":
        raw = _load_csv(input_path)
    else:
        raise ValueError("Unsupported input file format. Use .json or .csv")

    clauses = [_normalize(item) for item in raw]

    orchestrator = AgenticWorkflowOrchestrator()
    results = orchestrator.run_batch(clauses)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    if upload:
        store = build_store_from_env()
        if store is None:
            raise RuntimeError("Supabase upload requested, but env vars are missing.")
        source = os.getenv("WORKFLOW_SOURCE", "agentic_workflow_batch")
        upload_info = store.save_batch(results, source=source)
        results["supabase_upload"] = upload_info

    return results


def main() -> None:
    default_input = Path(__file__).resolve().parent / "inputs" / "clauses_input_example.json"
    default_output = Path(__file__).resolve().parent / "outputs" / "multi_clause_run_trace.json"

    parser = argparse.ArgumentParser(description="Run agentic workflow over multiple clauses.")
    parser.add_argument("--input", type=Path, default=default_input, help="Path to JSON/CSV clause input")
    parser.add_argument("--output", type=Path, default=default_output, help="Path to write run trace JSON")
    parser.add_argument("--upload", action="store_true", help="Upload results to Supabase")
    args = parser.parse_args()

    results = run(args.input, args.output, args.upload)
    print(f"Saved: {args.output}")
    print(f"total_clauses={results['total_clauses']}")
    print(f"auto_approved={results['auto_approved']}, abstain_escalate={results['abstain_escalate']}")
    if "supabase_upload" in results:
        info = results["supabase_upload"]
        print(f"Supabase uploaded run_id={info['run_id']} traces={info['uploaded_traces']}")


if __name__ == "__main__":
    main()
