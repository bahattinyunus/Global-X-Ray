# -*- coding: utf-8 -*-
"""
scripts/generate_master_readme.py
Generates the comprehensive, quote-rich, authoritative master README.md for Global-X-Ray.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 205 Ülke Verisini Yükle
with open(BASE_DIR / "global_datasets" / "countries_registry.json", encoding="utf-8") as f:
    countries = json.load(f)

# İstihbarat Teşkilatları Verisini Yükle
with open(BASE_DIR / "global_datasets" / "intelligence_agencies_registry.json", encoding="utf-8") as f:
    intel_registry = json.load(f)

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

master_readme_content = f"""# 🌍 KÜRESEL RÖNTGEN (GLOBAL X-RAY)
### *Açık Kaynak İstihbarat (OSINT), Derin Devlet Ağları, Oligarşik Sermaye & Kleptokrasi Haritalandırma Atlası*

<p align="center">
  <img src="https://img.shields.io/badge/OSINT-Standardized-red?style=for-the-badge&logo=target" alt="OSINT">
  <img src="https://img.shields.io/badge/Coverage-205%20Countries%20%26%20Entities-blue?style=for-the-badge&logo=globe" alt="Coverage">
  <img src="https://img.shields.io/badge/Architecture-4--Layer%20Deep%20State-black?style=for-the-badge" alt="4-Layer">
  <img src="https://img.shields.io/badge/Research%20Dossiers-8%20Deep%20Investigations-gold?style=for-the-badge" alt="Dossiers">
  <img src="https://img.shields.io/badge/Verification-Admiralty%20Code%20B2+-success?style=for-the-badge" alt="Verification">
  <img src="https://img.shields.io/badge/Global%20GDP-$105.5%20Trillion-green?style=for-the-badge" alt="Global GDP">
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

> *"Koyun sürüsünü andıran şaşkın kitlelerin tepişmesinden ve kükremesinden uzak, huzurlu bir düzen için kamuoyu özel sınıf tarafından yönlendirilmelidir."*  
> — **Walter Lippmann** (*Public Opinion*, 1922)

> *"Evrensel aldatmacanın hüküm sürdüğü dönemlerde hakikati söylemek devrimci bir eylemdir."*  
> — **George Orwell** (*1984*, 1949)

> *"Eğer savaşlar yalanlarla başlatılabiliyorsa, barış da gerçeklerle inşa edilebilir."*  
> — **Julian Assange** (WikiLeaks Kurucusu, 2011)

> *"Her yaptığımın ve her söylediğimin kaydedildiği bir dünyada yaşamak istemiyorum."*  
> — **Edward Snowden** (NSA Whistleblower, 2013)

> *"Hükümdar tuzakları tanımak için tilki, kurtları korkutmak için aslan olmak zorundadır."*  
> — **Niccolò Machiavelli** (*Il Principe*, 1532)

> *"İktidar yozlaştırır; mutlak iktidar ise mutlaka yozlaştırır."*  
> — **Lord Acton** (1887)

> *"Halkın çoğunluğu küçük bir yalandan ziyade büyük bir yalana çok daha kolay inanır."*  
> — **OSS Psikolojik Analiz Raporu** (1943)

> *"Bir toplulukta yağma bir grup insan için bir yaşam biçimi haline geldiğinde, zaman içinde kendilerine bunu meşrulaştıran bir hukuk sistemi ve bunu yücelten bir ahlak kodu inşa ederler."*  
> — **Frédéric Bastiat** (*Economic Sophisms*, 1845)

> *"Denizlere hükmeden ticarete hükmeder; ticarete hükmeden dünyanın zenginliğine ve dolayısıyla dünyanın kendisine hükmeder."*  
> — **Sir Walter Raleigh** (1610)

> *"Petrolü kontrol ederseniz ulusları kontrol edersiniz; gıdayı kontrol ederseniz insanları kontrol edersiniz; parayı kontrol ederseniz dünyayı kontrol edersiniz."*  
> — **Henry Kissinger** (Reelpolitik Doktrini)

---

## 📚 DERİN ARAŞTIRMA VE İSTİHBARAT DOSYALARI (/research)

