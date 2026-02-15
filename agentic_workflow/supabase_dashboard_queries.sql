-- Dashboard query pack for AACI agentic workflow traces
-- Assumes schema from `supabase_schema.sql` has been applied.

-- 1) Overall run summary (latest 30 days)
select
  count(*) as total_runs,
  coalesce(sum(total_clauses), 0) as total_clauses,
  coalesce(sum(auto_approved), 0) as total_auto_approved,
  coalesce(sum(abstain_escalate), 0) as total_escalated,
  case when coalesce(sum(total_clauses), 0) = 0 then 0
       else round(100.0 * coalesce(sum(auto_approved), 0) / sum(total_clauses), 2)
  end as auto_approval_rate_pct
from public.workflow_runs
where created_at >= now() - interval '30 days';

-- 2) Daily trend (approval vs escalation)
select
  date_trunc('day', created_at) as day,
  sum(total_clauses) as total_clauses,
  sum(auto_approved) as auto_approved,
  sum(abstain_escalate) as escalated,
  case when sum(total_clauses) = 0 then 0
       else round(100.0 * sum(auto_approved) / sum(total_clauses), 2)
  end as auto_approval_rate_pct
from public.workflow_runs
group by 1
order by 1 desc;

-- 3) Escalation hotspots by clause
select
  clause_id,
  count(*) as occurrences,
  sum(case when gate_action = 'abstain_escalate' then 1 else 0 end) as escalations,
  round(
    100.0 * sum(case when gate_action = 'abstain_escalate' then 1 else 0 end)
    / nullif(count(*), 0),
    2
  ) as escalation_rate_pct,
  round(avg(confidence)::numeric, 4) as avg_confidence,
  round(avg(uncertainty)::numeric, 4) as avg_uncertainty
from public.clause_traces
group by clause_id
order by escalations desc, occurrences desc;

-- 4) Confidence distribution buckets
select
  case
    when confidence < 0.5 then '<0.50'
    when confidence < 0.7 then '0.50-0.69'
    when confidence < 0.85 then '0.70-0.84'
    when confidence < 0.95 then '0.85-0.94'
    else '>=0.95'
  end as confidence_bucket,
  count(*) as trace_count,
  sum(case when gate_action = 'abstain_escalate' then 1 else 0 end) as escalated_count
from public.clause_traces
group by 1
order by 1;

-- 5) Risk-tier behavior
select
  risk_tier,
  count(*) as traces,
  sum(case when gate_action = 'auto_approve' then 1 else 0 end) as auto_approved,
  sum(case when gate_action = 'abstain_escalate' then 1 else 0 end) as escalated,
  round(100.0 * sum(case when gate_action = 'abstain_escalate' then 1 else 0 end) / nullif(count(*),0), 2) as escalation_rate_pct,
  round(avg(confidence)::numeric, 4) as avg_confidence,
  round(avg(uncertainty)::numeric, 4) as avg_uncertainty
from public.clause_traces
group by risk_tier
order by risk_tier;

-- 6) Latest run with per-clause details
with latest_run as (
  select id, created_at
  from public.workflow_runs
  order by created_at desc
  limit 1
)
select
  lr.created_at as run_created_at,
  ct.clause_id,
  ct.compliance_label,
  ct.confidence,
  ct.uncertainty,
  ct.risk_tier,
  ct.gate_action,
  ct.gate_reason
from latest_run lr
join public.clause_traces ct on ct.run_id = lr.id
order by ct.clause_id;

-- 7) Most common escalation reasons
select
  gate_reason,
  count(*) as occurrences
from public.clause_traces
where gate_action = 'abstain_escalate'
group by gate_reason
order by occurrences desc
limit 20;
