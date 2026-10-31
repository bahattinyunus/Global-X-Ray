"""
scripts/build_case_studies_and_datasets.py
Generates in-depth OSINT case studies in /dossiers and new strategic datasets in /global_datasets.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOSSIERS_DIR = BASE_DIR / "dossiers"
DATASETS_DIR = BASE_DIR / "global_datasets"

DOSSIERS_DIR.mkdir(parents=True, exist_ok=True)
DATASETS_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. CASE_STUDY_1MDB.md
# -------------------------------------------------------------
CS_1MDB = """# 🕵️ Vaka Analizi: 1MDB - Küresel Finans Tarihinin En Büyük Egemen Varlık Fonu Soygunu

> "This is one of the greatest financial heists in history... Money that belonged to the people of Malaysia was used to buy luxury yachts, Van Gogh paintings, Beverly Hills mansions, and finance Hollywood films."  
> — **Loretta Lynch**, *ABD Adalet Bakanı (DOJ Basın Açıklaması, 2016)*

> "If you owe the bank $100, that's your problem. If you steal $4.5 billion from a national development fund with the help of Wall Street bankers, that's geopolitics."  
> — **Tom Wright & Bradley Hope**, *Billion Dollar Whale* (2018)

---

## 1. Yönetici Özeti ve Olayın Anatomisi

**1MDB (1Malaysia Development Berhad)**; Malezya halkının refahını artırmak, doğrudan yabancı yatırım çekmek ve yeşil enerji projelerini finanse etmek amacıyla 2009 yılında dönemin Başbakanı **Necip Rezak (Najib Razak)** tarafından kurulan bir stratejik kalkınma fonudur.

Ancak fon; Malezyalı finansör **Jho Low** ve Başbakan Necip Rezak'ın koordinasyonunda, tarihin en karmaşık ulusötesi kara para aklama makinesine dönüştürülmüştür. 2009-2014 yılları arasında fondan **4.5 milyar dolardan fazla kamu kaynağı** sahte ortak girişimler, offshore paravan şirketler ve İsviçre banka hesapları üzerinden hortumlanmıştır.

---

## 2. Finansal Akış ve Katmanlama Şeması

```mermaid
sequenceDiagram
    autonumber
    participant 1MDB as 1MDB Devlet Fonu (Malezya)
    participant GS as Goldman Sachs (Tahvil İhracı)
    participant Shell as Paravan Şirketler (BVI / Seyşeller)
    participant Falcon as Falcon Bank / BSI (İsviçre / Singapur)
    participant Assets as Lüks Varlıklar (Yat, Sanat, Hollywood)

    1MDB->>GS: 6.5 Milyar Dolarlık tahvil ihracı yetkisi (Project Magnolia & Maximus)
    GS-->>1MDB: Tahvil fonları toplandı (GS: $600M komisyon kesintisi)
    1MDB->>Shell: Aabar Investments PJS Ltd (Sahte Abu Dabi Şirketi BVI)
    Shell->>Falcon: Katmanlama: Blackstone Asia / Tanore Finance hesapları
    Falcon->>1MDB: $681 Milyon doğrudan Başbakan Necip Rezak'ın kişisel AmBank hesabına
    Falcon->>Assets: Equanimity Süperyatı ($250M), Monet/Picasso tabloları, "The Wolf of Wall Street" filmi
```

---

## 3. Temel Soruşturma Bulguları ve OSINT Metodolojisi

1. **İsim Benzerliğiyle Dolandırıcılık (The Clone Company Technique):**
   - Abu Dabi devlet fonu olan meşru *Aabar Investments PJS* yerine, Britanya Virjin Adaları'nda (BVI) aynı isimle sahte bir kabuk şirket (*Aabar Investments PJS Limited*) tescil ettirilerek fonlar buraya aktarıldı.
2. **Wall Street Suç Ortaklığı (Goldman Sachs):**
   - Goldman Sachs Güneydoğu Asya Başkanı **Tim Leissner** ve ortağı **Roger Ng**, piyasa faizinin iki katı komisyon ($600 milyon) karşılığında şüpheli fon transferlerine göz yumdu. Goldman Sachs, DOJ ve Malezya hükümetine $3.9 milyar ceza ödemeyi kabul etti.
