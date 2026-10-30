# 📚 Veri Toplama Kılavuzu (Data Collection Guide)

Bu kılavuz, **Küresel Röntgen (Global X-Ray)** projesine veri toplarken, işlerken ve sisteme entegre ederken uyulması gereken metodolojiyi ve standartları belirler.

---

## 🎯 Temel Felsefe

Küresel Röntgen; resmi verilerin ötesine geçerek devletlerin gerçek karar mekanizmalarını, sermaye akışlarını ve derin güç odaklarını haritalandırmayı amaçlar. Ancak bunu yaparken spekülasyona, teyitsiz dedikoduya veya asılsız komplo teorilerine asla yer vermez. Her veri, somut bir dayanak ve rasyonel metodolojiyle sunulmalıdır.

---

## 🏛️ 4 Katmanlı Veri Toplama Protokolü

### Katman 1: Temel Taşlar (Kültür, Coğrafya ve Demografi)
- **Hedef Dosyalar:** `society_history.md`, `demographics.csv`
- **Toplanacak Veriler:**
  - Nüfus, yaş piramidi, kentleşme oranı, etnik ve dilsel kırılımlar.
  - Tarihsel kırılma anları, ulusal travmalar ve mitler.
  - Etnik ve mezhepsel fay hatları, bölgesel ayrımlar.
- **Kaynak Standartları:** BM Nüfus Fonu (UNFPA), Dünya Bankası, Pew Research, yerel istatistik kurumları, bağımsız akademik sosyoloji çalışmaları.

### Katman 2: Resmi Vitrin (The De Jure State)
- **Hedef Dosyalar:** `constitution_gov.md`
- **Toplanacak Veriler:**
  - Anayasal rejim (Başkanlık, Yarı-Başkanlık, Parlamenter vb.).
  - Yürütme, yasama ve yargı organlarının resmi işleyişi.
  - Resmi ittifaklar, askeri paktlar ve uluslararası antlaşmalar.
- **Kaynak Standartları:** Resmi Gazeteler, Hükümet portalları, V-Dem Enstitüsü, Freedom House yasal analizleri.

### Katman 3: Yüzey Ekonomisi (The Official Economy)
- **Hedef Dosyalar:** `macroeconomics.json`
- **Toplanacak Veriler:**
  - Nominal GSYH, Satın Alma Gücü Paritesi (SAGP), Enflasyon, Kamu Borcu / GSYH oranı.
  - En büyük ihracat ve ithalat kalemleri (HS kodları bazında).
  - Başlıca dış ticaret ortakları ve kritik emtia bağımlılıkları.
- **Kaynak Standartları:** IMF WEO, Dünya Bankası Open Data, UN Comtrade, OEC (Observatory of Economic Complexity).

### Katman 4: Karanlık Madde (OSINT & The De Facto Power)
- **Hedef Dosyalar:** `real_power_dynamics.md`, `oligarch_network.csv`, `media_censorship_matrix.md`
- **Toplanacak Veriler:**
  - Gölge karar alıcılar (aile hanedanları, askeri cuntalar, istihbarat elitleri, oligark konsorsiyumları).
  - Devlet ihaleleri, kamu kaynaklarının transfer edildiği holdingler ve offshore sermaye transferleri.
  - Medya sahiplik haritası, oto-sansür mekanizmaları ve dijital gözetim araçları (Pegasus vb.).
  - Küresel ve bölgesel uydu statüsü, dış vesayet ilişkileri.
- **Kaynak Standartları:** ICIJ (Panama/Pandora Papers), OCCRP, Bellingcat, Transparency International CPI, Mahkeme iddianameleri, bağımsız araştırmacı gazetecilik konsorsiyumları.

---

## 📋 Dosya ve İsimlendirme Standartları

1. Ülke klasör adları küçük harf ve İngilizce ISO standardında olmalıdır: örn. `turkey`, `united_states`, `russia`, `china`, `germany`, `saudi_arabia`.
2. Markdown dosyalarında başlıklar h1 (`#`), alt başlıklar h2 (`##`) hiyerarşisine uymalıdır.
3. CSV dosyalarında ayırıcı virgül (`,`) ve kodlama `UTF-8` olmalıdır.
4. JSON dosyaları 2 boşluk girintili, geçerli JSON sözdiziminde olmalıdır.
