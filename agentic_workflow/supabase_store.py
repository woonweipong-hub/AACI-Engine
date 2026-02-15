from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Dict, Any, List, Optional


class SupabaseTraceStore:
    def __init__(self, url: str, service_role_key: str):
        self.url = url.rstrip("/")
        self.service_role_key = service_role_key

    def _request(self, method: str, path: str, payload: Optional[Any] = None, prefer: str = "") -> Any:
        endpoint = f"{self.url}/rest/v1/{path.lstrip('/')}"
        body = None
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")

        headers = {
            "apikey": self.service_role_key,
            "Authorization": f"Bearer {self.service_role_key}",
            "Content-Type": "application/json",
        }
        if prefer:
            headers["Prefer"] = prefer

        req = urllib.request.Request(endpoint, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                raw = response.read().decode("utf-8", errors="ignore").strip()
                if not raw:
                    return None
                return json.loads(raw)
        except urllib.error.HTTPError as err:
            detail = err.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"Supabase request failed ({err.code}): {detail}") from err

    def create_workflow_run(self, results: Dict[str, Any], source: str = "agentic_workflow") -> str:
        payload = {
            "run_timestamp": results.get("run_timestamp"),
            "source": source,
            "total_clauses": int(results.get("total_clauses", 0)),
            "auto_approved": int(results.get("auto_approved", 0)),
            "abstain_escalate": int(results.get("abstain_escalate", 0)),
            "raw_json": results,
        }

        inserted = self._request(
            "POST",
            "workflow_runs?select=id",
            payload,
            prefer="return=representation",
        )
        if not inserted or not isinstance(inserted, list):
            raise RuntimeError("Supabase insert returned no workflow run record.")

        return inserted[0]["id"]

    def create_clause_traces(self, run_id: str, traces: List[Dict[str, Any]]) -> None:
        rows = []
        for trace in traces:
            gate = trace.get("gate_decision", {})
            rows.append(
                {
                    "run_id": run_id,
                    "clause_id": trace.get("clause_id"),
                    "compliance_label": trace.get("compliance_label"),
                    "confidence": trace.get("confidence"),
                    "uncertainty": trace.get("uncertainty"),
                    "risk_tier": trace.get("risk_tier"),
                    "gate_action": gate.get("action"),
                    "gate_reason": gate.get("reason"),
                    "trace_json": trace,
                }
            )

        if rows:
            self._request("POST", "clause_traces", rows)

    def save_batch(self, results: Dict[str, Any], source: str = "agentic_workflow") -> Dict[str, Any]:
        run_id = self.create_workflow_run(results, source=source)
        self.create_clause_traces(run_id, results.get("traces", []))
        return {
            "run_id": run_id,
            "total_clauses": int(results.get("total_clauses", 0)),
            "uploaded_traces": len(results.get("traces", [])),
        }


def build_store_from_env() -> Optional[SupabaseTraceStore]:
    url = os.getenv("SUPABASE_URL", "").strip()
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip()
    if not url or not key:
        return None
    return SupabaseTraceStore(url=url, service_role_key=key)