3. **Medya ve Muhalefetin Susturulması:**
   - Skandalı haberleştiren *The Edge* gazetesi kapatıldı, Başsavcı Abdul Gani Patail görevden alındı ve MACC (Malezya Yolsuzlukla Mücadele Komisyonu) dedektifleri tasfiye edildi.
   - Hakikat; bağımsız araştırmacı gazeteci **Clare Rewcastle Brown** (*The Sarawak Report*) ve sızdırılan 227.000 e-posta arşivi sayesinde deşifre edildi.

---

## 4. Çıkarılan İstihbari Dersler

* **Egemen Varlık Fonları (SWF) Denetim Boşluğu:** Devlet başkanının tek imza yetkisine sahip olduğu fonlar, parlamenter denetimden muaf tutulduğunda kleptokratik avlanma sahasına dönüşür.
* **Muhabir Bankacılık Zaafı:** JPMorgan, Deutsche Bank, Standard Chartered ve BSI gibi küresel bankalar, milyarlarca dolarlık uyumsuz transferleri sırf işlem ücreti kazanmak uğruna raporlamamıştır.
"""

# -------------------------------------------------------------
# 2. CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md
# -------------------------------------------------------------
CS_MAGNITSKY = """# 🕵️ Vaka Analizi: Magnitsky Vakası & Rus/Troika Laundromat Aklama Çarkı

> "Sergei Magnitsky died because he uncovered the theft of $230 million of Russian taxpayers' money by corrupt police officers and tax officials. They tortured him for 358 days to make him withdraw his testimony, and when he refused, they beat him to death with rubber batons."  
> — **Bill Browder**, *Red Notice: A True Story of High Finance, Murder, and One Man's Fight for Justice* (2015)

> "The Russian Laundromat was not an accident; it was an industrial-scale public utility for moving stolen state wealth into London penthouses and French Riviera villas."  
> — **OCCRP (Organized Crime and Corruption Reporting Project)**

---

## 1. Yönetici Özeti: 20 Milyar Dolarlık Aklama Boru Hattı

**Rus Çamaşırhanesi (The Russian Laundromat)** ve **Troika Laundromat**; 2011 ile 2014 yılları arasında Rusya'daki organize suç örgütleri, FSB görevlileri ve oligarklar tarafından hortumlanan **20.8 milyar doların** Moldova mahkemeleri ve Letonya/Estonya bankaları üzerinden Avrupa Birliği finans sistemine sokulduğu devasa bir aklama şebekesidir.

Bu düzenek, vergi müfettişi **Sergei Magnitsky**'nin 2008 yılında 230 milyon dolarlık bir vergi iadesi dolandırıcılığını ortaya çıkarması ve ardından Moskova'daki Butyrka Cezaevi'nde işkenceyle katledilmesiyle küresel bir jeopolitik kırılmaya yol açmıştır. Olay, ABD Kongresi'nin insan hakları ihlalcilerine yönelik küresel yaptırım yasası olan **Global Magnitsky Act**'i kabul etmesini sağlamıştır.

---

## 2. Aklama Döngüsünün Hukuki Hilesi: "Moldova Mahkeme Kararı Modeli"

```mermaid
flowchart TD
    subgraph Rusya["Rusya Federasyonu"]
        O["Oligark / Yolsuz Yetkili (Gölge Para)"] --> R1["Rus Şirketi (Garantör)"]
    end

    subgraph Britanya["İngiltere Paravanları"]
        UK1["İngiltere Shell Ltd A (Borçlu)"] <--> UK2["İngiltere Shell Ltd B (Alacaklı)"]
    end

    subgraph Moldova["Moldova Yargı Kumpası"]
        M_Judge["Rüşvetçi Moldova Hakimi<br/>(Sahte Borç İlamı Onayı)"]
        Moldin["Moldinconbank Hesabı"]
    end

    subgraph Bati["Baltık ve Batı Bankaları"]
        Trasta["Trasta Komercbanka (Letonya)"]
        Danske["Danske Bank Estonia ($200B Hacim)"]
        Assets["Avrupa Emlak, Yat ve Tahvil Piyasası"]
    end

    UK1 -.->|"Sahte $500M Borç Senedi"| UK2
    R1 -.->|"Borca Kefil Olur"| UK1
    UK2 --> M_Judge
    M_Judge -->|"Haciz Kararı Verir"| Moldin
    O -->|"Yasal Mahkeme Haczi Kılıfıyla Para Çıkar"| Moldin
    Moldin --> Trasta & Danske
    Trasta & Danske --> Assets
```

---

## 3. OCCRP Tarafından Deşifre Edilen Temel Bulgular

