# -*- coding: utf-8 -*-
"""
scripts/generate_master_readme.py
Generates the comprehensive, quote-rich, authoritative master README.md for Global-X-Ray,
including the 5 high-impact thematic intelligence graphics.
"""

import json
from pathlib import Path

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

# Bölge etiketleri ve emojileri
region_labels = {
    "middle_east": "🕌 Ortadoğu",
    "europe": "🏰 Avrupa",
    "asia": "⛩️ Asya",
    "americas": "🌎 Amerika",
    "africa": "🌍 Afrika",
    "oceania": "🏝️ Okyanusya"
}

# 205 Ülkelik Atlas Tablosu
atlas_rows = []
for c in countries_sorted:
    reg_label = region_labels.get(c["region"], c["region"])
    link = f"[{c['name']} İstihbarat Raporu]({c['slug']}/README.md)"
    sh_str = f"%{c.get('shadow_economy_pct', 25.0)}"
    gdp_str = f"${c.get('gdp_usd_b', 0):,.1f}B"
    atlas_rows.append(f"| **{c['name']}** | {reg_label} | `{c['code']}` | {c['capital']} | {link} | {gdp_str} | {sh_str} |")

atlas_table_md = "\n".join(atlas_rows)

# İstihbarat Teşkilatları Tablosu
intel_rows = []
for a in intel_registry["agencies"]:
    intel_rows.append(f"| **{a['country']}** | {a['primary_foreign']} | {a['primary_signals']} | {a['primary_domestic']} | `{a['estimated_annual_budget_usd']}` | {a['classification_level']} |")
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
  <img src="https://img.shields.io/badge/OSINT-Standardized-red?style=for-the-badge&logo=target" alt="OSINT">
  <img src="https://img.shields.io/badge/Coverage-205%20Countries%20%26%20Entities-blue?style=for-the-badge&logo=globe" alt="Coverage">
  <img src="https://img.shields.io/badge/Architecture-4--Layer%20Deep%20State-black?style=for-the-badge" alt="4-Layer">
  <img src="https://img.shields.io/badge/Research%20Dossiers-8%20Deep%20Investigations-gold?style=for-the-badge" alt="Dossiers">
  <img src="https://img.shields.io/badge/Case%20Studies-4%20Forensic%20Investigations-crimson?style=for-the-badge" alt="Case Studies">
  <img src="https://img.shields.io/badge/Verification-Admiralty%20Code%20B2+-success?style=for-the-badge" alt="Verification">
  <img src="https://img.shields.io/badge/Global%20GDP-$105.6%20Trillion-green?style=for-the-badge" alt="Global GDP">
  <img src="https://img.shields.io/badge/License-Open%20Intelligence-purple?style=for-the-badge" alt="License">
</p>

---

## 🏛️ GİRİŞ VE İKTİDARIN FELSEFESİ: KÜRESEL İSTİHBARAT KÜLLİYATI

> *"Görünen hükümetin arkasında, halka karşı hiçbir bağlılığı olmayan ve hiçbir sorumluluk kabul etmeyen görünmez bir hükümet taht kurmuştur. Bu görünmez hükümeti yok etmek, yozlaşmış iş dünyası ile yozlaşmış siyaset arasındaki kirli ittifakı bozmak, günümüzün ilk görevidir."*  
> — **Theodore Roosevelt** (ABD 26. Başkanı, 1912 İlerleme Partisi Platformu)

> *"Ticaret ve imalat dünyasında öyle bazı adamlar var ki, bir şeyden korkuyorlar. Biliyorlar ki bir yerlerde öyle organize, öyle sinsi, öyle uyanık, öyle kilitli ve öyle yaygın bir güç var ki, onu kınarken fısıltıyla bile konuşmamak en iyisi."*  
> — **Woodrow Wilson** (ABD 28. Başkanı, *The New Freedom*, 1913)

> *"Kitlelerin organize alışkanlıklarının ve kanaatlerinin bilinçli ve akıllıca manipülasyonu, demokratik bir toplumun önemli bir unsurudur. Toplumun bu görülmeyen mekanizmasını manipüle edenler, ülkemizin gerçek yönetici gücü olan görünmez bir hükümet teşkil ederler."*  
> — **Edward L. Bernays** (*Propaganda*, 1928)

