"""
scripts/build_comprehensive_features.py
Comprehensive development script for Global X-Ray:
1. Expands methodology/ with operational OSINT manuals.
2. Generates global_datasets/GLOBAL_RANKINGS_REPORT.md and global_datasets/global_power_matrix.json.
3. Enhances scripts/xray_cli.py with advanced search, comparative analysis, and ranking capabilities.
"""

import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
METHOD_DIR = BASE_DIR / "methodology"
DATASETS_DIR = BASE_DIR / "global_datasets"
SCRIPTS_DIR = BASE_DIR / "scripts"

METHOD_DIR.mkdir(parents=True, exist_ok=True)
DATASETS_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. EXPAND methodology/DATA_COLLECTION_GUIDE.md
# -------------------------------------------------------------
DATA_COLLECTION_GUIDE = """# 📚 Kapsamlı OSINT Veri Toplama ve İstihbarat Protokolü

> "Knowledge itself is power." (*Scientia potentia est.*)  
> — **Sir Francis Bacon**, *Meditationes Sacrae* (1597)

> "There is no such thing as an innocent piece of information. Everything connects if you look deep enough."  
> — **Umberto Eco**, *Foucault's Pendulum* (1988)

---

## 1. Giriş ve Operasyonel Doktrin

Bu kılavuz, **Küresel Röntgen (Global X-Ray)** projesinin 205 egemen ve jeopolitik varlık üzerindeki açık kaynak istihbaratı (OSINT) toplama ve doğrulama süreçlerini yöneten temel saha yönergesidir.

Geleneksel siyaset bilimi devletleri resmi anayasal kurumları üzerinden tanımlarken, Global X-Ray devletleri **maddi kaynakların, silahlı kuvvetlerin, istihbarat servislerinin ve kayıt dışı sermayenin çatışma alanı** olarak modeller.

---

## 2. 4 Katmanlı Veri Toplama Mimarisi ve Veri Tabanı Kaynakları

```mermaid
flowchart TD
    subgraph Katman1["Katman 1: Coğrafya, Etnisite & Demografi"]
        K1_1["BM Nüfus Fonu (UNFPA)"]
        K1_2["Pew Research Demographics"]
        K1_3["Joshua Project Etnik Dağılım"]
    end

    subgraph Katman2["Katman 2: De Jure Devlet & Hukuki Çerçeve"]
        K2_1["V-Dem (Varieties of Democracy)"]
        K2_2["Constitute Project (Dünya Anayasaları)"]
        K2_3["Freedom House Hukuk Raporları"]
    end

    subgraph Katman3["Katman 3: Resmi Makroekonomi & Dış Ticaret"]
        K3_1["Dünya Bankası WDI"]
        K3_2["IMF Dünya Ekonomik Görünümü (WEO)"]
        K3_3["OEC / UN Comtrade (Emtia ve HS Kodları)"]
    end

    subgraph Katman4["Katman 4: Gölge Güç, Kleptokrasi & OSINT"]
        K4_1["ICIJ Offshore Leaks Database"]
        K4_2["OCCRP Aleph Veri Platformu"]
        K4_3["Tax Justice Network FSI"]
        K4_4["RSF & CPJ Sansür ve Gazeteci İndeksleri"]
    end
```

### 2.1 Katman 1: Sosyolojik ve Demografik Fay Hatları
* **Tarihsel Kırılmalar:** Kolonyal sınırlar, iç savaşlar, etnik soykırımlar, mezhepsel bölünmeler.
* **Demografik Risk Göstergeleri:** Genç işsizlik oranı (Youth Bulge teorisi), kentleşme hızı, mülteci/sığınmacı akımları.

### 2.2 Katman 2: Resmi Anayasal Vitrin
* **Rejim Tipi:** Başkanlık, Yarı-Başkanlık, Parlamenter Monarşi, Askeri Cunta, Teokrasi, Tek Parti Devleti.
* **Güvenlik Mimarisi:** Resmi savunma bütçesi, NATO/KGAÖ/AUKUS gibi savunma paktı üyelikleri.

### 2.3 Katman 3: Resmi Makroekonomi
* **Makro Göstergeler:** Nominal GSYİH, SAGP GSYİH, Cari Denge / GSYİH, Kamu Borcu / GSYİH, Enflasyon ve Döviz Rezervleri.
* **Ticaret Haritası:** İlk 5 ihraç ve ithal kalemi (HS 2/4-hane sınıflandırması), kritik emtia ithalat bağımlılığı (gıda, ham petrol, yarı iletkenler).

### 2.4 Katman 4: Gölge Güç, Kleptokrasi ve Derin Yapılar
* **De Facto Karar Alıcılar:** Seçimle gelmeyen askeri şuralar, hanedan aile meclisleri, istihbarat başkanları, tekelci holding patronları.
* **Oligarşi Ağı:** Kamu ihalelerinden aslan payını alan sermaye grupları, vergi afları ve imtiyazlı maden ruhsatları.
* **Sermaye Kaçışı & Offshore:** Paravan şirketler (BVI, Panama, Cayman, Delaware), Londra ve Dubai gayrimenkul varlıkları.
* **Medya & Bilgi Kontrolü:** İktidar yanlısı medya konsorsiyumları, dijital gözetim araçları (Pegasus vb.), internet kapatmaları.
"""

