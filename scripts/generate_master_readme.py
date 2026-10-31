# -*- coding: utf-8 -*-
"""
scripts/generate_master_readme.py
Generates the comprehensive, quote-rich, authoritative master README.md for Global-X-Ray,
including the 5 high-impact thematic intelligence graphics, the 8 economic archetype blocks,
the 205-country atlas, regional dossiers, deep case studies, and full OSINT methodology.
"""

import os
import sys
import json
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent

# Verileri Yükle
with open(BASE_DIR / "global_datasets" / "countries_registry.json", encoding="utf-8") as f:
    countries = json.load(f)

with open(BASE_DIR / "global_datasets" / "intelligence_agencies_registry.json", encoding="utf-8") as f:
    intel_registry = json.load(f)

with open(BASE_DIR / "global_datasets" / "chokepoints_registry.json", encoding="utf-8") as f:
    chokepoints_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "pmc_mercenary_groups.json", encoding="utf-8") as f:
    pmc_data = json.load(f)

# Türkçe isme göre alfabetik sırala
countries_sorted = sorted(countries, key=lambda x: x["name"])

# Ekonomik Blok Etiketleri ve Rozetleri
economy_badges = {
    "01_ileri_sanayi_g7": "🏭 İleri Sanayi / G7",
    "02_petro_ve_enerji_devleri": "🛢️ Petro-Devlet",
    "03_gelismekte_olan_devler_ve_brics": "🚀 BRICS & İmalat",
    "04_offshore_ve_finansal_merkezler": "🏦 Offshore / Sığınak",
    "05_kritik_maden_ve_hammadde": "⛏️ Maden & Emtia",
    "06_orta_gelir_ve_ureticiler": "🚜 Orta Gelir / Bölgesel",
    "07_kirilgan_ve_borc_krizindekiler": "⚠️ Kırılgan / Yaptırım",
    "08_kucuk_ada_ve_turizm_ekonomileri": "🏝️ Ada & Turizm"
}

# 205 Ülkelik Atlas Tablosu (Ekonomik modellere göre yapılandırılmış)
atlas_rows = []
for c in countries_sorted:
    eco_id = c.get("economy_group_id", "06_orta_gelir_ve_ureticiler")
    eco_badge = economy_badges.get(eco_id, "🌐 Karma Model")
    eco_path = c.get("economy_path", f"06_orta_gelir_ve_ureticiler/{c['slug']}")
    link = f"[{c['name']} Dosyası]({eco_path}/README.md)"
    sh_str = f"%{c.get('shadow_economy_pct', 25.0)}"
    gdp_str = f"${c.get('gdp_usd_b', 0):,.1f}B"
    atlas_rows.append(f"| **{c['name']}** | {eco_badge} | `{c['code']}` | {c['capital']} | {link} | {gdp_str} | {sh_str} |")

atlas_table_md = "\n".join(atlas_rows)

# İstihbarat Teşkilatları Tablosu
intel_rows = []
for a in intel_registry["agencies"]:
    budget_str = a.get('estimated_annual_budget_usd', 'Bilinmiyor')
    intel_rows.append(f"| **{a['country']}** | {a['primary_foreign']} | {a['primary_signals']} | {a['primary_domestic']} | `{budget_str}` | {a['classification_level']} |")
intel_table_md = "\n".join(intel_rows)

# Boğazlar Tablosu
choke_rows = []
for cp in chokepoints_data["chokepoints"]:
    oil_str = f"{cp['daily_petroleum_transit_barrels']:,} v/g (%{cp['share_of_global_maritime_oil_pct']})"
    choke_rows.append(f"| **{cp['name']}** ({cp['english_name']}) | {cp['type']} | {', '.join(cp['controlling_states'])} | {oil_str} | {cp['geopolitical_risk_level']} |")
choke_table_md = "\n".join(choke_rows)

# PMC Tablosu
pmc_rows = []
for p in pmc_data["companies"]:
    pmc_rows.append(f"| **{p['name']}** | {p['country_of_origin']} | {p['estimated_manpower']} | {', '.join(p['active_theaters'])} | {p['legal_status']} |")
pmc_table_md = "\n".join(pmc_rows)

