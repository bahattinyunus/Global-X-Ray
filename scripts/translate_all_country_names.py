# -*- coding: utf-8 -*-
"""
scripts/translate_all_country_names.py
Ensures country names are 100% Turkish across all datasets, country files,
geopolitics & intelligence dossiers, and culture dossiers.
"""

import os
import sys
import json
import re
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "global_datasets"

COUNTRY_TRANSLATIONS = {
    "United States": "Amerika Birleşik Devletleri",
    "United States of America": "Amerika Birleşik Devletleri",
    "USA": "ABD",
    "Russia": "Rusya",
    "China": "Çin",
    "United Kingdom": "Birleşik Krallık",
    "UK": "Birleşik Krallık",
    "France": "Fransa",
    "Germany": "Almanya",
    "Turkey": "Türkiye",
    "Turkiye": "Türkiye",
    "Japan": "Japonya",
    "India": "Hindistan",
    "Italy": "İtalya",
    "Spain": "İspanya",
    "South Korea": "Güney Kore",
    "North Korea": "Kuzey Kore",
    "Brazil": "Brezilya",
    "Canada": "Kanada",
    "Australia": "Avustralya",
    "New Zealand": "Yeni Zelanda",
    "Egypt": "Mısır",
    "Greece": "Yunanistan",
    "Saudi Arabia": "Suudi Arabistan",
    "Iran": "İran",
    "Iraq": "Irak",
    "Syria": "Suriye",
    "Israel": "İsrail",
    "Palestine": "Filistin",
    "United Arab Emirates": "Birleşik Arap Emirlikleri",
    "UAE": "BAE",
    "Qatar": "Katar",
    "Kuwait": "Kuveyt",
    "Oman": "Umman",
    "Bahrain": "Bahreyn",
    "Yemen": "Yemen",
    "Jordan": "Ürdün",
    "Lebanon": "Lübnan",
    "Cyprus": "Kıbrıs",
    "Northern Cyprus": "Kuzey Kıbrıs",
    "Sweden": "İsveç",
    "Norway": "Norveç",
    "Denmark": "Danimarka",
    "Finland": "Finlandiya",
    "Switzerland": "İsviçre",
    "Austria": "Avusturya",
    "Netherlands": "Hollanda",
    "Belgium": "Belçika",
    "Poland": "Polonya",
    "Ukraine": "Ukrayna",
    "Belarus": "Belarus",
    "Serbia": "Sırbistan",
    "Bulgaria": "Bulgaristan",
    "Romania": "Romanya",
    "Hungary": "Macaristan",
    "Czech Republic": "Çekya",
    "Czechia": "Çekya",
    "Slovakia": "Slovakya",
    "Slovenia": "Slovenya",
    "Croatia": "Hırvatistan",
    "Bosnia and Herzegovina": "Bosna-Hersek",
    "Albania": "Arnavutluk",
    "North Macedonia": "Kuzey Makedonya",
    "Montenegro": "Karadağ",
    "Kosovo": "Kosova",
    "Portugal": "Portekiz",
    "Ireland": "İrlanda",
    "Iceland": "İzlanda",
    "Estonia": "Estonya",
    "Latvia": "Letonya",
    "Lithuania": "Litvanya",
    "Moldova": "Moldova",
    "Georgia": "Gürcistan",
    "Armenia": "Ermenistan",
    "Azerbaijan": "Azerbaycan",
    "Kazakhstan": "Kazakistan",
    "Uzbekistan": "Özbekistan",
    "Turkmenistan": "Türkmenistan",
    "Kyrgyzstan": "Kırgızistan",
    "Tajikistan": "Tacikistan",
    "Pakistan": "Pakistan",
    "Afghanistan": "Afganistan",
    "Bangladesh": "Bangladeş",
    "Sri Lanka": "Sri Lanka",
    "Nepal": "Nepal",
    "Bhutan": "Butan",
    "Myanmar": "Myanmar",
    "Thailand": "Tayland",
    "Vietnam": "Vietnam",
    "Indonesia": "Endonezya",
    "Malaysia": "Malezya",
    "Singapore": "Singapur",
    "Philippines": "Filipinler",
    "Taiwan": "Tayvan",
    "Hong Kong": "Hong Kong",
    "Macau": "Makao",
    "Mongolia": "Moğolistan",
    "South Africa": "Güney Afrika",
    "Nigeria": "Nijerya",
    "Kenya": "Kenya",
    "Ethiopia": "Etiyopya",
    "Ghana": "Gana",
    "Senegal": "Senegal",
    "Morocco": "Fas",
    "Algeria": "Cezayir",
    "Tunisia": "Tunus",
    "Libya": "Libya",
    "Sudan": "Sudan",
    "South Sudan": "Güney Sudan",
    "Somalia": "Somali",
    "Djibouti": "Cibuti",
    "Eritrea": "Eritre",
    "DR Congo": "Demokratik Kongo Cumhuriyeti",
    "Democratic Republic of the Congo": "Demokratik Kongo Cumhuriyeti",
    "Republic of the Congo": "Kongo Cumhuriyeti",
    "Congo": "Kongo",
    "Angola": "Angola",
    "Mozambique": "Mozambik",
    "Madagascar": "Madagaskar",
    "Tanzania": "Tanzanya",
    "Uganda": "Uganda",
    "Rwanda": "Ruanda",
    "Zambia": "Zambiya",
    "Zimbabwe": "Zimbabve",
    "Botswana": "Botsvana",
    "Namibia": "Namibya",
    "Cameroon": "Kamerun",
    "Gabon": "Gabon",
    "Chad": "Çad",
    "Niger": "Nijer",
    "Mali": "Mali",
    "Burkina Faso": "Burkina Faso",
    "Guinea": "Gine",
    "Ivory Coast": "Fildişi Sahili",
    "Cote d'Ivoire": "Fildişi Sahili",
    "Mauritania": "Moritanya",
    "Mexico": "Meksika",
    "Argentina": "Arjantin",
    "Colombia": "Kolombiya",
    "Chile": "Şili",
    "Peru": "Peru",
    "Venezuela": "Venezuela",
    "Ecuador": "Ekvador",
    "Bolivia": "Bolivya",
    "Paraguay": "Paraguay",
    "Uruguay": "Uruguay",
    "Cuba": "Küba",
    "Dominican Republic": "Dominik Cumhuriyeti",
    "Panama": "Panama",
    "Costa Rica": "Kosta Rika",
    "Guatemala": "Guatemala",
    "Honduras": "Honduras",
    "El Salvador": "El Salvador",
    "Nicaragua": "Nikaragua",
    "Haiti": "Haiti",
    "Jamaica": "Jamaika",
    "Bahamas": "Bahamalar",
    "Barbados": "Barbados",
    "Trinidad and Tobago": "Trinidad ve Tobago",
    "Guyana": "Guyana",
    "Suriname": "Surinam",
    "Papua New Guinea": "Papua Yeni Gine",
    "Fiji": "Fiji",
    "Solomon Islands": "Solomon Adaları",
    "Vanuatu": "Vanuatu",
    "Samoa": "Samoa",
    "Micronesia": "Mikronezya",
    "Cook Islands": "Cook Adaları",
    "Marshall Islands": "Marshall Adaları",
    "Palau": "Palau",
    "British Indian Ocean Territory (BIOT)": "Britanya Hint Okyanusu Toprakları (Diego Garcia)",
    "Panama & Liberia (Historical Flags)": "Panama & Liberya (Tarihsel Bayraklar)"
}