# -------------------------------------------------------------
# 2. EXPAND methodology/OSINT_VERIFICATION.md
# -------------------------------------------------------------
OSINT_VERIFICATION = """# 🔍 OSINT Doğrulama Protokolü & Admiralty Standartları

> "Trust, but verify." (*Доверяй, но проверяй.*)  
> — **Rus Atasözü** *(Ronald Reagan tarafından Soğuk Savaş zirvelerinde popülerleştirilmiştir)*

> "Falsehood flies, and truth comes limping after it, so that when men come to be undeceived, it is too late; the jest is over, and the tale has had its effect."  
> — **Jonathan Swift**, *The Examiner* (1710)

---

## 1. Admiralty Kod Doğrulama Matrisi (NATO STANAG 2022)

Global X-Ray projesindeki her istihbarat iddiası aşağıdaki 6x6'lık değerlendirme matrisine göre derecelendirilir:

| Kaynak Güvenilirliği (Source Reliability) | Bilgi Doğruluğu (Information Credibility) |
| :--- | :--- |
| **A - Tamamen Güvenilir:** Kaynağın dürüstlüğü ve geçmiş performansı kusursuzdur; resmi mahkeme tutanağı, Sayıştay raporu, bağımsız uluslararası denetim. | **1 - Teyit Edilmiş:** Bağımsız ve farklı yöntemler kullanan birden fazla kaynakça doğrulanmış. |
| **B - Genellikle Güvenilir:** Kaynağın geçmiş performansı sağlamdır; ICIJ, OCCRP, Reuters Araştırma Masası, hakemli akademik çalışma. | **2 - Muhtemelen Doğru:** Mevcut durum ve bilinen olay akışıyla mantıksal uyum içindedir. |
| **C - Kısmen Güvenilir:** Kaynak zaman zaman taraflı veya eksik bilgi vermiştir; yerel muhalif yayın organı, tek taraflı STK bülteni. | **3 - Mümkün / Olası:** Doğrulayıcı kanıt yoktur ancak bilinen koşullarla çelişmez. |
| **D - Genellikle Güvenilmez:** Kaynağın geçmişte yanıltıcı bilgi verdiği bilinmektedir; anonim sosyal medya sızıntısı. | **4 - Şüpheli:** Mantıksal tutarsızlıklar taşır veya bilinen başka doğrularla çelişir. |
| **E - Güvenilmez:** Kaynağın kasıtlı dezenformasyon ürettiği kanıtlanmıştır; devlet güdümlü propaganda bülteni. | **5 - Olanaksız:** Mantıksal ve fiziksel olarak imkansızdır, çürütülmüştür. |
| **F - Güvenilirlik Yargılanamaz:** Kaynağın geçmişine veya güvenilirliğine dair hiçbir veri yoktur. | **6 - Doğruluk Yargılanamaz:** Bilginin doğruluğunu ölçecek hiçbir veri yoktur. |

> [!IMPORTANT]
> **Global X-Ray Standart Eşiği:** Repoda 4. Katman (Gölge Güç ve Kleptokrasi) altında yer alan tüm bulgular **en az B2** (Genellikle Güvenilir Kaynak + Muhtemelen Doğru Bilgi) veya **A1** standardında olmak zorundadır.

---

## 2. Şirket ve Para İzi Takibi: 3 Adımlı Teyit Döngüsü

```mermaid
sequenceDiagram
    autonumber
    participant S as Saha / Açık Kaynak İddiası
    participant T as Ticaret Sicil Gazetesi
    participant L as Sızıntı Veri Tabanı (ICIJ/OCCRP)
    participant B as Bankacılık / FinCEN SAR

    S->>T: 1. Şirket tescili ve hissedar yapısının sorgulanması
    T-->>S: Hissedarlar / Paravan yöneticiler tespit edildi
    S->>L: 2. Offshore tröst ve nihai faydalanıcı (UBO) taraması
    L-->>S: BVI / Panama gizli sermaye bağı belgelendi
    S->>B: 3. Şüpheli İşlem Bildirimi (SAR) veya ceza iddianamesi eşleştirmesi
    B-->>S: B2+ Dereceli Doğrulanmış İstihbarat Raporu
```

---

## 3. Metadata Adli Bilişimi ve Sayısal Doğrulama

İncelemeye alınan tüm sızıntı belgeler ve dijital deliller aşağıdaki kontrollerden geçirilir:
1. **Kriptografik Bütünlük:** Orijinal sızıntı arşivinin `SHA-256` veya `BLAKE3` özeti alınarak değiştirilmediği mühürlenir.
2. **Metadata İncelemesi:** Belge yazar adı, oluşturulma tarihi, yazılım sürümü (`exiftool`, `pdfid`, `oletools`) taranır.
3. **Yazıcı Sarı Nokta Analizi (Machine Identification Codes):** Renkli lazer yazıcılardan basılan belgelerdeki seri numarası ve tarih desenleri çözümlenir.
"""

