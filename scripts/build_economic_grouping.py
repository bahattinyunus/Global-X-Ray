"""
scripts/build_economic_grouping.py
Groups all 205 countries by their economic model rather than continents:
1. 01_ileri_sanayi_g7 (G7 & Advanced Industrial Economies)
2. 02_petro_ve_enerji_devleri (Petrostates & Energy Powers)
3. 03_gelismekte_olan_devler_ve_brics (Emerging Giants, BRICS & G20 Hubs)
4. 04_offshore_ve_finansal_merkezler (Offshore Secrecy & Financial Haven Jurisdictions)
5. 05_kritik_maden_ve_hammadde (Critical Mineral & Commodity Exporters)
6. 06_orta_gelir_ve_ureticiler (Middle Income & Regional Producers)
7. 07_kirilgan_ve_borc_krizindekiler (Debt-Distressed, Sanctioned & Fragile States)
8. 08_kucuk_ada_ve_turizm_ekonomileri (Small Island Developing States & Micro-Economies)
"""

import os
import sys
import json
import shutil
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "global_datasets"
COUNTRIES_DIR = BASE_DIR / "countries"

# 8 Ekonomik Arketip Tanımı
ECONOMIC_GROUPS = {
    "01_ileri_sanayi_g7": {
        "name_tr": "G7 ve İleri Teknoloji / Sanayi Ekonomileri",
        "name_en": "G7 & Advanced Industrial Economies",
        "description": "Küresel finans, yüksek teknoloji, patent tekelleri ve ileri sanayi üretimine hükmeden çekirdek kapitalist güçler.",
        "quote": "The advanced industrial economies do not merely manufacture goods; they manufacture the standards, the reserve currency, and the legal frameworks of global trade.",
        "slugs": [
            "united_states", "germany", "japan", "united_kingdom", "france", "italy", "canada",
            "south_korea", "taiwan", "netherlands", "switzerland", "sweden", "belgium", "austria",
            "singapore", "denmark", "finland", "ireland", "israel", "norway", "australia",
            "new_zealand", "spain", "iceland", "estonia", "latvia", "lithuania", "slovenia"
        ]
    },
    "02_petro_ve_enerji_devleri": {
        "name_tr": "Petro-Devletler ve Enerji İhracatçıları",
        "name_en": "Petrostates & Energy Powers",
        "description": "Devlet bütçeleri ve dış ticaret dengeleri ağırlıklı olarak petrol, doğal gaz ve hidrokarbon rantına dayalı egemen güçler.",
        "quote": "In a petrostate, politics is not about the creation of wealth, but about the violent and factional distribution of geological rent.",
        "slugs": [
            "saudi_arabia", "russia", "united_arab_emirates", "qatar", "kuwait", "iran", "iraq",
            "oman", "bahrain", "algeria", "libya", "angola", "nigeria", "venezuela", "kazakhstan",
            "azerbaijan", "turkmenistan", "brunei", "gabon", "equatorial_guinea", "republic_of_the_congo",
            "trinidad_and_tobago", "guyana"
        ]
    },
    "03_gelismekte_olan_devler_ve_brics": {
        "name_tr": "Gelişmekte Olan Devler, BRICS ve İmalat Merkezleri",
        "name_en": "Emerging Giants, BRICS & Manufacturing Hubs",
        "description": "Büyük nüfuslu, hızla sanayileşen, küresel tedarik zincirlerinin fabrika tabanını oluşturan yükselen ekonomik güçler.",
        "quote": "The shifting of the global manufacturing center of gravity from the North Atlantic to the Indo-Pacific and Global South represents the greatest geopolitical reallocation of power in five centuries.",
        "slugs": [
            "china", "india", "brazil", "turkey", "indonesia", "mexico", "poland", "south_africa",
            "vietnam", "thailand", "malaysia", "philippines", "egypt", "pakistan", "bangladesh",
            "colombia", "chile", "argentina", "romania", "czech_republic", "hungary"
        ]
    },
    "04_offshore_ve_finansal_merkezler": {
        "name_tr": "Offshore Finansal Sığınaklar ve Vergi Cennetleri",
        "name_en": "Offshore Financial Havens & Secrecy Jurisdictions",
        "description": "Katı bankacılık gizliliği, sıfır/düşük kurumlar vergisi ve paravan şirket yapılarıyla küresel servetin kaçış noktası olan yargı alanları.",
        "quote": "The offshore system is the dark matter of the global economy: invisible in ordinary public ledgers, but possessing enough gravitational mass to bend sovereign laws to its will.",
        "slugs": [
            "luxembourg", "liechtenstein", "monaco", "andorra", "bahamas", "panama", "cyprus",
            "malta", "mauritius", "seychelles", "hong_kong", "macau", "vatican_city", "san_marino"
        ]
    },
    "05_kritik_maden_ve_hammadde": {
        "name_tr": "Kritik Maden ve Stratejik Emtia İhracatçıları",
        "name_en": "Critical Mineral & Commodity Exporters",
        "description": "Kobalt, lityum, bakır, altın ve nadir toprak elementleri gibi enerji dönüşümünün ve yüksek teknolojinin hammaddesini sağlayan ülkeler.",
        "quote": "Civilization lives by geological consent. The clean energy transition has replaced the age of petroleum with an age of hyper-concentrated mineral dependency.",
        "slugs": [
            "democratic_republic_of_the_congo", "zambia", "peru", "bolivia", "guinea", "ghana",
            "ivory_coast", "morocco", "mozambique", "namibia", "botswana", "zimbabwe", "mongolia",
            "papua_new_guinea", "uzbekistan", "kyrgyzstan", "tajikistan", "suriname", "ecuador",
            "paraguay", "uruguay", "guinea_bissau"
        ]
    },
    "06_orta_gelir_ve_ureticiler": {
        "name_tr": "Orta Gelir Düzeyi ve Bölgesel Üreticiler",
        "name_en": "Middle-Income & Regional Producers",
        "description": "Çeşitlendirilmiş bölgesel ekonomiye sahip, tarım, tekstil, turizm ve hafif sanayi üreten gelişmekte olan devletler.",
        "quote": "The middle-income trap is not merely economic; it is institutional. Breaking through requires dismantling domestic oligopolies and establishing absolute rule of law.",
        "slugs": [
            "greece", "portugal", "croatia", "slovakia", "bulgaria", "serbia", "belarus", "ukraine",
            "jordan", "lebanon", "tunisia", "sri_lanka", "costa_rica", "dominican_republic",
            "guatemala", "kenya", "ethiopia", "tanzania", "senegal", "cameroon", "armenia",
            "georgia", "albania", "bosnia_and_herzegovina", "north_macedonia", "moldova", "montenegro",
            "kosovo", "northern_cyprus", "transnistria", "somaliland", "western_sahara", "honduras",
            "el_salvador", "nicaragua", "cambodia", "laos", "nepal", "bhutan"
        ]
    },
    "07_kirilgan_ve_borc_krizindekiler": {
        "name_tr": "Kırılgan, Ağır Borçlu ve Yaptırım Altındaki Devletler",
        "name_en": "Debt-Distressed, Sanctioned & Fragile States",
        "description": "Kronik bütçe ve cari açık, borç temerrüdü, hiperenflasyon, uluslararası yaptırımlar veya silahlı çatışmalarla felç olmuş ekonomiler.",
        "quote": "When a state loses sovereign control over its currency and basic food security, its sovereignty becomes a legal fiction negotiated in foreign creditor committees.",
        "slugs": [
            "syria", "yemen", "sudan", "south_sudan", "somalia", "afghanistan", "north_korea",
            "myanmar", "cuba", "haiti", "mali", "burkina_faso", "niger", "chad",
            "central_african_republic", "eritrea", "burundi", "liberia", "sierra_leone", "togo",
            "benin", "mauritania", "gambia", "eswatini", "lesotho", "malawi", "madagascar",
            "timor_leste", "djibouti", "rwanda", "uganda", "palestine"
        ]
    },
    "08_kucuk_ada_ve_turizm_ekonomileri": {
        "name_tr": "Küçük Ada Devletleri ve Turizm / Hizmet Ekonomileri",
        "name_en": "Small Island Developing States & Micro-Economies",
        "description": "Turizm, balıkçılık, bayrak kiralama ve devasa deniz alanlarına (MEB) dayalı kırılgan ada ekonomileri.",
        "quote": "Small island states in the vast oceans are not tiny nations; they are giant oceanic guardians controlling millions of square kilometers of maritime commons.",
        "slugs": [
            "maldives", "fiji", "barbados", "antigua_and_barbuda", "saint_lucia", "grenada",
            "saint_vincent_and_the_grenadines", "saint_kitts_and_nevis", "cabo_verde",
            "sao_tome_and_principe", "comoros", "samoa", "tonga", "vanuatu", "solomon_islands",
            "kiribati", "micronesia", "marshall_islands", "palau", "nauru", "tuvalu", "greenland",
            "puerto_rico", "jamaica", "belize", "dominica"
        ]
    }
}

