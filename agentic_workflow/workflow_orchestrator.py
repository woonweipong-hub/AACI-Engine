from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any, List

from safety_gate import SafetyGate


@dataclass
class ClauseResult:
    clause_id: str
    compliance_label: str
    confidence: float
    uncertainty: float
    risk_tier: str = "A"
    evidence_refs: List[str] | None = None
    assumptions: List[str] | None = None


class AgenticWorkflowOrchestrator:
    """Minimal orchestrator for research experiments.

    This skeleton is intentionally light and independent from AECOA,
    so you can iterate quickly in the research folder.
    """

    def __init__(self):
        self.safety_gate = SafetyGate()

    def evaluate_clause_result(self, result: ClauseResult) -> Dict[str, Any]:
        gate = self.safety_gate.decide(
            confidence=result.confidence,
            uncertainty=result.uncertainty,
            risk_tier=result.risk_tier,
        )

        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "clause_id": result.clause_id,
            "compliance_label": result.compliance_label,
            "confidence": result.confidence,
            "uncertainty": result.uncertainty,
            "risk_tier": result.risk_tier,
            "gate_decision": gate.to_dict(),
            "evidence_refs": result.evidence_refs or [],
            "assumptions": result.assumptions or [],
        }

    def run_batch(self, clause_results: List[ClauseResult]) -> Dict[str, Any]:
        traces = [self.evaluate_clause_result(item) for item in clause_results]

        total = len(traces)
        escalated = sum(1 for t in traces if t["gate_decision"]["action"] == "abstain_escalate")

        return {
            "run_timestamp": datetime.utcnow().isoformat() + "Z",
            "total_clauses": total,
            "auto_approved": total - escalated,
            "abstain_escalate": escalated,
            "traces": traces,
        }


def to_dict(payload: Any) -> Dict[str, Any]:
    if hasattr(payload, "__dataclass_fields__"):
        return asdict(payload)
    if isinstance(payload, dict):
        return payload
    raise TypeError("Unsupported payload type")
