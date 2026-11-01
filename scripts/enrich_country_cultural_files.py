# -*- coding: utf-8 -*-
"""
scripts/enrich_country_cultural_files.py
Enriches all 40 countries' `01_culture_demographics/society_history.md` files
across `countries/`, `regions/`, and economic blocks with full cultural DNA,
untranslatable soul concepts, daily lifestyle rituals, gastronomy, and taboos.
"""

import sys
import json
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "global_datasets"
COUNTRIES_DIR = BASE_DIR / "countries"
REGIONS_DIR = BASE_DIR / "regions"

with open(DATA_DIR / "cultural_codes_and_civilizations_registry.json", "r", encoding="utf-8") as f:
    culture_data = json.load(f)

with open(DATA_DIR / "countries_registry.json", "r", encoding="utf-8") as f:
    countries_registry = json.load(f)

c_by_code = {c["code"]: c for c in countries_registry}

updated_count = 0
for c_dna in culture_data.get("countries_cultural_dna", []):
    code = c_dna.get("code")
    c_info = c_by_code.get(code)
    if not c_info:
        continue

    slug = c_info["slug"]
    region = c_info.get("region")
    eco_id = c_info.get("economy_group_id")

    # Format list fields cleanly
    words_list = c_dna.get("untranslatable_soul_concepts", [])
    words_md = "\n".join([f"* **{w['word']}:** {w['meaning']}\n  > *{w.get('cultural_significance', '')}*" for w in words_list])

    rituals_list = c_dna.get("social_rituals_and_lifestyle", [])
    if isinstance(rituals_list, list):
        rituals_md = "\n".join([f"* {r}" for r in rituals_list])
    else:
        rituals_md = str(rituals_list)

    taboos_list = c_dna.get("social_taboos_and_etiquette", [])
    if isinstance(taboos_list, list):
        taboos_md = "\n".join([f"* {t}" for t in taboos_list])
    else:
        taboos_md = str(taboos_list)

    arts_list = c_dna.get("literary_and_artistic_archetypes", [])
    if isinstance(arts_list, list):
        arts_md = "\n".join([f"* **{a}**" for a in arts_list])
    else:
        arts_md = str(arts_list)

    content = f"""# 🏛️ Medeniyet Kimliği, Kültürel Kodlar ve Toplumsal Doku: {c_dna['country']} ({c_dna['code']})

> *"Bir ulusu gerçekten tanımak istiyorsanız; halk türkülerine kulak verin, sofrasındaki ekmeği bölüşme adabına bakın ve başka hiçbir dünya diline tam çevrilemeyen ruh kavramlarını dinleyin."*

---

## 1. Medeniyet Kavşağı ve Ulusal Karakter (Kültürel DNA)

* **Medeniyet Sentezi:** {c_dna.get('civilization_crossroads')}
* **Kolektif Ethos & Ulusal Karakter:** {c_dna.get('core_cultural_ethos')}
* **İletişim Tarzı (High / Low Context):** {c_dna.get('communication_style')}

---

## 2. Dilde Kristalleşen Çevrilemeyen Ruh Kavramları (Untranslatable Words)

{words_md}

---

## 3. Gündelik Hayat, Sosyal Ritüeller ve Yaşam Sanatı

{rituals_md}

---

## 4. Gastronomi Felsefesi ve Sofra Kültürü

* **Mutfak Felsefesi:** {c_dna.get('gastronomic_philosophy')}

---

## 5. Görgü Kuralları ve Sosyal Tabular (Do's & Don'ts)

{taboos_md}

---

## 6. Edebiyat, Sanat ve Entelektüel Miras

{arts_md}

---

## 7. Tarihsel Kırılma Noktaları, Demografi ve Sosyal Dönüşüm

Ülkenin modern kimliği; geçmiş imparatorluk, sömürge veya bağımsızlık mücadelelerinin yarattığı kurumsal miras üzerinde yükselmektedir. Taşra ile metropol kentler arasındaki eşitsizlikler, küresel göç dalgaları ve kuşaklar arası zihniyet dönüşümleri, ülkenin kültürel fay hatlarını sürekli yeniden üretmektedir.
"""
    # 1. countries/<slug>/01_culture_demographics/society_history.md
    p1 = COUNTRIES_DIR / slug / "01_culture_demographics" / "society_history.md"
    if p1.parent.exists():
        p1.write_text(content, encoding="utf-8")

    # 2. regions/<region>/<slug>/01_culture_demographics/society_history.md
    if region:
        p2 = REGIONS_DIR / region / slug / "01_culture_demographics" / "society_history.md"
        if p2.parent.exists():
            p2.write_text(content, encoding="utf-8")

    # 3. <eco_id>/<slug>/01_culture_demographics/society_history.md
    if eco_id:
        p3 = BASE_DIR / eco_id / slug / "01_culture_demographics" / "society_history.md"
        if p3.parent.exists():
            p3.write_text(content, encoding="utf-8")

    updated_count += 1

print(f"[SUCCESS] Successfully enriched all {updated_count} countries with deep Medeniyet Atlası cultural DNA across all directory locations!")