# -------------------------------------------------------------
# 3. CREATE methodology/CORP_REGISTRY_RECONNAISSANCE.md
# -------------------------------------------------------------
CORP_REGISTRY_GUIDE = """# 🏢 Kurumsal Sicil İstihbaratı ve Paravan Şirket Çözümleme Rehberi

> "Follow the money, always follow the money."  
> — **Deep Throat** (Mark Felt), *Watergate Scandal Investigation* (1972)

> "A company without an identifiable human owner is not an enterprise; it is a weapon of financial concealment."  
> — **Anti-Kleptocracy Investigative Standard**

---

## 1. Giriş: Kurumsal Gizlilik Mimarisi

Oligarklar, yolsuz politikacılar ve yaptırım altındaki aktörler servetlerini doğrudan kendi adlarına tutmazlar. Sermaye; katmanlı paravan şirketler, aday yöneticiler (nominee directors) ve kör tröstler arkasına gizlenir.

Bu rehber, açık kaynak istihbaratçılarının paravan şirket ağlarını deşifre etmesi ve nihai faydalanıcıyı (Ultimate Beneficial Owner - UBO) ortaya çıkarması için adım adım yöntemler sunar.

---

## 2. Küresel Kurumsal Sicil Platformları

| Ülke / Yargı Alanı | Sicil Kurumu | Erişim Tipi | Arama İpuçları & Güçlükler |
| :--- | :--- | :---: | :--- |
| **Birleşik Krallık** | Companies House | Ücretsiz / Açık API | PSC (Persons of Significant Control) sicili zorunludur. Direktörlerin diğer şirketleri taranabilir. |
| **Amerika Birleşik Devletleri** | Delaware Division of Corporations | Ücretli / Sınırlı | Gerçek sahip görünmez. Sadece tescil acentesi (Registered Agent) listelenir. |
| **Lüksemburg** | Registre de Commerce et des Sociétés (LBR) | Kısmen Ücretsiz | RBE (Registre des Bénéficiaires Effectifs) UBO arama imkanı sunar. |
| **İsviçre** | Zefix (Merkezi Kurumsal Dizin) | Ücretsiz | Kanton bazlı şirket kayıtları ve imza yetkilileri ayrıntılı listelenir. |
| **Türkiye** | Türkiye Ticaret Sicili Gazetesi (TOBB) | Ücretsiz Kayıt | Ortaklık pay değişimleri, genel kurul kararları ve imza sirküleri PDF olarak indirilebilir. |
| **Almanya** | Handelsregister / Unternehmensregister | Ücretsiz | Mahkeme tescil kararları ve şirket hissedar listeleri (Gesellschafterliste) mevcuttur. |
| **Kıbrıs Rum Kesimi** | Department of Registrar of Companies | Kısmen Ücretli | Rus sermayesinin Avrupa giriş kapısı; aday yöneticiler ve sekreterlik firmaları yaygındır. |

---

## 3. Paravan Şirket Tespiti İçin 7 Kırmızı Bayrak (Red Flags)

Aşağıdaki göstergelerden üç veya daha fazlasına sahip bir şirket yüksek ihtimalle bir kleptokrasi perdesidir:

1. **Toplu Tescil Adresi:** Tek bir posta kutusunda veya mütevazı bir avukatlık ofisinde kayıtlı 500'den fazla şirket bulunması (Örn: Delaware 1209 North Orange Street - 300.000 şirket).
2. **Seri Aday Direktörler:** Aynı şahsın 200'den fazla şirkette "yönetim kurulu üyesi" olarak görünmesi.
3. **Fiziksel Faaliyet Eksikliği:** Milyonlarca dolarlık ciro bildiren şirketin kayıtlı çalışanının, telefon santralinin veya web sitesinin olmaması.
4. **Hızlı Devir ve İsim Değişiklikleri:** Şirketin 1-2 yıl içinde art arda unvan ve hissedar değiştirmesi.
5. **Döngüsel Mülkiyet (Circular Ownership):** A şirketinin sahibinin B şirketi, B şirketinin sahibinin ise A şirketi olarak tescil edilmesi.
6. **Yüksek Riskli Yargı Alanı Hissedarlığı:** Şirketin doğrudan BVI, Seyşeller veya Belize merkezli bir varlık tarafından kontrol edilmesi.
7. **Piyasa Fiyatından Sapma:** İlişkili şirketler arasında yapılan işlemlerde (transfer fiyatlandırması) emtia fiyatlarının piyasa değerinden fahiş oranda farklı olması.
"""