1. **Sahte Borç Senetleri:** İngiltere'de kayıtlı iki paravan şirket aralarında hiçbir mal alımı olmaksızın 500 milyon dolarlık hayali bir borç sözleşmesi imzalamakta, Rusya'daki bir şirket de bu borca kefil olmaktaydı.
2. **Moldovalı Hakimlerin İcrası:** Borç ödenmediği gerekçesiyle Moldovalı rüşvetçi bir hakime başvurulmakta; hakim birkaç saat içinde Rus garantörün Rusya'daki banka hesaplarına resmi haciz kararı çıkarmaktaydı.
3. **Meşrulaştırılmış Para Kaçışı:** Para, Rusya Merkez Bankası denetiminden "yabancı mahkeme ilamı" gereğince yasal olarak çıkmakta, Moldova üzerinden Letonya (Trasta Komercbanka) ve Estonya (Danske Bank) hesaplarına aktarılmaktaydı.

---

## 4. Jeopolitik Miras: Global Magnitsky Yaptırım Rejimi

* Sergei Magnitsky'nin ölümü sonrasında ABD'de kabul edilen yasa, günümüzde AB, İngiltere, Kanada ve Avustralya tarafından benimsenmiştir.
* Bu rejim; devletler yerine doğrudan bireysel insan hakları ihlalcilerinin, işkencecilerin ve kleptokratların mal varlıklarını dondurma ve vize iptali uygulama yetkisi tanımaktadır.
"""

# -------------------------------------------------------------
# 3. CASE_STUDY_ODEBRECHT_LAVA_JATO.md
# -------------------------------------------------------------
CS_ODEBRECHT = """# 🕵️ Vaka Analizi: Odebrecht & Lava Jato - Latin Amerika'nın Sistemik Rüşvet Karteli

> "Odebrecht created a literal 'Department of Bribery'—a fully functioning, shadow corporate division dedicated exclusively to paying off presidents, ministers, and political parties across an entire continent."  
> — **ABD Adalet Bakanlığı (DOJ) Cezai İddianamesi (2016)**

> "Lava Jato was not just an anti-corruption investigation; it was an earthquake that brought down presidents in Brazil, Peru, Ecuador, and Colombia."  
> — **Latin American Investigative Consortium**

---

## 1. Yönetici Özeti: 12 Ülke, 788 Milyon Dolar Rüşvet

Brezilya merkezli dev inşaat konglomeratı **Odebrecht**, kamu ihalelerini (barajlar, otoyollar, rafineriler, metro hatları) rekabetsiz kazanmak amacıyla Latin Amerika ve Afrika'daki 12 ülkede siyasilere **en az 788 milyon dolar rüşvet** dağıtmıştır.

Olay, 2014 yılında Curitiba'daki bir benzin istasyonunda döviz kaçakçılığı şüphesiyle başlayan **Operação Lava Jato (Araç Yıkama Operasyonu)** ile patlak vermiş; Brezilya devlet petrol şirketi **Petrobras** üzerinden kurulan devasa bir siyasi rüşvet ve komisyon çarkı deşifre edilmiştir.

---

## 2. "Yapılandırılmış Operasyonlar Bölümü" (Rüşvet Departmanı)

Odebrecht, rüşvet dağıtımını kurumsal bir işletme mantığıyla yönetmek için resmi olarak **Setor de Operações Estruturadas (Yapılandırılmış Operasyonlar Bölümü)** adında gizli bir birim kurmuştur:
* **MyWebDay & Drousys:** Rüşvet iletişimini yürütmek ve ödemeleri takip etmek için İsviçre'de barındırılan, internete kapalı, şifreli iki özel yazılım sistemi.
* **Kod Adları:** Siyasetçilere ve bakanlara gerçek isimleri yerine "Brezilya", "Ferrari", "Campanhas", "Caju" gibi kod adları verilmiştir.
* **Antigua Meinl Bank Satın Alımı:** Rüşvet akışını kesintisiz ve denetimsiz yürütmek amacıyla Antigua'daki Meinl Bank'ın hisseleri gizlice satın alınarak rüşvet paraları doğrudan şirket denetimindeki banka üzerinden transfer edilmiştir.

---

## 3. Siyasi ve Jeopolitik Yıkım

