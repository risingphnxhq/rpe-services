# Commercial evidence — bounded extension proposed for review

No migration or production deployment has been performed. This is the minimal extension proposed under the construction directive's schema-approval requirement.

## Existing systems and ownership

Keep the Google Apps Script Cases sheet as the existing inquiry/correspondence tracker and Corporate services_ops as the existing escalation-review records. Do not add another customer identity or universal case registry. Systems-side inspection found no offer/referral/commercial registry under the searched names; this is not proof that no differently named registry exists. Corporate access is currently unavailable to this session, so its existing structures must be reconciled before applying a schema extension.

## Proposed commercial records

1. **Offers:** existing editorial catalog projected into an appropriate approved commercial schema. Offer ID, owner, product/partner identity, destination, commercial status, eligibility/disclosure version, approval evidence and expiry. Public reads return only approved public entries. A preview is not an active offer; unverified links cannot become referral destinations.
2. **Commercial events:** append-only facts correlated to offer ID and existing inquiry/case ID, with source event ID, event type, timestamp, evidence reference and actual service actor. No email body, bank document, identity document or separate customer profile. Enforce uniqueness of source plus source event ID for safe retries.

Allowed event meanings must remain distinct: prepared inquiry, received inquiry, outbound referral, partner application, approval, sale, funding, earned commission, paid commission, reversal and exception. Browser preparation is not receipt. A browser click is not a partner application or revenue. Only verified provider/authorized reconciliation evidence can establish consequential partner or revenue events. Corrections append reversal/correction evidence rather than overwriting history.

## Connection to current inquiry operation

The storefront prepares `RPE-WEB-<uuid>` in the email subject/body, with a listed offer and customer-declared source code. Actual case receipt and its `RPE-SVC` reference are issued by the existing mail operation. A future bounded update to that operation should associate these references after receipt and write only authorized metadata to Supabase. Never trust customer-supplied references as ownership or accept their text as evidence of a sale. Preserve existing duplicate suppression, sensitive-message escalation and operator decisions.

## Deployment dependencies

- Read back current Apps Script deployment and existing Corporate review integration through an authorized connection.
- Prime CSE approves the smallest schema delta after checking existing registry alternatives.
- Prove authenticated event writes, duplicate retry, wrong offer/source, revoked authority, correction, and no inferred revenue.
- Verify support/admin receive/reply identities separately; they are not enabled for automated replies by this change.
- Bind the first genuinely approved partner/referral URL; no currently verified approved offer is supplied by the construction directive.
- Independently test and review customer-data, privacy and financial changes before release.

These are specific production dependencies. They do not authorize Foreman, PCC adapters, bridges, new email identities or replacement systems.