Bu araştırma külliyatı, projenin kuramsal omurgasını oluşturan 8 bağımsız, ansiklopedik inceleme dosyasından oluşur:

| Araştırma Dosyası | Tematik Alan | Kapsam & Temel Vurgular |
| :--- | :--- | :--- |
| 📑 [**THEORETICAL_FRAMEWORKS.md**](research/THEORETICAL_FRAMEWORKS.md) | Derin Devlet & Güç Seçkinleri Teorisi | C. Wright Mills (Güç Seçkinleri), Peter Dale Scott (Derin Politika), Carl Schmitt (İstisna Hali), Michael Glennon (İkili Devlet), Gladio ve Susurluk analizleri. |
| 💰 [**SHADOW_BANKING_AND_OFFSHORE_FLOWS.md**](research/SHADOW_BANKING_AND_OFFSHORE_FLOWS.md) | Küresel Kleptokrasi & Vergi Cennetleri | City of London, Delaware/Wyoming, İsviçre serbest limanları, Panama/Pandora Papers ifşaatları, Ticarete Dayalı Para Aklama (TBML) ve Mirror Trading. |
| 🧠 [**PROPAGANDA_AND_INFORMATION_WARFARE.md**](research/PROPAGANDA_AND_INFORMATION_WARFARE.md) | Bilişsel Savaş & Algoritmik Manipülasyon | Chomsky'nin 5 Filtreli Propaganda Modeli, Operation Mockingbird, KGB Aktif Tedbirler (Maskirovka), Pegasus ve Predator casus yazılım ekosistemleri. |
| 🚢 [**GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md**](research/GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md) | Jeopolitik Darboğazlar & Deniz Hakimiyeti | Hürmüz, Malakka, Babülmendep, Süveyş, Panama; denizaltı fiber optik kabloları ve SIGINT dinleme istasyonları, INSTC ve Kuşak-Yol koridorları. |
| ⚔️ [**MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md**](research/MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md) | Askeri-Endüstriyel Kompleks & Paralı Askerler | Savunma ihale kartelleri (Demir Üçgen), Döner Kapı mekanizması, Özel Askeri Şirketler (Wagner, Blackwater, Sadat), yapay zeka güdümlü algoritmik harp. |
| 🕵️ [**INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md**](research/INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md) | İstihbarat Teşkilatları & Örtülü Operasyonlar | Operation Ajax (1953), Condor Planı, Church Komitesi ifşaatları, Five Eyes (FVEY) paktı ve karşılıklı yasal boşluktan yararlanma mimarisi. |
| ⛏️ [**RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md**](research/RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md) | Kritik Madenler & Emtia Kartelleri | Lityum üçgeni, Kongo Kobalt tekeli, Glencore/Trafigura/Vitol İsviçre emtia oligopolü, 1974 Petrodolar paktı ve Petroyuan geçişi. |
| 🔓 [**WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md**](research/WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md) | İfşaatçılar, Kriptografi & Adli Standartlar | Pentagon Belgeleri'nden Vault 7'ye sızıntı analizi, metadata adli bilişimi, renkli yazıcı sarı nokta takibi ve Admiralty Kod (B2+) doğrulama standardı. |

---

## 🕵️ KÜRESEL İSTİHBARAT TEŞKİLATLARI & GÜÇ MİMARİSİ

Proje kapsamında takip edilen başlıca küresel istihbarat servisleri ve resmi operasyonel sınıflandırmaları (`global_datasets/intelligence_agencies_registry.json`):

| Ülke | Dış İstihbarat (HUMINT) | Sinyal İstihbaratı (SIGINT) | İç Güvenlik / Karşı İstihbarat | Tahmini Yıllık Bütçe | Operasyonel Sınıflandırma |
| :--- | :--- | :--- | :--- | :--- | :--- |
{intel_table_md}

---

## 🌐 PROJE AMACI VE VİZYONU