| Ülke | Etkilenen Liderler | Yargısal ve Siyasi Sonuçlar |
| :--- | :--- | :--- |
| **Brezilya** | Luiz Inácio Lula da Silva, Dilma Rousseff, Michel Temer | Lula hapis cezası aldı (daha sonra iptal edildi ve yeniden başkan seçildi); Dilma azledildi. |
| **Peru** | Alejandro Toledo, Alan García, Ollanta Humala, Pedro Pablo Kuczynski | Alan García polis tutuklamaya geldiğinde intihar etti; Toledo ve Humala tutuklandı. |
| **Ekvador** | Jorge Glas (Cumhurbaşkanı Yardımcısı) | 6 yıl hapis cezasına çarptırıldı. |
| **Kolombiya** | Juan Manuel Santos seçim kampanyası | Kampanyaya yasadışı Odebrecht bağışları yapıldığı doğrulandı. |
| **Panama** | Ricardo Martinelli çocukları | ABD'de aklama suçundan mahkum edildiler. |
"""

# -------------------------------------------------------------
# 4. CASE_STUDY_PEGASUS_PROJECT.md
# -------------------------------------------------------------
CS_PEGASUS = """# 🕵️ Vaka Analizi: Pegasus Projesi - Dijital Otokrasi ve Sıfır-Tıklama Siber İstihbarat

> "Pegasus turns your smartphone into a 24-hour surveillance device in your pocket. It reads your encrypted messages, turns on your microphone, tracks your GPS, and copies your passwords without you ever clicking a link."  
> — **Forbidden Stories & Amnesty International Security Lab (2021)**

> "In the 20th century, dictators needed secret police with listening vans outside your house. In the 21st century, they buy an Israeli software exploit and let Apple's own notification system deliver the spy into your bedroom."  
> — **Cyber-Intelligence OSINT Analysis**

---

## 1. Yönetici Özeti: NSO Group ve 50.000 Hedef Numara

Temmuz 2021'de 17 uluslararası medya kuruluşunun oluşturduğu **Forbidden Stories** konsorsiyumu ve **Uluslararası Af Örgütü Güvenlik Laboratuvarı**, İsrailli siber istihbarat şirketi **NSO Group** tarafından geliştirilen **Pegasus** casus yazılımının küresel çapta nasıl kötüye kullanıldığını ifşa etti.

Sızdırılan **50.000 telefon numarasından** oluşan hedef listesinde; en az 65 iş insanı, 85 insan hakları savunucusu, 189 gazeteci ve aralarında Fransa Cumhurbaşkanı Emmanuel Macron, Güney Afrika Devlet Başkanı Cyril Ramaphosa ve dönemin Pakistan Başbakanı İmran Han'ın da bulunduğu **14 devlet ve hükümet başkanı** yer almaktaydı.

---

## 2. Teknik Bilişim ve İstihbarat Mimarisi: Sıfır-Tıklama (Zero-Click)

Geleneksel oltalama (phishing) yöntemleri kullanıcının şüpheli bir linke tıklamasını gerektirirken, Pegasus **sıfır-tıklama (zero-click)** zaafiyetlerini kullanır:

```
[Saldırgan İstihbarat Servisi] 
           │
           ▼
[Görünmez iMessage / WhatsApp Bildirimi Gönderimi]
           │
           ▼
[CoreGraphics / WebKit PDF Ayrıştırıcı Taşması (FORCEDENTRY Zaafiyeti)]
           │
           ▼
[iOS Sandbox İhlali & Root/Kernel Yetkisi Elde Edilmesi]
           │
           ▼
[Şifreli Veri Çekimi (Signal, WhatsApp, Telegram, Kamera, Mikrofon)]
           │
           ▼
[Komuta Kontrol (C2) Sunucusuna Şifreli Telemetri Aktarımı]
```

---

## 3. Belgelenen İnsan Hakları İhlalleri ve Hedefler

1. **Cemal Kaşıkçı Cinayeti (2018):**
   - Suudi Arabistan muhalifi gazeteci Cemal Kaşıkçı'nın nişanlısı Hatice Cengiz'in, oğlu Abdullah'ın ve yakın çalışma arkadaşı Ömer Abdülaziz'in telefonlarına cinayet öncesinde ve sonrasında Pegasus yüklendiği adli bilişim raporlarıyla kanıtlandı.
2. **Meksika Narko-Siyaset İttifakı:**
   - Meksika hükümeti ve ordu istihbaratı (SEDENA), uyuşturucu kartellerinin cinayetlerini soruşturan bağımsız gazeteci Cecilio Pineda Birto'yu Pegasus ile takip etti; Pineda telefonunun izlenmesinden birkaç hafta sonra katledildi.