> *"Washington'daki gerçek yöneticiler görünmezdir ve güçlerini perde arkasından kullanırlar."*  
> — **Felix Frankfurter** (ABD Yüksek Mahkemesi Yargıcı, 1952)

> *"Siyaset; kimin, neyi, ne zaman ve nasıl aldığının incelenmesidir."*  
> — **Harold Lasswell** (*Politics: Who Gets What, When, How*, 1936)

> *"Her büyük servetin arkasında, faili asla cezalandırılmamış çünkü ustaca işlenmiş unutulmuş bir suç yatar."*  
> — **Honoré de Balzac** (*Le Père Goriot*, 1835)

> *"Bir ulusun para arzını basma ve kontrol etme yetkisini bana verin; yasalarını kimin yaptığını zerre kadar umursamam."*  
> — **Mayer Amschel Rothschild** (Uluslararası Finans Hanedanı Kurucusu)

> *"Bankacılar dünyaya hükmeder. Onlardan her şeyi alın ama para yaratma güçlerini bırakın; bir kalem darbesiyle her şeyi geri alacak kadar mevduat yaratırlar."*  
> — **Sir Josiah Stamp** (İngiltere Merkez Bankası Direktörü, 1927)

> *"Hükümet konseylerinde, askeri-endüstriyel kompleks tarafından yersiz nüfuz elde edilmesine karşı uyanık olmalıyız. Yanlış ellere geçmiş gücün yaratacağı felaket potansiyeli mevcuttur ve sürecektir."*  
> — **Dwight D. Eisenhower** (ABD 34. Başkanı, Veda Konuşması, 1961)

> *"Savaş bir hiledir, bir soygundur (War is a racket). Daima öyle olmuştur. Muhtemelen en eskisi, kolayca en karlı olanı, kesinlikle en acımasızıdır. Kârların dolarlarla, kayıpların ise canlarla hesaplandığı tek uluslararası iştir."*  
> — **Tümgeneral Smedley Butler** (*War is a Racket*, 1935)

> *"Savaş, siyasetin başka araçlarla devamıdır."*  
> — **Carl von Clausewitz** (*Vom Kriege*, 1832)

> *"Güçlü olan gücünün yettiğini yapar, zayıf olan ise çekmek zorunda olduğunu çeker."*  
> — **Thukididis** (*Peloponnesos Savaşları - Melos Diyaloğu*, MÖ 416)

> *"İnsanları pasif ve itaatkar tutmanın akıllıca yolu, kabul edilebilir kanaat spektrumunu sıkıca sınırlamak; fakat o dar spektrum içinde son derece canlı ve hararetli bir tartışmaya izin vermektir."*  
> — **Noam Chomsky** (*The Common Good*, 1998)

> *"Evrensel aldatmacanın hüküm sürdüğü dönemlerde hakikati söylemek devrimci bir eylemdir."*  
> — **George Orwell** (*1984*, 1949)

> *"Eğer savaşlar yalanlarla başlatılabiliyorsa, barış da gerçeklerle inşa edilebilir."*  
> — **Julian Assange** (WikiLeaks Kurucusu, 2011)

> *"Her yaptığımın ve her söylediğimin kaydedildiği bir dünyada yaşamak istemiyorum."*  
> — **Edward Snowden** (NSA Whistleblower, 2013)

> *"Hükümdar tuzakları tanımak için tilki, kurtları korkutmak için aslan olmak zorundadır."*  
> — **Niccolò Machiavelli** (*Il Principe*, 1532)

---

## 📐 ANALİTİK ÇERÇEVE: 4 KATMANLI DERİN DEVLET MODELİ

<p align="center">
  <img src="assets/images/4_layer_power_architecture.jpg" alt="4-Layer Deep State Power Architecture" width="90%">
</p>

```mermaid
flowchart TD
    subgraph Katmanlar["Global X-Ray 4 Katmanlı Güç Anatomisi"]
        L1["01. Kültür, Etnik Denge & Demografi<br/>(Tarihsel travmalar, mezhepsel fay hatları, göç dalgaları)"]
        L2["02. Resmi Devlet Mekanizması & Anayasa<br/>(Görünen yürütme, yargı, ordu teşkilatı, kanunlar)"]
        L3["03. Resmi Makroekonomi & Dış Ticaret<br/>(GSYİH, ihracat-ithalat, döviz rezervleri, bütçe açığı)"]
        L4["04. Gölge Güç, Kleptokrasi & OSINT<br/>(Gerçek güç merkezleri, oligark ağları, off-shore kaçış, sansür)"]
    end
    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 -.->|"Perde Arkasından Yönetir"| L2
```