**Küresel Röntgen (Global X-Ray)**, ulus devletlerin görünen resmi anayasal yapılarının ötesine geçerek; arka planda işleyen **derin güç odaklarını, askeri klikleri, istihbarat oligarşilerini, hanedan servetlerini, mafya-sermaye konsorsiyumlarını ve kayıt dışı para akışlarını** bilimsel ve doğrulanabilir OSINT (Open Source Intelligence) metodolojisi ile belgeleyen küresel bir araştırma ve istihbarat atlasıdır.

Proje, Birleşmiş Milletler üyesi tüm egemen devletler ile de-facto tanınan kritik jeopolitik bölgeler dahil olmak üzere **tam 205 ülkeyi ve bölgeyi** analiz kapsamına alır.

---

## 📐 ANALİTİK ÇERÇEVE: 4 KATMANLI DERİN DEVLET MODELİ

Her ülke klasörü, devlet mekanizmasını 4 temel anatomik katmana ayırarak analiz eder:

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

Gelişmekte olan ve otokratik ülkelerden batılı finans merkezlerine yönelen kayıt dışı servet transferinin anatomisi:

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

## 🛡️ DOĞRULAMA STANDARDI: ADMİRALTY CODE (B2+)

Bu repoda yer alan tüm iddialar, NATO / Admiralty Kod doğrulama standardına göre derecelendirilmiştir. Minimum kabul eşiğimiz **B2** düzeyidir:

* **Kaynak Güvenilirliği (B):** Genellikle güvenilir (Resmi belgeler, araştırma komisyonu raporları, uluslararası denetim sızıntıları, ICIJ, OCCRP verileri).
* **Bilgi Doğruluğu (2):** Muhtemelen doğru (En az iki bağımsız açık kaynak ve çapraz lojistik/finansal veriyle teyit edilmiş).

---

## 📊 KÜRESEL GÖSTERGELER & VERİ SETLERİ ÖZETİ

Repodaki `global_datasets/` klasörü altında tutulan standartlaştırılmış veriler:

| Gösterge | Kapsam | Kaynak Kurumlar / Metodoloji | Veri Yolu |
| :--- | :---: | :--- | :--- |
| **Kayıt Dışı Ekonomi İndeksi** | 205 Ülke | IMF, World Bank, Friedrich Schneider MIMIC Modeli | `global_datasets/global_shadow_economy.csv` |
| **Gerçek Basın Özgürlüğü** | 205 Ülke | RSF, CPJ, Gazeteci Cinayetleri ve Otosansür Skoru | `global_datasets/press_freedom_real_index.json` |
| **Vergi Cennetleri & Gizlilik** | 20 Merkez | Tax Justice Network Financial Secrecy Index (FSI) | `global_datasets/offshore_havens_matrix.csv` |
| **İstihbarat Teşkilatları** | 10 Güç | Sayıştaylar, İstihbarat Komisyonları, Savunma Bütçeleri | `global_datasets/intelligence_agencies_registry.json` |
| **Ülke Ana Sicili** | 205 Ülke | ISO-3166, Dünya Bankası WDI, Resmi Veriler | `global_datasets/countries_registry.json` |

---

## 🗺️ 205 ÜLKELİK KÜRESEL ATLAS İNDEKSİ

Aşağıdaki tabloda projedeki tüm bağımsız ülkeler alfabetik sırada listelenmiştir. Her bağlantı doğrudan **proje ana dizinindeki** ilgili ülkenin detaylı istihbarat profiline yönlendirir:

| Ülke | Bölge | ISO | Başkent | Rapor Bağlantısı | GSYİH (USD) | Kayıt Dışı (%) |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: |
{atlas_table_md}

---

## 🛠️ CLI İLE KULLANIM

Projeyi komut satırından hızlıca sorgulamak için `scripts/xray_cli.py` aracını kullanabilirsiniz:

```bash
# Türkiye profilini terminalde aç
python scripts/xray_cli.py turkey

# Almanya dosyasını incele
python scripts/xray_cli.py germany

# Tüm kayıtlı ülkeleri listele
python scripts/xray_cli.py --list
```

## 🧪 BÜTÜNLÜK TESTLERİ

Yapılan değişikliklerin ve 205 ülkenin doğruluğunu test etmek için:

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
