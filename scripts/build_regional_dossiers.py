"""
scripts/build_regional_dossiers.py
Generates comprehensive, quote-rich master regional dossiers (README.md) for all 6 regions:
- regions/middle_east/README.md
- regions/europe/README.md
- regions/asia/README.md
- regions/americas/README.md
- regions/africa/README.md
- regions/oceania/README.md
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REGIONS_DIR = BASE_DIR / "regions"
DATASETS_DIR = BASE_DIR / "global_datasets"

with open(DATASETS_DIR / "countries_registry.json", "r", encoding="utf-8") as f:
    countries = json.load(f)

# Group countries by region
regional_countries = {}
for c in countries:
    reg = c["region"]
    regional_countries.setdefault(reg, []).append(c)

# -------------------------------------------------------------
# 1. MIDDLE EAST
# -------------------------------------------------------------
ME_MD = f"""# 🕌 Ortadoğu Jeopolitik İstihbarat Dosyası (Middle East Strategic Dossier)

> "The Middle East is a region where the past is never dead; it's not even past. It is a chessboard where religions, empires, and pipelines collide in an eternal struggle for primacy."  
> — **Geopolitical Maxim of the Levant**

> "Whoever controls the oil of the Persian Gulf controls the economic lifeblood of the industrialized world."  
> — **Zbigniew Brzezinski**, *The Grand Chessboard* (1997)

---

## 1. Stratejik Giriş ve Güç Mimarisi

Ortadoğu; küresel hidrokarbon rezervlerinin %48'ine, kanıtlanmış doğal gaz rezervlerinin %40'ına ve dünya deniz ticaretinin iki kritik boğazına (Hürmüz ve Babülmendep) ev sahipliği yapan, tarihin en yoğun jeopolitik rekabet sahasıdır.

Bölgesel güç mimarisi, geleneksel Arap milliyetçiliğinin çöküşü sonrasında **dört ana hegemonik eksen** etrafında kutuplaşmıştır:
1. **İran Önderliğindeki Direniş Ekseni (Axis of Resistance):** Tahran-Bağdat-Şam-Beyrut-Sana karasal koridoru; asimetrik füze ve vekil güç şebekesi (Hizbullah, Haşdi Şabi, Ensarullah).
2. **Körfez-İsrail İttifakı (İbrahim Anlaşmaları Ekseni):** BAE, Suudi Arabistan, Bahreyn ve İsrail arasındaki teknolojik, istihbari ve finansal entegrasyon; İran çevreleme doktrini.
3. **Türkiye ve Neo-Osmanlı / Stratejik Özerklik Ekseni:** İHA/SİHA diplomasisi, Katar ile mali-askeri ittifak, Doğu Akdeniz (Mavi Vatan) ve Kuzey Irak/Suriye güvenlik kuşağı.
4. **Küresel Süper Güçlerin Müdahalesi:** ABD 5. Filosu (Bahreyn) ve CENTCOM üsleri; Rusya'nın Akdeniz varlığı (Tartus ve Hmeymim); Çin'in Kuşak-Yol ve enerji aracılığı (Suudi-İran uzlaşması).

---

## 2. Bölgesel Darboğazlar ve Enerji Güvenliği

```mermaid
flowchart LR
    subgraph Basra_Korfezi["Basra Körfezi / Enerji Kalbi"]
        K1["Suudi Arabistan / Kuveyt / BAE / Katar / Irak"] --> H["Hürmüz Boğazı<br/>(21 Milyon Varil/Gün Petrol)"]
    end
    H --> OM["Umman Denizi / Hint Okyanusu"]
    
    subgraph Kizildeniz_Hatti["Kızıldeniz Ticaret Koridoru"]
        BM["Babülmendep Boğazı<br/>(Yemen - Husi Füze Alanı)"] --> S["Süveyş Kanalı<br/>(Avrupa-Asya Geçişi)"]
    end
    OM --> BM
```

---

## 3. Bölge Ülkeleri ve Karşılaştırmalı İstihbarat Atlası