---

## 💸 KLEPTOKRASİ & OFF-SHORE SERMAYE KAÇIRMA DÖNGÜSÜ

<p align="center">
  <img src="assets/images/offshore_kleptocracy_network.jpg" alt="Global Offshore Kleptocracy and Capital Flight" width="90%">
</p>

```mermaid
sequenceDiagram
    autonumber
    actor Kleptokrat as Otokrat / Siyasi Klik
    participant Varlık as Kamu İhalesi & Doğal Kaynak
    participant Paravan as BVI / Delaware Kabuk Şirket
    participant Banka as İsviçre / Londra / Dubai Bankası
    participant RealEstate as Londra / NY / Dubai Gayrimenkulü

    Kleptokrat->>Varlık: Kamu ihalelerinden komisyon / Kaynak gaspı
    Varlık->>Paravan: Sahte fatura & Transfer fiyatlandırması
    Paravan->>Banka: Katmanlama (Layering) & İsimsiz Trust hesabı
    Banka->>RealEstate: Entegrasyon: Lüks gayrimenkul, yat & sanat eseri alımı
    Note over Kleptokrat,RealEstate: Sermaye tamamen aklanır ve batı hukuk güvencesine alınır.
```

---

## 🧠 BİLİŞSEL SAVAŞ & SİBER İSTİHBARAT MATRİSİ

<p align="center">
  <img src="assets/images/cognitive_warfare_surveillance.jpg" alt="Cognitive Warfare and Cyber Surveillance Matrix" width="90%">
</p>

Küresel sinyal istihbaratı (SIGINT), denizaltı fiber optik hat dinleme istasyonları, sıfır-tıklama mobil casus yazılımlar (Pegasus, Predator) ve kitlelerin algısını yöneten algoritmik sosyal medya filtreleri, 5. Nesil Harp (5GW) doktrininin temelini oluşturur.

---

## 🚢 KÜRESEL DENİZ DARBOĞAZLARI & TRANSİT KİLİTLERİ

<p align="center">
  <img src="assets/images/geopolitical_chokepoints.jpg" alt="Geopolitical Chokepoints and Strategic Corridors" width="90%">
</p>

Dünya deniz petrolünün ve ticaretinin aktığı kilit boğazlar (`global_datasets/chokepoints_registry.json`):

| Boğaz / Kanal | Tip | Kıyıdaş Devletler | Günlük Petrol Transiti | Jeopolitik Risk Seviyesi |
| :--- | :--- | :--- | :--- | :--- |
{choke_table_md}

---

## 🗺️ BÖLGESEL MASTER JEOPOLİTİK DOSYALARI (/regions)

Kıtalar bazında güç mimarisi, güvenlik paktları ve çatışma hatları:

| Bölge | Jeostratejik Kapsam | Dosya Bağlantısı |
| :--- | :--- | :--- |
| 🕌 **Ortadoğu** | Hürmüz ve Babülmendep, Direniş Ekseni, İbrahim Paktı, Körfez Hanedan Tröstleri | [**regions/middle_east/README.md**](regions/middle_east/README.md) |
| 🏰 **Avrupa** | NATO Kuzey Kanadı, Suwalki Koridoru, Rusya Enerji Ayrışması, City of London & Lüksemburg | [**regions/europe/README.md**](regions/europe/README.md) |
| ⛩️ **Asya & Hint-Pasifik** | ABD-Çin Rekabeti, Birinci Ada Zinciri, Tayvan Yarı İletken Tekeli, Malakka İkilemi | [**regions/asia/README.md**](regions/asia/README.md) |
| 🌎 **Amerika** | Monroe Doktrini, Narko-Kartel Kartografyası (CJNG/Sinaloa), Lityum Üçgeni, Panama Kanalı | [**regions/americas/README.md**](regions/americas/README.md) |
| 🌍 **Afrika** | Yeni Afrika Paylaşım Savaşı, Françafrique Çöküşü, Sahel Darbeler Kuşağı, Wagner / Afrika Kolordusu | [**regions/africa/README.md**](regions/africa/README.md) |
| 🏝️ **Okyanusya** | AUKUS Paktı, Pasifik Ada Devletleri MEB Hakimiyeti, Çin Güvenlik Anlaşmaları | [**regions/oceania/README.md**](regions/oceania/README.md) |

