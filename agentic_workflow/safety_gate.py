from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class SafetyGateThresholds:
    tier_a_min_confidence: float = 0.90
    tier_b_min_confidence: float = 0.75
    tier_a_max_uncertainty: float = 0.25
    tier_b_max_uncertainty: float = 0.40


@dataclass
class SafetyGateDecision:
    action: str
    risk_tier: str
    confidence: float
    uncertainty: float
    reason: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class SafetyGate:
    """Risk-aware decision policy for compliance outcomes.

    Actions:
    - auto_approve
    - abstain_escalate
    """

    def __init__(self, thresholds: SafetyGateThresholds | None = None):
        self.thresholds = thresholds or SafetyGateThresholds()

    def decide(self, confidence: float, uncertainty: float, risk_tier: str = "A") -> SafetyGateDecision:
        tier = (risk_tier or "A").strip().upper()

        if tier == "A":
            min_confidence = self.thresholds.tier_a_min_confidence
            max_uncertainty = self.thresholds.tier_a_max_uncertainty
        else:
            min_confidence = self.thresholds.tier_b_min_confidence
            max_uncertainty = self.thresholds.tier_b_max_uncertainty

        if confidence >= min_confidence and uncertainty <= max_uncertainty:
            return SafetyGateDecision(
                action="auto_approve",
                risk_tier=tier,
                confidence=confidence,
                uncertainty=uncertainty,
                reason="Within confidence and uncertainty thresholds.",
            )

        reasons = []
        if confidence < min_confidence:
            reasons.append(f"confidence {confidence:.3f} < required {min_confidence:.3f}")
        if uncertainty > max_uncertainty:
            reasons.append(f"uncertainty {uncertainty:.3f} > allowed {max_uncertainty:.3f}")

        return SafetyGateDecision(
            action="abstain_escalate",
            risk_tier=tier,
            confidence=confidence,
            uncertainty=uncertainty,
            reason="; ".join(reasons) if reasons else "Threshold mismatch.",
        )
