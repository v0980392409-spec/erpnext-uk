# Ukrainian translation for Frappe and ERPNext

**Український інтерфейс для ERPNext 16.** Ставиться окремим застосунком, ядро не змінює,
оновлення ERPNext його не зачіпає. Покриває 99 % рядків інтерфейсу.

> **Половина каталогу — машинний переклад без вичитки людиною: 8 190 рядків із 16 304.**
> Прочитайте розділ «Quality» нижче, перш ніж ставити на робочу базу.

---

## What this is

A gettext catalogue that gives Frappe and ERPNext a Ukrainian interface. Ukrainian ships with
neither project: there is no `uk.po` in `frappe/locale/` or `erpnext/locale/`, and `uk` is not
one of the 35 target languages of the official Crowdin project, so it cannot be contributed
there either ([frappe/frappe#42525](https://github.com/frappe/frappe/issues/42525) asks for it).

This repository is the workaround: a Frappe app whose only content is `locale/uk.po`. Frappe
merges catalogues across all installed apps, and an app installed after `frappe` and `erpnext`
overrides their strings. Nothing in core is patched, so upgrades do not touch it.

Unofficial community project. Not affiliated with or endorsed by Frappe Technologies.

## Quality — read this before installing

The catalogue is assembled from four sources, and they are not of equal quality:

| Source | Strings | Human-written? |
|---|---:|---|
| Community corpus from `version-14` CSVs | ~5 800 | yes, 8 named translators |
| Community Crowdin project, this author's own work | 2 329 | yes |
| **Machine translation, not proofread** | **8 190** | **no** |
| Corrections applied over the first two | 847 | no (they fix human strings) |
| **Total** | **16 304 of 16 469 (99.0 %)** | |

The machine layer covers the strings nobody had ever translated — mostly validation messages,
error text, field help and rarely-seen screens. It was produced string by string against the
`#.` context comments in `main.pot`, checked for placeholder integrity, and the whole catalogue
passes `msgfmt --check`. It has **not** been read by a human end to end.

What that means in practice: the parts of the UI you see every day are largely human-translated
and were in daily use before this repository existed. The deeper you go into rare error
messages, the more likely you are to meet a machine string. If you find an awkward one, please
report it — see below.

The 165 untranslated strings are deliberate: HTTP verbs, field and queue identifiers, paper
sizes, barcode types, font and product names.

## Install

```bash
cd ~/frappe-bench
bench get-app https://github.com/v0980392409-spec/erpnext-uk
bench --site YOUR-SITE install-app erpnext_uk
bench compile-po-to-mo --app erpnext_uk --locale uk
bench --site YOUR-SITE clear-cache
```

Then set the language: **Settings → System Settings → Language → Ukrainian**. Each user can
override it in their own profile; a user whose language is empty follows System Settings.

**Reload the browser with a hard refresh** (`Ctrl+Shift+R` / `Cmd+Shift+R`). Frappe embeds the
translation dictionary into the page when it is generated, so a tab opened before installation
keeps the old one and looks untranslated.

Built against ERPNext 16 / Frappe 16 (`main.pot` from `develop`). Older versions will work but
strings that no longer exist are simply ignored.

## Found a bad translation?

That is the most useful thing you can contribute — every reported string turns a machine
guess into a checked one.

- **Open an issue** with the English original and what you saw. That is enough.
- **Or open a pull request** against `erpnext_uk/locale/uk.po`.

`uk.po` is generated from source layers, so a PR editing it is merged by hand into those layers
and the file is regenerated. Your change is kept and credited; it just does not survive as a
commit to the `.po` itself.

## Where the translations come from

The base is the community's own work, which had been stranded: Ukrainian existed as `uk.csv`
in both repositories on `version-14`, from before the gettext migration, and in a community
Crowdin project (`crowdin.com/project/erpnext-translations`) that is not connected to the
repositories, so nothing from it ever reached a release.

Translators of that corpus, whose work is the foundation of this catalogue:
**laser**, **dvortsov**, **p.kulinich**, **oa.service.online**, **vsevsimlutsk**, **meghna90**,
**oddooptronix**, and **v0980392409**.

Terminology follows accounting usage rather than literal English: `Trial Balance` →
«Оборотно-сальдова відомість», `Stock Ledger` → «Картка складського обліку», `Party` →
«Контрагент», `Blanket Order` → «Рамкова угода».

## Status upstream

The proper home for this is the official Crowdin project, where the sync bot would carry it into
releases automatically. That needs `uk` to be enabled as a target language first —
[frappe/frappe#42525](https://github.com/frappe/frappe/issues/42525). Until then, this app is
the only way to run ERPNext in Ukrainian. If the language is enabled, this catalogue will be
offered there and this repository becomes a stopgap.

## Maintenance, honestly

This is a by-product of a private project that runs ERPNext in Ukrainian daily. It is updated
when that project updates, which in practice means with new ERPNext releases. Issues and pull
requests are welcome and will be answered, but this is not a funded effort — please read the
Quality section and set your expectations from it.

## License

GPL-3.0-or-later. The catalogue derives from `frappe/erpnext` (GPL-3.0) and `frappe/frappe`
(MIT); the combined work follows the stricter of the two.
