# Ukrainian translation for Frappe and ERPNext

**Український інтерфейс для ERPNext 16.** Ставиться окремим застосунком, ядро не змінює,
оновлення ERPNext його не зачіпає. Доповнює офіційний переклад: офіційний `uk.po` у
Frappe та ERPNext покриває близько 15 % рядків, разом із цим застосунком — 86 %.

> **Частина каталогу — машинний переклад без вичитки людиною: 6 375 рядків із 16 145 (39,5 %).**
> Прочитайте розділ «Quality» нижче, перш ніж ставити на робочу базу.

---

## What this is

A gettext catalogue that gives Frappe and ERPNext a fuller Ukrainian interface.

Since September 2026 Ukrainian is a target language of the official Frappe Crowdin project
([frappe/frappe#42525](https://github.com/frappe/frappe/issues/42525)), and the sync bot ships
`uk.po` in both `frappe` and `erpnext` (it is in the version-16 releases from mid-October 2026,
frappe v16.52.0 and erpnext v16.51.1). Crowdin exports **only approved strings**, so the official
file currently covers about 15 % of the interface (2 879 of 18 600 strings); the rest shows in English.

This app fills the gap. It is a Frappe app whose only content is `locale/uk.po`. Frappe merges
catalogues across all installed apps, and an app installed after `frappe` and `erpnext`
overrides their strings. Nothing in core is patched, so upgrades do not touch it.

**It agrees with the official translation.** Every string that both catalogues translate has the
same text here as in the official `uk.po` (checked for this release: 0 differences in 2 840 shared
strings), so installing the app never replaces proofread official text with another variant.
Version 0.1.0 predates the official file and did override about 2 140 of those strings with older
wording — upgrade to 0.2.0.

Unofficial community project. Not affiliated with or endorsed by Frappe Technologies.

## Quality — read this before installing

The catalogue is assembled from five sources, and they are not of equal quality:

| Source | Strings | Human-written? |
|---|---:|---|
| Official Crowdin project, proofread and approved by this author | 2 946 | yes |
| Community corpus from `version-14` CSVs | 4 111 | yes, 8 named translators |
| Community Crowdin project, this author's own work | 2 025 | yes |
| Corrections applied over the human sources | 688 | no (they fix human strings) |
| **Machine translation, not proofread** | **6 375** | **no** |
| **Total** | **16 145 of 18 673 (86.5 %)** | |

The machine layer covers strings nobody had translated — mostly validation messages, error text,
field help and rarely-seen screens. It was produced string by string against the `#.` context
comments in `main.pot`, checked for placeholder integrity, and the whole catalogue passes
`msgfmt --check`. It has **not** been read by a human end to end.

What that means in practice: the parts of the UI you see every day are largely human-translated,
and the most visible ones are proofread in the official project. The deeper you go into rare error
messages, the more likely you are to meet a machine string.

About 2 500 strings are not translated at all. Most of them appeared in Frappe and ERPNext
16.35–16.52 and have not reached any source yet; they show in English unless the official file
has them. A few are deliberate: HTTP verbs, field and queue identifiers, paper sizes, barcode
types, font and product names.

## Install

```bash
cd ~/frappe-bench
bench get-app https://github.com/v0980392409-spec/erpnext-uk
bench --site YOUR-SITE install-app erpnext_uk
bench compile-po-to-mo --app erpnext_uk --locale uk
bench --site YOUR-SITE clear-cache
```

Upgrading from 0.1.0: `bench update --apps erpnext_uk` or `git pull` in `apps/erpnext_uk`,
then the last two commands above.

Then set the language: **Settings → System Settings → Language → Ukrainian**. Each user can
override it in their own profile; a user whose language is empty follows System Settings.

**Reload the browser with a hard refresh** (`Ctrl+Shift+R` / `Cmd+Shift+R`). Frappe embeds the
translation dictionary into the page when it is generated, so a tab opened before installation
keeps the old one and looks untranslated.

Built against Frappe 16 / ERPNext 16, `main.pot` from the `version-16-hotfix` branches (October
2026). Older 16.x versions work too; strings that do not exist there are simply ignored.

## Found a bad translation?

That is the most useful thing you can contribute — every reported string turns a machine
guess into a checked one.

- **Best: fix it in the official Crowdin project** ([crowdin.com/project/frappe](https://crowdin.com/project/frappe),
  language Ukrainian). Once approved there it reaches Frappe/ERPNext releases and this catalogue.
- **Or open an issue** here with the English original and what you saw. That is enough.
- **Or open a pull request** against `erpnext_uk/locale/uk.po`.

`uk.po` is generated from source layers, so a PR editing it is merged by hand into those layers
and the file is regenerated. Your change is kept and credited; it just does not survive as a
commit to the `.po` itself.

## Where the translations come from

The base is the community's own work, which had been stranded: Ukrainian existed as `uk.csv`
in both repositories on `version-14`, from before the gettext migration, and in a community
Crowdin project (`crowdin.com/project/erpnext-translations`) that was never connected to the
repositories. Since September 2026 the most visible strings are also proofread in the official
Crowdin project, and that work is taken back here with priority over everything else.

Translators of the version-14 corpus, whose work is the foundation of this catalogue:
**laser**, **dvortsov**, **p.kulinich**, **oa.service.online**, **vsevsimlutsk**, **meghna90**,
**oddooptronix**, and **v0980392409**.

Terminology follows Ukrainian accounting usage rather than literal English, and the same terms are
used in the official Crowdin project: `Item` → «Номенклатура», `Party` → «Контрагент», `Submit` →
«Провести», `Stock Entry` → «Рух ТМЦ», `Delivery Note` → «Видаткова накладна», `Valuation Rate` →
«Собівартість», `Trial Balance` → «Оборотно-сальдова відомість», `Stock Ledger` → «Картка
складського обліку», `Blanket Order` → «Рамкове замовлення».

## Status upstream

The proper home for this work is the official Crowdin project, and that is where proofreading now
happens. As more strings are approved there, the official `uk.po` grows and this app matters less;
it stays useful for as long as a large part of the interface is not yet approved upstream.

## Maintenance, honestly

This is a by-product of a private project that runs ERPNext in Ukrainian daily. The catalogue is
rebuilt after proofreading batches in the official project, so that it keeps agreeing with the
official file, and against new ERPNext releases. Issues and pull requests are welcome and will be
answered, but this is not a funded effort — please read the Quality section and set your
expectations from it.

## License

GPL-3.0-or-later. The catalogue derives from `frappe/erpnext` (GPL-3.0) and `frappe/frappe`
(MIT); the combined work follows the stricter of the two.