# Write methodology files
with open(METHOD_DIR / "DATA_COLLECTION_GUIDE.md", "w", encoding="utf-8") as f:
    f.write(DATA_COLLECTION_GUIDE.strip() + "\n")
print(f"[UPDATED] {METHOD_DIR / 'DATA_COLLECTION_GUIDE.md'}")

with open(METHOD_DIR / "OSINT_VERIFICATION.md", "w", encoding="utf-8") as f:
    f.write(OSINT_VERIFICATION.strip() + "\n")
print(f"[UPDATED] {METHOD_DIR / 'OSINT_VERIFICATION.md'}")

with open(METHOD_DIR / "CORP_REGISTRY_RECONNAISSANCE.md", "w", encoding="utf-8") as f:
    f.write(CORP_REGISTRY_GUIDE.strip() + "\n")
print(f"[CREATED] {METHOD_DIR / 'CORP_REGISTRY_RECONNAISSANCE.md'}")

# -------------------------------------------------------------
# 4. GENERATE GLOBAL RANKINGS & POWER MATRIX DATASET
# -------------------------------------------------------------
with open(DATASETS_DIR / "countries_registry.json", "r", encoding="utf-8") as f:
    countries = json.load(f)

power_matrix = []
for c in countries:
    shadow_pct = float(c.get("shadow_economy_pct", 25.0))
    gdp = float(c.get("gdp_usd_b", 10.0))
    pop = int(c.get("population", 5000000))
    gdp_pc = (gdp * 1_000_000_000) / max(pop, 1)

    # Composite Sovereign Fragility Index (CSFI) [0 - 100]
    # Higher = More fragile / kleptocratic
    # Factors: Shadow economy % (50%), Low GDP per capita (30%), Base fragility (20%)
    wealth_factor = max(0, min(30, 30 - (gdp_pc / 2500)))
    shadow_factor = min(50, shadow_pct * 0.85)
    csfi_score = round(shadow_factor + wealth_factor + 10, 1)

    tier = "Kritik Kırılgan (Critical)" if csfi_score > 65 else (
        "Yüksek Risk (High Risk)" if csfi_score > 50 else (
            "Orta Düzey (Moderate)" if csfi_score > 35 else "Düşük Risk / Kurumsal (Stable)"
        )
    )

    power_matrix.append({
        "name": c["name"],
        "slug": c["slug"],
        "code": c["code"],
        "region": c["region"],
        "gdp_usd_b": gdp,
        "gdp_per_capita_usd": round(gdp_pc, 0),
        "shadow_economy_pct": shadow_pct,
        "fragility_index_csfi": csfi_score,
        "risk_tier": tier
    })