Aşağıdaki tabloda Ortadoğu bölgesinde analiz edilen tüm egemen devletler ve kritik jeopolitik varlıklar listelenmiştir:

| Ülke / Bölge | ISO | Başkent | Nominal GSYİH | Gölge Ekonomi (%) | Fiili Güç Odakları & Rejim Tipi | Rapor Bağlantısı |
| :--- | :---: | :--- | :---: | :---: | :--- | :--- |
"""

for c in sorted(regional_countries.get("middle_east", []), key=lambda x: x["name"]):
    ME_MD += f"| **{c['name']}** | `{c['code']}` | {c['capital']} | ${c['gdp_usd_b']:,.1f}B | %{c['shadow_economy_pct']} | {c.get('official_leader', 'N/A')} | [{c['name']} Raporu]({c['slug']}/README.md) |\n"

ME_MD += """
---

## 4. Bölgesel Yeraltı Sermaye Akışları ve Kara Para Rotaları
* **Dubai Serbest Bölgeleri (DMCC/DIFC):** Altın ticareti, Rus yaptırım sermayesi kaçışı, İran takas ağları (Hawala).
* **Körfez Hanedan Tröstleri:** Kamu petrol gelirlerinin aile servetlerine aktarılması ve Londra gayrimenkul yatırımları.
* **Captagon Uyuşturucu Karteli:** Suriye rejimi ve müttefik milislerin yıllık $5-10 milyar hacmindeki uyuşturucu finansmanı.
"""

# -------------------------------------------------------------
# 2. EUROPE
# -------------------------------------------------------------
EUR_MD = f"""# 🏰 Avrupa Jeopolitik İstihbarat Dosyası (Europe Strategic Dossier)

> "Europe is a garden surrounded by a jungle. The jungle has a strong growth capacity, and the wall will never be high enough to protect the garden."  
> — **Josep Borrell**, *EU High Representative for Foreign Affairs* (2022)

> "Europe will be forged in crises, and will be the sum of the solutions adopted for those crises."  
> — **Jean Monnet**, *Memoirs* (1976)

---

## 1. Stratejik Giriş: Soğuk Savaş Sonrası Güvenlik Kırılması

Avrupa kıtası; 1945 sonrası inşa edilen kurala dayalı uluslararası düzenin ve transatlantik ittifakın kalbidir. Ancak 2022 Ukrayna Savaşı ile birlikte kıta, İkinci Dünya Savaşı'ndan bu yana en derin jeopolitik ve askeri dönüşümünü yaşamaktadır:
* **NATO Genişlemesi ve Kuzey Kanadı:** Finlandiya ve İsveç'in katılımıyla Baltık Denizi bir "NATO gölüne" dönüşmüş, Rusya ile 1.340 km'lik yeni bir sınır hattı açılmıştır.
* **Suwalki Koridoru:** Polonya ile Litvanya arasında, Belarus ile Rusya'nın Kaliningrad ekslavı arasına sıkışmış 65 millik stratejik boğaz; NATO'nun en savunmasız kara koridorudur.
* **Enerji Ayrışması:** Rus boru hattı gazına (Kuzey Akım 1/2) olan bağımlılığın sonlandırılması; ABD LNG'sine ve Norveç şebekesine geçişin getirdiği yüksek sanayi maliyeti.

---

## 2. Finansal Aklama Merkezleri ve Avrupa Vergi Tahkimi

Avrupa Birliği yasal şeffaflık iddialarına rağmen, dünyanın en büyük kurumsal vergi kaçırma ve off-shore aklama ağlarından bazılarına ev sahipliği yapmaktadır:
* **City of London & Crown Dependencies:** Doğu Bloku kleptokratlarının ve küresel fonların ana aklama merkezi.
* **Lüksemburg SOPARFI Şirketleri:** Çokuluslu tekellerin karlarını sıfıra yakın vergiyle park ettiği holding cenneti.
* **İsviçre Bankacılık Mirası:** Numaralı hesaplar reforme edilse de serbest limanlar (Freeports) ve avukat-müvekkil gizliliğiyle korunan tröstler.
* **Hollanda / İrlanda Kanalı:** Teknoloji devlerinin (Apple, Google) patent karlarını vergiden kaçırdığı "Double Irish / Dutch Sandwich" yapıları.