---

## 📁 DERİN ADLİ OSINT VAKA ANALİZLERİ (/dossiers)

Tarihin en büyük kleptokratik ve siber istihbarat operasyonlarının adli bilişim ve finansal akış analizleri:

| Vaka Dosyası | Konu | Temel Bulgular & Yöntem |
| :--- | :--- | :--- |
| 💸 [**CASE_STUDY_1MDB.md**](dossiers/CASE_STUDY_1MDB.md) | 1MDB Egemen Varlık Fonu Soygunu | $4.5 Milyar kamu kaynağının Goldman Sachs ve BVI paravan şirketleri üzerinden aklanması. |
| ⚖️ [**CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md**](dossiers/CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md) | Magnitsky & Rus Çamaşırhanesi | Moldova mahkeme ilamları ve Danske Bank üzerinden $20+ milyar oligark parasının Avrupa'ya kaçırılması. |
| 🏗️ [**CASE_STUDY_ODEBRECHT_LAVA_JATO.md**](dossiers/CASE_STUDY_ODEBRECHT_LAVA_JATO.md) | Odebrecht & Lava Jato Rüşvet Karteli | 12 ülkede başkanlara rüşvet dağıtmak için kurulan resmi "Yapılandırılmış Operasyonlar Bölümü". |
| 📱 [**CASE_STUDY_PEGASUS_PROJECT.md**](dossiers/CASE_STUDY_PEGASUS_PROJECT.md) | Pegasus Sıfır-Tıklama Siber Casusluk | NSO Group casus yazılımının Kaşıkçı cinayeti, 14 devlet başkanı ve 189 gazeteciye karşı kullanımı. |

---

## ⚔️ ÖZEL ASKERİ ŞİRKETLER (PMC) & PARAMİLİTERLER

Devletlerin örtülü operasyon ve vekil savaşlarında kullandığı askeri yükleniciler (`global_datasets/pmc_mercenary_groups.json`):

| Şirket / Şebeke | Menşei | Tahmini İnsan Gücü | Aktif Harekât Sahaları | Hukuki Statü |
| :--- | :--- | :---: | :--- | :--- |
{pmc_table_md}

---

## 📚 ANSİKLOPEDİK ARAŞTIRMA DOSYALARI (/research)

| Araştırma Dosyası | Tematik Alan | Kapsam & Temel Vurgular |
| :--- | :--- | :--- |
| 📑 [**THEORETICAL_FRAMEWORKS.md**](research/THEORETICAL_FRAMEWORKS.md) | Derin Devlet & Güç Seçkinleri Teorisi | C. Wright Mills, Peter Dale Scott, Carl Schmitt, Michael Glennon, Gladio ve Susurluk. |
| 💰 [**SHADOW_BANKING_AND_OFFSHORE_FLOWS.md**](research/SHADOW_BANKING_AND_OFFSHORE_FLOWS.md) | Küresel Kleptokrasi & Vergi Cennetleri | City of London, Delaware, Panama/Pandora Papers, TBML ve Mirror Trading. |
| 🧠 [**PROPAGANDA_AND_INFORMATION_WARFARE.md**](research/PROPAGANDA_AND_INFORMATION_WARFARE.md) | Bilişsel Savaş & Algoritmik Manipülasyon | Chomsky Propaganda Modeli, Operation Mockingbird, Maskirovka, Pegasus/Predator siber araçları. |
| 🚢 [**GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md**](research/GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md) | Jeopolitik Darboğazlar & Deniz Hakimiyeti | Hürmüz, Malakka, Süveyş; denizaltı fiber optik kabloları ve SIGINT dinleme istasyonları. |
| ⚔️ [**MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md**](research/MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md) | Askeri-Endüstriyel Kompleks & Paralı Askerler | Savunma ihale Demir Üçgeni, Döner Kapı mekanizması, algoritmik harp ve dron doygunluğu. |
| 🕵️ [**INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md**](research/INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md) | İstihbarat Teşkilatları & Örtülü Operasyonlar | Operation Ajax (1953), Condor Planı, Church Komitesi ifşaatları, Five Eyes (FVEY) paktı. |
| ⛏️ [**RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md**](research/RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md) | Kritik Madenler & Emtia Kartelleri | Lityum üçgeni, Kongo Kobaltı, Glencore/Trafigura/Vitol emtia oligopolü, Petrodolar/Petroyuan. |
| 🔓 [**WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md**](research/WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md) | İfşaatçılar, Kriptografi & Adli Standartlar | Pentagon Belgeleri'nden Vault 7'ye sızıntı analizi, metadata bilişimi ve Admiralty Kod (B2+). |

