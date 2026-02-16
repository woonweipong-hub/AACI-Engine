# Quality Gate Checklist (Before Accepting JSONL)

## Structural checks
- [ ] Valid JSON on every line
- [ ] Passes canonical_clause_schema.json
- [ ] Required fields present for every record

## Semantic checks
- [ ] Clause IDs and source pages are correct
- [ ] Numeric thresholds and units are exact
- [ ] Applicability and constraints are separated
- [ ] Prohibitions represented explicitly (not inferred)

## Safety checks
- [ ] Risk tier assigned
- [ ] Auto-decision policy set
- [ ] Escalation trigger defined for uncertain/ambiguous cases

## Consistency checks
- [ ] No contradictory constraints for same clause
- [ ] Similar clauses use consistent field names and units
- [ ] Output keys follow naming convention

## Human review checks
- [ ] Ambiguity flags are reasonable
- [ ] At least one sample from each ambiguity type reviewed
- [ ] Reviewer sign-off recorded with timestamp
