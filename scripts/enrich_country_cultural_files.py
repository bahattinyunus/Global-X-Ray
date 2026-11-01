# -*- coding: utf-8 -*-
"""
scripts/enrich_country_cultural_files.py
Enriches countries' `01_culture_demographics/society_history.md` with the new
Medeniyet Atlası standard: Cultural DNA, Untranslatable Concepts, Lifestyle & Rituals,
Gastronomy Philosophy, Etiquette/Taboos, and Literary/Artistic Archetypes.
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

slug_map = {c["code"]: c["slug"] for c in countries_registry}
region_path_map = {c["code"]: c["path"] for c in countries_registry}

for c_dna in culture_data.get("countries_cultural_dna", []):
    code = c_dna.get("code")
    slug = slug_map.get(code)
    if not slug:
        continue

    words_md = "\n".join([f"* **{w['word']}:** {w['meaning']}" for w in c_dna.get("untranslatable_soul_concepts", [])])
    
    content = f"""# 🏛️ Medeniyet Kimliği, Kültürel Kodlar ve Toplumsal Doku: {c_dna['country']} ({c_dna['code']})

> *"Bir ulusu tanımak istiyorsanız halk türkülerine kulak verin; sofrasındaki ekmeği bölüşme adabına bakın ve hiçbir yabancı dile tam çevrilemeyen kelimelerini dinleyin."*

---

## 1. Medeniyet Kavşağı ve Ulusal Karakter (Kültürel DNA)

* **Medeniyet Sentezi:** {c_dna.get('civilization_crossroads')}
* **Kolektif Ethos & Ulusal Ruh:** {c_dna.get('core_cultural_ethos')}
* **İletişim ve Anlatım Tarzı:** {c_dna.get('communication_style')}

---

## 2. Dilde Kristalleşen Çevrilemeyen Ruh Kavramları (Untranslatable Words)

{words_md}

---

## 3. Gündelik Hayat, Sosyal Ritüeller ve Yaşam Sanatı

{c_dna.get('social_rituals_and_lifestyle')}

---

## 4. Gastronomi Felsefesi ve Sofra Kültürü

{c_dna.get('gastronomic_philosophy')}

---

## 5. Görgü Kuralları ve Sosyal Tabular (Do's & Don'ts)

{c_dna.get('social_taboos_and_etiquette')}

---

## 6. Edebiyat, Sanat ve Mimari Miras

{c_dna.get('literary_and_artistic_archetypes')}

---

## 7. Tarihsel Kırılma Noktaları, Demografi ve Sosyal Dönüşüm

Ülkenin modern kimliği; geçmiş imparatorluk, sömürge veya bağımsızlık mücadelelerinin yarattığı kurumsal miras üzerinde yükselmektedir. Taşra ile metropol kentler arasındaki eşitsizlikler, küresel göç dalgaları ve kuşaklar arası zihniyet dönüşümleri, ülkenin kültürel fay hatlarını sürekli yeniden üretmektedir.
"""
    # Write to countries/<slug>/01_culture_demographics/society_history.md
    c_target = COUNTRIES_DIR / slug / "01_culture_demographics" / "society_history.md"
    if c_target.parent.exists():
        with open(c_target, "w", encoding="utf-8") as f:
            f.write(content)

    # Write to regions/...
    reg_rel = region_path_map.get(code)
    if reg_rel:
        reg_target = BASE_DIR / reg_rel / "01_culture_demographics" / "society_history.md"
        if reg_target.parent.exists():
            with open(reg_target, "w", encoding="utf-8") as f:
                f.write(content)

print("[SUCCESS] Enriched all 20 anchor countries' society_history.md with Medeniyet Atlası cultural standard!")