---

## 3. Bölge Ülkeleri ve Karşılaştırmalı İstihbarat Atlası

| Ülke / Bölge | ISO | Başkent | Nominal GSYİH | Gölge Ekonomi (%) | Fiili Güç Odakları & Rejim Tipi | Rapor Bağlantısı |
| :--- | :---: | :--- | :---: | :---: | :--- | :--- |
"""

for c in sorted(regional_countries.get("europe", []), key=lambda x: x["name"]):
    EUR_MD += f"| **{c['name']}** | `{c['code']}` | {c['capital']} | ${c['gdp_usd_b']:,.1f}B | %{c['shadow_economy_pct']} | {c.get('official_leader', 'N/A')} | [{c['name']} Raporu]({c['slug']}/README.md) |\n"

# -------------------------------------------------------------
# 3. ASIA
# -------------------------------------------------------------
ASIA_MD = f"""# ⛩️ Asya & Hint-Pasifik Jeopolitik İstihbarat Dosyası (Asia & Indo-Pacific Dossier)

> "Let China sleep, for when she wakes, she will shake the world."  
> — **Napoleon Bonaparte** (1817)

> "The Indo-Pacific is the world's economic engine and the epicenter of 21st-century great power competition."  
> — **Indo-Pacific Strategic Review**

---

## 1. Stratejik Giriş: Küresel Güç Merkezinin Doğuya Kayması

Asya ve Hint-Pasifik bölgesi; dünya nüfusunun %60'ına, küresel deniz ticaretinin üçte ikisine ve ileri teknoloji tedarik zincirlerinin (yarı iletkenler, lityum piller, tüketici elektroniği) mutlak çoğunluğuna ev sahipliği yapmaktadır.

Bölgenin ana jeostratejik fay hatları:
1. **ABD-Çin Küresel Hegemonya Savaşı:** Birinci Ada Zinciri (Japonya, Tayvan, Filipinler) üzerinden Çin Donanması'nın (PLAN) açık denizlere çıkışını engelleme stratejisi.
2. **Tayvan Boğazı ve Yarı İletken Tekeli:** TSMC'nin dünyanın en gelişmiş (<3nm) çiplerinin %90'ını üretmesi; bir Tayvan krizinin küresel ekonomide yaratacağı yıllık $2.5 Trilyonluk şok.
3. **Güney Çin Denizi Askerileşmesi:** Yapay adalar, füze platformları ve Dokuz Çizgili Hat (Nine-Dash Line) üzerinden komşu ülkelerin (Vietnam, Filipinler, Malezya) EEZ haklarının ilhakı.
4. **Malakka İkilemi:** Çin'in ithal ham petrolünün %80'inin Malakka Boğazı'ndan geçmesi ve olası bir deniz ablukası riski.

---

## 2. Bölge Ülkeleri ve Karşılaştırmalı İstihbarat Atlası

| Ülke / Bölge | ISO | Başkent | Nominal GSYİH | Gölge Ekonomi (%) | Fiili Güç Odakları & Rejim Tipi | Rapor Bağlantısı |
| :--- | :---: | :--- | :---: | :---: | :--- | :--- |
"""

for c in sorted(regional_countries.get("asia", []), key=lambda x: x["name"]):
    ASIA_MD += f"| **{c['name']}** | `{c['code']}` | {c['capital']} | ${c['gdp_usd_b']:,.1f}B | %{c['shadow_economy_pct']} | {c.get('official_leader', 'N/A')} | [{c['name']} Raporu]({c['slug']}/README.md) |\n"

# -------------------------------------------------------------
# 4. AMERICAS
# -------------------------------------------------------------
AMER_MD = f"""# 🌎 Amerika Kıtası Jeopolitik İstihbarat Dosyası (Americas Strategic Dossier)