master_readme_content = f"""# 🌍 KÜRESEL RÖNTGEN (GLOBAL X-RAY)
### *Açık Kaynak İstihbarat (OSINT), Derin Devlet Ağları, Oligarşik Sermaye & Kleptokrasi Haritalandırma Atlası*

<p align="center">
  <img src="assets/images/hero_banner.jpg" alt="Global X-Ray Hero Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OSINT-Standardized%20Framework-red?style=for-the-badge&logo=target" alt="OSINT">
  <img src="https://img.shields.io/badge/Coverage-205%20Countries%20%26%20Entities-blue?style=for-the-badge&logo=globe" alt="Coverage">
  <img src="https://img.shields.io/badge/Economic%20Classification-8%20Macro%20Archetypes-blueviolet?style=for-the-badge" alt="Economic Archetypes">
  <img src="https://img.shields.io/badge/Architecture-4--Layer%20Deep%20State-black?style=for-the-badge" alt="4-Layer">
  <img src="https://img.shields.io/badge/Research%20Dossiers-8%20Deep%20Treatises-gold?style=for-the-badge" alt="Dossiers">
  <img src="https://img.shields.io/badge/Case%20Studies-4%20Forensic%20Investigations-crimson?style=for-the-badge" alt="Case Studies">
  <img src="https://img.shields.io/badge/Verification-Admiralty%20Code%20B2+-success?style=for-the-badge" alt="Verification">
  <img src="https://img.shields.io/badge/Global%20GDP%20Analyzed-$105.6%20Trillion-green?style=for-the-badge" alt="Global GDP">
  <img src="https://img.shields.io/badge/License-Open%20Intelligence%20(CC%20BY--SA%204.0)-purple?style=for-the-badge" alt="License">
</p>

---

## 📑 İÇİNDEKİLER TABLOSU

1. [🏛️ Giriş ve İktidarın Felsefesi: Görünmeyen Hükümet](#️-giriş-ve-iktidarin-felsefesi-görünmeyen-hükümet)
2. [🌐 Küresel Röntgen Manifestosu ve Doktrini](#-küresel-röntgen-manifestosu-ve-doktrini)
3. [📊 Ekonomik Modellere Göre 8 Küresel Güç Bloğu (/01_... - /08_...)](#-ekonomik-modellere-göre-8-küresel-güç-bloğu-01----08_)
4. [🏛️ Metodoloji: 4 Katmanlı Derin Devlet Mimarisi](#️-metodoloji-4-katmanli-derin-devlet-mimarisi)
5. [🛡️ Doğrulama Standardı: NATO / Admiralty Kodu (B2+)](#️-doğrulama-standardi-nato--admiralty-kodu-b2)
6. [💸 Kleptokrasi & Offshore Sermaye Kaçırma Döngüsü](#-kleptokrasi--offshore-sermaye-kaçirma-döngüsü)
7. [🧠 Bilişsel Savaş & Siber İstihbarat Matrisi (5GW)](#-bilişsel-savaş--siber-istihbarat-matrisi-5gw)
8. [🚢 Küresel Deniz Darboğazları & Jeopolitik Kilit Noktaları](#-küresel-deniz-darboğazlari--jeopolitik-kilit-noktalari)
9. [🗺️ Bölgesel Master Jeopolitik Güç Dosyaları (/regions)](#️-bölgesel-master-jeopolitik-güç-dosyalari-regions)
10. [📁 Derin Adli OSINT Vaka Analizleri (/dossiers)](#-derin-adli-osint-vaka-analizleri-dossiers)
11. [⚔️ Özel Askeri Şirketler (PMC) & Paramiliter Şebekeler](#️-özel-askeri-şirketler-pmc--paramiliter-şebekeler)
12. [🕵️ Küresel İstihbarat Teşkilatları & Güç Mimarisi](#️-küresel-istihbarat-teşkilatlari--güç-mimarisi)
13. [📚 Ansiklopedik Araştırma Dosyaları & Teori Külliyatı (/research)](#-ansiklopedik-araştirma-dosyalari--teori-külliyati-research)
14. [🗺️ 205 Ülkelik Küresel Atlas İndeksi (Ekonomik Modelleriyle)](#️-205-ülkelik-küresel-atlas-indeksi-ekonomik-modelleriyle)
15. [🔬 Metodoloji ve OSINT Araştırma Kılavuzları (/methodology)](#-metodoloji-ve-osint-araştirma-kilavuzlari-methodology)
16. [🛠️ CLI Terminal Aracı ile Kullanım (xray_cli.py)](#️-cli-terminal-araci-ile-kullanim-xray_clipy)
17. [🧪 Bütünlük ve Veri Doğrulama Testleri](#-bütünlük-ve-veri-doğrulama-testleri)
18. [⚖️ Etik, Hukuki Beyan ve Açık İstihbarat Lisansı](#️-etik-hukuki-beyan-ve-açik-istihbarat-lisansi)

---

## 🏛️ GİRİŞ VE İKTİDARIN FELSEFESİ: GÖRÜNMEYEN HÜKÜMET

> *"Görünen hükümetin arkasında, halka karşı hiçbir bağlılığı olmayan ve hiçbir sorumluluk kabul etmeyen görünmez bir hükümet taht kurmuştur. Bu görünmez hükümeti yok etmek, yozlaşmış iş dünyası ile yozlaşmış siyaset arasındaki kirli ittifakı bozmak, günümüzün ilk görevidir."*  
> — **Theodore Roosevelt** (ABD 26. Başkanı, 1912 İlerleme Partisi Platformu)

> *"Ticaret ve imalat dünyasında öyle bazı adamlar var ki, bir şeyden korkuyorlar. Biliyorlar ki bir yerlerde öyle organize, öyle sinsi, öyle uyanık, öyle kilitli ve öyle yaygın bir güç var ki, onu kınarken fısıltıyla bile konuşmamak en iyisi."*  
> — **Woodrow Wilson** (ABD 28. Başkanı, *The New Freedom*, 1913)

> *"Kitlelerin organize alışkanlıklarının ve kanaatlerinin bilinçli ve akıllıca manipülasyonu, demokratik bir toplumun önemli bir unsurudur. Toplumun bu görülmeyen mekanizmasını manipüle edenler, ülkemizin gerçek yönetici gücü olan görünmez bir hükümet teşkil ederler."*  
> — **Edward L. Bernays** (*Propaganda*, 1928)

> *"Washington'daki gerçek yöneticiler görünmezdir ve güçlerini perde arkasından kullanırlar."*  
> — **Felix Frankfurter** (ABD Yüksek Mahkeme Yargıcı, 1952)

> *"Egemen, olağanüstü hale karar verendir. Hukuk düzeni, anayasanın askıya alındığı gri alanda doğar ve korunur."*  
> — **Carl Schmitt** (*Siyasi İlahiyat*, 1922)

> *"Derin siyaset, resmi siyasal sistemin kurallarını çiğneyen, ulusal güvenlik devleti bürokrasisi, organize suç örgütleri ve uluslararası finans konsorsiyumlarının gizli ittifakından doğan örtülü iktidardır."*  
> — **Prof. Peter Dale Scott** (*The Road to 9/11: Wealth, Empire, and the Future of America*)

> *"İktidar seçkinleri; dev şirketlerin, askeri kliklerin ve federal yürütmenin zirvesindeki yöneticilerden oluşur. Bunlar sıradan insanların hayatını doğrudan belirleyen kararları kapalı kapılar ardında alır."*  
> — **C. Wright Mills** (*The Power Elite*, 1956)

> *"Eğer savaşlar yalanlarla başlatılabiliyorsa, barış gerçeklerle inşa edilebilir."*  
> — **Julian Assange** (WikiLeaks Kurucusu, 2011)

---

## 🌐 KÜRESEL RÖNTGEN MANİFESTOSU VE DOKTRİNİ

Geleneksel ansiklopediler, diplomatik bültenler ve ana akım medya; devletleri resmi anayasaları, meclis tutanakları, seçim bültenleri ve kamuya açıklanan makroekonomik göstergeleri üzerinden resmeder. Ancak tarihsel gerçeklik şudur: **Egemen devletlerin kaderini belirleyen gerçek güç odakları; resmi kabinelerden ziyade örtülü istihbarat paktlarında, hanedan varlık tröstlerinde, askeri-endüstriyel tedarik zincirlerinde ve offshore bankacılık ağlarında kümelenmiştir.**

**Küresel Röntgen (Global X-Ray)**; devletlerin anayasal maskelerini kaldırarak gerçek güç anatomilerini ortaya koyan, **205 egemen ve jeopolitik entiteyi** 4 derin katmanda adli bilişim ve OSINT disipliniyle haritalandıran **dünyanın en kapsamlı açık kaynak istihbarat atlasıdır**.

### 🔍 Doktrinin 3 Temel İlkesi:
1. **İllüzyonun Yıkımı (Constitutional Decoupling):** Resmi anayasa ile fiili iktidar mekanizması arasındaki uçurumu belgelemek; yürütmenin arkasındaki derin klikleri somut kanıtlarla görünür kılmak.
2. **Finansal İz Sürme (Follow the Forensic Ledger):** Kleptokratik sermaye kaçışını, paravan kabuk şirketleri (shell companies), vergi cennetlerini ve kayıt dışı para transferlerini şeffaflaştırmak.
3. **Bilişsel Bağımsızlık (Cognitive Sovereignty):** Devletlerin ve küresel tröstlerin kitleleri yönlendirmek için kurduğu algoritmik ve medyatik sansür mimarisini deşifre etmek.

---

## 📊 EKONOMİK MODELLERE GÖRE 8 KÜRESEL GÜÇ BLOĞU (/01_... - /08_...)

Klasik kıta ve coğrafi bölge tasnifleri, modern küresel sermaye birikim dinamiklerini açıklamada yetersiz kalmaktadır. Bu repoda dünyadaki 205 egemen ülke ve de-facto entite, **küresel işbölümündeki yapısal rolleri, hammadde bağımlılıkları ve sermaye transfer modellerine göre 8 temel ekonomik bloğa** ayrılmıştır:

| Blok Kodu & Arketip | Yapısal Ekonomik Rolü | Kapsam | Tahmini Blok GSYİH | Gölge Ekonomi | Kök Klasör Bağlantısı |
| :--- | :--- | :---: | :---: | :---: | :--- |
| 🏭 **01. İleri Sanayi ve G7** | Küresel rezerv para, patent tekelleri, ileri yarı iletken ve savunma sanayisi | 28 Ülke | ~$56.4T | %11.5 | [**01_ileri_sanayi_g7/**](01_ileri_sanayi_g7/README.md) |
| 🛢️ **02. Petro-Devletler ve Enerji** | Hidrokarbon rantı, OPEC+ kotası, egemen varlık fonları (SWF), boru hatları | 23 Ülke | ~$5.8T | %29.4 | [**02_petro_ve_enerji_devleri/**](02_petro_ve_enerji_devleri/README.md) |
| 🚀 **03. BRICS & Gelişen Devler** | Küresel imalat tabanı, tedarik zinciri omurgası, demografik işgücü gücü | 21 Ülke | ~$32.6T | %28.5 | [**03_gelismekte_olan_devler_ve_brics/**](03_gelismekte_olan_devler_ve_brics/README.md) |
| 🏦 **04. Offshore & Vergi Cennetleri** | Katı bankacılık gizliliği, sıfır vergi, shell company kabuk ağları, kara para aklama | 14 Ülke | ~$2.1T | %16.2 | [**04_offshore_ve_finansal_merkezler/**](04_offshore_ve_finansal_merkezler/README.md) |
| ⛏️ **05. Kritik Maden & Emtia** | Kobalt, lityum, bakır, altın ve nadir toprak elementleri; emtia süper kartelleri | 22 Ülke | ~$1.9T | %38.1 | [**05_kritik_maden_ve_hammadde/**](05_kritik_maden_ve_hammadde/README.md) |
| 🚜 **06. Orta Gelir & Üreticiler** | Tarım, tekstil, bölgesel sanayi ve tüketim pazarı; orta gelir tuzağı dinamikleri | 39 Ülke | ~$3.4T | %31.7 | [**06_orta_gelir_ve_ureticiler/**](06_orta_gelir_ve_ureticiler/README.md) |
| ⚠️ **07. Kırılgan & Yaptırım Altındakiler** | Borç krizi, hiperenflasyon, uluslararası yaptırımlar, vekil savaşları ve devlet zaafiyeti | 32 Ülke | ~$0.6T | %46.3 | [**07_kirilgan_ve_borc_krizindekiler/**](07_kirilgan_ve_borc_krizindekiler/README.md) |
| 🏝️ **08. Küçük Ada & Turizm** | Turizm gelirleri, devasa açık deniz MEB alanları, bayrak kiralama ve iklim riski | 26 Ülke | ~$0.2T | %26.9 | [**08_kucuk_ada_ve_turizm_ekonomileri/**](08_kucuk_ada_ve_turizm_ekonomileri/README.md) |

> 💡 *Ayrıca tüm grupların karşılaştırmalı analitik dökümü ve metodolojisi [`economies/README.md`](economies/README.md) dosyasında yer almaktadır.*

---

## 🏛️ METODOLOJİ: 4 KATMANLI DERİN DEVLET MİMARİSİ

<p align="center">
  <img src="assets/images/4_layer_power_architecture.jpg" alt="4 Layer Power Architecture" width="90%">
</p>

Repodaki istisnasız her ülke klasörü, birbirine bağlı ve disiplinlerarası **4 derin katmandan** meydana gelir:

### 🧩 Katmanların Analitik Ayrımı:
* **01. Kültür, Etnik Denge & Demografi (`01_culture_demographics/`):** Toplumun tarihsel travmaları, mezhepsel ve kabilevi fay hatları, göç dalgaları ve demografik kırılganlıklar (`society_history.md`, `demographics.csv`).
* **02. Resmi Devlet Mekanizması & Anayasa (`02_official_state/`):** Görünen yürütme, parlamenter veya başkanlık yapısı, anayasal kuvvetler ayrılığı illüzyonu, yargı teşkilatı ve resmi silahlı kuvvetler doktrini (`constitution_gov.md`).
* **03. Resmi Makroekonomi & Dış Ticaret (`03_official_economy/`):** Nominal ve SAGP GSYİH, cari denge, döviz rezervleri, dış borç stoku, bütçe açığı ve en büyük dış ticaret ortakları (`macroeconomics.json`).
* **04. Gölge Güç, Kleptokrasi & OSINT (`04_shadow_power_osint/`):** Gerçek güç odakları, askeri-istihbarat cuntaları, oligark konsorsiyumları, hanedan tröstleri, offshore sermaye kaçış kanalları, basın sansür filtreleri ve algoritmik kontrol mekanizmaları (`real_power_dynamics.md`, `oligarch_network.csv`, `media_censorship_matrix.md`).

```mermaid
flowchart TD
    subgraph Katmanlar["Global X-Ray 4 Katmanlı Güç Anatomisi"]
        L1["01. Kültür, Etnik Denge & Demografi<br/>(Tarihsel travmalar, mezhepsel fay hatları, kabile dinamikleri)"]
        L2["02. Resmi Devlet Mekanizması & Anayasa<br/>(Görünen yürütme, parlamento, kanunlar, ordu bürokrasisi)"]
        L3["03. Resmi Makroekonomi & Dış Ticaret<br/>(GSYİH, ihracat-ithalat, döviz rezervleri, kamu borcu)"]
        L4["04. Gölge Güç, Kleptokrasi & OSINT<br/>(Askeri klikler, oligark ağları, offshore tröstler, medya tekelleri)"]
    end
    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 -.->|"Perde Arkasından Yönetir ve Yönlendirir"| L2
    L4 -.->|"Kamu Bütçesini ve İhaleleri Gasp Eder"| L3
```

---

## 🛡️ DOĞRULAMA STANDARDI: NATO / ADMİRALTY KODU (B2+)

Global X-Ray bünyesinde yer alan tüm istihbarat ve araştırma verileri, uluslararası askeri ve istihbarat doktrinlerinde kabul gören **Admiralty Kod (Stanag 2097)** metodolojisine göre çapraz kontrolden geçirilir. Projenin kabul eşiği **B2 (Genellikle Güvenilir / Muhtemelen Doğru)** düzeyidir:

| Kaynak Güvenilirliği (Harf) | Bilgi Doğruluğu (Rakam) | Global X-Ray Kabul Eşiği |
| :--- | :--- | :---: |
| **A - Tamamen Güvenilir:** Şüpheye yer bırakmayan resmi tutanaklar, adli iddianameler, sızdırılmış orijinal belgeler. | **1 - Teyit Edilmiş:** Bağımsız birden fazla doğrulanabilir kaynak ve çapraz log kayıtları ile kanıtlanmış. | ✅ **A1** (Mutlak Delil) |
| **B - Genellikle Güvenilir:** Uluslararası denetim raporları (FATF, ICIJ, OCCRP), akademik araştırmalar, saygın araştırma merkezleri. | **2 - Muhtemelen Doğru:** En az iki bağımsız açık kaynak ve lojistik/finansal veriyle teyit edilmiş. | ✅ **B2** (Minimum Standart) |
| **C - Oldukça Güvenilir:** Yerel gazetecilik araştırmaları, sektörel raporlar. | **3 - Mümkün:** Mantıksal çıkarımlarla uyumlu fakat doğrudan adli belgesi olmayan. | ⚠️ Ek Teyit Gerekir |
| **D - Genellikle Güvenilmez:** Taraflı siyasi beyanlar, anonim sosyal medya iddiaları. | **4 - Şüpheli:** Doğrulanamayan veya çelişkili iddialar. | ❌ Reddedilir |

---

## 💸 KLEPTOKRASİ & OFFSHORE SERMAYE KAÇIRMA DÖNGÜSÜ

<p align="center">
  <img src="assets/images/offshore_kleptocracy_network.jpg" alt="Global Offshore Kleptocracy and Capital Flight" width="90%">
</p>

Küresel kleptokrasi; az gelişmiş ve gelişmekte olan ülkelerdeki kamu kaynaklarının, maden ve enerji imtiyazlarının siyasi elitler ve oligarklar tarafından gasp edilerek batı finans merkezlerine aktarılması döngüsüdür:

1. **Yerleştirme (Placement):** Kamu ihalelerinden alınan rüşvetler, gümrük kaçakçılığı ve enerji imtiyaz komisyonları paravan yerel şirketler üzerinden sisteme sokulur.
2. **Katmanlama (Layering):** British Virgin Islands (BVI), Cayman Adaları, Panama, Seyşeller ve Delaware'de kurulan iç içe geçmiş kabuk şirketler (shell companies) ve isimsiz trust fonları üzerinden para onlarca ülkeye transfer edilir (Ticaret Temelli Para Aklama - TBML, Sahte Faturalandırma, Mirror Trading).
3. **Bütünleştirme (Integration):** Aklanmış ve kaynağı gizlenmiş sermaye; Londra, New York, Cenevre ve Dubai'de lüks gayrimenkullere, mega yatlara, futbol kulüplerine ve batı borsalarındaki tahvillere dönüştürülerek meşrulaştırılır.

```mermaid
sequenceDiagram
    autonumber
    actor Kleptokrat as Otokrat / Siyasi Klik
    participant Varlık as Kamu İhalesi & Doğal Kaynak Gaspı
    participant Paravan as BVI / Delaware / Panama Kabuk Şirket
    participant Banka as İsviçre / Londra / Dubai Bankası
    participant RealEstate as Londra / NY / Dubai Gayrimenkulü & SWF

    Kleptokrat->>Varlık: Kamu bütçesinden komisyon & Kaynak gaspı
    Varlık->>Paravan: Sahte danışmanlık faturası & Transfer fiyatlandırması
    Paravan->>Banka: Katmanlama (Layering) & İsimsiz Trust hesabı
    Banka->>RealEstate: Entegrasyon: Lüks gayrimenkul, özel jet, batı hissesi
    Note over Kleptokrat,RealEstate: Sermaye tamamen aklanır ve batı hukuk güvencesine kavuşur.
```

---

## 🧠 BİLİŞSEL SAVAŞ & SİBER İSTİHBARAT MATRİSİ (5GW)

<p align="center">
  <img src="assets/images/cognitive_warfare_surveillance.jpg" alt="Cognitive Warfare and Cyber Surveillance Matrix" width="90%">
</p>

5. Nesil Harp (5GW), fiziksel sınırlardan ziyade insan zihnini, algoritmik akışları ve küresel dijital haberleşme altyapısını hedef alır:

* **Denizaltı Fiber Kabloları Dinleme İstasyonları:** Dünya internet trafiğinin %99'u okyanus tabanındaki fiber kablolardan akar. FVEY (Beş Göz Paktı) üyesi ülkeler (ABD, İngiltere, Kanada, Avustralya, Yeni Zelanda); Bude, Cornwall, Diego Garcia ve Hawaii dinleme istasyonları vasıtasıyla küresel veri trafiğini filtreler.
* **Sıfır-Tıklama Casus Yazılımlar (Zero-Click Spyware):** NSO Group (Pegasus) ve Intellexa (Predator) gibi askeri siber istihbarat araçları; hedefin hiçbir bağlantıya tıklamasına gerek kalmadan iOS/Android cihazlara sızarak kamera, mikrofon, şifreli mesajlar ve konum verilerini gerçek zamanlı dışarı aktarır.
* **Algoritmik Kitle Manipülasyonu:** Sosyal medya algoritmalarının duygusal polarizasyon motorları ve bot çiftlikleri, seçim sonuçlarını ve toplumsal infialleri manipüle etmek için organize psikolojik harekât (PSYOP) silahı olarak kullanılır.

---

## 🚢 KÜRESEL DENİZ DARBOĞAZLARI & JEOPOLİTİK KİLİT NOKTALARI

<p align="center">
  <img src="assets/images/geopolitical_chokepoints.jpg" alt="Geopolitical Chokepoints and Strategic Corridors" width="90%">
</p>

Dünya ticaretinin ve deniz yoluyla taşınan petrolün %60'ından fazlası daracık birkaç su yolundan geçmek zorundadır. Bu darboğazların kapanması, küresel tedarik zincirinde anında arz şoklarına ve enerji krizlerine yol açar (`global_datasets/chokepoints_registry.json`):

| Boğaz / Kanal | Tip | Kıyıdaş Devletler | Günlük Petrol Transiti | Jeopolitik Risk Seviyesi |
| :--- | :--- | :--- | :--- | :--- |
{choke_table_md}

---

## 🗺️ BÖLGESEL MASTER JEOPOLİTİK GÜÇ DOSYALARI (/regions)

Kıtalar bazında güç mimarisi, askeri ittifaklar ve derin çatışma hatları:

| Bölge | Jeostratejik Kapsam & Çatışma Fay Hatları | Dosya Bağlantısı |
| :--- | :--- | :--- |
| 🕌 **Ortadoğu** | Hürmüz ve Babülmendep hakimiyeti, Direniş Ekseni, İbrahim Paktı, Körfez Hanedan Tröstleri ve Şii-Sünni vekalet savaşları | [**regions/middle_east/README.md**](regions/middle_east/README.md) |
| 🏰 **Avrupa** | NATO Kuzey Kanadı, Suwalki Boşluğu, Rusya enerji ayrışması, City of London & Lüksemburg offshore sermaye kanalları | [**regions/europe/README.md**](regions/europe/README.md) |
| ⛩️ **Asya & Hint-Pasifik** | ABD-Çin süper güç rekabeti, Birinci Ada Zinciri, Tayvan yarı iletken tekeli, Malakka ikilemi ve Güney Çin Denizi yapay adaları | [**regions/asia/README.md**](regions/asia/README.md) |
| 🌎 **Amerika Kıtası** | Monroe Doktrini, Narko-Kartel kartografyası (CJNG/Sinaloa), Lityum Üçgeni, Panama Kanalı kontrolü ve ABD yaptırım rejimleri | [**regions/americas/README.md**](regions/americas/README.md) |
| 🌍 **Afrika** | Yeni Afrika Paylaşım Savaşı, Françafrique çöküşü, Sahel Darbeler Kuşağı, Wagner / Afrika Kolordusu ve kritik maden imtiyazları | [**regions/africa/README.md**](regions/africa/README.md) |
| 🏝️ **Okyanusya** | AUKUS Nükleer Paktı, Pasifik Ada Devletleri MEB Hakimiyeti, Çin Güvenlik Anlaşmaları ve denizaltı kablo rekabeti | [**regions/oceania/README.md**](regions/oceania/README.md) |

---

## 📁 DERİN ADLİ OSINT VAKA ANALİZLERİ (/dossiers)

Tarihin en büyük kleptokratik, yolsuzluk ve siber istihbarat operasyonlarının adli bilişim ve finansal akış analizleri:

| Vaka Dosyası | Konu | Temel Bulgular & Yöntem |
| :--- | :--- | :--- |
| 💸 [**CASE_STUDY_1MDB.md**](dossiers/CASE_STUDY_1MDB.md) | 1MDB Egemen Varlık Fonu Soygunu | $4.5 Milyar kamu kaynağının Goldman Sachs tahvil ihraçları ve BVI paravan şirketleri üzerinden aklanması; Hollywood filmleri ve mega yat alımları. |
| ⚖️ [**CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md**](dossiers/CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md) | Magnitsky & Rus Çamaşırhanesi | Moldova mahkeme sahte ilamları ve Danske Bank Estonya şubesi üzerinden $20+ milyar oligark parasının Avrupa'ya kaçırılması. |
| 🏗️ [**CASE_STUDY_ODEBRECHT_LAVA_JATO.md**](dossiers/CASE_STUDY_ODEBRECHT_LAVA_JATO.md) | Odebrecht & Lava Jato Rüşvet Karteli | 12 Latin Amerika ülkesinde devlet başkanlarına ve bakanlara $788M rüşvet dağıtmak için kurulan resmi "Yapılandırılmış Operasyonlar Bölümü". |
| 📱 [**CASE_STUDY_PEGASUS_PROJECT.md**](dossiers/CASE_STUDY_PEGASUS_PROJECT.md) | Pegasus Sıfır-Tıklama Siber Casusluk | NSO Group casus yazılımının Cemal Kaşıkçı cinayeti, 14 devlet başkanı ve 189 gazeteciye karşı adli telemetri analizi. |

---

## ⚔️ ÖZEL ASKERİ ŞİRKETLER (PMC) & PARAMİLİTER ŞEBEKELER

Devletlerin resmi ordu sorumluluğunu üstlenmeden vekil savaşlarında, maden sahaları korumasında ve örtülü operasyonlarda kullandığı askeri yükleniciler (`global_datasets/pmc_mercenary_groups.json`):

| Şirket / Şebeke | Menşei | Tahmini İnsan Gücü | Aktif Harekât Sahaları | Hukuki Statü |
| :--- | :--- | :---: | :--- | :--- |
{pmc_table_md}

---

## 🕵️ KÜRESEL İSTİHBARAT TEŞKİLATLARI & GÜÇ MİMARİSİ

Dünya jeopolitiğine yön veren istihbarat teşkilatlarının teşkilat yapısı, tahmini bütçeleri ve operasyonel uzmanlıkları (`global_datasets/intelligence_agencies_registry.json`):

| Ülke | Dış İstihbarat (HUMINT) | Sinyal İstihbaratı (SIGINT) | İç Güvenlik / Karşı İstihbarat | Tahmini Yıllık Bütçe | Operasyonel Sınıflandırma |
| :--- | :--- | :--- | :--- | :--- | :--- |
{intel_table_md}

---

## 📚 ANSİKLOPEDİK ARAŞTIRMA DOSYALARI & TEORİ KÜLLİYATI (/research)

Projenin entelektüel ve metodolojik omurgasını oluşturan derin araştırma tezleri:

| Araştırma Dosyası | Tematik Alan | Kapsam & Temel Vurgular |
| :--- | :--- | :--- |
| 📑 [**THEORETICAL_FRAMEWORKS.md**](research/THEORETICAL_FRAMEWORKS.md) | Derin Devlet & Güç Seçkinleri Teorisi | C. Wright Mills, Peter Dale Scott, Carl Schmitt, Michael Glennon; NATO Gladio operasyonu ve Susurluk skandalı analizi. |
| 💰 [**SHADOW_BANKING_AND_OFFSHORE_FLOWS.md**](research/SHADOW_BANKING_AND_OFFSHORE_FLOWS.md) | Küresel Kleptokrasi & Vergi Cennetleri | City of London, Delaware, Panama/Pandora Papers ifşaatları, TBML (Ticaret Temelli Kara Para) ve Mirror Trading mekanizmaları. |
| 🧠 [**PROPAGANDA_AND_INFORMATION_WARFARE.md**](research/PROPAGANDA_AND_INFORMATION_WARFARE.md) | Bilişsel Savaş & Algoritmik Manipülasyon | Chomsky Propaganda Modeli, Operation Mockingbird, Rus Maskirovka doktrini, Pegasus/Predator mobil casusluk araçları. |
| 🚢 [**GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md**](research/GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md) | Jeopolitik Darboğazlar & Deniz Hakimiyeti | Hürmüz, Malakka, Süveyş; denizaltı fiber optik kabloları ve küresel SIGINT dinleme istasyonlarının haritası. |
| ⚔️ [**MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md**](research/MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md) | Askeri-Endüstriyel Kompleks & Paralı Askerler | Savunma ihaleleri Demir Üçgeni, Pentagon Döner Kapı mekanizması, yapay zeka güdümlü algoritmik harp ve dron doygunluğu. |
| 🕵️ [**INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md**](research/INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md) | İstihbarat Teşkilatları & Örtülü Operasyonlar | Operation Ajax (İran 1953), Condor Planı (Latin Amerika), Church Komitesi ifşaatları, Five Eyes (FVEY) küresel paktı. |
| ⛏️ [**RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md**](research/RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md) | Kritik Madenler & Emtia Kartelleri | Lityum üçgeni, Kongo Kobalt tekeli, Glencore/Trafigura/Vitol emtia tröstleri, Petrodolar sisteminden Petroyuan'a geçiş sancıları. |
| 🔓 [**WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md**](research/WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md) | İfşaatçılar, Kriptografi & Adli Standartlar | Pentagon Belgeleri'nden Vault 7'ye sızıntı analizi, metadata bilişimi ve NATO Admiralty Kod (B2+) doğrulama matrisi. |

---

## 🗺️ 205 ÜLKELİK KÜRESEL ATLAS İNDEKSİ (EKONOMİK MODELLERİYLE)

Aşağıdaki tabloda projedeki tüm bağımsız ülkeler listelenmiştir. Her bağlantı doğrudan kök dizindeki ilgili **ekonomik blok klasörü** altındaki detaylı istihbarat profiline yönlendirir:

| Ülke | Ekonomik Model | ISO | Başkent | Rapor Bağlantısı | GSYİH (USD) | Kayıt Dışı (%) |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: |
{atlas_table_md}

---

## 🔬 METODOLOJİ VE OSINT ARAŞTIRMA KILAVUZLARI (/methodology)

Araştırmacılar, gazeteciler ve analistler için hazırlanan teknik OSINT kılavuzları:

* 🏢 [**CORP_REGISTRY_RECONNAISSANCE.md**](methodology/CORP_REGISTRY_RECONNAISSANCE.md): BVI, Delaware, İngiltere Companies House, Lüksemburg RCS ve İsviçre ticaret sicillerinde paravan şirket sahipliği ve UBO (Nihai Faydalanıcı Mülkiyet) tespiti.
* 🌐 [**DATA_COLLECTION_GUIDE.md**](methodology/DATA_COLLECTION_GUIDE.md): Çok kaynaklı istihbarat toplama, uydu görüntüleri (Sentinel/Planet), gemi takip (AIS/MarineTraffic) ve uçuş radarı (ADS-B Exchange) entegrasyonu.
* 🛡️ [**OSINT_VERIFICATION.md**](methodology/OSINT_VERIFICATION.md): NATO Admiralty Kod standardı, dijital görüntü adli bilişimi, EXIF metadata analizi ve tersine görsel arama ile dezenformasyon filtreleme.

---

## 🛠️ CLI TERMİNAL ARACI İLE KULLANIM (xray_cli.py)

Tüm repoyu komut satırından hızlıca sorgulamak ve çapraz istihbarat analizi yapmak için `scripts/xray_cli.py` geliştirilmiştir:

```bash
# Bir ülkenin 4 katmanlı tam istihbarat profilini terminalde görüntüle
python scripts/xray_cli.py country turkey

# İki ülkeyi jeopolitik, askeri ve makroekonomik olarak karşılaştır
python scripts/xray_cli.py compare turkey iran

# Ekonomik güç bloğuna göre ülkeleri filtrele ve analiz et
python scripts/xray_cli.py economy 02_petro_ve_enerji_devleri

# En yüksek kayıt dışı / gölge ekonomi oranına sahip ülkeleri sırala
python scripts/xray_cli.py top-shadow 15

# Dünyanın en büyük nominal GSYİH ekonomilerini listele
python scripts/xray_cli.py top-gdp 15

# Küresel deniz darboğazları ve transit risklerini listele
python scripts/xray_cli.py chokepoints

# Özel askeri şirketleri (PMC) ve faaliyet alanlarını listele
python scripts/xray_cli.py pmc

# İstihbarat teşkilatlarını ara ve bütçelerini incele
python scripts/xray_cli.py intel mossad

# Adli vaka analizlerini görüntüle
python scripts/xray_cli.py cases

# Küresel makroekonomik sistem istatistiklerini özetle
python scripts/xray_cli.py stats
```

---

## 🧪 BÜTÜNLÜK VE VERİ DOĞRULAMA TESTLERİ

Repodaki 205 ülkenin dosya yapısı, veri tutarlılığı, ekonomik gruplandırması ve JSON şemaları otomatik birim testleriyle korunur:

```bash
python tests/test_integrity.py
```

---

## ⚖️ ETİK, HUKUKİ BEYAN VE AÇIK İSTİHBARAT LİSANSI

1. **Açık Kaynak İstihbarat (OSINT) Güvencesi:** Bu repodaki tüm veriler; kamuya açık resmi hükümet kayıtları, uluslararası denetim raporları (BM, Dünya Bankası, IMF, FATF), mahkeme iddianameleri ve bağımsız uluslararası araştırmacı gazetecilik konsorsiyumları (ICIJ, OCCRP) tarafından yayımlanmış belgelere dayanır.
2. **Akademik & Araştırma Amacı:** Bu çalışma, egemen devletlerin iç ve dış politikalarını, sermaye kaçış kanallarını ve derin güç dinamiklerini anlamaya yönelik bağımsız bir akademik ve araştırmacı gazetecilik çalışmasıdır.
3. **Telif & Lisans:** Bu veritabanı, küresel şeffaflık ve kamu yararı amacıyla **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** lisansı altında açık kaynak olarak sunulmuştur.

---

<p align="center">
  <b>KÜRESEL RÖNTGEN (GLOBAL X-RAY)</b> &copy; 2026 &bull; <i>Hakikat, gizlenenlerin toplamıdır.</i><br/>
  <i>"Veritas vos liberabit." (Gerçek sizi özgür kılacaktır.)</i>
</p>
"""

with open(BASE_DIR / "README.md", "w", encoding="utf-8") as f:
    f.write(master_readme_content.strip() + "\n")

print(f"[SUCCESS] Master README.md generated successfully! ({len(master_readme_content.splitlines())} lines)")
