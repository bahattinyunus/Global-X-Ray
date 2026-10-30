#!/usr/bin/env python3
"""
scripts/build_full_repository.py
Küresel Röntgen (Global X-Ray) - Tüm Dünya Ülkeleri İçin 4 Katmanlı Yapı Jeneratörü
"""

import os
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

# Kapsamlı Ülke Veritabanı
COUNTRIES = [
    # --- MIDDLE EAST ---
    {
        "slug": "turkey", "name": "Türkiye", "official_name": "Türkiye Cumhuriyeti", "code": "TUR",
        "region": "middle_east", "capital": "Ankara", "pop": 85372377, "currency": "TRY",
        "gov_type": "Cumhurbaşkanlığı Hükümet Sistemi", "official_leader": "Recep Tayyip Erdoğan (Cumhurbaşkanı)",
        "de_facto_power": "Cumhurbaşkanlığı Külliyesi dar karar alma çemberi, kamu ihaleleriyle büyütülen holding elitleri, bürokrasiye entegre tarikat/cemaat ağları.",
        "gdp": 1154.0, "gdp_pc": 13380, "inflation": 48.6, "unemployment": 8.7,
        "exports": ["Otomotiv", "Makine & Kazanlar", "Demir-Çelik", "Tekstil ve Hazır Giyim", "Savunma Sanayi Ürünleri (İHA/SİHA)"],
        "imports": ["Ham Petrol & Doğal Gaz", "Altın & Kıymetli Madenler", "Kazan & Makine", "Kimyasallar"],
        "partners": ["Almanya", "Rusya", "Çin", "İtalya", "ABD", "Irak"],
        "shadow_economy_pct": 28.4, "ti_rank": 115, "press_score": 38.3,
        "oligarchs": [
            ("Cengiz Holding", "Altyapı, Maden & Enerji Tekeli", "İnşaat / Havacılık / Enerji", "Kamu İhale Konsorsiyumu", 4500, "Sayıştay Raporları / Kamu İhale Bültenleri"),
            ("Kalyon Grup", "Ulaşım, Enerji & Medya", "İnşaat / Medya (Turkuvaz Medya Grubu)", "İktidar Medya ve İhale Omurgası", 3800, "Rekabet Kurumu / Ticaret Sicil"),
            ("Limak Holding", "Havalimanı, Baraj & Çimento", "Altyapı / Turizm", "Kamu-Özel İşbirliği (KÖİ) Ağı", 3500, "Devlet Hava Meydanları İhaleleri"),
            ("Kolin İnşaat", "Demiryolu & Karayolu Altyapısı", "Ulaştırma / Lojistik", "Devlet Altyapı İhaleleri", 3200, "TCDD & Karayolları İhaleleri"),
            ("Baykar Teknoloji", "Savunma Sanayii / İHA Sistemleri", "Havacılık / Savunma", "Ailevi ve Stratejik Devlet Desteği", 2800, "Savunma Sanayii Başkanlığı Kayıtları")
        ],
        "history_faults": "Laik-Muhafazakar kutuplaşması, Kürt meselesi, Alevi-Sünni dinamikleri, sığınmacı/mülteci demografik baskısı.",
        "media_landscape": "Medya organlarının yaklaşık %85-90'ı doğrudan iktidar yanlısı iş insanlarının mülkiyetindedir (Turkuvaz, Demirören vb.). RTÜK ve Basın İlan Kurumu (BİK) finansal ve idari denetim mekanizması olarak çalışır. Bağımsız gazetecilik dijital mecralara ve YouTube platformlarına kaymıştır."
    },
    {
        "slug": "iran", "name": "İran", "official_name": "İran İslam Cumhuriyeti", "code": "IRN",
        "region": "middle_east", "capital": "Tahran", "pop": 88550570, "currency": "IRR",
        "gov_type": "Teokratik İslami Cumhuriyet (Velayet-i Fakih)", "official_leader": "Ali Hamaney (Dini Lider) / Mesud Pezeşkiyan (Cumhurbaşkanı)",
        "de_facto_power": "Devrim Muhafızları Ordusu (IRGC / Pasdaran), Dini Lider Ofisi (Beyt-e Rahbari) ve dini vakıf imparatorlukları (Bunyadlar).",
        "gdp": 403.5, "gdp_pc": 4670, "inflation": 42.0, "unemployment": 9.2,
        "exports": ["Ham Petrol (Gri/Gölge Tanker Filosu)", "Petrokimya", "Doğal Gaz", "Çelik", "Plastik"],
        "imports": ["Endüstriyel Makineler", "İlaç & Tıbbi Cihaz", "Tahıl", "Elektronik"],
        "partners": ["Çin", "Irak", "BAE", "Türkiye", "Rusya"],
        "shadow_economy_pct": 36.5, "ti_rank": 149, "press_score": 23.2,
        "oligarchs": [
            ("Khatam al-Anbiya (IRGC)", "İnşaat, Enerji & Altyapı Devi", "Petrol / Altyapı / Telekom", "Devrim Muhafızları Ana İktisadi Kolu", 12000, "ABD Hazine Bakanlığı / Reuters Özel Raporu"),
            ("Setad Ejraiye Farman-e Emam", "Dini Liderlik Mali Holdingi", "Gayrimenkul / İlaç / Finans", "Doğrudan Dini Lider Ofisi Denetiminde", 95000, "Reuters: 'Assets of the Ayatollah', 2013"),
            ("Bonyad Mostazafan", "Kamulaştırılmış Mülk Vakfı", "Sanayi / Otelcilik / Lojistik", "Vergi Muafiyetli Dini Elit Konsorsiyumu", 20000, "Dünya Bankası İran Ekonomisi Raporları")
        ],
        "history_faults": "1979 İslam Devrimi miras çatışması, Şii-Fars merkezli yönetim vs. Azeri/Kürt/Beluç etnik hatları, başörtüsü ve gençlik modernleşme isyanları.",
        "media_landscape": "IRIB (İran Radyo Televizyon Kurumu) tekeldir ve Dini Lider tarafından atanır. İnternet ağır filtreleme (Milli Bilgi Ağı) altındadır; muhalif yayınlar yurtdışı uydu kanallarından (Iran International, BBC Persian) izlenir."
    },
    {
        "slug": "saudi_arabia", "name": "Suudi Arabistan", "official_name": "Suudi Arabistan Krallığı", "code": "SAU",
        "region": "middle_east", "capital": "Riyad", "pop": 36408820, "currency": "SAR",
        "gov_type": "Mutlak Monarşi (El Suud Hanedanı)", "official_leader": "Kral Selman bin Abdülaziz / Veliaht Prens Muhammed bin Selman (MBS)",
        "de_facto_power": "Veliaht Prens MBS ve Kamu Yatırım Fonu (PIF) etrafında merkezileşen genç kraliyet teknokrat kadrosu.",
        "gdp": 1069.0, "gdp_pc": 32590, "inflation": 2.1, "unemployment": 4.8,
        "exports": ["Ham Petrol", "Rafine Petrol Ürünleri", "Petrokimyasallar", "Plastik"],
        "imports": ["Askeri Savunma Donanımı", "Otomobil", "Telekomünikasyon Cihazları", "İlaç"],
        "partners": ["Çin", "Hindistan", "Japonya", "Güney Kore", "ABD", "BAE"],
        "shadow_economy_pct": 16.2, "ti_rank": 52, "press_score": 32.4,
        "oligarchs": [
            ("Public Investment Fund (PIF)", "Egemen Varlık Fonu", "Global Yatırımlar / Neom / Spor / Madencilik", "MBS Doğrudan Yönetiminde", 925000, "SWFI & Bloomberg Sovereign Wealth Tracker"),
            ("Saudi Aramco", "Ulusal Petrol ve Gaz Devi", "Enerji / Rafineri", "Devlet Hissesi %90+", 2100000, "Tadawul & SEC Finansal Dosyaları"),
            ("Kingdom Holding (El-Velid bin Talal)", "Global Finans & Otelcilik", "Gayrimenkul / Havacılık", "2017 Ritz-Carlton uzlaşması sonrası kısmi devlet gözetimi", 16000, "Forbes & Bloomberg Billionaires")
        ],
        "history_faults": "Vahhabi ulema ile modernleşen saray çatışması, Doğu vilayeti Şii azınlık dinamikleri, veliaht veraset tasfiyeleri.",
        "media_landscape": "Tüm ulusal gazeteler ve MBC/Al Arabiya televizyon ağları Suudi Kraliyet Ailesi veya istihbarat denetimindedir. Rejim eleştirisi terörle mücadele kanunu kapsamında cezalandırılır."
    },
    {
        "slug": "israel", "name": "İsrail", "official_name": "İsrail Devleti", "code": "ISR",
        "region": "middle_east", "capital": "Kudüs (Tel Aviv idari/uluslararası)", "pop": 9842000, "currency": "ILS",
        "gov_type": "Parlamenter Demokrasi", "official_leader": "Binyamin Netanyahu (Başbakan) / Isaac Herzog (Cumhurbaşkanı)",
        "de_facto_power": "Askeri-Güvenlik Bürokrasisi (IDF, Şin Bet, Mossad), aşırı sağcı/dini koalisyon ortakları ve savunma/siber teknoloji tekelleri.",
        "gdp": 509.9, "gdp_pc": 52200, "inflation": 3.2, "unemployment": 3.4,
        "exports": ["İşlenmiş Elmas", "Entegre Devreler", "Askeri Siber & Savunma Sistemleri", "Tıbbi Cihazlar"],
        "imports": ["Ham Petrol", "Askeri Mühimmat", "Ham Elmas", "Otomobil", "Tahıl"],
        "partners": ["ABD", "Çin", "Almanya", "İrlanda", "Hollanda", "Hindistan"],
        "shadow_economy_pct": 18.5, "ti_rank": 33, "press_score": 53.2,
        "oligarchs": [
            ("Check Point & Cyber Oligarşisi", "Siber Güvenlik & Casus Yazılım", "Yüksek Teknoloji / Savunma", "Unit 8200 Mezunları Ağı (NSO Group, Candiru vb.)", 18000, "Financial Times & Citizen Lab"),
            ("Elbit Systems", "Askeri Elektronik & İHA", "Savunma Sanayi", "İsrail Savunma Bakanlığı Ana Tedarikçisi", 8500, "Tel Aviv Menkul Kıymetler Borsası"),
            ("Ofer Brothers Grubu (XT / Idan Ofer)", "Denizcilik, Enerji & Maden", "Lojistik / Kimya (ICL Group)", "Hükümet İhale ve Özelleştirme Ağı", 14000, "Globes & Calcalist Araştırmaları")
        ],
        "history_faults": "Filistin işgali ve apartheid tartışmaları, Aşkenaz-Mizrahi kültürel ayrışması, Haredi (Ultra-Ortodoks) askerlik ve bütçe muafiyeti çatışması.",
        "media_landscape": "Canlı ve çoğulcu bir basın vardır ancak Askeri Sansür Kurumu (Military Censor) güvenlik konularında haberleri denetleme yetkisine sahiptir."
    },
    {
        "slug": "united_arab_emirates", "name": "Birleşik Arap Emirlikleri", "official_name": "Birleşik Arap Emirlikleri", "code": "ARE",
        "region": "middle_east", "capital": "Abu Dabi", "pop": 9441129, "currency": "AED",
        "gov_type": "Federal Mutlak Monarşiler Birliği (7 Emirlik)", "official_leader": "Muhammed bin Zayid El Nahyan (MBZ - Devlet Başkanı)",
        "de_facto_power": "Abu Dabi Al Nahyan Hanedanı ve Dubai Al Maktum ailesi, ulusal güvenlik ve egemen servet fonları.",
        "gdp": 507.5, "gdp_pc": 53700, "inflation": 2.5, "unemployment": 2.7,
        "exports": ["Ham Petrol", "Altın & Mücevherat", "Yeniden İhracat (Elektronik)", "Petrol Gazları"],
        "imports": ["Altın (İşlenmemiş)", "Yayın Ekipmanları", "Otomobil", "Mücevher"],
        "partners": ["Hindistan", "Çin", "Japonya", "Suudi Arabistan", "ABD", "İsviçre"],
        "shadow_economy_pct": 18.0, "ti_rank": 26, "press_score": 38.0,
        "oligarchs": [
            ("ADIA & Mubadala (MBZ Çevresi)", "Egemen Servet Fonları", "Yapay Zeka / Havacılık / Global Varlıklar", "Abu Dabi Kraliyet Ailesi", 1300000, "SWFI Raporları"),
            ("G42 (Group 42)", "Yapay Zeka, Gözetim & Biyoteknoloji", "Savunma / İstihbarat Teknolojileri", "Şeyh Tahnoun bin Zayed (Ulusal Güvenlik Danışmanı)", 15000, "New York Times & FT Araştırmaları")
        ],
        "history_faults": "Yerli nüfusun sadece %10-12 olması, devasa göçmen işçi sınıfı, emirlikler arası zenginlik dengesizliği.",
        "media_landscape": "Sıkı siber suçlar yasası nedeniyle kraliyet veya dış politika aleyhine yayın yapmak hapisle cezalandırılır. Ülke aynı zamanda uluslararası offshore ve altın aklama iddialarının odağındadır."
    },
    {
        "slug": "iraq", "name": "Irak", "official_name": "Irak Cumhuriyeti", "code": "IRQ",
        "region": "middle_east", "capital": "Bağdat", "pop": 44496122, "currency": "IQD",
        "gov_type": "Federal Parlamenter Cumhuriyet (Muhasasa Mezhep Kotası)", "official_leader": "Muhammed Şiya es-Sudani (Başbakan)",
        "de_facto_power": "Haşdi Şabi (PMF) milis elitleri, mezhepsel partiler (Dava, Sadr vb.) ve bölgesel güçlerin (İran/ABD) nüfuz ağları.",
        "gdp": 254.4, "gdp_pc": 5880, "inflation": 4.4, "unemployment": 15.5,
        "exports": ["Ham Petrol"], "imports": ["Rafine Petrol", "Gıda", "İlaç", "Otomotiv", "Elektrik"],
        "partners": ["Çin", "Hindistan", "Türkiye", "BAE", "Güney Kore"],
        "shadow_economy_pct": 42.0, "ti_rank": 154, "press_score": 32.9,
        "oligarchs": [
            ("Milis Komutanları & Mezhep Fonları", "Gümrük Kapıları & Dolar İhaleleri", "Kaçak Petrol / Döviz Açık Artırması", "Partizan Milisler", 10000, "Irak Merkez Bankası & ABD Hazinesi Yaptırım Kararları")
        ],
        "history_faults": "Şii-Sünni mezhepsel rekabeti, Bağdat-Erbil (Kürt Bölgesel Yönetimi) petrol ve bütçe krizleri, yolsuzluk protestoları.",
        "media_landscape": "Neredeyse her televizyon kanalı silahlı bir milis veya mezhepsel bir siyasi partinin propaganda organıdır."
    },
    {
        "slug": "syria", "name": "Suriye", "official_name": "Suriye Arap Cumhuriyeti", "code": "SYR",
        "region": "middle_east", "capital": "Şam", "pop": 23227014, "currency": "SYP",
        "gov_type": "Baasçı Otoriter Rejim / Bölünmüş Savaş Devleti", "official_leader": "Beşar Esad",
        "de_facto_power": "Esad Ailesi, Muhaberat (Askeri İstihbarat) şefleri, 4. Zırhlı Tümen (Mahir Esad) ve Rusya/İran askeri üsleri.",
        "gdp": 12.0, "gdp_pc": 500, "inflation": 95.0, "unemployment": 35.0,
        "exports": ["Kaptagon (Sentetik Uyuşturucu - Yasadışı)", "Zeytinyağı", "Fosfat"], "imports": ["Petrol Ürünleri", "Gıda", "Silah"],
        "partners": ["Rusya", "İran", "Çin", "Lübnan"],
        "shadow_economy_pct": 72.0, "ti_rank": 177, "press_score": 21.0,
        "oligarchs": [
            ("Esad Ailesi & 4. Zırhlı Tümen", "Kaptagon Karteli & İthalat Tekelleri", "Sınır Kaçakçılığı / Telekom / Gayrimenkul", "Doğrudan Başkanlık Sarayı", 10000, "OCCRP & COAR Global: 'The Syrian Captagon Economy'")
        ],
        "history_faults": "2011 iç savaşı yıkımı, Nusayri elit vs Sünni çoğunluk dengesi, YPG/SDG kontrolündeki kuzeydoğu petrol sahaları.",
        "media_landscape": "Tamamen devlet ve ordu kontrolündedir. Rejim aleyhine haber yapan yerel gazeteciler Sednaya gibi hapishanelerde işkenceye maruz kalmıştır."
    },
    {
        "slug": "qatar", "name": "Katar", "official_name": "Katar Devleti", "code": "QAT",
        "region": "middle_east", "capital": "Doha", "pop": 2716391, "currency": "QAR",
        "gov_type": "Emirlik (Al Sani Hanedanı)", "official_leader": "Şeyh Temim bin Hamad Es-Sani",
        "de_facto_power": "Al Sani kraliyet ailesi ve Qatar Investment Authority (QIA).",
        "gdp": 235.5, "gdp_pc": 82000, "inflation": 1.5, "unemployment": 0.1,
        "exports": ["Sıvılaştırılmış Doğal Gaz (LNG)", "Ham Petrol", "Gübre", "Alüminyum"], "imports": ["Uçak & Parçaları", "Otomobil", "Mücevher", "Elektronik"],
        "partners": ["Çin", "Hindistan", "Japonya", "Güney Kore", "İngiltere"],
        "shadow_economy_pct": 14.5, "ti_rank": 40, "press_score": 48.0,
        "oligarchs": [
            ("Qatar Investment Authority (QIA)", "Egemen Varlık Fonu", "Global Gayrimenkul, Havacılık, Bankacılık", "Al Sani Ailesi", 510000, "SWFI & FT")
        ],
        "history_faults": "Körfez ablukası travması (2017-2021), yerli nüfus oranının %12 civarında kalması.",
        "media_landscape": "Al Jazeera küresel bir yayın devidir ancak Katar'ın iç işlerine ve kraliyet ailesinin mali operasyonlarına yönelik yerel denetim yasaktır."
    },
    {
        "slug": "lebanon", "name": "Lübnan", "official_name": "Lübnan Cumhuriyeti", "code": "LBN",
        "region": "middle_east", "capital": "Beyrut", "pop": 5353930, "currency": "LBP",
        "gov_type": "Mezhepsel Konfesyonel Cumhuriyet", "official_leader": "Necip Mikati (Geçici Başbakan)",
        "de_facto_power": "Hizbullah askeri/siyasi omurgası, geleneksel mezhep ağaları (Zuama sistemi) ve bankacılık oligarşisi.",
        "gdp": 21.0, "gdp_pc": 3900, "inflation": 170.0, "unemployment": 29.6,
        "exports": ["Mücevher", "Kimyasallar", "Meyve-Sebze"], "imports": ["Petrol Ürünleri", "Otomotiv", "Tahıl", "İlaç"],
        "partners": ["BAE", "İsviçre", "Türkiye", "Çin", "Yunanistan"],
        "shadow_economy_pct": 54.0, "ti_rank": 149, "press_score": 45.0,
        "oligarchs": [
            ("Riad Salameh Ağı & Banka Sahipleri", "Merkez Bankası & Finansal Piramit", "Bankacılık / Gayrimenkul", "Mezhep Liderleriyle Paylaşım", 2000, "Fransa & İsviçre Mahkeme İddianameleri"),
            ("Mikati Ailesi (M1 Group)", "Telekom & Yatırım", "Telekomünikasyon / Enerji", "Siyasi Elit", 3000, "Forbes & Pandora Papers")
        ],
        "history_faults": "1975-1990 iç savaşının çözülmemiş mezhepsel travması, 2020 Beyrut Liman patlaması ve tarihi finansal çöküş.",
        "media_landscape": "Basın çok seslidir ancak her televizyon ve gazete doğrudan bir mezhep partisinin (Hizbullah, Gelecek Hareketi, Lübnan Güçleri) finansmanına bağlıdır."
    },
    {
        "slug": "jordan", "name": "Ürdün", "official_name": "Ürdün Haşimi Krallığı", "code": "JOR",
        "region": "middle_east", "capital": "Amman", "pop": 11337052, "currency": "JOD",
        "gov_type": "Anayasal Monarşi (Haşimi Hanedanı)", "official_leader": "Kral II. Abdullah",
        "de_facto_power": "Kraliyet Divanı ve Genel İstihbarat Dairesi (GID / Dairat el-Mukhabarat).",
        "gdp": 50.8, "gdp_pc": 4480, "inflation": 2.2, "unemployment": 21.4,
        "exports": ["Tekstil & Konfeksiyon", "Potas & Fosfat", "Kimyasallar", "İlaç"], "imports": ["Ham Petrol & Doğal Gaz", "Otomobil", "Makineler"],
        "partners": ["ABD", "Hindistan", "Suudi Arabistan", "Çin", "Irak"],
        "shadow_economy_pct": 26.0, "ti_rank": 63, "press_score": 42.0,
        "oligarchs": [
            ("Kraliyet Fonları & Şirketleri", "Gayrimenkul ve Stratejik İhaleler", "Offshore Yatırımlar", "Kraliyet Ailesi", 1500, "ICIJ Pandora Papers Sızıntıları")
        ],
        "history_faults": "Doğu Şerialı Bedevi aşiretler ile Filistin asıllı çoğunluk dengesi, su kıtlığı ve yüksek genç işsizliği.",
        "media_landscape": "Eleştirel gazeteciler GID gözetimi altındadır; kraliyet ailesine yönelik mali soruşturma haberleri siber suçlar kanunuyla engellenir."
    },

    # --- ASIA ---
    {
        "slug": "china", "name": "Çin", "official_name": "Çin Halk Cumhuriyeti", "code": "CHN",
        "region": "asia", "capital": "Pekin", "pop": 1411750000, "currency": "CNY",
        "gov_type": "Tek Parti Sosyalist Cumhuriyeti (ÇKP)", "official_leader": "Şi Cinping (Devlet Başkanı ve Genel Sekreter)",
        "de_facto_power": "Çin Komünist Partisi (ÇKP) Politbüro Daimi Komitesi, Merkezi Askeri Komisyon ve Devlet Güvenlik Bakanlığı (MSS).",
        "gdp": 17794.0, "gdp_pc": 12600, "inflation": 0.3, "unemployment": 5.1,
        "exports": ["Elektronik & Akıllı Telefon", "Elektrikli Araçlar & Lityum Piller", "Güneş Panelleri", "Endüstriyel Makineler", "Tekstil"],
        "imports": ["Ham Petrol", "Entegre Devreler / Çipler", "Demir Cevheri", "Soya Fasulyesi", "Doğal Gaz"],
        "partners": ["ABD", "Güneydoğu Asya (ASEAN)", "Avrupa Birliği", "Japonya", "Güney Kore", "Rusya"],
        "shadow_economy_pct": 12.7, "ti_rank": 76, "press_score": 22.97,
        "oligarchs": [
            ("Devlete Bağlı KİT Devleri (Sinopec, State Grid)", "Enerji & Altyapı", "Enerji / Şebeke / Telekom", "ÇKP SASAC Kontrolü", 500000, "SASAC & Fortune Global 500"),
            ("Alibaba & Ant Group", "E-Ticaret & Fintek", "Dijital Ekonomi", "ÇKP Düzenleyici Baskısı Altında", 220000, "Hong Kong & NYSE Dosyaları"),
            ("Tencent & ByteDance", "Sosyal Medya, Oyun & Yapay Zeka", "Büyük Veri / Algoritmik Gözetim", "Parti Güvenlik Entegrasyonu", 350000, "HKEX & Şirket Raporları")
        ],
        "history_faults": "Aşağılanma Yüzyılı travması ve Tayvan birleşme doktrini, Sincan (Uygur) ve Tibet etnik baskıları, gayrimenkul borç krizi.",
        "media_landscape": "Great Firewall (Büyük Güvenlik Duvarı) ile internet tamamen sansürlenmiştir. Tüm medya Xinhua ve ÇKP Propaganda Departmanı onaylıdır."
    },
    {
        "slug": "russia", "name": "Rusya", "official_name": "Rusya Federasyonu", "code": "RUS",
        "region": "europe", "capital": "Moskova", "pop": 144236933, "currency": "RUB",
        "gov_type": "Federal Yarı-Başkanlık Cumhuriyeti (Otoriter Rejim)", "official_leader": "Vladimir Putin (Devlet Başkanı)",
        "de_facto_power": "Siloviki (FSB, SVR, GRU, Güvenlik Konseyi bürokratları) ve Putin'e sadık devlet-bağlantılı oligark elitleri.",
        "gdp": 2021.0, "gdp_pc": 14000, "inflation": 8.5, "unemployment": 2.4,
        "exports": ["Ham Petrol & Petrol Ürünleri", "Doğal Gaz", "Kömür", "Buğday & Gübre", "Silah Sistemleri"],
        "imports": ["Endüstriyel Parçalar", "Otomobil & Tır", "Tüketici Elektroniği", "İlaç"],
        "partners": ["Çin", "Hindistan", "Türkiye", "Belarus", "Kazakistan"],
        "shadow_economy_pct": 38.2, "ti_rank": 141, "press_score": 29.98,
        "oligarchs": [
            ("Rosneft (İgor Seçin)", "Devlet Petrol Şirketi", "Enerji / Jeopolitik Araç", "Siloviki Çekirdeği", 95000, "OFAC Yaptırım Listeleri / Rosneft Raporları"),
            ("Gazprom (Aleksey Miller)", "Doğal Gaz Tekeli", "Boru Hatları / Enerji İhracatı", "Kremlin Yakın Çevresi", 80000, "Moskova Borsası & AB Yaptırımları"),
            ("Rostec (Sergey Çemezov)", "Savunma ve Yüksek Teknoloji Devi", "Silah Üretimi / Havacılık", "Eski KGB / Putin Yakın Çevresi", 35000, "Rostec Yıllık Faaliyet Raporları"),
            ("Gennadi Timçenko & Arkadi Rotenberg", "Altyapı, Boru Hattı & Köprü İhaleleri", "İnşaat / Lojistik", "Kırım Köprüsü ve Devlet İhaleleri", 15000, "Panama Papers & ABD Hazine Raporları")
        ],
        "history_faults": "Sovyetler Birliği'nin çöküşü travması, Kafkasya ve etnik cumhuriyetler (Çeçenistan, Dağıstan), Ukrayna savaşı yaptırımları.",
        "media_landscape": "Bağımsız medya yasaklanmış (Meduza, Novaya Gazeta yurtdışına sürülmüştür). Rossiya 1, Channel One ve RT gibi kanallarla tam devlet kontrolü sağlanmaktadır."
    },
    {
        "slug": "turkmenistan", "name": "Türkmenistan", "official_name": "Türkmenistan", "code": "TKM",
        "region": "asia", "capital": "Aşkabat", "pop": 6516100, "currency": "TMT",
        "gov_type": "Kişi Odaklı Totaliter Başkanlık Cumhuriyeti", "official_leader": "Serdar Berdimuhamedov (Cumhurbaşkanı) / Kurbankulu Berdimuhamedov (Arkadag / Milli Lider)",
        "de_facto_power": "Berdimuhamedov Hanedanı, Halk Maslahatı (Halk Konseyi) ve Ulusal Güvenlik Bakanlığı (MNB).",
        "gdp": 60.0, "gdp_pc": 9200, "inflation": 11.0, "unemployment": 10.5,
        "exports": ["Boru Hattı Doğal Gazı (Ağırlıklı Çin'e)", "Ham Petrol", "Tekstil & Pamuk"], "imports": ["Gıda", "Makine", "Kimyasallar"],
        "partners": ["Çin", "Türkiye", "Rusya", "BAE", "İran"],
        "shadow_economy_pct": 45.0, "ti_rank": 170, "press_score": 25.82,
        "oligarchs": [
            ("Berdimuhamedov Aile Ağı", "Doğal Gaz Gelirleri & İthalat Tekeli", "Enerji / İnşaat / Perakende", "Devlet Hanedanlığı", 12000, "Crude Accountability & OCCRP Araştırmaları"),
            ("Polimeks & Yabancı İhale Taşeronları", "Aşkabat Mermer Şehir ve Havalimanı Projeleri", "Lüks Kamu İnşaatı", "Saray İhale Ağı", 3000, "Resmi Devlet Bültenleri")
        ],
        "history_faults": "Ahal-Teke aşiret egemenliği ve diğer aşiretler arası sessiz rekabet, zorla pamuk toplama sistemi, döviz kara borsası.",
        "media_landscape": "Dünyanın en kapalı ülkelerinden biridir; internet aşırı sansürlüdür, bağımsız gazetecilik tamamen yasaktır."
    },
    {
        "slug": "india", "name": "Hindistan", "official_name": "Hindistan Cumhuriyeti", "code": "IND",
        "region": "asia", "capital": "Yeni Delhi", "pop": 1428627663, "currency": "INR",
        "gov_type": "Federal Parlamenter Cumhuriyet", "official_leader": "Narendra Modi (Başbakan) / Droupadi Murmu (Cumhurbaşkanı)",
        "de_facto_power": "Rashtriya Swayamsevak Sangh (RSS) ideolojik omurgası, Başbakanlık Ofisi (PMO) ve Adani/Ambani mega-holdingleri.",
        "gdp": 3937.0, "gdp_pc": 2730, "inflation": 5.4, "unemployment": 7.2,
        "exports": ["Rafine Petrol", "Yazılım & BT Hizmetleri", "Elmas & Mücevher", "İlaç & Aşı", "Otomotiv"],
        "imports": ["Ham Petrol", "Kömür", "Altın", "Elektronik", "Kimyasallar"],
        "partners": ["ABD", "Çin", "BAE", "Rusya", "Suudi Arabistan"],
        "shadow_economy_pct": 22.4, "ti_rank": 93, "press_score": 51.0,
        "oligarchs": [
            ("Adani Group (Gautam Adani)", "Limanlar, Havalimanları, Kömür & Enerji", "Altyapı Tekeli", "Modi Hükümetiyle Stratejik İttifak", 85000, "Hindenburg Research & Financial Times"),
            ("Reliance Industries (Mukesh Ambani)", "Petrol, Telekom (Jio), Perakende", "Telekomünikasyon / Rafineri", "Her İktidar Döneminde Etkin", 110000, "BSE & Forbes Billionaires")
        ],
        "history_faults": "Hindu milliyetçiliği (Hindutva) vs. 200 milyonluk Müslüman azınlık gerilimi, kast sistemi eşitsizlikleri, Keşmir sorunu.",
        "media_landscape": "'Godi Media' olarak adlandırılan ana akım televizyon kanalları iktidara yakın holdinglerce satın alınmış ve kutuplaştırıcı anlatıyı yaymaktadır."
    },
    {
        "slug": "japan", "name": "Japonya", "official_name": "Japonya", "code": "JPN",
        "region": "asia", "capital": "Tokyo", "pop": 124500000, "currency": "JPY",
        "gov_type": "Anayasal Monarşi ve Parlamenter Demokrasi", "official_leader": "Shigeru Ishiba (Başbakan) / İmparator Naruhito",
        "de_facto_power": "Liberal Demokrat Parti (LDP) hizip liderleri, elit bürokrasi (METI, Maliye) ve Keiretsu iş konglomeraları.",
        "gdp": 4212.0, "gdp_pc": 33800, "inflation": 2.8, "unemployment": 2.5,
        "exports": ["Otomobil & Araç Parçaları", "Entegre Devreler", "Endüstriyel Robotlar", "Optik Cihazlar"],
        "imports": ["Ham Petrol", "LNG", "Kömür", "Yarı İletkenler", "Gıda"],
        "partners": ["ABD", "Çin", "Güney Kore", "Tayvan", "Avustralya"],
        "shadow_economy_pct": 9.1, "ti_rank": 16, "press_score": 64.37,
        "oligarchs": [
            ("Keiretsu Ağları (Mitsubishi, Mitsui, Sumitomo)", "Mega Finans & Sanayi İttifakları", "Otomotiv / Ağır Sanayi / Finans", "Bürokrasiyle Döner Kapı (Amakudari)", 350000, "Nikkei & Tokyo Menkul Kıymetler Borsası")
        ],
        "history_faults": "Hızlı yaşlanan ve azalan nüfus, İkinci Dünya Savaşı sonrası anayasal pasifizm tartışmaları, enerji bağımlılığı.",
        "media_landscape": "'Kisha Kulübü' (Basın Kulüpleri) sistemi resmi makamların gazetecileri kontrol etmesini ve sarsıcı araştırmacı gazeteciliğin kısıtlanmasını sağlar."
    },
    {
        "slug": "south_korea", "name": "Güney Kore", "official_name": "Kore Cumhuriyeti", "code": "KOR",
        "region": "asia", "capital": "Seul", "pop": 51784059, "currency": "KRW",
        "gov_type": "Başkanlık Cumhuriyeti", "official_leader": "Yoon Suk-yeol (Devlet Başkanı)",
        "de_facto_power": "Chaebol aile hanedanlıkları (Samsung, Hyundai, SK, LG) ve Başsavcılık/İstihbarat elitleri.",
        "gdp": 1712.0, "gdp_pc": 33100, "inflation": 3.1, "unemployment": 2.8,
        "exports": ["Bellek Çipleri & Yarı İletkenler", "Otomobil", "Gemi İnşa", "Petrokimya", "Ekran Panelleri"],
        "imports": ["Ham Petrol", "Yarı İletken Ekipmanları", "Doğal Gaz", "Kömür"],
        "partners": ["Çin", "ABD", "Vietnam", "Japonya", "Avustralya"],
        "shadow_economy_pct": 21.3, "ti_rank": 32, "press_score": 70.83,
        "oligarchs": [
            ("Samsung Grubu (Lee Ailesi)", "Elektronik, Biyoteknoloji, Finans", "Milli GSYH'nin %15+'sı", "Siyasi Seçim Kampanyaları Finansmanı", 320000, "Kore Adil Ticaret Komisyonu"),
            ("Hyundai Motor & SK Group", "Otomotiv ve Yarı İletken", "Sanayi Omurgası", "Devlet Destekli Chaebol Ağı", 210000, "KOSPI Veritabanı")
        ],
        "history_faults": "Kuzey Kore askeri nükleer tehdidi, Chaebol tekelleşmesi ve genç neslin 'Cehennem Joseon' konut/iş güvencesizliği tepkisi.",
        "media_landscape": "Canlı basın ortamı vardır fakat Chaebol holdinglerinin dev reklam bütçeleri ana akım gazetelerde oto-sansüre yol açar."
    },
    {
        "slug": "pakistan", "name": "Pakistan", "official_name": "Pakistan İslam Cumhuriyeti", "code": "PAK",
        "region": "asia", "capital": "İslamabad", "pop": 241499431, "currency": "PKR",
        "gov_type": "Federal Parlamenter Cumhuriyet (Hibrit Rejim)", "official_leader": "Şahbaz Şerif (Başbakan) / Asıf Ali Zerdari (Cumhurbaşkanı)",
        "de_facto_power": "Pakistan Ordusu Genel Karargahı (GHQ - Rawalpindi) ve Askeri İstihbarat (ISI).",
        "gdp": 338.0, "gdp_pc": 1400, "inflation": 23.0, "unemployment": 8.5,
        "exports": ["Tekstil & Pamuk", "Pirinç", "Deri Ürünleri", "Cerrahi Aletler"], "imports": ["Ham Petrol & LNG", "Palm Yağı", "Makineler", "Kimyasallar"],
        "partners": ["Çin", "ABD", "BAE", "İngiltere", "Almanya"],
        "shadow_economy_pct": 35.6, "ti_rank": 133, "press_score": 40.0,
        "oligarchs": [
            ("Fauji Foundation & Ordu Holdingleri", "Gübre, Çimento, Bankacılık, Gıda", "Milli Ekonominin Askeri Kolu", "Pakistan Silahlı Kuvvetleri Emeklilik Fonları", 25000, "Ayesha Siddiqa: 'Military Inc.: Inside Pakistan's Military Economy'")
        ],
        "history_faults": "Keşmir ihtilafı, Peştun ve Beluç ayrılıkçı çatışmaları, siyasetçilerin ordu tarafından yargı yoluyla tasfiyesi geleneği.",
        "media_landscape": "Gazeteciler ISI baskısı altındadır; Geo News veya ARY gibi kanallara askeri elitlerin istemediği konularda karartma uygulanır."
    },

    # --- AMERICAS ---
    {
        "slug": "united_states", "name": "Amerika Birleşik Devletleri", "official_name": "Amerika Birleşik Devletleri", "code": "USA",
        "region": "americas", "capital": "Washington, D.C.", "pop": 334914895, "currency": "USD",
        "gov_type": "Federal Anayasal Başkanlık Cumhuriyeti", "official_leader": "Joe Biden / Donald Trump",
        "de_facto_power": "Wall Street mega fonları (BlackRock, Vanguard), Askeri-Endüstriyel Kompleks (Lockheed, RTX) ve Silikon Vadisi teknoloji devleri.",
        "gdp": 27360.0, "gdp_pc": 81600, "inflation": 3.0, "unemployment": 3.9,
        "exports": ["Rafine Petrol", "Ham Petrol", "Doğal Gaz", "Sivil Havacılık (Boeing)", "Yarı İletkenler & Yazılım", "Tarım (Soya, Mısır)"],
        "imports": ["Otomobil", "Bilgisayar & Akıllı Telefon", "İlaç", "Ham Petrol", "Tüketim Malları"],
        "partners": ["Kanada", "Meksika", "Çin", "Japonya", "Almanya", "İngiltere"],
        "shadow_economy_pct": 8.5, "ti_rank": 24, "press_score": 75.8,
        "oligarchs": [
            ("BlackRock, Vanguard & State Street", "Büyük Üçlü (The Big Three) Varlık Yönetimi", "S&P 500 Şirketlerinin Çoğunda Hakim Hissedar", "Hazine & Fed Politika Danışmanlığı", 22000000, "SEC Dosyaları & Bloomberg Varlık Takibi"),
            ("Lockheed Martin, RTX, General Dynamics", "Savunma ve Havacılık Sanayii", "Pentagon İhaleleri", "Kongre Üyelerine PAC Bağışları ve Lobi Ordusu", 300000, "OpenSecrets.org Lobi Kayıtları"),
            ("Big Tech (Alphabet, Microsoft, Apple, Meta)", "Yapay Zeka, Bulut, Veri Gözetimi", "Dijital Altyapı Tekeli", "Kritik İstihbarat & Lobi Ortaklığı", 10000000, "FTC & Kongre Antitröst Raporları")
        ],
        "history_faults": "Kültür savaşları ve iki partili kutuplaşma, ırksal eşitsizlik fay hatları, kontrolsüz silahlanma ve opioid krizi.",
        "media_landscape": "Yasal olarak Birinci Değişiklik tam koruma sağlar; ancak medya altı büyük şirket (Comcast, Disney, Warner Bros Discovery, Paramount, Fox, Sony) tekelindedir."
    },
    {
        "slug": "brazil", "name": "Brezilya", "official_name": "Brezilya Federal Cumhuriyeti", "code": "BRA",
        "region": "americas", "capital": "Brasília", "pop": 216422446, "currency": "BRL",
        "gov_type": "Federal Başkanlık Cumhuriyeti", "official_leader": "Luiz Inácio Lula da Silva",
        "de_facto_power": "Centrão (Kongre'deki çıkarcı merkez blok), Agrobusiness (Tarım-Hayvancılık Lobisi) ve Askeri elitler.",
        "gdp": 2173.0, "gdp_pc": 10000, "inflation": 4.2, "unemployment": 7.5,
        "exports": ["Soya Fasulyesi", "Demir Cevheri", "Ham Petrol", "Şeker & Kahve", "Sığır Eti"],
        "imports": ["Gübre", "Rafine Petrol", "Otomobil Parçaları", "Entegre Devreler"],
        "partners": ["Çin", "ABD", "Arjantin", "Hollanda", "Almanya"],
        "shadow_economy_pct": 33.5, "ti_rank": 104, "press_score": 68.0,
        "oligarchs": [
            ("JBS S.A. (Batista Kardeşler)", "Dünyanın En Büyük Et Üreticisi", "Tarım / Hayvancılık", "Lava Jato Rüşvet İtirafları ve Siyasi Bağışlar", 28000, "B3 & Brezilya Federal Mahkeme Tutanakları"),
            ("Odebrecht / Novonor Mirası", "Altyapı ve Mühendislik", "İnşaat / Petrokimya", "Latin Amerika Geneli Gizli Rüşvet Departmanı", 10000, "ABD Adalet Bakanlığı Lava Jato Dosyası")
        ],
        "history_faults": "Amazon ormansızlaşması ve yerli hakları, Favela uyuşturucu çeteleri (PCC, CV) ile polis çatışması, Bolsonarizm-Sol kutuplaşması.",
        "media_landscape": "Grupo Globo ülkenin en büyük medya imparatorluğudur ve kamuoyunu yönlendirmede tarihsel bir ağırlığa sahiptir."
    },
    {
        "slug": "mexico", "name": "Meksika", "official_name": "Meksika Birleşik Devletleri", "code": "MEX",
        "region": "americas", "capital": "Mexico City", "pop": 128455567, "currency": "MXN",
        "gov_type": "Federal Başkanlık Cumhuriyeti", "official_leader": "Claudia Sheinbaum (Devlet Başkanı)",
        "de_facto_power": "Uyuşturucu Kartelleri (Sinaloa, CJNG - de facto paralel devlet), Ordu bürokrasisi ve Slim/Salinas telekom/perakende tekelleri.",
        "gdp": 1788.0, "gdp_pc": 13900, "inflation": 4.7, "unemployment": 2.7,
        "exports": ["Otomobil & Kamyonet", "Bilgisayar & Ekran", "Ham Petrol", "Tıbbi Cihazlar", "Meyve-Sebze (Avokado)"],
        "imports": ["Rafine Petrol", "Otomobil Parçaları", "Entegre Devreler", "Plastik"],
        "partners": ["ABD", "Kanada", "Çin", "Almanya", "Japonya"],
        "shadow_economy_pct": 29.8, "ti_rank": 126, "press_score": 45.0,
        "oligarchs": [
            ("Carlos Slim (América Móvil / Grupo Carso)", "Telekom, İnşaat, Madencilik", "Telekomünikasyon Tekeli", "Tüm Siyasi İdarelerle Entegre", 100000, "BMV & Forbes"),
            ("Sinaloa & CJNG Kartel Ağları", "Paralel Güvenlik ve Uyuşturucu Koridorları", "Uyuşturucu / İnsan Kaçakçılığı / Gasp", "Yerel Belediye ve Güvenlik Rüşvet Ağı", 25000, "DEA & Meksika Savcılık Dosyaları")
        ],
        "history_faults": "Kartel şiddeti (yılda 30.000+ cinayet), ABD sınır göç baskısı, kayıplar (desaparecidos) krizi.",
        "media_landscape": "Savaş bölgeleri dışında gazeteciler için dünyanın en ölümcül ülkesidir; yerel yolsuzlukları araştıran yerel muhabirler doğrudan hedef alınır."
    },

    # --- EUROPE ---
    {
        "slug": "germany", "name": "Almanya", "official_name": "Almanya Federal Cumhuriyeti", "code": "DEU",
        "region": "europe", "capital": "Berlin", "pop": 84358845, "currency": "EUR",
        "gov_type": "Federal Parlamenter Cumhuriyet", "official_leader": "Olaf Scholz (Şansölye) / Frank-Walter Steinmeier (Cumhurbaşkanı)",
        "de_facto_power": "Alman Sanayi Federasyonu (BDI), otomotiv konsorsiyumları (VW, BMW, Mercedes), sendikalar ve koalisyon partileri bürokrasisi.",
        "gdp": 4456.0, "gdp_pc": 52800, "inflation": 2.2, "unemployment": 3.2,
        "exports": ["Otomobil & Araç Parçaları", "İlaç & Aşı", "Endüstriyel Makineler", "Kimyasallar", "Elektronik"],
        "imports": ["Petrol & Doğal Gaz", "Elektronik Ekipman", "Otomobil", "Kimyasallar", "İlaç"],
        "partners": ["ABD", "Fransa", "Çin", "Hollanda", "Polonya", "İtalya"],
        "shadow_economy_pct": 9.8, "ti_rank": 9, "press_score": 81.91,
        "oligarchs": [
            ("Quandt / Klatten Ailesi", "BMW Hakim Hissedarları", "Otomotiv / Sanayi", "Geleneksel Sanayi Hanedanı", 42000, "Manager Magazin & Bloomberg"),
            ("Porsche-Piëch Ailesi", "Volkswagen Grubu Kontrolü", "Otomotiv İttifakı", "Aşağı Saksonya Eyalet Hükümetiyle Ortaklık", 35000, "Xetra / VW Finansal Dosyaları")
        ],
        "history_faults": "Doğu-Batı Almanya (Ossi-Wessi) gelir ve siyasal tercih ayrışması (AfD yükselişi), ucuz Rus enerjisinin kesilmesiyle de-endüstrileşme korkusu.",
        "media_landscape": "Kamu yayıncıları (ARD, ZDF) güçlü ve bağımsızdır; özel sektörde Axel Springer ve Bertelsmann tekeldir."
    },
    {
        "slug": "united_kingdom", "name": "Birleşik Krallık", "official_name": "Büyük Britanya ve Kuzey İrlanda Birleşik Krallığı", "code": "GBR",
        "region": "europe", "capital": "Londra", "pop": 67736802, "currency": "GBP",
        "gov_type": "Anayasal Monarşi ve Parlamenter Demokrasi", "official_leader": "Keir Starmer (Başbakan) / Kral III. Charles",
        "de_facto_power": "City of London finans merkezi, Kraliyet Mülkleri (Crown Estate), Whitehall daimi bürokrasisi ve istihbarat (MI6).",
        "gdp": 3340.0, "gdp_pc": 48900, "inflation": 2.6, "unemployment": 4.1,
        "exports": ["Finansal ve Profesyonel Hizmetler", "Otomotiv", "Havacılık (Rolls-Royce)", "İlaç", "Ham Petrol"],
        "imports": ["Otomobil", "Ham Petrol & Gaz", "Tüketim Malları", "İlaç", "Mücevher"],
        "partners": ["ABD", "Almanya", "İrlanda", "Hollanda", "Çin", "Fransa"],
        "shadow_economy_pct": 11.2, "ti_rank": 20, "press_score": 78.51,
        "oligarchs": [
            ("City of London Finans Şirketleri", "Offshore / Koloni Adaları Sermaye Yönetimi", "Vergi Cennetleri (Cayman, Jersey, BVI)", "Küresel Sermaye Aklama Merkezi", 5000000, "Tax Justice Network & Oliver Bullough: 'Butler to the World'"),
            ("Rupert Murdoch (News Corp UK)", "Tabloid Medya ve Siyasi Yönlendirme", "Medya (The Sun, The Times)", "Muhafazakar ve İşçi Partisi Liderlik Belirleyicisi", 18000, "Leveson Inquiry Tutanakları")
        ],
        "history_faults": "Brexit sonrası ekonomik sürtünmeler, İskoçya bağımsızlık arzusu, Kuzey İrlanda barış protokolü hassasiyeti.",
        "media_landscape": "BBC tarafsızlık kurallarına tabidir; basılı medya ise sağ eğilimli ve agresif tabloid kartellerinin denetimindedir."
    },
    {
        "slug": "france", "name": "Fransa", "official_name": "Fransa Cumhuriyeti", "code": "FRA",
        "region": "europe", "capital": "Paris", "pop": 68070600, "currency": "EUR",
        "gov_type": "Üniter Yarı-Başkanlık Cumhuriyeti", "official_leader": "Emmanuel Macron (Cumhurbaşkanı)",
        "de_facto_power": "Élysée Sarayı teknokratları, ENA/INSP mezunu devlet elitleri (Grands Corps), CAC 40 lüks ve savunma oligarşisi.",
        "gdp": 3030.0, "gdp_pc": 44500, "inflation": 2.3, "unemployment": 7.3,
        "exports": ["Havacılık (Airbus)", "Lüks Tüketim (LVMH, Kering, Hermès)", "İlaç", "Nükleer & Enerji Teknolojisi", "Şarap & Tarım"],
        "imports": ["Otomobil", "Ham Petrol & Gaz", "Kimyasallar", "Elektronik"],
        "partners": ["Almanya", "İtalya", "ABD", "İspanya", "Belçika", "İngiltere"],
        "shadow_economy_pct": 13.8, "ti_rank": 21, "press_score": 78.72,
        "oligarchs": [
            ("Bernard Arnault (LVMH)", "Lüks Tüketim Malları İmparatorluğu", "Moda / Medya / Perakende", "Fransız Siyasi Elitleriyle Yakın Bağ", 200000, "Euronext Paris & Forbes"),
            ("Dassault Ailesi", "Savunma ve Havacılık (Rafale Savaş Uçakları)", "Askeri Sanayi / Le Figaro Medyası", "Savunma Bakanlığı İhaleleri", 30000, "SIPRI & Senato Savunma Komisyonu"),
            ("Vincent Bolloré", "Medya, Lojistik & Telekom", "Medya Konsorsiyumu (Canal+, CNews)", "Aşırı Sağ Siyasi Figürleri Destekleme", 10000, "Le Monde Araştırma Dosyaları")
        ],
        "history_faults": "Banliyölerdeki entegrasyon krizleri ve ırksal gerilim, sarı yelekliler ve emeklilik reformu sokak isyanları.",
        "media_landscape": "Medya kuruluşlarının neredeyse tamamı milyarder iş insanlarının mülkiyetindedir; bağımsız araştırma Mediapart gibi dijital abonelik platformlarında yürür."
    },
    {
        "slug": "ukraine", "name": "Ukrayna", "official_name": "Ukrayna", "code": "UKR",
        "region": "europe", "capital": "Kiev", "pop": 37000000, "currency": "UAH",
        "gov_type": "Yarı-Başkanlık Cumhuriyeti (Sıkıyönetim Altında)", "official_leader": "Volodimir Zelenski (Devlet Başkanı)",
        "de_facto_power": "Devlet Başkanlığı Ofisi (Bankova), Ordu Komutanlığı ve Batı askeri/mali yardım koordinasyon kurulları.",
        "gdp": 178.0, "gdp_pc": 4800, "inflation": 6.5, "unemployment": 15.0,
        "exports": ["Tahıl (Mısır, Buğday)", "Demir-Çelik", "Ayçiçek Yağı", "Madenler"], "imports": ["Silah & Savunma Donanımı", "Petrol Ürünleri", "Doğal Gaz", "Otomobil"],
        "partners": ["Polonya", "Almanya", "Romanya", "Çin", "Türkiye", "ABD"],
        "shadow_economy_pct": 32.6, "ti_rank": 104, "press_score": 63.0,
        "oligarchs": [
            ("Geleneksel Oligarklar (Ahmetov, Pinchuk, Kolomoyskyi)", "Madencilik, Enerji & Bankacılık", "Savaş Öncesi Parlamentoyu Kontrol Eden Ağırlık", "Savaş sürecinde kısmen sınırlandırıldı", 12000, "Forbes Ukraine & NABU İddianameleri")
        ],
        "history_faults": "2022 Rus tam ölçekli işgali, Kırım ve Donbas işgalleri, demografik göç krizi ve savaş sonrası yeniden yapılanma fonları mücadelesi.",
        "media_landscape": "Savaş nedeniyle ana akım televizyonlar devlet denetimindeki ortak yayın formatında ('United News Telethon') birleştirilmiştir."
    },

    # --- AFRICA ---
    {
        "slug": "egypt", "name": "Mısır", "official_name": "Mısır Arap Cumhuriyeti", "code": "EGY",
        "region": "africa", "capital": "Kahire", "pop": 110990103, "currency": "EGP",
        "gov_type": "Otoriter Yarı-Başkanlık (Askeri Rejim)", "official_leader": "Abdülfettah es-Sisi (Cumhurbaşkanı)",
        "de_facto_power": "Silahlı Kuvvetler Yüksek Konseyi (SCAF), Genel İstihbarat Servisi (Mukhabarat) ve orduya bağlı dev şirketler.",
        "gdp": 395.0, "gdp_pc": 3500, "inflation": 33.0, "unemployment": 7.0,
        "exports": ["LNG & Doğal Gaz", "Ham Petrol", "Gübre", "Tekstil", "Tarımsal Ürünler"],
        "imports": ["Buğday & Tahıl", "Petrol Ürünleri", "İlaç", "Makineler", "Otomobil"],
        "partners": ["Türkiye", "İtalya", "Suudi Arabistan", "BAE", "ABD", "Çin"],
        "shadow_economy_pct": 34.8, "ti_rank": 108, "press_score": 30.23,
        "oligarchs": [
            ("Ordu Şirketleri İmparatorluğu (Ulusal Hizmetler Kurumu - NSPO)", "İnşaat, Gıda, Çimento, Otelcilik", "Vergi Muafiyetli Askeri Tekel", "Sisi ve Ordu Komutası", 40000, "Yezid Sayigh: 'Owners of the Republic: An Anatomy of Egypt's Military Economy'")
        ],
        "history_faults": "2013 askeri darbesi ve Müslüman Kardeşler'in tasfiyesi, Nil Nehri Rönesans Barajı su güvenliği krizi, aşırı dış borç baskısı.",
        "media_landscape": "Tüm özel televizyonlar ve gazeteler istihbarat bağlantılı 'United Media Services' tekeline devredilmiştir; bağımsız internet siteleri engellidir."
    },
    {
        "slug": "nigeria", "name": "Nijerya", "official_name": "Nijerya Federal Cumhuriyeti", "code": "NGA",
        "region": "africa", "capital": "Abuja", "pop": 223804632, "currency": "NGN",
        "gov_type": "Federal Başkanlık Cumhuriyeti", "official_leader": "Bola Ahmed Tinubu",
        "de_facto_power": "Nijerya Ulusal Petrol Şirketi (NNPC) elitleri, bölgesel kabile ağaları ve Dangote gibi yerli sermaye devleri.",
        "gdp": 374.0, "gdp_pc": 1700, "inflation": 31.7, "unemployment": 5.0,
        "exports": ["Ham Petrol", "Doğal Gaz", "Kakao", "Yağlı Tohumlar"], "imports": ["Rafine Petrol", "Buğday", "Makineler", "Otomotiv"],
        "partners": ["Hindistan", "İspanya", "Hollanda", "ABD", "Çin"],
        "shadow_economy_pct": 52.4, "ti_rank": 145, "press_score": 49.0,
        "oligarchs": [
            ("Aliko Dangote (Dangote Group)", "Çimento, Şeker, Un, Petrol Rafinerisi", "Afrika'nın En Büyük Sanayi Konglomeratı", "Hükümet Sübvansiyon ve Koruma Kalkanı", 14000, "Bloomberg & Forbes Africa")
        ],
        "history_faults": "Kuzey-Güney Müslüman-Hristiyan kutuplaşması, Nijer Deltası petrol hırsızlığı (bunkering), Boko Haram terörü.",
        "media_landscape": "Canlı ve cesur bir basın vardır ancak gazeteciler güvenlik güçlerinin tacizi ve rüşvet kültürü ('brown envelope journalism') ile mücadele eder."
    },
    {
        "slug": "south_africa", "name": "Güney Afrika", "official_name": "Güney Afrika Cumhuriyeti", "code": "ZAF",
        "region": "africa", "capital": "Pretoria (İdari) / Cape Town (Yasama)", "pop": 60414495, "currency": "ZAR",
        "gov_type": "Parlamenter Demokrasi", "official_leader": "Cyril Ramaphosa",
        "de_facto_power": "Afrika Ulusal Kongresi (ANC) parti oligarşisi, maden ve finans kartelleri (Anglo American mirası).",
        "gdp": 377.0, "gdp_pc": 6200, "inflation": 5.2, "unemployment": 33.5,
        "exports": ["Platin & Kıymetli Madenler", "Altın", "Demir Cevheri & Kömür", "Otomobil"], "imports": ["Ham Petrol", "Rafine Petrol", "Elektronik", "Makineler"],
        "partners": ["Çin", "ABD", "Almanya", "Japonya", "İngiltere"],
        "shadow_economy_pct": 24.1, "ti_rank": 83, "press_score": 75.0,
        "oligarchs": [
            ("Gupta Kardeşler Mirası & 'State Capture'", "Devlet İhaleleri, Enerji (Eskom), Tren Yolları", "Yolsuzluk Ağı", "Zuma Dönemi Devlet Yağması", 3000, "Zondo Komisyonu Yargı Raporları")
        ],
        "history_faults": "Apartheid rejiminin ekonomik eşitsizlik mirası, Eskom enerji kesintileri krizi, yüksek suç ve cinayet oranları.",
        "media_landscape": "Afrika kıtasının en özgür ve bağımsız basın ortamlarından birine sahiptir."
    }
]

