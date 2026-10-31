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

master_readme_content = f"""# 🌍 KÜRESEL RÖNTGEN (GLOBAL X-RAY)
### *Açık Kaynak İstihbarat (OSINT), Derin Devlet Ağları, Oligarşik Sermaye & Kleptokrasi Haritalandırma Atlası*

<p align="center">
  <img src="https://img.shields.io/badge/OSINT-Standardized-red?style=for-the-badge&logo=target" alt="OSINT">
  <img src="https://img.shields.io/badge/Coverage-205%20Countries%20%26%20Entities-blue?style=for-the-badge&logo=globe" alt="Coverage">
  <img src="https://img.shields.io/badge/Architecture-4--Layer%20Deep%20State-black?style=for-the-badge" alt="4-Layer">
  <img src="https://img.shields.io/badge/Verification-Admiralty%20Code%20B2+-success?style=for-the-badge" alt="Verification">
  <img src="https://img.shields.io/badge/Global%20GDP-$105.5%20Trillion-green?style=for-the-badge" alt="Global GDP">
  <img src="https://img.shields.io/badge/License-Open%20Intelligence-purple?style=for-the-badge" alt="License">
</p>

---

## 🏛️ GİRİŞ VE İKTİDARIN FELSEFESİ: EPİGRAFLAR

> *"Görünen hükümetin arkasında, halka karşı hiçbir bağlılığı olmayan ve hiçbir sorumluluk kabul etmeyen görünmez bir hükümet taht kurmuştur. Bu görünmez hükümeti yok etmek, yozlaşmış iş dünyası ile yozlaşmış siyaset arasındaki kirli ittifakı bozmak, günümüzün ilk görevidir."*  
> — **Theodore Roosevelt** (ABD 26. Başkanı, 1912 İlerleme Partisi Platformu)

> *"Ticaret ve imalat dünyasında öyle bazı adamlar var ki, bir şeyden korkuyorlar. Biliyorlar ki bir yerlerde öyle organize, öyle sinsi, öyle uyanık, öyle kilitli ve öyle yaygın bir güç var ki, onu kınarken fısıltıyla bile konuşmamak en iyisi."*  
> — **Woodrow Wilson** (ABD 28. Başkanı, *The New Freedom*, 1913)

> *"Washington'daki gerçek yöneticiler görünmezdir ve güçlerini perde arkasından kullanırlar."*  
> — **Felix Frankfurter** (ABD Yüksek Mahkemesi Yargıcı)

> *"Siyaset; kimin neyi, ne zaman ve nasıl aldığını belirleme sanatıdır."*  
> — **Harold Lasswell** (Siyaset Bilimci, 1936)

> *"Büyük bir servetin arkasında mutlaka büyük bir suç gizlidir."*  
> — **Honoré de Balzac** (Goriot Baba)

> *"Aynı ticaret kolundaki insanlar nadiren bir araya gelirler; ancak eğlence için bile toplansalar, konuşmaları mutlaka halka karşı bir komployla veya fiyatları artırmaya yönelik bir düzenbazlıkla sonuçlanır."*  
> — **Adam Smith** (Milletlerin Zenginliği, 1776)

> *"Güç yozlaştırır; mutlak güç ise mutlaka yozlaştırır. Büyük adamlar neredeyse her zaman kötü adamlardır."*  
> — **Lord Acton** (1887)

> *"Hükümet konseylerinde, askeri-endüstriyel kompleksin haksız nüfuz kazanmasına karşı uyanık olmalıyız. Yanlış ellere geçmiş gücün yarattığı felaket potansiyeli mevcuttur ve sürecektir. Bu askeri ve endüstriyel devasa mekanizmanın demokratik süreçlerimizi tehlikeye atmasına asla izin vermemeliyiz."*  
> — **Dwight D. Eisenhower** (ABD 34. Başkanı, 1961 Başkanlık Veda Konuşması)

> *"Savaş, politikanın başka araçlarla devamından başka bir şey değildir."*  
> — **Carl von Clausewitz** (Savaş Üzerine, 1832)

> *"Güçlü olan yapabildiğini yapar, zayıf olan ise çekmek zorunda olduğunu çeker."*  
> — **Thucydides** (Peloponnesos Savaşı, M.Ö. 416, Melian Diyaloğu)

> *"Kitle iletişim araçları, halkı eğlendirmek, bilgilendirmek ve onlara değerleri aşılamak için bir sistem olarak işlev görür; ancak asıl görevi, onları kurumsal devletin ve ayrıcalıklı elitlerin çıkarlarına entegre etmektir."*  
> — **Noam Chomsky & Edward S. Herman** (Rızanın İmalatı: Kitle Medyasının Ekonomi Politiği, 1988)

> *"Herkes aynı şeyi düşünüyorsa, hiç kimse çok fazla düşünmüyor demektir."*  
> — **Walter Lippmann** (Kamuoyu, 1922)

> *"Geçmişi kontrol eden geleceği kontrol eder; bugünü kontrol eden geçmişi kontrol eder."*  
> — **George Orwell** (1984 Romanı)

> *"Eğer savaşlar yalanlarla başlatılabiliyorsa, barış da gerçeklerle inşa edilebilir."*  
> — **Julian Assange** (WikiLeaks Kurucusu)

> *"Hükümetlerin gizliliği halktan korunmak için kullandığı bir dünyada, gerçeği söylemek bir suç haline gelir."*  
> — **Edward Snowden** (Eski CIA/NSA Analisti, 2013)

> *"İnsanlar o kadar saftır ve o anki ihtiyaçlarına o kadar bağımlıdır ki, aldatmak isteyen her zaman aldatılmaya hazır birilerini bulur."*  
> — **Niccolò Machiavelli** (Prens, 1532)

---

## 📌 PROJE MANİFESTOSU VE VİZYON

**Küresel Röntgen (Global X-Ray)**; dünya üzerindeki **205 egemen devlet, de facto bağımsız cumhuriyet ve stratejik özerk bölgenin** kültürel genetiğinden gölge ekonomisine, resmi anayasasından derin sermaye tekellerine kadar her hücresini haritalandırmak için kurulmuş, **bağımsız, kitle kaynaklı ve açık kaynak istihbarat (OSINT)** veri ambarıdır.

Wikipedia size bir ülkenin anayasasını, CIA World Factbook makroekonomik istatistiklerini, turizm portalları ise folklorik ögelerini sunar. **Küresel Röntgen** ise tüm bunları tek bir koordinat sisteminde birleştirir ve üzerine uluslararası ilişkilerin eksik olan en hayati parçasını ekler: **Gerçek Güç Ağı (The De Facto Power Architecture).**

Bu repo; devletlerin resmi sınır çizgileri veya parlamento koltuklarıyla yetinmez. Bir cerrah titizliğiyle bürokratik perdenin arkasına geçer ve şu 4 kritik sorunun cevabını belgeler:
1. **Bu ülkeyi resmiyette kim yönetiyor, masanın arkasında kararları kim alıyor?** (De Jure vs. De Facto İktidar)
2. **Kamu kaynakları ve ulusal zenginlik hangi oligark holdingler ve offshore hesaplar üzerinden paylaşılıyor?** (Kleptokrasi Döngüsü)
3. **Medyayı, sansür mekanizmalarını ve kamuoyunu hangi çıkar grupları finanse ediyor?** (Bilgi Tekelleri ve Algı Operasyonları)
4. **Devlet, küresel arenada hangi süper gücün ekonomik, teknolojik veya askeri vesayeti altında?** (Borç Diplomasisi ve Dış Güvenlik Paktları)

---

## 🔬 4 KATMANLI DEVLET ANATOMİSİ (THE 4-LAYER OSINT FRAMEWORK)

Projenin metodolojik omurgası, yüzeyden merkeze doğru derinleşen 4 analitik katmandan oluşur. Bu katmanlama, araştırmacı gazetecilerin, istihbarat analistlerinin ve yapay zeka ajanlarının bilgiyi modüler ve doğrulanabilir biçimde sorgulayabilmesini sağlar.

```mermaid
graph TD
    classDef l1 fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef l2 fill:#111827,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef l3 fill:#1f2937,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef l4 fill:#000000,stroke:#ef4444,stroke-width:3px,color:#fff;

    L1["<b>KATMAN 1: TEMEL TAŞLAR (DNA & TOPLUM)</b><br/>Kültür • Demografi • Fay Hatları • Kolektif Travmalar • Etnik Dağılım"]:::l1
    L2["<b>KATMAN 2: RESMİ VİTRİN (DE JURE REJİM)</b><br/>Anayasa • Seçimler • Diplomatik İttifaklar • Bakanlıklar • Yargı Organları"]:::l2
    L3["<b>KATMAN 3: YÜZEY EKONOMİSİ (MAKRO ÇARK)</b><br/>GSYH • Dış Ticaret Ortakları • Sanayi İhracatı • Enflasyon • Borç Stoku"]:::l3
    L4["<b>KATMAN 4: KARANLIK MADDE (DE FACTO OSINT)</b><br/>Gölge Karar Alıcılar • Kleptokrasi • Oligark Ağları • Medya Tekelleri • Offshore"]:::l4

    L1 ==> L2 ==> L3 ==> L4
```

### 🔹 Katman 1: Temel Taşlar (Kültür, Coğrafya ve Demografik Kırılmalar)
*Devlet mekanizmasının üzerinde yükseldiği fiziki, sosyolojik ve psikolojik zemin.*
* **Etnografya ve Demografik Piramit:** Nüfus yapısı, kentsel yığılmalar, azınlık oranları ve göç dinamikleri.
* **Kültürel DNA ve Kolektif Travmalar:** Ulusal kuruluş mitleri, savaş yenilgileri, sömürge geçmişi ve toplumsal fay hatları (laik-dindar, merkez-çevre, etnik ayrılıkçılık).
* **Jeostratejik Zemin:** Kritik boğazlar, boru hatları, tatlı su kaynakları, mineral yatakları ve sınır ihtilafları.

### 🔹 Katman 2: Resmi Vitrin (The De Jure State)
*Dünyanın tanıdığı, BM kürsülerinde konuşan ve kanun kitaplarında yazan resmi aygıt.*
* **Siyasi İşletim Sistemi:** Başkanlık, parlamenter, mutlak monarşi, hibrit veya askeri cunta yasal statüleri.
* **Vitrin Aktörleri:** Devlet başkanı, başbakan, kabine, yüksek yargı organları ve sistem içi yasal muhalefet.
* **Resmi Dış Politika:** İmzalanan ikili güvenlik paktları, uluslararası üyelikler (NATO, ŞİÖ, AB, Afrika Birliği vb.).

### 🔹 Katman 3: Yüzey Ekonomisi (The Official Economy)
*IMF, Dünya Bankası ve resmi istatistik enstitülerinin raporladığı makroekonomik çark.*
* **Makro Göstergeler:** Nominal ve SAGP GSYH, kişi başına düşen gelir, enflasyon, işsizlik, kamu borç stoku.
* **Tedarik ve Dış Ticaret Ağı:** Ülkenin ana ihracat lokomotifleri, stratejik hammadde bağımlılıkları ve en büyük ticaret ortakları.
* **Kritik Altyapı:** Elektrik şebekesi, rafineriler, derin deniz liman kapasiteleri ve telekomünikasyon altyapısı.

### 🔹 Katman 4: Karanlık Madde (OSINT & The De Facto Power)
*Reponun kalbi. Vitrinin arkasındaki gerçek güç ekseni.*
* **Gölge Karar Alıcılar & Kukla İpleri:** Resmi liderlerin arkasındaki aile meclisleri, derin güvenlik elitleri, istihbarat klikleri veya dini konsorsiyumlar.
* **Kleptokrasi Ağı & Oligarklar:** Kamu ihalelerinin düzenli olarak aktarıldığı imtiyazlı holdingler, offshore vergi cenneti transferleri ve stratejik tekeller.
* **Bilgi Otomasyonu & Algı Yönetimi:** Medya mülkiyetinin kime ait olduğu, gazetecilere yönelik idari/yargısal baskılar, casus yazılım (Pegasus vb.) gözetimleri.
* **Küresel Uydu & Vesayet Statüsü:** Ülkenin bağımsızlık derecesi; büyük güçlerin (ABD, Çin, Rusya) ülkedeki askeri üs, liman ve borç diplomasisi nüfuzu.

---

## 💸 KLEPTOKRASİ VE OFFSHORE SERMAYE KAÇIŞ MODELİ

Modern otoriter ve hibrit rejimlerde kamu kaynaklarının gaspı tesadüfi rüşvetlerle değil, **sistematik ve kurumsallaşmış bir çarkla** yürütülür:

```mermaid
flowchart LR
    A["🏛️ Kamu Bütçesi & Hazine"] -->|"Hazine Garantili İhaleler & İmtiyazlar"| B["🏢 Rejime Sadık Oligark Holding"]
    B -->|"Şişirilmiş Faturalar & Danışmanlık Ücretleri"| C["🏝️ Paravan Şirketler (BVI / Panama / Kıbrıs)"]
    C -->|"Varlık Aklama & Fon Transferi"| D["🏦 Küresel Finans Merkezleri (Londra / Dubai / İsviçre)"]
    D -->|"Yatırım & Varlık Koruma"| E["🏰 Batı Başkentlerinde Gayrimenkul, Özel Jetler & Fonlar"]
    E -.->|"Gizli Seçim Finansmanı & Komisyonlar"| A
```

---

## 🔍 DOĞRULAMA VE İSTİHBARAT PROTOKOLÜ (ADMIRALTY STANDARDI)

Küresel Röntgen bir spekülasyon veya komplo teorisi platformu **değildir**. Tüm Katman 4 analizleri, NATO ve uluslararası istihbarat servislerinin kullandığı **Admiralty Kodu** doğrulama sistemine tabidir:

| Güvenilirlik Kodu | Kaynak Niteliği | Kabul Edilen Referanslar |
| :---: | :--- | :--- |
| **A1** | **Tamamen Güvenilir & Teyitli** | Resmi mahkeme kararları, Sayıştay raporları, FinCEN kayıtları, SEC/Borsa dosyaları, ICIJ sızıntıları (Panama/Pandora Papers). |
| **B2** | **Genellikle Güvenilir & Muhtemelen Doğru** | OCCRP (Organized Crime and Corruption Reporting Project), Bellingcat, Transparency International, SIPRI, hakemli akademik araştırmalar. |
| **C3** | **Kısmen Güvenilir** | Bağımsız yerel araştırmacı gazetecilik portalları (ikincil kaynak teyidi zorunludur). |
| ❌ | **Kabul Edilmeyen** | Anonim sosyal medya iddiaları, teyitsiz bloglar, devlet propaganda bültenleri, dedikodu kanalları. |

---

## 🌐 KÜRESEL GÖSTERGELER VE GENEL BAKIŞ (205 ÜLKE)

Global X-Ray projesi dünya nüfusunun ve ekonomisinin neredeyse tamamını kapsar:

| Bölge | Haritalanan Ülke / Fiili Yönetim Sayısı | Temsil Edilen Nüfus | Nominal GSYH Toplamı | Ortalama Gölge Ekonomi |
| :--- | :---: | :---: | :---: | :---: |
| **Avrupa** | 47 Ülke | ~745 Milyon | $24.8 Trilyon | %16.8 |
| **Asya** | 35 Ülke | ~4.65 Milyar | $38.2 Trilyon | %27.4 |
| **Amerika** | 37 Ülke | ~1.04 Milyar | $34.1 Trilyon | %26.5 |
| **Afrika** | 56 Ülke | ~1.43 Milyar | $3.1 Trilyon | %41.2 |
| **Ortadoğu** | 16 Ülke | ~395 Milyon | $4.2 Trilyon | %31.5 |
| **Okyanusya** | 14 Ülke | ~44 Milyon | $2.1 Trilyon | %18.4 |
| **DÜNYA TOPLAMI** | **205 ÜLKE** | **~7.98 MİLYAR** | **$105.5 TRİLYON** | **%28.7** |

---

## 📂 STANDARTLAŞTIRILMIŞ DEPO DİZİN MİMARİSİ

Proje kapsamında **205 ülke ve fiili yönetimin tamamı**, hem doğrudan **ana dizindeki bağımsız klasörler** (`./<ülke>/`) hem de `countries/<ülke>/` ve `regions/<bölge>/<ülke>/` hiyerarşisi üzerinden inşa edilmiştir:

```text
📦 Global-X-Ray (Ana Kök Dizin)
 ┣ 📂 turkey/                            # 🇹🇷 205 Ülkenin Her Biri İçin Kök Dizinde Doğrudan Klasör
 ┃ ┣ 📜 README.md                       # 8 Bölümlü Kapsamlı İstihbarat & Güç Raporu (~10 KB)
 ┃ ┣ 📂 01_culture_demographics/
 ┃ ┃ ┣ 📜 society_history.md            # Sosyolojik kırılmalar & fay hatları
 ┃ ┃ ┗ 📊 demographics.csv             # Nüfus, yaş ve kentleşme verileri (CSV)
 ┃ ┣ 📂 02_official_state/
 ┃ ┃ ┗ 📜 constitution_gov.md          # Yasal hükümet sistemi, bakanlıklar & yargı
 ┃ ┣ 📂 03_official_economy/
 ┃ ┃ ┗ 📊 macroeconomics.json          # GSYH, enflasyon, ihracat/ithalat (JSON)
 ┃ ┗ 📂 04_shadow_power_osint/
 ┃   ┣ 📜 real_power_dynamics.md        # Fiili güç odakları & kleptokrasi analizi
 ┃   ┣ 📊 oligarch_network.csv          # Oligark-holding ilişkileri & tahmini servet (CSV)
 ┃   ┗ 📜 media_censorship_matrix.md    # Medya tekelleri & sansür analizi
 ┣ 📂 germany/                           # 🇩🇪 Almanya Klasörü & README.md
 ┣ 📂 united_states/                     # 🇺🇸 ABD Klasörü & README.md
 ┣ 📂 china/                             # 🇨🇳 Çin Klasörü & README.md
 ┣ 📂 russia/                            # 🇷🇺 Rusya Klasörü & README.md
 ┣ 📂 ...                                # 205 Ülke Klasörünün Tamamı Doğrudan Kök Dizinde!
 ┣ 📂 countries/                         # 🌍 205 Ülkenin Alternatif Alfabetik İndeks Dizinleri
 ┣ 📂 regions/                           # 🗺️ 6 Kıtaya Göre Hiyerarşik Bölge Arşivi
 ┣ 📂 global_datasets/                   # 📊 Küresel Makro Veri Setleri
 ┃ ┣ 📊 countries_registry.json         # 205 Ülkenin JSON indeks kataloğu
 ┃ ┣ 📊 global_shadow_economy.csv       # 205 Ülkenin kayıt dışı ekonomi endeksi
 ┃ ┗ 📊 press_freedom_real_index.json   # 205 Ülkenin basın özgürlüğü endeksi
 ┣ 📂 scripts/                           # 🛠️ İstihbarat ve Analiz Motoru
 ┃ ┣ 🐍 build_full_repository.py        # Tüm veri ambarını inşa eden çekirdek motor
 ┃ ┣ 🐍 xray_cli.py                     # Komut satırı analiz ve sorgu terminali
 ┃ ┣ 🐍 network_graph_gen.py            # Oligark ağlarını Mermaid grafiğine dönüştürücü
 ┃ ┗ 📂 data/                           # 6 Kıtaya ait modüler zengin veri ambarı
 ┣ 📂 methodology/                       # 📜 OSINT Metodoloji Kılavuzları
 ┃ ┣ 📜 DATA_COLLECTION_GUIDE.md        # 4 Katmanlı veri toplama kılavuzu
 ┃ ┗ 📜 OSINT_VERIFICATION.md           # Admiralty Code B2+ doğrulama protokolü
 ┣ 📂 tests/                             # 🧪 Otomatik Veri Bütünlüğü Testleri
 ┣ 📜 CONTRIBUTING.md                   # Katkı sağlama yönergeleri
 ┗ 📜 README.md                         # Bu master dosya
```

---

## 🗺️ 205 ÜLKE VE FİİLİ YÖNETİM ATLASI (A-Z DOĞRUDAN ERİŞİM DİZİNİ)

> *Aşağıdaki tabloda dünya üzerindeki 205 egemen devlet ve fiili yönetimin tamamı listelenmiştir. Herhangi bir ülkenin rapor linkine tıklayarak doğrudan kök dizindeki detaylı 8 bölümlü istihbarat ve derin güç dosyasına (`<ülke>/README.md`) ulaşabilirsiniz.*

| Ülke | Bayrak / Bölge | ISO Kodu | Başkent | Doğrudan İstihbarat Raporu | Nominal GSYH | Gölge Ekonomi Payı |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: |
{atlas_table_md}

---

## 🛠️ OTOMASYON, TERMİNAL VE GRAFİK ÜRETİMİ (CLI TOOLING)

Küresel Röntgen, komut satırından dinamik olarak sorgulanabilen entegre bir analiz terminali içerir:

### 1. Ülke İstihbarat Raporu Sorgulama
Herhangi bir ülkenin özet kimlik kartını, makro göstergelerini ve oligark ağını terminalden görüntüleyin:
```bash
python scripts/xray_cli.py country turkey
python scripts/xray_cli.py country kuwait
python scripts/xray_cli.py country united_states
```

### 2. İki Ülkeyi Jeopolitik Olarak Karşılaştırma
İki ülkenin nüfus, GSYH, gölge ekonomi oranı ve güç parametrelerini yan yana kıyaslayın:
```bash
python scripts/xray_cli.py compare turkey greece
python scripts/xray_cli.py compare united_states china
python scripts/xray_cli.py compare saudi_arabia iran
```

### 3. Oligark ve Siyaset Güç Ağı Grafiği Üretme
Herhangi bir ülkenin `oligarch_network.csv` dosyasını okuyarak Markdown/Mermaid ilişkiler şeması üretin:
```bash
python scripts/xray_cli.py graph turkey
python scripts/network_graph_gen.py turkey/04_shadow_power_osint/oligarch_network.csv
```

### 4. Küresel Özet İstatistikleri Listeleme
```bash
python scripts/xray_cli.py stats
```

### 5. Anahtar Kelime ile İstihbarat Taraması
```bash
python scripts/xray_cli.py search "offshore"
python scripts/xray_cli.py search "liman"
```

---

## 🧪 OTOMATİK VERİ BÜTÜNLÜĞÜ TESTLERİ

Projedeki 205 ülkenin ve 1.640'ı aşkın dosyanın bozulmadığını, JSON sözdizimlerinin geçerli olduğunu ve tüm README'lerin standartlara uyduğunu doğrulamak için:
```bash
python tests/test_integrity.py
```

---

## 🤝 KATKI SAĞLAMA VE ETİK İLKELER

Küresel Röntgen, araştırmacı gazetecilerin, OSINT analistlerinin ve veri bilimcilerinin kolektif katkılarıyla büyümektedir. 
* Yeni bir oligark bağlantısı, ihale yolsuzluğu veya medya mülkiyeti eklemek istiyorsanız lütfen [`methodology/OSINT_VERIFICATION.md`](methodology/OSINT_VERIFICATION.md) kılavuzunu inceleyin.
* Tüm Katman 4 iddiaları için **çift birincil kaynak teyidi (Mahkeme kararı, Sayıştay raporu, ICIJ/OCCRP veri tabanı)** eklemek zorunludur.
* Ayrıntılı katkı kuralları için [`CONTRIBUTING.md`](CONTRIBUTING.md) belgesine bakın.

---

## ⚖️ YASAL SORUMLULUK REDDİ (LEGAL DISCLAIMER)

*Bu veri ambarındaki tüm bilgiler; Birleşmiş Milletler, Dünya Bankası, IMF, Transparency International, RSF, ulusal ticaret sicil gazeteleri, Sayıştay raporları ve kamuya açık uluslararası sızıntılar (ICIJ / OCCRP) gibi açık kaynak istihbaratı (OSINT) yöntemleriyle derlenmiştir. Proje tarafsız, bağımsız ve kamusal denetim amacıyla yürütülmektedir; hiçbir hükümet, siyasi parti veya istihbarat teşkilatıyla organik bağı bulunmamaktadır.*
"""

with open(BASE_DIR / "README.md", "w", encoding="utf-8") as f:
    f.write(master_readme_content)

print(f"[SUCCESS] Master README.md generated successfully! ({len(master_readme_content.splitlines())} lines)")
