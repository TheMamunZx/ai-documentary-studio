# Fact-Checking & Claim Control

## Purpose
Prevent unsupported statements, false precision, causal leaps, and dramatized assumptions from entering narration, captions, maps, or generated imagery.

## Audit procedure
1. Break the script into one factual proposition per sentence or clause.
2. Assign claim IDs and link each to source IDs in `claim_register.csv`.
3. Verify names, dates, units, currencies, translations, locations, rankings, quantities, and quotation attribution.
4. Check whether the source directly supports the wording, not merely the general topic.
5. Look for contrary or newer evidence, especially for scientific, political, economic, health, or current-technology claims.
6. Separate observation from inference and correlation from causation.
7. Use calibrated language only where evidence supports uncertainty; qualifiers do not rescue unsupported claims.
8. Flag any claim needing an on-screen caveat or a visible source citation.

## High-risk language
Scrutinize words such as “first”, “only”, “impossible”, “perfect”, “unprecedented”, “proven”, “secret”, “hidden”, “scientists cannot explain”, “the real reason”, and exact percentages or dates. These require direct support and careful scope.

## Deliverable
`fact_check_report.md` with claim ID, draft wording, status, supporting/contradicting evidence, source IDs, risk, correction, and on-screen note. No high-impact unresolved claim may be presented as established fact.