> "America for the Americans." (*The Monroe Doctrine, 1823*)  
> — **James Monroe** (ABD 5. Başkanı)

> "Poor Mexico, so far from God and so close to the United States."  
> — **Porfirio Díaz** (Meksika Devlet Başkanı)

---

## 1. Stratejik Giriş: Kuzey Hegemonyası ve Güneyin Kırılganlığı

Amerika kıtası; kuzeydeki süper güç Amerika Birleşik Devletleri ve Kanada ile güneydeki zengin doğal kaynaklara sahip ancak kronik siyasi istikrarsızlık ve kartel şiddetiyle boğuşan Latin Amerika arasındaki asimetrik güç dengesi üzerine kuruludur.

Kıtanın temel jeopolitik çatışma alanları:
1. **Monroe Doktrini ve Dış Güç Nüfuzu:** Çin'in Güney Amerika'daki liman yatırımları (Peru Chancay Mega Limanı), soya/bakır/lityum alımları ve Kuşak-Yol anlaşmaları.
2. **Ulusötesi Uyuşturucu Kartelleri:** Sinaloa Karteli, CJNG (Jalisco Nueva Generación) ve Kolombiya klanlarının devasa bütçeleri, askeri düzeyde silahlanmaları ve siyaseti ele geçirmeleri (narko-devletleşme).
3. **Lityum Üçgeni (Şili, Bolivya, Arjantin):** Dünya lityum rezervlerinin %56'sı ve batarya tedarik zincirleri üzerindeki jeostratejik mücadele.
4. **Panama Kanalı Darboğazı:** İklim değişikliği ve su seviyesi düşüşleri nedeniyle transit kısıtlamaları ve alternatif rotalar.

---

## 2. Bölge Ülkeleri ve Karşılaştırmalı İstihbarat Atlası

| Ülke / Bölge | ISO | Başkent | Nominal GSYİH | Gölge Ekonomi (%) | Fiili Güç Odakları & Rejim Tipi | Rapor Bağlantısı |
| :--- | :---: | :--- | :---: | :---: | :--- | :--- |
"""

for c in sorted(regional_countries.get("americas", []), key=lambda x: x["name"]):
    AMER_MD += f"| **{c['name']}** | `{c['code']}` | {c['capital']} | ${c['gdp_usd_b']:,.1f}B | %{c['shadow_economy_pct']} | {c.get('official_leader', 'N/A')} | [{c['name']} Raporu]({c['slug']}/README.md) |\n"

# -------------------------------------------------------------
# 5. AFRICA
# -------------------------------------------------------------
AFR_MD = f"""# 🌍 Afrika Jeopolitik İstihbarat Dosyası (Africa Strategic Dossier)

> "Africa is not poor; Africa is poorly managed, and its wealth is ruthlessly plundered."  
> — **Pan-Africanist Maxim**

> "The scramble for Africa never ended; it merely traded gunboats for sovereign debt contracts and private military contractors."  
> — **Contemporary OSINT African Dossier**

---

## 1. Stratejik Giriş: Yeni Afrika Paylaşım Savaşı

Afrika kıtası; küresel kobaltın %70'ine, platin rezervlerinin %90'ına, uranyum, elmas ve devasa ekilebilir tarım arazilerine ev sahipliği yapmaktadır. 21. yüzyılda kıta, geleneksel sömürgeci güçler ile yükselen revizyonist aktörlerin kıyasıya bir mücadele alanıdır:
* **Françafrique Sisteminin Çöküşü:** Mali, Burkina Faso, Nijer ve Gabon'da art arda gerçekleşen askeri darbeler; Fransız askeri varlığının ve CFA Frangı hegemonyasının tasfiye edilmesi.
* **Rusya ve Paramiliter Nüfuz:** Wagner Grubu / Afrika Kolordusu'nun maden hakları (altın, elmas) karşılığında askeri cuntalara rejim koruma hizmeti sağlaması.
* **Çin'in Altyapı ve Borç Diplomasisi:** Limanlar, demiryolları ve maden imtiyazları karşılığında verilen milyarlarca dolarlık devlet kredileri.
* **Sahel Terör ve Göç Koridoru:** Cihadist gruplar (JNIM, ISGS) ve Akdeniz'e yönelen kitlesel göç rotaları.