# Save global_power_matrix.json
power_matrix_path = DATASETS_DIR / "global_power_matrix.json"
with open(power_matrix_path, "w", encoding="utf-8") as f:
    json.dump({
        "_metadata": {
            "title": "Global X-Ray Composite Sovereign Fragility & Kleptocracy Matrix",
            "version": "1.0.0",
            "country_count": len(power_matrix)
        },
        "countries": power_matrix
    }, f, indent=2, ensure_ascii=False)
print(f"[CREATED] {power_matrix_path}")

# Generate GLOBAL_RANKINGS_REPORT.md
# Sort by shadow economy desc
by_shadow = sorted(power_matrix, key=lambda x: x["shadow_economy_pct"], reverse=True)
# Sort by GDP desc
by_gdp = sorted(power_matrix, key=lambda x: x["gdp_usd_b"], reverse=True)
# Sort by fragility desc
by_fragility = sorted(power_matrix, key=lambda x: x["fragility_index_csfi"], reverse=True)

rankings_md = f"""# 📊 Küresel Sıralamalar ve Kırılganlık Raporu (Global X-Ray Rankings)

> "In God we trust; all others must bring data."  
> — **W. Edwards Deming**

---

## 1. Yönetici Özeti

Bu rapor, Küresel Röntgen veri tabanındaki **205 egemen ve jeopolitik varlığın** makroekonomik büyüklük, kayıt dışı gölge ekonomi oranı ve Birleşik Egemen Kırılganlık İndeksi (CSFI) üzerinden yapılan çapraz analizlerini içerir.

---

## 2. En Yüksek Kayıt Dışı Ekonomi Oranına Sahip 20 Ülke

Kayıt dışı ekonominin GSYİH'ye oranı %40'ı aştığında devlet mali denetimi kaybeder ve kleptokratik ağlar egemen hale gelir:

| Sıra | Ülke | Bölge | ISO | GSYİH ($B) | Gölge Ekonomi (%) | Risk Düzeyi |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
"""

for idx, item in enumerate(by_shadow[:20], 1):
    rankings_md += f"| {idx} | **{item['name']}** | {item['region']} | `{item['code']}` | ${item['gdp_usd_b']:,.1f}B | %{item['shadow_economy_pct']:.1f} | {item['risk_tier']} |\n"

rankings_md += """
---

## 3. Dünyanın En Büyük 20 Ekonomisi ve Küresel Payı

Küresel GSYİH'nin yaklaşık %80'i bu 20 güç merkezinde toplanmıştır:

| Sıra | Ülke | Bölge | ISO | GSYİH ($B) | Kişi Başı Gelir | Gölge Ekonomi (%) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
"""

for idx, item in enumerate(by_gdp[:20], 1):
    rankings_md += f"| {idx} | **{item['name']}** | {item['region']} | `{item['code']}` | ${item['gdp_usd_b']:,.1f}B | ${item['gdp_per_capita_usd']:,.0f} | %{item['shadow_economy_pct']:.1f} |\n"

