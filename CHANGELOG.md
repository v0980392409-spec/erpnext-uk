# Changelog

## 0.2.1 — 2026-10-15

- **709 new strings of the everyday Frappe interface** (data import, roles and permissions, workspace
  restore, user settings, search, Kanban cards, email composer, onboarding) — strings added in
  Frappe 16.35–16.52. Machine translations already in the official Crowdin project were proofread:
  316 kept, 175 corrected (for example the number suffix «Ar», Indian *arab*, had been rendered
  «Доповнена реальність» — augmented reality), 218 missing ones translated. All 709 are approved
  there, so they also reach the official `uk.po`.
- 16 854 of 18 673 strings (90.3 %); still 0 differences with the official file in shared strings.

## 0.2.0 — 2026-10-15

Ukrainian now ships in Frappe and ERPNext themselves (approved strings from the official Crowdin
project, about 15 % of the interface). This release makes the app a complement to that file
instead of a replacement:

- **Agrees with the official `uk.po`.** 0.1.0 overrode about 2 140 strings that are now proofread
  upstream with older wording; in 0.2.0 every string both catalogues translate is identical
  (0 differences in 2 840 shared strings).
- **New top source: 2 946 strings proofread and approved in the official Crowdin project.**
- **Rebuilt against `version-16-hotfix` `main.pot`** (Frappe v16.52, ERPNext v16.51): 16 145 of
  18 673 strings (86.5 %). Against the current releases 0.1.0 covered 85.2 %; the 99 % it reported
  was measured against September `main.pot`. About 2 500 strings added in 16.35–16.52 are not
  translated yet.
- **Machine share down** from 8 190 strings (50 %) to 6 375 (39.5 %).
- **Terminology aligned with the official project:** `Item` → «Номенклатура» (no more «товар» /
  «предмет»), `Submit` → «Провести», `Valuation Rate` → «Собівартість», `Work Order` →
  «Замовлення на виробництво», and document names `Stock Entry` → «Рух ТМЦ», `Delivery Note` →
  «Видаткова накладна», `Sales Invoice` → «Рахунок-фактура (продаж)», `Material Request` →
  «Заявка на матеріали», `Stock Reconciliation` → «Інвентаризація» and others, including messages
  where they appear in oblique cases.
- Strings that moved between `frappe` and `erpnext` keep their translation.
- `msgfmt --check` clean.

## 0.1.0

First public release. Catalogue built against Frappe 16 / ERPNext 16 `main.pot` from `develop`:
16 304 of 16 469 strings (99.0 %), `msgfmt --check` clean.

Assembled from the community `version-14` corpus and the community Crowdin project, with 847
corrections of demonstrable errors in them (`Job Card` had been «Карта вакансій», `Pick List`
had been the imperative «Виберіть список», `Liability` had been «Відповідальність»), and 8 190
machine-translated strings for text nobody had translated before.