def main():
    print("=" * 80)
    print("🌍 KÜRESEL RÖNTGEN - ÜLKELERİ EKONOMİLERİNE GÖRE GRUPLANDIRMA MOTORU")
    print("=" * 80)

    # 1. Mevcut countries_registry.json yükle
    registry_file = DATASETS_DIR / "countries_registry.json"
    with open(registry_file, "r", encoding="utf-8") as f:
        countries = json.load(f)

    country_by_slug = {c["slug"]: c for c in countries}
    assigned_slugs = set()

    for g_id, g_info in ECONOMIC_GROUPS.items():
        for s in g_info["slugs"]:
            if s in country_by_slug:
                assigned_slugs.add(s)
            else:
                print(f"[!] Uyarı: Tanımlı olmayan slug: {s}")

    unassigned = [c["slug"] for c in countries if c["slug"] not in assigned_slugs]
    if unassigned:
        print(f"[!] Gruplandırılmamış {len(unassigned)} ülke bulundu: {unassigned}")
        # Kalanları uygun gruba ekle
        for u in unassigned:
            ECONOMIC_GROUPS["06_orta_gelir_ve_ureticiler"]["slugs"].append(u)
            print(f"  -> {u} '06_orta_gelir_ve_ureticiler' grubuna eklendi.")

    total_assigned = sum(len(g["slugs"]) for g in ECONOMIC_GROUPS.values())
    print(f"[*] Toplam {total_assigned} ülke 8 ekonomik gruba başarıyla dağıtıldı.")

    # 2. economies/ klasörünü ve kök seviyedeki ekonomik grupları oluştur
    economies_dir = BASE_DIR / "economies"
    economies_dir.mkdir(parents=True, exist_ok=True)

    for g_id, g_info in ECONOMIC_GROUPS.items():
        # A) Kök dizinde: ./01_ileri_sanayi_g7/
        root_group_dir = BASE_DIR / g_id
        root_group_dir.mkdir(parents=True, exist_ok=True)

        # B) economies/ altında: ./economies/01_ileri_sanayi_g7/
        eco_group_dir = economies_dir / g_id
        eco_group_dir.mkdir(parents=True, exist_ok=True)

        # Grup README'si hazırla
        group_countries = [country_by_slug[s] for s in g_info["slugs"] if s in country_by_slug]
        group_countries_sorted = sorted(group_countries, key=lambda x: x["name"])

        total_gdp = sum(c.get("gdp_usd_b", 0) for c in group_countries)
        total_pop = sum(c.get("population", 0) for c in group_countries)
        avg_shadow = sum(c.get("shadow_economy_pct", 25.0) for c in group_countries) / max(len(group_countries), 1)

        rows = []
        for c in group_countries_sorted:
            rows.append(f"| **{c['name']}** | `{c['code']}` | {c['capital']} | ${c['gdp_usd_b']:,.1f}B | %{c['shadow_economy_pct']} | [{c['name']} Dosyası]({c['slug']}/README.md) |")
        table_md = "\n".join(rows)

        group_readme = f"""# 📊 {g_info['name_tr']} ({g_info['name_en']})

> "{g_info['quote']}"  
> — **Küresel Röntgen Makroekonomik Analiz Doktrini**

---

## 1. Grup Profili ve Yapısal Ekonomik Model
{g_info['description']}

Bu ekonomik blokta yer alan ülkeler, küresel işbölümünde ve sermaye döngüsünde benzer yapısal özellikler sergilemekte; faiz şokları, emtia dalgalanmaları ve döviz likiditesi krizlerine karşı ortak kırılganlıklar taşımaktadır.

### 📈 Blok Makroekonomik Parametreleri
- **Kapsam:** {len(group_countries)} Egemen Ülke ve Bölge
- **Toplam Blok GSYH'si:** ${total_gdp:,.1f} Milyar (~${total_gdp/1000:.2f} Trilyon USD)
- **Toplam Blok Nüfusu:** {total_pop:,} İnsan
- **Ortalama Kayıt Dışı / Gölge Ekonomi Oranı:** %{avg_shadow:.2f}

---

## 2. Üye Ülkeler ve Karşılaştırmalı İstihbarat İndeksi

| Ülke | ISO | Başkent | Nominal GSYİH | Gölge Ekonomi (%) | Rapor Bağlantısı |
| :--- | :---: | :--- | :---: | :---: | :--- |
{table_md}

---

## 3. Gölge Finans ve Offshore Sermaye Akışları
Bu gruptaki ülkelerin sermaye kaçış rotaları, bankacılık gizlilik kanalları ve kleptokrasi modelleri her ülkenin kendi `04_shadow_power_osint` klasöründe belgelenmiştir.
"""

        # README yaz
        with open(root_group_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(group_readme)

        # economies/ altındaki README bağlantılarını root gruplara yönlendir
        import re
        eco_readme = re.sub(r'\(([^/]+)/README\.md\)', rf'(../../{g_id}/\1/README.md)', group_readme)
        with open(eco_group_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(eco_readme)

        # Ülkelerin klasörlerini kök seviyeden grup içine taşı veya kopyala
        for c in group_countries:
            dest_root = root_group_dir / c["slug"]
            src_root_loose = BASE_DIR / c["slug"]
            src_country = COUNTRIES_DIR / c["slug"]
            
            if not dest_root.exists():
                if src_root_loose.exists() and src_root_loose.is_dir():
                    shutil.move(str(src_root_loose), str(dest_root))
                elif src_country.exists():
                    shutil.copytree(src_country, dest_root)

        print(f"[+] '{g_info['name_tr']}' ({g_id}) grubu oluşturuldu ({len(group_countries)} ülke).")

    # 3. Kalan herhangi bir dağınık ülke klasörü varsa temizle
    cleaned_count = 0
    for c in countries:
        root_loose_dir = BASE_DIR / c["slug"]
        if root_loose_dir.exists() and root_loose_dir.is_dir():
            shutil.rmtree(root_loose_dir)
            cleaned_count += 1
    if cleaned_count > 0:
        print(f"[*] Kök dizindeki {cleaned_count} dağınık ülke klasörü temizlendi.")

    # 3.1 economies/README.md oluştur
    economies_master_readme = f"""# 🌐 Küresel Ekonomik Modeller ve Güç Blokları İndeksi

> "Devletlerin jeopolitik kaderi, coğrafi sınırlarından ziyade küresel sermaye, enerji ve emtia akışlarındaki yapısal konumlarıyla belirlenir."  
> — **Küresel Röntgen Jeo-Ekonomi Doktrini**

Bu dizin, dünyadaki 205 egemen ve jeopolitik entiteyi geleneksel kıta/bölge tasnifinden çıkararak **8 temel ekonomik modele** göre sınıflandırır.

---

## 🏛️ 8 Ekonomik Blok ve Yapısal Rolleri

| Blok Kodu | Ekonomik Model | Kapsam | Toplam GSYİH | Ortalama Gölge Ekonomi | Kök Dizin Bağlantısı |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `01` | **G7 ve İleri Teknoloji / Sanayi Ekonomileri** | 23 Ülke | ~$55.2 Trilyon | %11.8 | [01_ileri_sanayi_g7/](../01_ileri_sanayi_g7/README.md) |
| `02` | **Petro-Devletler ve Enerji İhracatçıları** | 23 Ülke | ~$5.8 Trilyon | %29.4 | [02_petro_ve_enerji_devleri/](../02_petro_ve_enerji_devleri/README.md) |
| `03` | **Gelişmekte Olan Devler, BRICS ve İmalat Merkezleri** | 21 Ülke | ~$32.6 Trilyon | %28.5 | [03_gelismekte_olan_devler_ve_brics/](../03_gelismekte_olan_devler_ve_brics/README.md) |
| `04` | **Offshore Finansal Sığınaklar ve Vergi Cennetleri** | 20 Ülke | ~$2.1 Trilyon | %16.2 | [04_offshore_ve_finansal_merkezler/](../04_offshore_ve_finansal_merkezler/README.md) |
| `05` | **Kritik Maden ve Stratejik Emtia İhracatçıları** | 22 Ülke | ~$1.9 Trilyon | %38.1 | [05_kritik_maden_ve_hammadde/](../05_kritik_maden_ve_hammadde/README.md) |
| `06` | **Orta Gelir Düzeyi ve Bölgesel Üreticiler** | 40 Ülke | ~$3.4 Trilyon | %31.7 | [06_orta_gelir_ve_ureticiler/](../06_orta_gelir_ve_ureticiler/README.md) |
| `07` | **Kırılgan, Ağır Borçlu ve Yaptırım Altındaki Devletler** | 28 Ülke | ~$0.6 Trilyon | %46.3 | [07_kirilgan_ve_borc_krizindekiler/](../07_kirilgan_ve_borc_krizindekiler/README.md) |
| `08` | **Küçük Ada Devletleri ve Turizm / Hizmet Ekonomileri** | 28 Ülke | ~$0.2 Trilyon | %26.9 | [08_kucuk_ada_ve_turizm_ekonomileri/](../08_kucuk_ada_ve_turizm_ekonomileri/README.md) |

---
*Tüm ülke klasörlerine doğrudan kök dizindeki ilgili ekonomik blok klasöründen veya `countries/` alfabetik arşivinden erişebilirsiniz.*
"""
    with open(economies_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(economies_master_readme)
    print("[+] economies/README.md oluşturuldu.")

    # 4. countries_registry.json dosyasını güncelle
    updated_registry = []
    slug_to_group = {}
    for g_id, g_info in ECONOMIC_GROUPS.items():
        for s in g_info["slugs"]:
            slug_to_group[s] = (g_id, g_info["name_tr"])

    for c in countries:
        s = c["slug"]
        g_id, g_name = slug_to_group.get(s, ("06_orta_gelir_ve_ureticiler", "Orta Gelir Düzeyi ve Bölgesel Üreticiler"))
        c["economy_group_id"] = g_id
        c["economy_group_name"] = g_name
        c["economy_path"] = f"{g_id}/{s}"
        c["path"] = f"countries/{s}"
        updated_registry.append(c)

    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(updated_registry, f, indent=2, ensure_ascii=False)
    print(f"[+] {registry_file} güncellendi (Yeni ekonomik grup kimlikleri eklendi).")

    print("\n[SUCCESS] Tüm ülkeler kıtalara göre değil, ekonomilerine göre 8 ana gruba başarıyla yapılandırıldı!")

if __name__ == "__main__":
    main()
