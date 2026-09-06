app_name = "erpnext_uk"
app_title = "Ukrainian translation for Frappe and ERPNext"
app_publisher = "Viktor Stephenson"
app_description = "Український переклад інтерфейсу Frappe і ERPNext — каталог gettext"
app_email = "273153052+v0980392409-spec@users.noreply.github.com"
app_license = "gpl-3.0"

# Застосунок не додає жодного доктайпу, хука чи скрипта. Його єдиний вміст —
# erpnext_uk/locale/uk.po. Frappe зливає каталоги всіх ВСТАНОВЛЕНИХ застосунків
# (frappe/translate.py, get_translations_from_apps), і застосунок, встановлений
# після frappe та erpnext, перекриває їхні рядки. Тому окремий застосунок, а не
# правка чужих файлів: оновлення ERPNext його не зачіпає.