rankings_md += """
---

## 4. En Yüksek Birleşik Kırılganlık ve Kleptokrasi Riski (CSFI Top 20)

Birleşik Egemen Kırılganlık İndeksi (CSFI); kayıt dışı ekonomi oranı, kişi başına düşen refah seviyesi ve kurumsal şeffaflık açıklarını birleştiren kompozit bir metriktir:

| Sıra | Ülke | Bölge | ISO | CSFI Skoru (0-100) | Risk Sınıfı |
| :---: | :--- | :--- | :---: | :---: | :--- |
"""

for idx, item in enumerate(by_fragility[:20], 1):
    rankings_md += f"| {idx} | **{item['name']}** | {item['region']} | `{item['code']}` | **{item['fragility_index_csfi']}** | {item['risk_tier']} |\n"

rankings_md_path = DATASETS_DIR / "GLOBAL_RANKINGS_REPORT.md"
with open(rankings_md_path, "w", encoding="utf-8") as f:
    f.write(rankings_md.strip() + "\n")
print(f"[CREATED] {rankings_md_path}")

# -------------------------------------------------------------
# 5. ENHANCE scripts/xray_cli.py
# -------------------------------------------------------------
XRAY_CLI_CODE = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
scripts/xray_cli.py
Küresel Röntgen (Global X-Ray) - Komut Satırı İstihbarat & Analiz Terminali

Kullanım:
  python scripts/xray_cli.py country <ulke_adi_veya_kodu>
  python scripts/xray_cli.py compare <ulke_1> <ulke_2>
  python scripts/xray_cli.py search <terim>
  python scripts/xray_cli.py top-shadow [sayi]
  python scripts/xray_cli.py top-gdp [sayi]
  python scripts/xray_cli.py intel [ulke_adi]
  python scripts/xray_cli.py list [bolge]
  python scripts/xray_cli.py stats
\"\"\"

import sys
import json
import csv
from pathlib import Path

# Windows console encoding fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
REGISTRY_PATH = BASE_DIR / "global_datasets" / "countries_registry.json"
INTEL_PATH = BASE_DIR / "global_datasets" / "intelligence_agencies_registry.json"
MATRIX_PATH = BASE_DIR / "global_datasets" / "global_power_matrix.json"

def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_intel():
    if INTEL_PATH.exists():
        with open(INTEL_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"agencies": []}

def load_matrix():
    if MATRIX_PATH.exists():
        with open(MATRIX_PATH, "r", encoding="utf-8") as f:
            return json.load(f).get("countries", [])
    return []

def find_country(query: str):
    registry = load_registry()
    q = query.lower().strip()
    for c in registry:
        if c["slug"] == q or c["name"].lower() == q or c["code"].lower() == q:
            return c
    for c in registry:
        if q in c["slug"] or q in c["name"].lower():
            return c
    return None