def tr(name):
    return COUNTRY_TRANSLATIONS.get(name, name)

def update_json_file(file_path, updater):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    updater(data)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {file_path.name}")

def main():
    # 1. nuclear_arsenals_and_triad_registry.json
    def update_nuclear(d):
        for p in d.get("nuclear_powers", []):
            p["country"] = tr(p["country"])
        sharing = d.get("nato_nuclear_sharing", {})
        if "host_countries" in sharing:
            sharing["host_countries"] = [tr(c) for c in sharing["host_countries"]]
    update_json_file(DATASETS_DIR / "nuclear_arsenals_and_triad_registry.json", update_nuclear)

    # 2. global_arms_trade_and_contractors.json
    def update_arms(d):
        for c in d.get("top_prime_contractors", []):
            c["country"] = tr(c["country"])
        exp_imp = d.get("top_exporters_vs_importers", {})
        for ex in exp_imp.get("exporters", []):
            ex["country"] = tr(ex["country"])
        for im in exp_imp.get("importers", []):
            im["country"] = tr(im["country"])
    update_json_file(DATASETS_DIR / "global_arms_trade_and_contractors.json", update_arms)

    # 3. sanctions_and_embargoes_registry.json
    def update_sanctions(d):
        for s in d.get("targeted_states", []):
            s["country"] = tr(s["country"])
            s["primary_sanctioners"] = [
                x.replace("USA", "ABD").replace("EU", "AB").replace("GBR", "Birleşik Krallık")
                 .replace("JPN", "Japonya").replace("CAN", "Kanada").replace("AUS", "Avustralya")
                 .replace("CHE", "İsviçre").replace("UN", "BM")
                for x in s.get("primary_sanctioners", [])
            ]
    update_json_file(DATASETS_DIR / "sanctions_and_embargoes_registry.json", update_sanctions)

    # 4. critical_raw_materials_supply_chain.json
    def update_minerals(d):
        for m in d.get("minerals", []):
            for mn in m.get("top_mining_nations", []):
                mn["country"] = tr(mn["country"])
            ref = m.get("refining_monopoly", {})
            if "dominant_nation" in ref:
                dom = ref["dominant_nation"]
                for eng, turk in COUNTRY_TRANSLATIONS.items():
                    dom = dom.replace(eng, turk)
                ref["dominant_nation"] = dom
    update_json_file(DATASETS_DIR / "critical_raw_materials_supply_chain.json", update_minerals)

    # 5. subsea_cables_and_sigint_stations.json
    def update_cables(d):
        for s in d.get("global_sigint_interception_stations", []):
            s["country"] = tr(s["country"])
    update_json_file(DATASETS_DIR / "subsea_cables_and_sigint_stations.json", update_cables)

    # 6. sovereign_wealth_funds_registry.json
    def update_swf(d):
        for f in d.get("funds", []):
            f["country"] = tr(f["country"])
    update_json_file(DATASETS_DIR / "sovereign_wealth_funds_registry.json", update_swf)

    # 7. shadow_fleet_maritime_registry.json
    def update_shadow_fleet(d):
        for fl in d.get("flags_of_convenience", []):
            fl["flag_state"] = tr(fl["flag_state"])
    update_json_file(DATASETS_DIR / "shadow_fleet_maritime_registry.json", update_shadow_fleet)

    # 8. intelligence_agencies_registry.json
    def update_intel(d):
        for a in d.get("agencies", []):
            a["country"] = tr(a["country"])
    update_json_file(DATASETS_DIR / "intelligence_agencies_registry.json", update_intel)

    # 9. cultural_codes_and_civilizations_registry.json
    def update_culture(d):
        for r in d.get("civilization_realms", []):
            if "representative_states" in r:
                r["representative_states"] = [tr(c) for c in r["representative_states"]]
    update_json_file(DATASETS_DIR / "cultural_codes_and_civilizations_registry.json", update_culture)

    # 10. Update all 205 country README.md files in countries/, regions/, and economic blocks
    region_map = {
        "Middle East": "Orta Doğu",
        "Europe": "Avrupa",
        "Asia": "Asya & Hint-Pasifik",
        "Americas": "Amerika Kıtası",
        "Africa": "Afrika",
        "Oceania": "Okyanusya"
    }

    country_count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        if "README.md" in files:
            p = Path(root) / "README.md"
            # Sadece ülke klasörleri içindeki README'leri hedefle
            # (içinde 'Coğrafi Bölge' veya 'Bölge: ' olan dosyalar)
            try:
                content = p.read_text(encoding="utf-8")
                modified = False
                for eng_reg, tr_reg in region_map.items():
                    target1 = f"Bölge: {eng_reg}"
                    rep1 = f"Bölge: {tr_reg}"
                    if target1 in content:
                        content = content.replace(target1, rep1)
                        modified = True

                    target2 = f"| **Coğrafi Bölge** | {eng_reg} |"
                    rep2 = f"| **Coğrafi Bölge** | {tr_reg} |"
                    if target2 in content:
                        content = content.replace(target2, rep2)
                        modified = True

                if modified:
                    p.write_text(content, encoding="utf-8")
                    country_count += 1
            except Exception as e:
                pass

    print(f"Updated {country_count} country README files with Turkish region names.")

if __name__ == "__main__":
    main()
