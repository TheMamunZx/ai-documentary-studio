# Copyright, Licensing & Provenance Audit

## Asset coverage
Track every video, still image, audio track, SFX, font, map tile, chart, dataset, screen capture, and AI-generated asset. Fields: asset ID, filename/path, creator/provider, source URL, acquisition date, license/terms URL, attribution text, commercial-use permission, modification permission, territory/term restrictions, model/provider terms, release/consent status, and reviewer decision.

## Rules
- “Free download” is not a license.
- Read the specific asset's license and the provider's current terms; do not infer from site branding.
- Flag non-commercial-only, editorial-only, attribution-required, share-alike, no-derivative, account-restricted, or unclear rights.
- Do not remove watermarks, bypass access controls, or use unlicensed ripped media.
- Real-person face/voice use requires rights and consent appropriate to the use; avoid impersonation.
- Escalate unclear legal questions to the user or qualified reviewer; do not present a legal opinion as definitive clearance.

## Deliverable
`asset_rights_register.csv` with per-asset `cleared`, `restricted`, `pending`, or `rejected` status and a blocking issues list.
