# Batch 1 — commercial navigation and catalog

Proposed against main `70e78b5d49eec5ac600e5acfa0c3d77365f9f647`.

## Changes

The existing static storefront now has navigation to Products & Connectivity, Business Services (PBS), Business Financing (PNC), and Business Network (DIBANA). Three informational destination pages and four homepage cards explain current availability. Existing About and Help links remain.

The eleven original pages retain their main content, product information, forms, scripts, disclosures and footer. Only common navigation/style changes affect every original page; the homepage additionally receives the destination cards. No framework or hosting changes.

`offer-catalog.json` is a versioned editorial catalog for the six displayed products/destinations, not a customer or case database. It records identity, ownership, category, description, destination, availability, disclosure, commission unknowns, eligibility unknowns and verification dates. Page destinations are source-checked; commercial verification remains null. No offer is marked commercially active. Existing supplier facts remain explicitly dated October 15, 2026. This batch introduces no prices, commissions, approved partners, order or application claims.

PBS links lead to existing assessment previews with their limitations explained. PNC provides education and a user-sent general email inquiry, not a credit application or lender introduction. DIBANA has no unverified enrollment link. PBO is not duplicated. No personal-data capture, tracking, cross-system transfer, database, email sender, adapter, bridge or authority root is added.

## Existing assets reused

Existing black/ivory/gold styles, header/logo, footer, product catalog, product detail pages, connectivity finder, comparison, inquiry builder, email address and privacy/disclosure pages.

## Verification

Run `python tests/check_catalog.py` from a checkout containing the baseline commit. The checks cover all fourteen pages' common navigation, local links/fragments, six catalog entries and preservation of eleven baseline page bodies/scripts outside the intentional insertions. Initial result: 31 checks passed. These are source checks, not a browser or independent assurance pass.

Playwright is installed in the construction environment, but Chromium is absent. Desktop/mobile, keyboard, print and visual interaction acceptance remain outstanding. No CATE review or production release is claimed.

## Review and release conditions

Prime CSE reviews this bounded implementation before the next batch. CATE independently checks desktop/mobile navigation, keyboard focus/order, existing catalog filtering/comparison/inquiry behavior, status labels and the lack of unapproved commercial actions. Keep existing storefront behavior available throughout.

No Supabase schema/policy changes. No newly approved referral destination or earned revenue established. Batch 2 requires actual partner approval, verified referral URL and required disclosures. Systems PSC packet retrieval/receiving acknowledgment is pending connection access; the pasted Founder-transferred construction order provided this proposal's scope. This document is not receiving acknowledgment or CATE acceptance.