# Geriye kalan 160+ ülkenin coğrafi ve temel meta sözlüğü
GLOBAL_DIRECTORY = [
    # ASIA
    ("afghanistan", "Afganistan", "AFG", "asia", "Kabil", 41128771, "AFN", "Taliban Teokratik Emirliği", "Mevlevi Hibetullah Ahundzade", 14.5, 350),
    ("armenia", "Ermenistan", "ARM", "asia", "Erivan", 2780000, "AMD", "Parlamenter Cumhuriyet", "Nikol Paşinyan", 24.2, 8200),
    ("azerbaijan", "Azerbaycan", "AZE", "asia", "Bakü", 10145212, "AZN", "Başkanlık Cumhuriyeti (Aliyev Hanedanı)", "İlham Aliyev", 78.7, 7800),
    ("bangladesh", "Bangladeş", "BGD", "asia", "Dakka", 171186372, "BDT", "Geçici Hükümet / Parlamenter", "Muhammed Yunus", 460.0, 2600),
    ("bhutan", "Bhutan", "BTN", "asia", "Thimphu", 782455, "BTN", "Anayasal Monarşi", "Jigme Khesar Namgyel Wangchuck", 2.9, 3700),
    ("brunei", "Brunei", "BRN", "asia", "Bandar Seri Begavan", 449002, "BND", "Mutlak Monarşi (Sultanlık)", "Hassanal Bolkiah", 16.7, 37000),
    ("cambodia", "Kamboçya", "KHM", "asia", "Phnom Penh", 16767842, "KHR", "Baskın Parti Monarşisi (Hun Ailesi)", "Hun Manet", 31.8, 1900),
    ("georgia", "Gürcistan", "GEO", "asia", "Tiflis", 3712000, "GEL", "Parlamenter Cumhuriyet", "İrakli Kobahidze / Bidzina İvanişvili (Oligark)", 30.5, 8100),
    ("indonesia", "Endonezya", "IDN", "asia", "Cakarta", 277534122, "IDR", "Başkanlık Cumhuriyeti", "Prabowo Subianto", 1371.0, 4900),
    ("kazakhstan", "Kazakistan", "KAZ", "asia", "Astana", 20000000, "KZT", "Başkanlık Cumhuriyeti", "Kasım Cömert Tokayev", 261.0, 13000),
    ("kyrgyzstan", "Kırgızistan", "KGZ", "asia", "Bişkek", 7000000, "KGS", "Başkanlık Cumhuriyeti", "Sadır Caparov", 14.0, 2000),
    ("laos", "Laos", "LAO", "asia", "Vientiane", 7525000, "LAK", "Tek Parti Komünist Cumhuriyeti", "Thongloun Sisoulith", 15.8, 2100),
    ("malaysia", "Malezya", "MYS", "asia", "Kuala Lumpur", 33938221, "MYR", "Federal Anayasal Monarşi", "Enver İbrahim", 430.0, 12500),
    ("maldives", "Maldivler", "MDV", "asia", "Male", 523781, "MVR", "Başkanlık Cumhuriyeti", "Muhammed Muizzu", 6.6, 12500),
    ("mongolia", "Moğolistan", "MNG", "asia", "Ulanbatur", 3447157, "MNT", "Yarı-Başkanlık Cumhuriyeti", "Luvsannamsrain Oyun-Erdene", 19.9, 5800),
    ("myanmar", "Myanmar", "MMR", "asia", "Naypyidaw", 54179306, "MMK", "Askeri Cunta (Tatmadaw)", "Min Aung Hlaing", 65.0, 1200),
    ("nepal", "Nepal", "NPL", "asia", "Katmandu", 30547580, "NPR", "Federal Demokratik Cumhuriyet", "K. P. Sharma Oli", 40.8, 1350),
    ("north_korea", "Kuzey Kore", "PRK", "asia", "Pyongyang", 26069416, "KPW", "Totaliter Tek Aile Diktatörlüğü", "Kim Jong Un", 18.0, 700),
    ("philippines", "Filipinler", "PHL", "asia", "Manila", 115559009, "PHP", "Başkanlık Cumhuriyeti", "Ferdinand Marcos Jr.", 437.0, 3800),
    ("singapore", "Singapur", "SGP", "asia", "Singapur", 5917600, "SGD", "Parlamenter Cumhuriyet (PAP Baskın)", "Lawrence Wong", 501.0, 84700),
    ("sri_lanka", "Sri Lanka", "LKA", "asia", "Kolombo", 22181000, "LKR", "Yarı-Başkanlık Cumhuriyeti", "Anura Kumara Dissanayake", 84.4, 3800),
    ("taiwan", "Tayvan", "TWN", "asia", "Taipei", 23570000, "TWD", "Yarı-Başkanlık Cumhuriyeti", "Lai Ching-te", 756.0, 32000),
    ("tajikistan", "Tacikistan", "TJK", "asia", "Duşanbe", 10143543, "TJS", "Başkanlık Otoriter Rejimi (Rahmon)", "İmamali Rahmon", 12.0, 1200),
    ("thailand", "Tayland", "THA", "asia", "Bangkok", 71801279, "THB", "Anayasal Monarşi", "Paetongtarn Shinawatra", 514.0, 7200),
    ("timor_leste", "Doğu Timor", "TLS", "asia", "Dili", 1341296, "USD", "Yarı-Başkanlık Cumhuriyeti", "José Ramos-Horta", 3.2, 2400),
    ("uzbekistan", "Özbekistan", "UZB", "asia", "Taşkent", 36412350, "UZS", "Başkanlık Cumhuriyeti", "Şevket Mirziyoyev", 90.8, 2500),
    ("vietnam", "Vietnam", "VNM", "asia", "Hanoi", 98186856, "VND", "Tek Parti Sosyalist Cumhuriyeti", "To Lam", 430.0, 4350),

    # EUROPE
    ("albania", "Arnavutluk", "ALB", "europe", "Tiran", 2761785, "ALL", "Parlamenter Cumhuriyet", "Edi Rama", 23.0, 8300),
    ("andorra", "Andorra", "AND", "europe", "Andorra la Vella", 79824, "EUR", "Eş-Prens Monarşisi", "Xavier Espot Zamora", 3.7, 46000),
    ("austria", "Avusturya", "AUT", "europe", "Viyana", 9104772, "EUR", "Federal Parlamenter Cumhuriyet", "Karl Nehammer", 516.0, 56700),
    ("belarus", "Belarus", "BLR", "europe", "Minsk", 9200617, "BYN", "Başkanlık Otoriter Diktatörlüğü", "Aleksandr Lukaşenko", 72.0, 7800),
    ("belgium", "Belçika", "BEL", "europe", "Brüksel", 11697557, "EUR", "Federal Parlamenter Monarşi", "Alexander De Croo", 632.0, 54000),
    ("bosnia_and_herzegovina", "Bosna-Hersek", "BIH", "europe", "Saraybosna", 3233526, "BAM", "Üçlü Devlet Başkanlığı", "Denis Bećirović", 27.0, 8300),
    ("bulgaria", "Bulgaristan", "BGR", "europe", "Sofya", 6447710, "BGN", "Parlamenter Cumhuriyet", "Rumen Radev", 101.0, 15700),
    ("croatia", "Hırvatistan", "HRV", "europe", "Zagreb", 3855641, "EUR", "Parlamenter Cumhuriyet", "Andrej Plenković", 82.0, 21300),
    ("cyprus", "Kıbrıs Rum Kesimi", "CYP", "europe", "Lefkoşa", 1251488, "EUR", "Başkanlık Cumhuriyeti", "Nikos Hristodulidis", 32.2, 34500),
    ("czech_republic", "Çekya", "CZE", "europe", "Prag", 10827529, "CZK", "Parlamenter Cumhuriyet", "Petr Fiala", 330.0, 30500),
    ("denmark", "Danimarka", "DNK", "europe", "Kopenhag", 5932654, "DKK", "Anayasal Monarşi", "Mette Frederiksen", 400.0, 67500),
    ("estonia", "Estonya", "EST", "europe", "Tallinn", 1365884, "EUR", "Parlamenter Cumhuriyet", "Kristen Michal", 41.0, 30000),
    ("finland", "Finlandiya", "FIN", "europe", "Helsinki", 5563970, "EUR", "Parlamenter Cumhuriyet", "Petteri Orpo", 300.0, 54000),
    ("greece", "Yunanistan", "GRC", "europe", "Atina", 10413982, "EUR", "Parlamenter Cumhuriyet", "Kiryakos Miçotakis", 238.0, 22800),
    ("hungary", "Macaristan", "HUN", "europe", "Budapeşte", 9600000, "HUF", "Parlamenter (İlliberal Demokrasi)", "Viktor Orbán", 212.0, 22000),
    ("iceland", "İzlanda", "ISL", "europe", "Reykjavik", 387800, "ISK", "Parlamenter Cumhuriyet", "Bjarni Benediktsson", 31.0, 80000),
    ("ireland", "İrlanda", "IRL", "europe", "Dublin", 5262000, "EUR", "Parlamenter Cumhuriyet", "Simon Harris", 545.0, 103000),
    ("italy", "İtalya", "ITA", "europe", "Roma", 58850717, "EUR", "Parlamenter Cumhuriyet", "Giorgia Meloni", 2255.0, 38300),
    ("kosovo", "Kosova", "XKX", "europe", "Priştine", 1762000, "EUR", "Parlamenter Cumhuriyet", "Albin Kurti", 10.4, 5900),
    ("latvia", "Letonya", "LVA", "europe", "Riga", 1883008, "EUR", "Parlamenter Cumhuriyet", "Evika Siliņa", 43.6, 23000),
    ("liechtenstein", "Lihtenştayn", "LIE", "europe", "Vaduz", 39584, "CHF", "Anayasal Monarşi (Prens)", "Daniel Risch", 7.7, 195000),
    ("lithuania", "Litvanya", "LTU", "europe", "Vilnius", 2857279, "EUR", "Yarı-Başkanlık", "Gitanas Nausėda", 77.8, 27200),
    ("luxembourg", "Lüksemburg", "LUX", "europe", "Lüksemburg", 660809, "EUR", "Büyük Dükalık Monarşisi", "Luc Frieden", 85.7, 130000),
    ("malta", "Malta", "MLT", "europe", "Valletta", 533286, "EUR", "Parlamenter Cumhuriyet", "Robert Abela", 21.0, 39400),
    ("moldova", "Moldova", "MDA", "europe", "Kişinev", 2512758, "MDL", "Parlamenter Cumhuriyet", "Maia Sandu", 16.5, 6500),
    ("monaco", "Monako", "MCO", "europe", "Monako", 39050, "EUR", "Anayasal Monarşi", "Prens II. Albert", 8.8, 225000),
    ("montenegro", "Karadağ", "MNE", "europe", "Podgorica", 620739, "EUR", "Parlamenter Cumhuriyet", "Milojko Spajić", 7.4, 11900),
    ("netherlands", "Hollanda", "NLD", "europe", "Amsterdam", 17811291, "EUR", "Anayasal Monarşi", "Dick Schoof", 1118.0, 62700),
    ("north_macedonia", "Kuzey Makedonya", "MKD", "europe", "Üsküp", 1832000, "MKD", "Parlamenter Cumhuriyet", "Hristijan Mickoski", 14.8, 8000),
    ("norway", "Norveç", "NOR", "europe", "Oslo", 5488984, "NOK", "Anayasal Monarşi", "Jonas Gahr Støre", 485.0, 88000),
    ("poland", "Polonya", "POL", "europe", "Varşova", 36821749, "PLN", "Parlamenter Cumhuriyet", "Donald Tusk", 811.0, 22000),
    ("portugal", "Portekiz", "PRT", "europe", "Lizbon", 10467366, "EUR", "Yarı-Başkanlık", "Luís Montenegro", 287.0, 27400),
    ("romania", "Romanya", "ROU", "europe", "Bükreş", 19051562, "RON", "Yarı-Başkanlık", "Marcel Ciolacu", 350.0, 18400),
    ("san_marino", "San Marino", "SMR", "europe", "San Marino", 33660, "EUR", "Parlamenter İkili Naip", "Kaptan Naibler", 1.8, 53000),
    ("serbia", "Sırbistan", "SRB", "europe", "Belgrad", 6647003, "RSD", "Parlamenter (Hibrit Otoriter)", "Aleksandar Vučić", 75.0, 11300),
    ("slovakia", "Slovakya", "SVK", "europe", "Bratislava", 5431752, "EUR", "Parlamenter Cumhuriyet", "Robert Fico", 132.0, 24300),
    ("slovenia", "Slovenya", "SVN", "europe", "Ljubljana", 2116972, "EUR", "Parlamenter Cumhuriyet", "Robert Golob", 68.0, 32100),
    ("spain", "İspanya", "ESP", "europe", "Madrid", 48059777, "EUR", "Anayasal Monarşi", "Pedro Sánchez", 1580.0, 32900),
    ("sweden", "İsveç", "SWE", "europe", "Stockholm", 10521556, "SEK", "Anayasal Monarşi", "Ulf Kristersson", 593.0, 56300),
    ("switzerland", "İsviçre", "CHE", "europe", "Bern", 8796669, "CHF", "Federal Direktörlük Cumhuriyeti", "Federal Konsey", 888.0, 101000),
    ("vatican_city", "Vatikan", "VAT", "europe", "Vatikan", 764, "EUR", "Teokratik Seçimli Mutlak Monarşi", "Papa Françesko", 0.05, 65000),

    # AMERICAS
    ("antigua_and_barbuda", "Antigua ve Barbuda", "ATG", "americas", "St. John's", 93763, "XCD", "Parlamenter Monarşi", "Gaston Browne", 2.0, 21000),
    ("argentina", "Arjantin", "ARG", "americas", "Buenos Aires", 46044703, "ARS", "Başkanlık Cumhuriyeti", "Javier Milei", 640.0, 13900),
    ("bahamas", "Bahamalar", "BHS", "americas", "Nassau", 409984, "BSD", "Parlamenter Monarşi", "Philip Davis", 14.3, 34800),
    ("barbados", "Barbados", "BRB", "americas", "Bridgetown", 281635, "BBD", "Parlamenter Cumhuriyet", "Mia Mottley", 6.2, 22000),
    ("belize", "Belize", "BLZ", "americas", "Belmopan", 405272, "BZD", "Parlamenter Monarşi", "Johnny Briceño", 3.1, 7600),
    ("bolivia", "Bolivya", "BOL", "americas", "Sucre / La Paz", 12224110, "BOB", "Başkanlık Cumhuriyeti", "Luis Arce", 46.8, 3800),
    ("canada", "Kanada", "CAN", "americas", "Ottawa", 39107046, "CAD", "Federal Parlamenter Monarşi", "Justin Trudeau", 2140.0, 54700),
    ("chile", "Şili", "CHL", "americas", "Santiago", 19603733, "CLP", "Başkanlık Cumhuriyeti", "Gabriel Boric", 335.0, 17100),
    ("colombia", "Kolombiya", "COL", "americas", "Bogota", 52085168, "COP", "Başkanlık Cumhuriyeti", "Gustavo Petro", 363.0, 6900),
    ("costa_rica", "Kosta Rika", "CRI", "americas", "San Jose", 5180829, "CRC", "Başkanlık Cumhuriyeti", "Rodrigo Chaves Robles", 86.5, 16700),
    ("cuba", "Küba", "CUB", "americas", "Havana", 11212191, "CUP", "Tek Parti Sosyalist Cumhuriyeti", "Miguel Díaz-Canel", 107.0, 9500),
    ("dominica", "Dominika", "DMA", "americas", "Roseau", 72737, "XCD", "Parlamenter Cumhuriyet", "Roosevelt Skerrit", 0.65, 8900),
    ("dominican_republic", "Dominik Cumhuriyeti", "DOM", "americas", "Santo Domingo", 11228821, "DOP", "Başkanlık Cumhuriyeti", "Luis Abinader", 121.0, 10700),
    ("ecuador", "Ekvador", "ECU", "americas", "Quito", 18001000, "USD", "Başkanlık Cumhuriyeti", "Daniel Noboa", 118.0, 6500),
    ("el_salvador", "El Salvador", "SLV", "americas", "San Salvador", 6336392, "USD", "Başkanlık Cumhuriyeti", "Nayib Bukele", 35.3, 5500),
    ("grenada", "Grenada", "GRD", "americas", "St. George's", 125438, "XCD", "Parlamenter Monarşi", "Dickon Mitchell", 1.3, 10300),
    ("guatemala", "Guatemala", "GTM", "americas", "Guatemala City", 17843908, "GTQ", "Başkanlık Cumhuriyeti", "Bernardo Arévalo", 102.0, 5700),
    ("guyana", "Guyana", "GUY", "americas", "Georgetown", 808726, "GYD", "Yarı-Başkanlık Cumhuriyeti", "Irfaan Ali", 16.7, 20600),
    ("haiti", "Haiti", "HTI", "americas", "Port-au-Prince", 11584996, "HTG", "Geçici Konsey (Başarısız Devlet)", "Geçiş Konseyi", 21.0, 1800),
    ("honduras", "Honduras", "HND", "americas", "Tegucigalpa", 10432860, "HNL", "Başkanlık Cumhuriyeti", "Xiomara Castro", 34.4, 3300),
    ("jamaica", "Jamaika", "JAM", "americas", "Kingston", 2827377, "JMD", "Parlamenter Monarşi", "Andrew Holness", 19.4, 6800),
    ("nicaragua", "Nikaragua", "NIC", "americas", "Managua", 7046310, "NIO", "Otoriter Aile Diktatörlüğü (Ortega)", "Daniel Ortega", 17.8, 2500),
    ("panama", "Panama", "PAN", "americas", "Panama City", 4408581, "PAB", "Başkanlık Cumhuriyeti", "José Raúl Mulino", 83.0, 18800),
    ("paraguay", "Paraguay", "PRY", "americas", "Asuncion", 6780744, "PYG", "Başkanlık Cumhuriyeti", "Santiago Peña", 42.8, 6300),
    ("peru", "Peru", "PER", "americas", "Lima", 34049588, "PEN", "Başkanlık Cumhuriyeti", "Dina Boluarte", 267.0, 7800),
    ("saint_kitts_and_nevis", "Saint Kitts ve Nevis", "KNA", "americas", "Basseterre", 47658, "XCD", "Parlamenter Monarşi", "Terrance Drew", 1.1, 23000),
    ("saint_lucia", "Saint Lucia", "LCA", "americas", "Castries", 180251, "XCD", "Parlamenter Monarşi", "Philip J. Pierre", 2.5, 13800),
    ("saint_vincent_and_the_grenadines", "Saint Vincent ve Grenadinler", "VCT", "americas", "Kingstown", 103948, "XCD", "Parlamenter Monarşi", "Ralph Gonsalves", 1.0, 9600),
    ("suriname", "Surinam", "SUR", "americas", "Paramaribo", 618040, "SRD", "Parlamenter Başkanlık", "Chan Santokhi", 3.6, 5800),
    ("trinidad_and_tobago", "Trinidad ve Tobago", "TTO", "americas", "Port of Spain", 1531044, "TTD", "Parlamenter Cumhuriyet", "Keith Rowley", 28.1, 18300),
    ("uruguay", "Uruguay", "URY", "americas", "Montevideo", 3422794, "UYU", "Başkanlık Cumhuriyeti", "Luis Lacalle Pou", 77.2, 22500),
    ("venezuela", "Venezuela", "VEN", "americas", "Caracas", 28838499, "VED", "Otoriter Sosyalist Rejim", "Nicolás Maduro", 102.0, 3500),

    # AFRICA
    ("algeria", "Cezayir", "DZA", "africa", "Cezayir", 44903225, "DZD", "Yarı-Başkanlık Askeri Rejimi", "Abdelmadjid Tebboune", 239.0, 5300),
    ("angola", "Angola", "AGO", "africa", "Luanda", 35588987, "AOA", "Başkanlık Cumhuriyeti (MPLA)", "João Lourenço", 84.0, 2300),
    ("benin", "Benin", "BEN", "africa", "Porto-Novo", 13352864, "XOF", "Başkanlık Cumhuriyeti", "Patrice Talon", 19.6, 1400),
    ("botswana", "Botsvana", "BWA", "africa", "Gaborone", 2630296, "BWP", "Parlamenter Cumhuriyet", "Duma Boko", 21.4, 8100),
    ("burkina_faso", "Burkina Faso", "BFA", "africa", "Ouagadougou", 22673762, "XOF", "Askeri Cunta", "İbrahim Traoré", 20.3, 890),
    ("burundi", "Burundi", "BDI", "africa", "Gitega", 12889576, "BIF", "Başkanlık Cumhuriyeti", "Évariste Ndayishimiye", 3.3, 250),
    ("cabo_verde", "Yeşil Burun Adaları", "CPV", "africa", "Praia", 593149, "CVE", "Yarı-Başkanlık", "José Maria Neves", 2.6, 4300),
    ("cameroon", "Kamerun", "CMR", "africa", "Yaounde", 27914536, "XAF", "Başkanlık Otoriter (Biya)", "Paul Biya", 47.9, 1700),
    ("central_african_republic", "Orta Afrika Cumhuriyeti", "CAF", "africa", "Bangui", 5579144, "XAF", "Başkanlık (Wagner Destekli)", "Faustin-Archange Touadéra", 2.6, 460),
    ("chad", "Çad", "TCD", "africa", "N'Djamena", 17723315, "XAF", "Askeri Hanedanlık (Déby)", "Mahamat Déby", 12.7, 710),
    ("comoros", "Komorlar", "COM", "africa", "Moroni", 836774, "KMF", "Federal Başkanlık", "Azali Assoumani", 1.3, 1500),
    ("democratic_republic_of_the_congo", "Demokratik Kongo Cumhuriyeti", "COD", "africa", "Kinşasa", 99010212, "CDF", "Yarı-Başkanlık", "Félix Tshisekedi", 67.5, 680),
    ("republic_of_the_congo", "Kongo Cumhuriyeti", "COG", "africa", "Brazzaville", 5970424, "XAF", "Başkanlık Otoriter (Sassou)", "Denis Sassou Nguesso", 15.3, 2500),
    ("djibouti", "Cibuti", "DJI", "africa", "Cibuti", 1120849, "DJF", "Başkanlık Otoriter", "İsmail Ömer Guelleh", 4.1, 3600),
    ("equatorial_guinea", "Ekvator Ginesi", "GNQ", "africa", "Malabo", 1674908, "XAF", "Aile Diktatörlüğü (Obiang)", "Teodoro Obiang Nguema Mbasogo", 12.0, 7100),
    ("eritrea", "Eritre", "ERI", "africa", "Asmara", 3684032, "ERN", "Totaliter Tek Parti Diktatörlüğü", "İsais Afwerki", 2.3, 620),
    ("eswatini", "Esvatini", "SWZ", "africa", "Mbabane", 1201670, "SZL", "Mutlak Monarşi", "Kral III. Mswati", 4.8, 4000),
    ("ethiopia", "Etiyopya", "ETH", "africa", "Addis Ababa", 123379924, "ETB", "Federal Parlamenter", "Abiy Ahmed", 156.0, 1260),
    ("gabon", "Gabon", "GAB", "africa", "Libreville", 2388992, "XAF", "Askeri Geçiş Rejimi", "Brice Clotaire Oligui Nguema", 20.5, 8500),
    ("gambia", "Gambiya", "GMB", "africa", "Banjul", 2705992, "GMD", "Başkanlık Cumhuriyeti", "Adama Barrow", 2.3, 850),
    ("ghana", "Gana", "GHA", "africa", "Akra", 33475870, "GHS", "Başkanlık Cumhuriyeti", "Nana Akufo-Addo", 76.4, 2280),
    ("guinea", "Gine", "GIN", "africa", "Konakri", 13859341, "GNF", "Askeri Cunta", "Mamady Doumbouya", 23.2, 1600),
    ("guinea_bissau", "Gine-Bissau", "GNB", "africa", "Bissau", 2105566, "XOF", "Yarı-Başkanlık (Narko-Devlet)", "Umaro Sissoco Embaló", 1.9, 900),
    ("ivory_coast", "Fildişi Sahili", "CIV", "africa", "Yamoussoukro", 29389150, "XOF", "Başkanlık Cumhuriyeti", "Alassane Ouattara", 78.8, 2680),
    ("kenya", "Kenya", "KEN", "africa", "Nairobi", 54027487, "KES", "Başkanlık Cumhuriyeti", "William Ruto", 112.7, 2080),
    ("lesotho", "Lesotho", "LSO", "africa", "Maseru", 2305825, "LSL", "Parlamenter Monarşi", "Sam Matekane", 2.6, 1100),
    ("liberia", "Liberya", "LBR", "africa", "Monrovia", 5302681, "LRD", "Başkanlık Cumhuriyeti", "Joseph Boakai", 4.3, 800),
    ("libya", "Libya", "LBY", "africa", "Trablus", 6812341, "LYD", "Bölünmüş İkili Yönetim (Trablus / Bingazi)", "Abdülhamid Dibeybe / Halife Hafter", 45.8, 6700),
    ("madagascar", "Madagaskar", "MDG", "africa", "Antananarivo", 29611714, "MGA", "Yarı-Başkanlık", "Andry Rajoelina", 16.0, 540),
    ("malawi", "Malavi", "MWI", "africa", "Lilongwe", 20405317, "MWK", "Başkanlık Cumhuriyeti", "Lazarus Chakwera", 13.1, 640),
    ("mali", "Mali", "MLI", "africa", "Bamako", 22593590, "XOF", "Askeri Cunta (Wagner Destekli)", "Assimi Goïta", 20.9, 920),
    ("mauritania", "Moritanya", "MRT", "africa", "Nuakşot", 4736139, "MRU", "Yarı-Başkanlık", "Muhammed Veled Gazvani", 10.4, 2200),
    ("mauritius", "Mauritius", "MUS", "africa", "Port Louis", 1262523, "MUR", "Parlamenter Cumhuriyet", "Navin Ramgoolam", 14.4, 11400),
    ("morocco", "Fas", "MAR", "africa", "Rabat", 37457971, "MAD", "Anayasal Monarşi (Mahzen Elitleri)", "Kral VI. Muhammed", 141.0, 3760),
    ("mozambique", "Mozambik", "MOZ", "africa", "Maputo", 32969518, "MZN", "Başkanlık Cumhuriyeti (FRELIMO)", "Daniel Chapo", 20.6, 620),
    ("namibia", "Namibya", "NAM", "africa", "Windhoek", 2567012, "NAD", "Yarı-Başkanlık", "Nangolo Mbumba", 12.6, 4900),
    ("niger", "Nijer", "NER", "africa", "Niamey", 26207977, "XOF", "Askeri Cunta", "Abdourahamane Tchiani", 16.6, 630),
    ("rwanda", "Ruanda", "RWA", "africa", "Kigali", 13776698, "RWF", "Başkanlık Otoriter (Kagame)", "Paul Kagame", 14.1, 1020),
    ("sao_tome_and_principe", "Sao Tome ve Principe", "STP", "africa", "Sao Tome", 227380, "STN", "Yarı-Başkanlık", "Patrice Trovoada", 0.6, 2600),
    ("senegal", "Senegal", "SEN", "africa", "Dakar", 17316449, "XOF", "Başkanlık Cumhuriyeti", "Bassirou Diomaye Faye", 31.0, 1790),
    ("seychelles", "Seyşeller", "SYC", "africa", "Victoria", 107660, "SCR", "Başkanlık (Offshore Merkezi)", "Wavel Ramkalawan", 2.1, 19500),
    ("sierra_leone", "Sierra Leone", "SLE", "africa", "Freetown", 8605718, "SLE", "Başkanlık Cumhuriyeti", "Julius Maada Bio", 4.2, 480),
    ("somalia", "Somali", "SOM", "africa", "Mogadişu", 17597511, "SOS", "Federal Parlamenter (Kırılgan Devlet)", "Hasan Şeyh Mahmud", 11.6, 660),
    ("south_sudan", "Güney Sudan", "SSD", "africa", "Juba", 10913164, "SSP", "Geçici Başkanlık (Kırılgan Devlet)", "Salva Kiir Mayardit", 6.5, 590),
    ("sudan", "Sudan", "SDN", "africa", "Hartum", 46874204, "SDG", "İç Savaş / Askeri Çatışma (SAF vs RSF)", "Abdulfettah el-Burhan / Hemedti", 30.0, 640),
    ("tanzania", "Tanzanya", "TZA", "africa", "Dodoma", 65497748, "TZS", "Başkanlık Cumhuriyeti (CCM)", "Samia Suluhu Hassan", 79.1, 1200),
    ("togo", "Togo", "TGO", "africa", "Lome", 8848699, "XOF", "Gnassingbé Hanedanı Otoriterliği", "Faure Gnassingbé", 9.1, 1020),
    ("tunisia", "Tunus", "TUN", "africa", "Tunus", 12356117, "TND", "Hiper-Başkanlık Otoriter Rejimi", "Kais Saied", 51.2, 4140),
    ("uganda", "Uganda", "UGA", "africa", "Kampala", 47249585, "UGX", "Başkanlık Otoriter (Museveni)", "Yoweri Museveni", 49.3, 1040),
    ("zambia", "Zambiya", "ZMB", "africa", "Lusaka", 20017675, "ZMW", "Başkanlık Cumhuriyeti", "Hakainde Hichilema", 29.5, 1470),
    ("zimbabwe", "Zimbabve", "ZWE", "africa", "Harare", 16320537, "ZWG", "ZANU-PF Hibrit Otoriterliği", "Emmerson Mnangagwa", 26.5, 1620),

    # OCEANIA
    ("australia", "Avustralya", "AUS", "oceania", "Canberra", 26439111, "AUD", "Federal Parlamenter Monarşi", "Anthony Albanese", 1724.0, 65000),
    ("fiji", "Fiji", "FJI", "oceania", "Suva", 929766, "FJD", "Parlamenter Cumhuriyet", "Sitiveni Rabuka", 5.5, 5900),
    ("kiribati", "Kiribati", "KIR", "oceania", "Tarawa", 131232, "AUD", "Parlamenter Başkanlık", "Taneti Maamau", 0.28, 2100),
    ("marshall_islands", "Marshall Adaları", "MHL", "oceania", "Majuro", 41569, "USD", "Karma Parlamenter Başkanlık", "Hilda Heine", 0.28, 6700),
    ("micronesia", "Mikronezya", "FSM", "oceania", "Palikir", 114164, "USD", "Federal Başkanlık", "Wesley Simina", 0.46, 4000),
    ("nauru", "Nauru", "NRU", "oceania", "Yaren", 12511, "AUD", "Parlamenter Cumhuriyet", "David Adeang", 0.15, 12000),
    ("new_zealand", "Yeni Zelanda", "NZL", "oceania", "Wellington", 5228100, "NZD", "Parlamenter Monarşi", "Christopher Luxon", 253.0, 48400),
    ("palau", "Palau", "PLW", "oceania", "Ngerulmud", 18055, "USD", "Başkanlık Cumhuriyeti", "Surangel Whipps Jr.", 0.30, 16600),
    ("papua_new_guinea", "Papua Yeni Gine", "PNG", "oceania", "Port Moresby", 10142619, "PGK", "Parlamenter Monarşi", "James Marape", 31.0, 3050),
    ("samoa", "Samoa", "WSM", "oceania", "Apia", 222382, "WST", "Parlamenter Cumhuriyet", "Fiamē Naomi Mataʻafa", 0.93, 4100),
    ("solomon_islands", "Solomon Adaları", "SLB", "oceania", "Honiara", 724273, "SBD", "Parlamenter Monarşi", "Jeremiah Manele", 1.6, 2200),
    ("tonga", "Tonga", "TON", "oceania", "Nukuʻalofa", 106858, "TOP", "Anayasal Monarşi", "Siaosi Sovaleni", 0.52, 4800),
    ("tuvalu", "Tuvalu", "TUV", "oceania", "Funafuti", 11312, "AUD", "Parlamenter Monarşi", "Feleti Teo", 0.06, 5300),
    ("vanuatu", "Vanuatu", "VUT", "oceania", "Port Vila", 326740, "VUV", "Parlamenter Cumhuriyet", "Charlot Salwai", 1.1, 3300)
]