3. **Avrupa Birliği Skandalları:**
   - İspanya'da Katalan siyasetçilerin, Polonya'da muhalefet liderlerinin ve Yunanistan'da gazetecilerin bizzat ulusal istihbarat servisleri tarafından dinlendiği doğrulandı.
"""

# Write dossiers
DOSSIER_FILES = {
    "CASE_STUDY_1MDB.md": CS_1MDB,
    "CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md": CS_MAGNITSKY,
    "CASE_STUDY_ODEBRECHT_LAVA_JATO.md": CS_ODEBRECHT,
    "CASE_STUDY_PEGASUS_PROJECT.md": CS_PEGASUS,
}

for filename, content in DOSSIER_FILES.items():
    dest = DOSSIERS_DIR / filename
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[CREATED] {dest.relative_to(BASE_DIR)}")

# -------------------------------------------------------------
# 5. NEW GLOBAL DATASET: chokepoints_registry.json
# -------------------------------------------------------------
CHOKEPOINTS_DATA = {
    "_metadata": {
        "title": "Küresel Stratejik Boğazlar, Kanallar ve Transit Darboğazları Sicili",
        "version": "1.0.0",
        "source_authority": "US Energy Information Administration (EIA), IMO, Lloyd's List"
    },
    "chokepoints": [
        {
            "name": "Hürmüz Boğazı",
            "english_name": "Strait of Hormuz",
            "type": "Doğal Deniz Boğazı",
            "controlling_states": ["İran", "Umman"],
            "daily_petroleum_transit_barrels": 21000000,
            "share_of_global_maritime_oil_pct": 21.0,
            "annual_vessel_transits": 33000,
            "asymmetric_threats": ["İran seyir füzeleri", "Deniz mayınlama", "Hızlı hücumbot sürüleri"],
            "alternative_route": "Suudi Doğu-Batı Petroline boru hattı (Kısmi kapasite)",
            "geopolitical_risk_level": "Aşırı Yüksek (Critical)"
        },
        {
            "name": "Malakka Boğazı",
            "english_name": "Strait of Malacca",
            "type": "Doğal Deniz Boğazı",
            "controlling_states": ["Endonezya", "Malezya", "Singapur"],
            "daily_petroleum_transit_barrels": 16000000,
            "share_of_global_maritime_oil_pct": 16.0,
            "annual_vessel_transits": 84000,
            "asymmetric_threats": ["Deniz haydutluğu", "Batılı donanmaların blokajı (Malakka İkilemi)"],
            "alternative_route": "Sunda ve Lombok boğazları (+3 gün, +$1.2M sefer maliyeti)",
            "geopolitical_risk_level": "Yüksek (High)"
        },
        {
            "name": "Süveyş Kanalı",
            "english_name": "Suez Canal",
            "type": "Yapay Su Yolu",
            "controlling_states": ["Mısır"],
            "daily_petroleum_transit_barrels": 5500000,
            "share_of_global_maritime_oil_pct": 9.0,
            "annual_vessel_transits": 22000,
            "asymmetric_threats": ["Gemi karaya oturması (Ever Given)", "Sina terör saldırıları"],
            "alternative_route": "Ümit Burnu (Güney Afrika) rotası (+10-14 gün seyir)",
            "geopolitical_risk_level": "Yüksek (High)"
        },
        {
            "name": "Babülmendep Boğazı",
            "english_name": "Bab el-Mandeb Strait",
            "type": "Doğal Deniz Boğazı",
            "controlling_states": ["Yemen", "Cibuti", "Eritre"],
            "daily_petroleum_transit_barrels": 4800000,
            "share_of_global_maritime_oil_pct": 8.0,
            "annual_vessel_transits": 21000,
            "asymmetric_threats": ["Husi gemisavar balistik füzeleri ve intihar İHA'ları"],
            "alternative_route": "Ümit Burnu etrafından dolaşım",
            "geopolitical_risk_level": "Kritik Savaş Alanı (Hostile)"
        },
        {
            "name": "Panama Kanalı",
            "english_name": "Panama Canal",
            "type": "Yapay Su Yolu (Kademeli Havuz Sistemi)",
            "controlling_states": ["Panama"],
            "daily_petroleum_transit_barrels": 1000000,
            "share_of_global_maritime_oil_pct": 3.0,
            "annual_vessel_transits": 14000,
            "asymmetric_threats": ["Tatlı su kıtlığı ve Gatun Gölü kuraklığı", "Teknik arızalar"],
            "alternative_route": "Macellan Boğazı / Horn Burnu (+22 gün)",
            "geopolitical_risk_level": "Orta / Ekolojik Risk (Moderate)"
        },
        {
            "name": "İstanbul ve Çanakkale Boğazları",
            "english_name": "Turkish Straits (Bosporus & Dardanelles)",
            "type": "Doğal Deniz Boğazları (Montrö Rejimi)",
            "controlling_states": ["Türkiye"],
            "daily_petroleum_transit_barrels": 3000000,
            "share_of_global_maritime_oil_pct": 3.5,
            "annual_vessel_transits": 40000,
            "asymmetric_threats": ["Montrö Boğazlar Sözleşmesi kısıtlamaları", "Karadeniz serseri mayınları"],
            "alternative_route": "Kara boru hatları (BTC, CPC)",
            "geopolitical_risk_level": "Stratejik & Hukuki Kilit (Strategic)"
        }
    ]
}

with open(DATASETS_DIR / "chokepoints_registry.json", "w", encoding="utf-8") as f:
    json.dump(CHOKEPOINTS_DATA, f, indent=2, ensure_ascii=False)
print(f"[CREATED] {DATASETS_DIR / 'chokepoints_registry.json'}")

# -------------------------------------------------------------
# 6. NEW GLOBAL DATASET: pmc_mercenary_groups.json
# -------------------------------------------------------------
PMC_DATA = {
    "_metadata": {
        "title": "Özel Askeri Şirketler (PMC) ve Paramiliter Şebekeler Sicili",
        "version": "1.0.0",
        "admiralty_verification": "B2+"
    },
    "companies": [
        {
            "name": "Wagner Group / Afrika Kolordusu (Africa Corps)",
            "country_of_origin": "Rusya",
            "legal_status": "Savunma Bakanlığı (GRU) bağlı gayriresmi paramiliter güç",
            "estimated_manpower": "35,000 - 50,000",
            "active_theaters": ["Mali", "Burkina Faso", "Nijer", "Orta Afrika Cumhuriyeti", "Suriye", "Libya"],
            "primary_revenue_sources": ["Altın ve elmas madeni imtiyazları", "Doğal gaz sahası güvenliği"],
            "international_sanctions": ["ABD OFAC Yaptırımları", "AB Terör Örgütü Nitelemesi"]
        },
        {
            "name": "Constellis (Eski Blackwater / Academi)",
            "country_of_origin": "Amerika Birleşik Devletleri",
            "legal_status": "Kayıtlı ABD Savunma ve Güvenlik Yüklenicisi",
            "estimated_manpower": "16,000+",
            "active_theaters": ["Irak", "Afganistan", "Körfez Ülkeleri", "Afrika"],
            "primary_revenue_sources": ["ABD Dışişleri ve Pentagon koruma sözleşmeleri"],
            "international_sanctions": ["Nisour Meydanı katliamı davası tazminatları"]
        },
        {
            "name": "Frontier Services Group (FSG)",
            "country_of_origin": "Hong Kong / Çin (Kurucu: Erik Prince)",
            "legal_status": "Hong Kong Borsası kotasyonlu lojistik ve güvenlik şirketi",
            "estimated_manpower": "3,000+",
            "active_theaters": ["Kuşak-Yol güzergahı", "Demokratik Kongo Cumhuriyeti", "Sudan", "Pakistan"],
            "primary_revenue_sources": ["Çin devlet madencilik ve altyapı projelerinin korunması"],
            "international_sanctions": ["ABD Ticaret Bakanlığı Denetim Listesi"]
        },
        {
            "name": "SADAT Uluslararası Savunma Danışmanlık",
            "country_of_origin": "Türkiye",
            "legal_status": "Özel Savunma ve Stratejik Danışmanlık Şirketi",
            "estimated_manpower": "1,000+ (Yedek eğitim havuzu)",
            "active_theaters": ["Suriye", "Libya", "Kafkaslar"],
            "primary_revenue_sources": ["Gayrinizami harp eğitimi, askeri lojistik danışmanlık"],
            "international_sanctions": ["Çeşitli muhalif ve uluslararası STK raporları"]
        }
    ]
}

with open(DATASETS_DIR / "pmc_mercenary_groups.json", "w", encoding="utf-8") as f:
    json.dump(PMC_DATA, f, indent=2, ensure_ascii=False)
print(f"[CREATED] {DATASETS_DIR / 'pmc_mercenary_groups.json'}")

print("\n[SUCCESS] Tüm vaka analizleri ve yeni stratejik veri setleri oluşturuldu!")