---

## 2. Bölge Ülkeleri ve Karşılaştırmalı İstihbarat Atlası

| Ülke / Bölge | ISO | Başkent | Nominal GSYİH | Gölge Ekonomi (%) | Fiili Güç Odakları & Rejim Tipi | Rapor Bağlantısı |
| :--- | :---: | :--- | :---: | :---: | :--- | :--- |
"""

for c in sorted(regional_countries.get("africa", []), key=lambda x: x["name"]):
    AFR_MD += f"| **{c['name']}** | `{c['code']}` | {c['capital']} | ${c['gdp_usd_b']:,.1f}B | %{c['shadow_economy_pct']} | {c.get('official_leader', 'N/A')} | [{c['name']} Raporu]({c['slug']}/README.md) |\n"

# -------------------------------------------------------------
# 6. OCEANIA
# -------------------------------------------------------------
OCE_MD = f"""# 🏝️ Okyanusya & Pasifik Adaları Jeopolitik İstihbarat Dosyası (Oceania Dossier)

> "Small island states in the vast Pacific are not isolated fragments; they are giant ocean states controlling millions of square kilometers of sovereign waters."  
> — **Pacific Islands Forum Declaration**

---

## 1. Stratejik Giriş: Büyük Okyanusta Hakimiyet Mücadelesi

Okyanusya; Avustralya ve Yeni Zelanda gibi gelişmiş Batılı güç merkezleri ile binlerce ada devletinden (Melanezya, Mikronezya, Polinezya) oluşur. Coğrafi olarak izole görünmesine rağmen, gezegenin en büyük Münhasır Ekonomik Bölgelerine (MEB) ve transpasifik fiber optik kablo rotalarına ev sahipliği yapar.

Temel Jeopolitik Dinamikler:
* **AUKUS Paktı:** Avustralya'nın nükleer enerjili denizaltılarla donatılması ve ABD-İngiltere ile derin askeri entegrasyonu.
* **Çin'in Pasifik'e Açılma Hamlesi:** Solomon Adaları ile imzalanan gizli güvenlik paktı, liman ve havaalanı inşaatları.
* **Kritik Deniz Tabanı Madenciliği:** Okyanus tabanındaki nikel, kobalt ve manganez nodülleri üzerinde uluslararası ruhsat kapışması.

---

## 2. Bölge Ülkeleri ve Karşılaştırmalı İstihbarat Atlası

| Ülke / Bölge | ISO | Başkent | Nominal GSYİH | Gölge Ekonomi (%) | Fiili Güç Odakları & Rejim Tipi | Rapor Bağlantısı |
| :--- | :---: | :--- | :---: | :---: | :--- | :--- |
"""

for c in sorted(regional_countries.get("oceania", []), key=lambda x: x["name"]):
    OCE_MD += f"| **{c['name']}** | `{c['code']}` | {c['capital']} | ${c['gdp_usd_b']:,.1f}B | %{c['shadow_economy_pct']} | {c.get('official_leader', 'N/A')} | [{c['name']} Raporu]({c['slug']}/README.md) |\n"

# Write all regional dossiers
REGIONAL_FILES = {
    "middle_east": ME_MD,
    "europe": EUR_MD,
    "asia": ASIA_MD,
    "americas": AMER_MD,
    "africa": AFR_MD,
    "oceania": OCE_MD,
}

for reg_name, content in REGIONAL_FILES.items():
    dest = REGIONS_DIR / reg_name / "README.md"
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[CREATED] {dest.relative_to(BASE_DIR)}")

print("\n[SUCCESS] Tüm 6 bölge master istihbarat dosyası başarıyla üretildi!")