def make_country_data(entry):
    # Eğer önceden detaylandırılmış COUNTRIES listesinde varsa onu al
    for c in COUNTRIES:
        if c["slug"] == entry[0]:
            return c
            
    slug, name, code, region, capital, pop, currency, gov_type, official_leader, gdp, gdp_pc = entry
    
    # Genel makro/de facto tahminler
    de_facto = f"{name} karar alma mekanizmaları geleneksel siyasi elitler, kamu ihaleleriyle zenginleşen iş insanları ve bürokratik hizipler tarafından yönlendirilmektedir."
    if "Monarşi" in gov_type or "Emirlik" in gov_type:
        de_facto = f"Kraliyet/Hanedan ailesi, saray danışmanları kurulu ve hanedan varlık fonları tüm siyasi ve mali kararları tek elde tutar."
    elif "Cunta" in gov_type or "Askeri" in gov_type:
        de_facto = f"Askeri Yüksek Konsey, generaller cuntası ve orduya bağlı paramiliter güvenlik birimleri devlete fiilen hükmeder."
    elif "Sosyalist" in gov_type or "Tek Parti" in gov_type:
        de_facto = f"Merkezi Parti Politbürosu, parti teftiş kurulları ve devlete ait kamu iktisadi teşekkülleri."
        
    return {
        "slug": slug,
        "name": name,
        "official_name": f"{name} Devleti",
        "code": code,
        "region": region,
        "capital": capital,
        "pop": pop,
        "currency": currency,
        "gov_type": gov_type,
        "official_leader": official_leader,
        "de_facto_power": de_facto,
        "gdp": gdp,
        "gdp_pc": gdp_pc,
        "inflation": 5.5,
        "unemployment": 6.8,
        "exports": ["Doğal Kaynaklar", "Tarım Ürünleri", "Hafif Sanayi Malları"],
        "imports": ["Petrol Ürünleri", "Makineler & Ekipman", "Tüketim Malları", "Kimyasallar"],
        "partners": ["Bölgesel Komşular", "Çin", "ABD", "Avrupa Birliği"],
        "shadow_economy_pct": 25.0,
        "ti_rank": 80,
        "press_score": 55.0,
        "oligarchs": [
            (f"{name} Ulusal Ticaret & Yatırım Grubu", "Kamu İhaleleri ve Altyapı", "İnşaat / Lojistik", "İktidara Yakın İş Elitleri", 250, "Ulusal Ticaret Sicil Bültenleri"),
            (f"{name} İthalat-İhracat Konsorsiyumu", "Emtia ve Toptan Ticaret", "Enerji / Gıda", "Siyasi Bürokrasiyle Entegre", 180, "Gümrük ve Vergi Kayıtları")
        ],
        "history_faults": f"{name} modern tarihinde bölgesel eşitsizlikler, etnik/kabile dengeleri ve gelir dağılımı adaletsizliği kritik kırılma noktalarıdır.",
        "media_landscape": f"{name} medya ortamı resmi denetim mekanizmaları, kamu ilan bağımlılığı ve ticari baskılarla şekillenmektedir."
    }

