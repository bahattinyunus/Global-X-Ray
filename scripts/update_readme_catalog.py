# -*- coding: utf-8 -*-
"""
scripts/update_readme_catalog.py
Updates root README.md with direct countries/ tree and full 205-country clickable atlas.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "global_datasets" / "countries_registry.json", encoding="utf-8") as f:
    countries = json.load(f)

# Sort alphabetically by Turkish country name
countries_sorted = sorted(countries, key=lambda x: x["name"])

table_lines = [
    "## 🗺️ 205 ÜLKE VE FİİLİ YÖNETİM ATLASI (A-Z DOĞRUDAN ERİŞİM DİZİNİ)\n",
    "> *Aşağıdaki tabloda dünya üzerindeki 205 egemen ve fiili devletin tamamı listelenmiştir. Her ülkenin adına tıklayarak doğrudan o ülkenin bağımsız klasöründeki detaylı 8 bölümlü istihbarat ve derin güç raporuna (`countries/<ülke>/README.md`) ulaşabilirsiniz.*\n",
    "| Ülke | Bayrak / Bölge | ISO Kodu | Başkent | Doğrudan İstihbarat Raporu | Gölge Ekonomi Payı |",
    "| :--- | :--- | :---: | :--- | :--- | :---: |"
]

region_labels = {
    "middle_east": "🕌 Ortadoğu",
    "europe": "🏰 Avrupa",
    "asia": "⛩️ Asya",
    "americas": "🌎 Amerika",
    "africa": "🌍 Afrika",
    "oceania": "🏝️ Okyanusya"
}

for c in countries_sorted:
    reg_label = region_labels.get(c["region"], c["region"])
    link = f"[{c['name']} İstihbarat Dosyası](countries/{c['slug']}/README.md)"
    sh_str = f"%{c.get('shadow_economy_pct', 25.0)}"
    table_lines.append(f"| **{c['name']}** | {reg_label} | `{c['code']}` | {c['capital']} | {link} | {sh_str} |")

country_table_md = "\n".join(table_lines) + "\n\n---\n\n"

with open(BASE_DIR / "README.md", "r", encoding="utf-8") as f:
    content = f.read()

old_tree_start = "## 📂 STANDARTLAŞTIRILMIŞ DEPO DİZİN MİMARİSİ"
new_tree = """## 📂 STANDARTLAŞTIRILMIŞ DEPO DİZİN MİMARİSİ

Proje kapsamında **205 ülke ve fiili yönetimin tamamı**, hem doğrudan alfabetik erişim (`countries/<ülke>/`) hem de bölgesel hiyerarşik yapı (`regions/<bölge>/<ülke>/`) üzerinden bağımsız ve derinlemesine dosya setleriyle inşa edilmiştir:

```text
📦 Global-X-Ray
 ┣ 📂 countries                          # 🌍 205 ÜLKENİN TAMAMI İÇİN AYRI KLASÖR VE README
 ┃ ┣ 📂 turkey
 ┃ ┃ ┣ 📜 README.md                     # 8 Bölümlü Kapsamlı İstihbarat & Güç Raporu
 ┃ ┃ ┣ 📂 01_culture_demographics
 ┃ ┃ ┃ ┣ 📜 society_history.md          # Sosyolojik kırılmalar & fay hatları
 ┃ ┃ ┃ ┗ 📊 demographics.csv           # Nüfus & kentsel veriler (CSV)
 ┃ ┃ ┣ 📂 02_official_state
 ┃ ┃ ┃ ┗ 📜 constitution_gov.md        # Yasal hükümet sistemi & resmi liderler
 ┃ ┃ ┣ 📂 03_official_economy
 ┃ ┃ ┃ ┗ 📊 macroeconomics.json        # Makroekonomik göstergeler (JSON)
 ┃ ┃ ┗ 📂 04_shadow_power_osint
 ┃ ┃   ┣ 📜 real_power_dynamics.md      # Fiili güç odakları & kleptokrasi
 ┃ ┃   ┣ 📊 oligarch_network.csv        # Oligark-siyaset bağlantıları (CSV)
 ┃ ┃   ┗ 📜 media_censorship_matrix.md  # Medya tekelleri & sansür analizi
 ┃ ┣ 📂 germany
 ┃ ┣ 📂 united_states
 ┃ ┣ 📂 china
 ┃ ┣ 📂 russia
 ┃ ┗ 📂 ... (205 Ülke Klasörünün Tamamı)
 ┣ 📂 regions                            # 🗺️ Bölgesel Hiyerarşik Dizin (africa, americas, asia, europe, middle_east, oceania)
 ┣ 📂 global_datasets                    # 📊 205 Ülkenin Küresel İndeksleri
 ┃ ┣ 📊 countries_registry.json           # 205 ülke indeks kataloğu
 ┃ ┣ 📊 global_shadow_economy.csv         # 205 ülke gölge ekonomi endeksi
 ┃ ┗ 📊 press_freedom_real_index.json     # 205 ülke basın özgürlüğü endeksi
 ┣ 📂 scripts
 ┃ ┣ 🐍 build_full_repository.py          # Tüm repo veri ambarını inşa eden motor
 ┃ ┣ 🐍 xray_cli.py                       # Komut satırı analiz terminali
 ┃ ┗ 📂 data                              # 6 Kıtaya ait modüler veri ambarı
 ┣ 📂 methodology
 ┃ ┣ 📜 DATA_COLLECTION_GUIDE.md          # 4 Katmanlı veri toplama kılavuzu
 ┃ ┗ 📜 OSINT_VERIFICATION.md             # Admiralty Code B2+ doğrulama protokolü
 ┣ 📂 templates
 ┃ ┗ 📜 country_template.md               # Ülke şablonu
 ┣ 📜 CONTRIBUTING.md                     # Katkı sağlama yönergeleri
 ┗ 📜 README.md
```

---

""" + country_table_md

idx_start = content.find(old_tree_start)
idx_end = content.find("## 🔍 DOĞRULAMA VE İSTİHBARAT PROTOKOLÜ")
if idx_start != -1 and idx_end != -1:
    content = content[:idx_start] + new_tree + content[idx_end:]
    with open(BASE_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("[+] README.md başarıyla güncellendi (A-Z 205 Ülke Dizini ve countries/ mimarisi eklendi).")
else:
    print("[-] Başlık işaretçileri bulunamadı.")