---

## 🕵️ KÜRESEL İSTİHBARAT TEŞKİLATLARI & GÜÇ MİMARİSİ

| Ülke | Dış İstihbarat (HUMINT) | Sinyal İstihbaratı (SIGINT) | İç Güvenlik / Karşı İstihbarat | Tahmini Yıllık Bütçe | Operasyonel Sınıflandırma |
| :--- | :--- | :--- | :--- | :--- | :--- |
{intel_table_md}

---

## 🌐 PROJE AMACI VE VİZYONU

**Küresel Röntgen (Global X-Ray)**, ulus devletlerin görünen resmi anayasal yapılarının ötesine geçerek; arka planda işleyen **derin güç odaklarını, askeri klikleri, istihbarat oligarşilerini, hanedan servetlerini, mafya-sermaye konsorsiyumlarını ve kayıt dışı para akışlarını** bilimsel ve doğrulanabilir OSINT (Open Source Intelligence) metodolojisi ile belgeleyen küresel bir araştırma ve istihbarat atlasıdır.

Proje, Birleşmiş Milletler üyesi tüm egemen devletler ile de-facto tanınan kritik jeopolitik bölgeler dahil olmak üzere **tam 205 ülkeyi ve bölgeyi** analiz kapsamına alır.

---

## 🛡️ DOĞRULAMA STANDARDI: ADMİRALTY CODE (B2+)

Bu repoda yer alan tüm iddialar, NATO / Admiralty Kod doğrulama standardına göre derecelendirilmiştir. Minimum kabul eşiğimiz **B2** düzeyidir:

* **Kaynak Güvenilirliği (B):** Genellikle güvenilir (Resmi belgeler, araştırma komisyonu raporları, uluslararası denetim sızıntıları, ICIJ, OCCRP verileri).
* **Bilgi Doğruluğu (2):** Muhtemelen doğru (En az iki bağımsız açık kaynak ve çapraz lojistik/finansal veriyle teyit edilmiş).

---

## 🗺️ 205 ÜLKELİK KÜRESEL ATLAS İNDEKSİ

Aşağıdaki tabloda projedeki tüm bağımsız ülkeler listelenmiştir. Her bağlantı doğrudan **proje ana dizinindeki** ilgili ülkenin detaylı istihbarat profiline yönlendirir:

| Ülke | Bölge | ISO | Başkent | Rapor Bağlantısı | GSYİH (USD) | Kayıt Dışı (%) |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: |
{atlas_table_md}

---

## 🛠️ CLI İLE KULLANIM

Projeyi komut satırından hızlıca sorgulamak için `scripts/xray_cli.py` aracını kullanabilirsiniz:

```bash
# Türkiye profilini terminalde aç
python scripts/xray_cli.py turkey

# İki ülkeyi jeopolitik olarak karşılaştır
python scripts/xray_cli.py compare turkey iran

# Boğazlar ve transit koridorlarını incele
python scripts/xray_cli.py chokepoints

# Özel askeri şirketleri (PMC) listele
python scripts/xray_cli.py pmc

# Vaka analizlerini görüntüle
python scripts/xray_cli.py cases
```

## 🧪 BÜTÜNLÜK TESTLERİ

```bash
python tests/test_integrity.py
```

---

<p align="center">
  <b>Global X-Ray</b> &copy; 2026 &bull; <i>Hakikat, gizlenenlerin toplamıdır.</i>
</p>
"""

with open(BASE_DIR / "README.md", "w", encoding="utf-8") as f:
    f.write(master_readme_content.strip() + "\n")

print(f"[SUCCESS] Master README.md generated successfully! ({len(master_readme_content.splitlines())} lines)")