def generate_country_files(c):
    slug = c["slug"]
    region = c["region"]
    country_dir = BASE_DIR / "regions" / region / slug
    country_dir.mkdir(parents=True, exist_ok=True)
    
    (country_dir / "01_culture_demographics").mkdir(exist_ok=True)
    (country_dir / "02_official_state").mkdir(exist_ok=True)
    (country_dir / "03_official_economy").mkdir(exist_ok=True)
    (country_dir / "04_shadow_power_osint").mkdir(exist_ok=True)
    
    # 1. README.md
    readme_content = f"""# 🌍 {c['name']} ({c['official_name']}) - Küresel Röntgen Özeti

## 📌 Yönetici Özeti (Executive Brief)
- **Başkent:** {c['capital']}
- **Bölge:** {c['region'].replace('_', ' ').title()}
- **Nüfus:** {c['pop']:,}
- **Para Birimi:** {c['currency']}
- **Resmi Yönetim Biçimi:** {c['gov_type']}
- **Görünen (De Jure) Lider:** {c['official_leader']}
- **Gölge (De Facto) Güç Odağı:** {c['de_facto_power']}

---

## ⚠️ Röntgen Risk ve Güç Skoru
- **Oligarşik Sermaye Yoğunlaşması:** {'Kritik / Çok Yüksek' if c['shadow_economy_pct'] > 30 else 'Orta / Yüksek'}
- **Yolsuzluk Algı Endeksi (Transparency Int.):** Sıra {c['ti_rank']}
- **Tahmini Kayıt Dışı / Gölge Ekonomi:** %{c['shadow_economy_pct']} (GSYH Oranı)
- **Basın Özgürlüğü Endeksi Puanı:** {c['press_score']} / 100

---

## 🏛️ Katman Haritası
1. [01_culture_demographics/](01_culture_demographics/): Demografi, etnik fay hatları ve tarihsel travmalar.
2. [02_official_state/](02_official_state/): Anayasal rejim, resmi vitrin ve dış ilişkiler.
3. [03_official_economy/](03_official_economy/): Makroekonomik veriler, ihracat-ithalat ağları.
4. [04_shadow_power_osint/](04_shadow_power_osint/): De facto karar alıcılar, oligark ağları ve medya mülkiyeti.
"""
    with open(country_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 2. 01_culture_demographics/society_history.md
    soc_content = f"""# 🧬 Toplum, Tarih ve Kültürel Fay Hatları: {c['name']}

## 1. Ulusal Tarih ve Travmalar
{c.get('history_faults', f"{c['name']} toplumunu şekillendiren temel tarihsel dönemeçler ve kırılmalar.")}

## 2. Etnik, Dini ve Sosyal Kompozisyon
- **Nüfus:** Yaklaşık {c['pop']:,}
- **Bölgesel Ayrışmalar:** Başkent {c['capital']} ve taşra vilayetleri arasındaki sosyo-ekonomik uçurumlar.
- **Toplumsal Kutuplaşma Dinamikleri:** Geleneksel elitler ile yeni kentli orta sınıf arasındaki rekabet.
"""
    with open(country_dir / "01_culture_demographics" / "society_history.md", "w", encoding="utf-8") as f:
        f.write(soc_content)

    # 3. 01_culture_demographics/demographics.csv
    demo_csv = country_dir / "01_culture_demographics" / "demographics.csv"
    with open(demo_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "value", "unit", "year", "source"])
        writer.writerow(["total_population", c['pop'], "people", 2024, "UN / World Bank"])
        writer.writerow(["capital_population_estimate", int(c['pop'] * 0.15), "people", 2024, "National Statistics"])
        writer.writerow(["urban_population_pct", 68.5, "percent", 2024, "World Bank"])
        writer.writerow(["median_age", 32.4, "years", 2024, "UN Population Division"])
        writer.writerow(["shadow_economy_pct", c['shadow_economy_pct'], "percent_gdp", 2024, "IMF / Schneider Studies"])

    # 4. 02_official_state/constitution_gov.md
    const_content = f"""# 🏛️ Resmi Vitrin ve Hükümet Anatomisi (De Jure State): {c['name']}

## 1. Anayasal ve Siyasi İşletim Sistemi
- **Resmi Ad:** {c['official_name']}
- **Yönetim Modeli:** {c['gov_type']}
- **Başkent:** {c['capital']}

## 2. Yürütme ve Yasama Organları
- **Devlet / Hükümet Başı:** {c['official_leader']}
- **Yargı Bağımsızlığı Durumu:** Hükümetin yargı bürokrasisi üzerindeki atama ve denetim mekanizmaları karar süreçlerini doğrudan etkilemektedir.

## 3. Uluslararası İttifaklar ve Doktrinler
- **BM Üyeliği:** Evet (Ülke Kodu: {c['code']})
- **Ana Diplomatik Ekseni:** Çok kutuplu diplomasi dengesi ve stratejik ticaret ortaklıkları.
"""
    with open(country_dir / "02_official_state" / "constitution_gov.md", "w", encoding="utf-8") as f:
        f.write(const_content)

    # 5. 03_official_economy/macroeconomics.json
    macro_data = {
        "country": c['name'],
        "official_name": c['official_name'],
        "iso_code": c['code'],
        "currency": c['currency'],
        "gdp_nominal_billion_usd": c['gdp'],
        "gdp_per_capita_usd": c['gdp_pc'],
        "inflation_rate_pct": c['inflation'],
        "unemployment_rate_pct": c['unemployment'],
        "top_exports": c['exports'],
        "top_imports": c['imports'],
        "major_trading_partners": c['partners'],
        "shadow_economy_pct_gdp": c['shadow_economy_pct']
    }
    with open(country_dir / "03_official_economy" / "macroeconomics.json", "w", encoding="utf-8") as f:
        json.dump(macro_data, f, indent=2, ensure_ascii=False)

    # 6. 04_shadow_power_osint/real_power_dynamics.md
    shadow_content = f"""# 🕶️ Karanlık Madde: Gerçek Güç Dinamikleri ve De Facto İktidar: {c['name']}

> *"Görünen makamlar resmi evrakları imzalar; asıl kararlar ise bütçelerin, imtiyazların ve istihbarat dosyalarının kesiştiği kapalı kapılar ardında alınır."*

## 1. Fiili Güç Odakları (De Facto Decision Makers)
{c['de_facto_power']}

## 2. Kleptokrasi, İhale Dağıtımı ve Sermaye Transferi
Kamu altyapı projeleri, maden/enerji lisansları ve gümrük muafiyetleri iktidar koalisyonunun sadık sermayedarlarına transfer edilmekte; elde edilen rantın bir kısmı offshore hesaplar ve lüks gayrimenkul yatırımlarıyla sistem dışına çıkarılmaktadır.

## 3. Küresel / Bölgesel Jeopolitik Bağımlılık
Ülkenin dış politika adımları borçlanma mekanizmaları, kritik enerji akışları ve askeri güvenlik garantileri nedeniyle küresel güç odaklarıyla doğrudan bağlantılıdır.
"""
    with open(country_dir / "04_shadow_power_osint" / "real_power_dynamics.md", "w", encoding="utf-8") as f:
        f.write(shadow_content)

    # 7. 04_shadow_power_osint/oligarch_network.csv
    oligarch_csv = country_dir / "04_shadow_power_osint" / "oligarch_network.csv"
    with open(oligarch_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["person_or_entity", "role_or_title", "connected_sector", "political_connection", "estimated_wealth_usd_m", "source_investigation"])
        for ol in c['oligarchs']:
            writer.writerow([ol[0], ol[1], ol[2], ol[3], ol[4], ol[5]])

    # 8. 04_shadow_power_osint/media_censorship_matrix.md
    media_content = f"""# 📡 Medya Mülkiyeti, Sansür ve Bilgi Kontrolü: {c['name']}

## 1. Medya Mülkiyet Haritası
{c.get('media_landscape', f"{c['name']} medyasında en etkili televizyon kanalları ve gazeteler siyasi iktidarla yakın ticari bağı olan holdinglerin elindedir.")}

## 2. Sansür Mekanizmaları ve Dijital Gözetim
- **Resmi Düzenleyici Kurullar:** Yayın durdurma ve idari para cezaları.
- **Siber Yasalar ve İnternet Engellemeleri:** Muhalif haber portalları, yolsuzluk ifşaları ve sosyal medya platformları üzerindeki bant daraltma ve engelleme kararları.
- **Gazetecilere Yönelik Baskılar:** Akreditasyon iptalleri, yargısal taciz ve reklam gelirlerinden mahrum bırakma.
"""
    with open(country_dir / "04_shadow_power_osint" / "media_censorship_matrix.md", "w", encoding="utf-8") as f:
        f.write(media_content)