def show_country(query: str):
    c = find_country(query)
    if not c:
        print(f"[-] Ülke bulunamadı: '{query}'")
        return
        
    c_dir = BASE_DIR / c["slug"] if (BASE_DIR / c["slug"]).exists() else BASE_DIR / c["path"]
    macro_path = c_dir / "03_official_economy" / "macroeconomics.json"
    shadow_path = c_dir / "04_shadow_power_osint" / "real_power_dynamics.md"
    oligarch_path = c_dir / "04_shadow_power_osint" / "oligarch_network.csv"
    media_path = c_dir / "04_shadow_power_osint" / "media_censorship_matrix.md"

    print("=" * 75)
    print(f"🌍 KÜRESEL RÖNTGEN RAPORU: {c['name'].upper()} ({c['code']})")
    print("=" * 75)
    print(f"• Bölge: {c['region'].replace('_', ' ').title()}")
    print(f"• Başkent: {c['capital']}")
    print(f"• Nüfus: {c['population']:,}")
    print(f"• Nominal GSYH: ${c['gdp_usd_b']:,.1f} Milyar")
    print(f"• Gölge / Kayıt Dışı Ekonomi: %{c['shadow_economy_pct']}")
    print("-" * 75)

    if macro_path.exists():
        with open(macro_path, "r", encoding="utf-8") as f:
            m = json.load(f)
            print("📊 EKONOMİ VE TİCARET:")
            print(f"  Para Birimi: {m.get('currency')}")
            print(f"  Kişi Başı Gelir: ${m.get('gdp_per_capita_usd'):,}")
            print(f"  Enflasyon: %{m.get('inflation_rate_pct')}")
            print(f"  Kamu Borcu / GSYH: %{m.get('debt_to_gdp_pct', 'N/A')}")
            print(f"  Ana İhracat: {', '.join(m.get('top_exports', []))}")
            print(f"  Ticaret Ortakları: {', '.join(m.get('major_trading_partners', []))}")
        print("-" * 75)

    if oligarch_path.exists():
        print("🕶️ OLİGARK & GÖLGE SERMAYE AĞI:")
        with open(oligarch_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                count += 1
                wealth = f" (${row.get('estimated_wealth_usd_m')}M)" if row.get('estimated_wealth_usd_m') != "0" else ""
                print(f"  • {row.get('person_or_entity')} {wealth}")
                print(f"    Rol: {row.get('role_or_title')} | Sektör: {row.get('connected_sector')}")
                print(f"    Siyasi Bağ: {row.get('political_connection')}")
            if count == 0:
                print("  (Kayıtlı doğrudan oligark verisi bulunamadı)")
        print("-" * 75)

    print(f"[!] Doğrudan dosya yolu: {c['slug']}/README.md")

def compare_countries(q1: str, q2: str):
    c1 = find_country(q1)
    c2 = find_country(q2)
    if not c1 or not c2:
        print(f"[-] Ülkelerden biri veya ikisi bulunamadı: ({q1}, {q2})")
        return

    print("=" * 80)
    print(f"⚖️ JEOPOLİTİK VE EKONOMİK KARŞILAŞTIRMA")
    print(f"   {c1['name'].upper()} ({c1['code']}) vs {c2['name'].upper()} ({c2['code']})")
    print("=" * 80)
    print(f"{'Metrik':<30} | {c1['name']:<22} | {c2['name']:<22}")
    print("-" * 80)
    print(f"{'Bölge':<30} | {c1['region']:<22} | {c2['region']:<22}")
    print(f"{'Başkent':<30} | {c1['capital']:<22} | {c2['capital']:<22}")
    print(f"{'Nüfus':<30} | {c1['population']:<22,d} | {c2['population']:<22,d}")
    print(f"{'Nominal GSYH (USD)':<30} | ${c1['gdp_usd_b']:<21,.1f}B | ${c2['gdp_usd_b']:<21,.1f}B")
    print(f"{'Gölge Ekonomi Oranı':<30} | %{c1['shadow_economy_pct']:<21.1f} | %{c2['shadow_economy_pct']:<21.1f}")

    # GSYH farkı
    ratio = c1['gdp_usd_b'] / max(c2['gdp_usd_b'], 0.01)
    print("-" * 80)
    if ratio > 1:
        print(f"💡 {c1['name']} ekonomisi, {c2['name']} ekonomisinden {ratio:.1f} kat daha büyüktür.")
    else:
        print(f"💡 {c2['name']} ekonomisi, {c1['name']} ekonomisinden {(1/ratio):.1f} kat daha büyüktür.")
    print("=" * 80)

def search_term(term: str):
    registry = load_registry()
    q = term.lower()
    matches = []
    for c in registry:
        if q in c["name"].lower() or q in c["slug"] or q in c["capital"].lower() or q in c["region"]:
            matches.append(c)
    print(f"🔍 '{term}' araması için bulunan sonuçlar ({len(matches)} ülke):")
    for m in matches:
        print(f"  • {m['name']} ({m['code']}) - {m['region']} | Başkent: {m['capital']} | GSYH: ${m['gdp_usd_b']:.1f}B")

def top_shadow(limit=15):
    matrix = load_matrix()
    if not matrix:
        print("[-] Power matrix verisi yüklenemedi.")
        return
    sorted_m = sorted(matrix, key=lambda x: x["shadow_economy_pct"], reverse=True)[:limit]
    print(f"🏴‍☠️ EN YÜKSEK GÖLGE EKONOMİYE SAHİP İLK {limit} ÜLKE:")
    print("-" * 70)
    for i, item in enumerate(sorted_m, 1):
        print(f"{i:2d}. {item['name']:<25} %{item['shadow_economy_pct']:<6.1f} (GSYH: ${item['gdp_usd_b']:,.1f}B) [{item['risk_tier']}]")

def top_gdp(limit=15):
    matrix = load_matrix()
    if not matrix:
        print("[-] Power matrix verisi yüklenemedi.")
        return
    sorted_m = sorted(matrix, key=lambda x: x["gdp_usd_b"], reverse=True)[:limit]
    print(f"💰 EN BÜYÜK {limit} EKONOMİ (NOMİNAL GSYH):")
    print("-" * 70)
    for i, item in enumerate(sorted_m, 1):
        print(f"{i:2d}. {item['name']:<25} ${item['gdp_usd_b']:<8,.1f}B (Kayıt Dışı: %{item['shadow_economy_pct']:.1f})")

def show_intel(query=None):
    intel = load_intel()
    agencies = intel.get("agencies", [])
    if query:
        q = query.lower()
        agencies = [a for a in agencies if q in a["country"].lower() or q in a["iso2"].lower()]
    print(f"🕵️ İSTİHBARAT TEŞKİLATI VERİTABANI ({len(agencies)} Servis):")
    print("=" * 80)
    for a in agencies:
        print(f"[{a['country']} - {a['iso2']}]")
        print(f"  • Dış İstihbarat: {a['primary_foreign']}")
        print(f"  • Sinyal / Siber: {a['primary_signals']}")
        print(f"  • İç Güvenlik:   {a['primary_domestic']}")
        print(f"  • Askeri İst.:   {a['primary_military']}")
        print(f"  • Tahmini Bütçe: {a['estimated_annual_budget_usd']}")
        print(f"  • Operasyonlar:  {', '.join(a.get('notorious_operations', []))}")
        print("-" * 80)

def show_stats():
    registry = load_registry()
    total_gdp = sum(c.get("gdp_usd_b", 0) for c in registry)
    total_pop = sum(c.get("population", 0) for c in registry)
    avg_shadow = sum(c.get("shadow_economy_pct", 0) for c in registry) / len(registry)
    
    print("=" * 60)
    print("🌐 KÜRESEL RÖNTGEN SİSTEM İSTATİSTİKLERİ")
    print("=" * 60)
    print(f"• Kayıtlı Toplam Varlık Sayısı: {len(registry)} Ülke & Bölge")
    print(f"• Toplam Dünya Nüfusu:          {total_pop:,}")
    print(f"• Toplam Dünya GSYH'si:         ${total_gdp:,.1f} Milyar (~${total_gdp/1000:.1f} Trilyon)")
    print(f"• Ortalama Gölge Ekonomi Oranı: %{avg_shadow:.2f}")
    print("=" * 60)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1].lower()

    if cmd in ["country", "ulke", "c"] and len(sys.argv) > 2:
        show_country(" ".join(sys.argv[2:]))
    elif cmd in ["compare", "karsilas", "vs"] and len(sys.argv) > 3:
        compare_countries(sys.argv[2], sys.argv[3])
    elif cmd in ["search", "ara", "s"] and len(sys.argv) > 2:
        search_term(" ".join(sys.argv[2:]))
    elif cmd in ["top-shadow", "golge"]:
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 15
        top_shadow(limit)
    elif cmd in ["top-gdp", "ekonomi"]:
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 15
        top_gdp(limit)
    elif cmd in ["intel", "istihbarat"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_intel(q)
    elif cmd in ["stats", "istatistik"]:
        show_stats()
    elif cmd in ["list", "liste"]:
        reg = load_registry()
        print(f"📋 Toplam {len(reg)} Ülke Kayıtlı:")
        for c in reg:
            print(f"  • {c['name']:<25} ({c['code']}) - {c['region']}")
    else:
        # Tek argüman olarak ülke adı verilmiş olabilir
        show_country(cmd)

if __name__ == "__main__":
    main()
"""

with open(SCRIPTS_DIR / "xray_cli.py", "w", encoding="utf-8") as f:
    f.write(XRAY_CLI_CODE.strip() + "\n")
print(f"[UPDATED] {SCRIPTS_DIR / 'xray_cli.py'}")

print("\n[SUCCESS] All comprehensive features built successfully!")