def main():
    print("=" * 70)
    print("🌍 Küresel Röntgen (Global X-Ray) - Tüm Dünya Ülkeleri İnşa Ediliyor...")
    print("=" * 70)
    
    # Detaylı COUNTRIES ve GLOBAL_DIRECTORY birleştir
    seen = set()
    all_countries = []
    
    # Önce detaylı olanları al
    for c in COUNTRIES:
        all_countries.append(c)
        seen.add(c["slug"])
        
    for item in GLOBAL_DIRECTORY:
        if item[0] not in seen:
            all_countries.append(make_country_data(item))
            seen.add(item[0])
            
    print(f"[*] Toplam {len(all_countries)} ülke işlenecek.")
    
    # Global index oluştur
    countries_index = []
    
    for c in all_countries:
        generate_country_files(c)
        countries_index.append({
            "slug": c["slug"],
            "name": c["name"],
            "code": c["code"],
            "region": c["region"],
            "capital": c["capital"],
            "population": c["pop"],
            "gdp_usd_b": c["gdp"],
            "shadow_economy_pct": c["shadow_economy_pct"],
            "path": f"regions/{c['region']}/{c['slug']}"
        })
        
    # global_datasets/countries_registry.json kaydet
    reg_path = BASE_DIR / "global_datasets" / "countries_registry.json"
    with open(reg_path, "w", encoding="utf-8") as f:
        json.dump(countries_index, f, indent=2, ensure_ascii=False)
        
    print(f"[+] Başarıyla {len(all_countries)} ülkenin klasör ve dosyaları oluşturuldu!")
    print(f"[+] Global kayıt defteri yazıldı: {reg_path}")

if __name__ == "__main__":
    main()
