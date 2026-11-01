# -*- coding: utf-8 -*-
"""
scripts/generate_master_readme.py
Generates the comprehensive, quote-rich, authoritative master README.md for Medeniyet Atlası,
featuring:
1. Central Cultural & Civilizational Encyclopedia (9 Civilization Realms, 20 Country Cultural DNA Profiles,
   Untranslatable Soul Concepts Gallery, Gastronomy & Table Rituals, Etiquette & Taboos).
2. 8 Global Economic Archetype Blocks (/01_... - /08_...).
3. 4-Layer Power & Civilization Architecture.
4. Strategic Geopolitics & Intelligence Routing Matrix (/geopolitics_and_intelligence/*.md).
5. Regional dossiers (/regions), 12 forensic case studies (/dossiers), 12 research papers (/research).
6. 205-country complete atlas index with direct links to all sub-contents (Culture, Shadow Power, State, Economy).
7. OSINT methodology, CLI usage, and test verification.
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

with open(BASE_DIR / "global_datasets" / "cultural_codes_and_civilizations_registry.json", encoding="utf-8") as f:
    culture_data = json.load(f)

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

# Bölge İsimleri ve İkonları
region_meta = {
    "middle_east": ("🕌 Orta Doğu", "regions/middle_east/README.md"),
    "europe": ("🏰 Avrupa", "regions/europe/README.md"),
    "asia": ("⛩️ Asya & Hint-Pasifik", "regions/asia/README.md"),
    "americas": ("🌎 Amerika Kıtası", "regions/americas/README.md"),
    "africa": ("🌍 Afrika", "regions/africa/README.md"),
    "oceania": ("🏝️ Okyanusya", "regions/oceania/README.md")
}

# 1. Bölgesel Hızlı Erişim Bölümü
regional_sections = []
for reg_key, (reg_title, reg_link) in region_meta.items():
    reg_countries = [c for c in countries_sorted if c.get("region") == reg_key]
    country_badges = [
        f"[`{c['name']}`](countries/{c['slug']}/README.md)"
        for c in reg_countries
    ]
    badge_str = " • ".join(country_badges)
    regional_sections.append(
        f"#### {reg_title} ({len(reg_countries)} Ülke) — [*Bölge Raporu*]({reg_link})\n{badge_str}\n"
    )

regional_nav_md = "\n".join(regional_sections)

# 2. 205 Ülkelik Alt İçerik Yönlendirme Matrisi (Master Table)
atlas_rows = []
for c in countries_sorted:
    c_slug = c["slug"]
    eco_id = c.get("economy_group_id", "06_orta_gelir_ve_ureticiler")
    eco_badge = economy_badges.get(eco_id, "🌐 Karma Model")
    eco_path = c.get("economy_path", f"countries/{c_slug}")
    
    country_link = f"[{c['name']}](countries/{c_slug}/README.md)"
    eco_badge_link = f"[{eco_badge}]({eco_path}/README.md)"
    culture_link = f"[🎭 Kültür & Tarih](countries/{c_slug}/01_culture_demographics/society_history.md)"
    shadow_link = f"[🕵️ Gölge Güç](countries/{c_slug}/04_shadow_power_osint/real_power_dynamics.md)"
    state_link = f"[🏛️ Anayasa](countries/{c_slug}/02_official_state/constitution_gov.md)"
    econ_link = f"[📈 Makroekonomi](countries/{c_slug}/03_official_economy/macroeconomics.json)"
    
    atlas_rows.append(
        f"| **{country_link}** | `{c['code']}` | {c['capital']} | {eco_badge_link} | {culture_link} | {shadow_link} | {state_link} | {econ_link} |"
    )

atlas_table_md = "\n".join(atlas_rows)

# 3. Medeniyet Havzaları Tablosu
realms_rows = []
for r in culture_data.get("civilization_realms", []):
    realms_rows.append(
        f"| **{r['name']}** | {r['core_philosophy']} | `{', '.join(r['representative_states'])}` | `{', '.join(r.get('key_values', []))}` |"
    )
realms_table_md = "\n".join(realms_rows)

# 4. Kültürel Kodlar ve Ulusal DNA Tablosu (20 Ülke)
culture_rows = []
for c in culture_data.get("countries_cultural_dna", []):
    words_list = [f"**{w['word']}** (*{w['meaning']}*)" for w in c.get("untranslatable_soul_concepts", [])[:2]]
    words_str = "<br/>• ".join(words_list)
    if words_str:
        words_str = "• " + words_str
    ethos = c.get('core_cultural_ethos', '')
    if len(ethos) > 85:
        ethos = ethos[:82] + "..."
    comm = c.get('communication_style', '')
    if len(comm) > 60:
        comm = comm[:57] + "..."
    gastro = c.get('gastronomic_philosophy', '')
    if len(gastro) > 75:
        gastro = gastro[:72] + "..."
    culture_rows.append(
        f"| **{c['country']}** (`{c['code']}`) | {ethos} | {words_str} | {comm} | {gastro} |"
    )
culture_table_md = "\n".join(culture_rows)

# 5. İkonik Çevrilemeyen Ruh Kavramları Galerisi
iconic_concepts = [
    {
        "word": "Gönül",
        "culture": "🇹🇷 Türk (Anadolu)",
        "meaning": "Akıl ile kalbin, sevgi ile merhametin birleştiği; fiziki kalbin ötesindeki manevi, kırılgan ve sınırsız insan cevheri.",
        "quote": "«Gönül Çalab'ın tahtı, Çalap gönüle baktı / İki cihan bedbahtı, kim gönül yıkar ise» — Yunus Emre"
    },
    {
        "word": "Ikigai (生きがい)",
        "culture": "🇯🇵 Japon (Okinawa)",
        "meaning": "Sabah yataktan uyanma sebebi; tutku, misyon, meslek ve yeteneğin kesiştiği varoluşsal yaşam gayesi.",
        "quote": "«Küçük şeylerde derin anlam bulmak, acele etmeden akışta kalmak.»"
    },
    {
        "word": "Wabi-Sabi (侘寂)",
        "culture": "🇯🇵 Japon",
        "meaning": "Kusurlu, eksik, geçici ve mütevazı olanın içindeki dingin güzelliği ve hüznü kabul etme estetiği.",
        "quote": "«Kırılan çanağın altınla onarılması (Kintsugi); yara izleri kusur değil, tarihin şeref madalyasıdır.»"
    },
    {
        "word": "Gemütlichkeit",
        "culture": "🇩🇪 Alman & Avusturya",
        "meaning": "Sıcak, huzurlu, telaşsız, dostlarla paylaşılan ve mekanla kurulan güven dolu dingin aidiyet hali.",
        "quote": "«Zamanın durduğu, samimi bir sofra ve güvende hissedilen bir dost meclisi.»"
    },
    {
        "word": "Saudade",
        "culture": "🇵🇹 Portekiz & Brezilya",
        "meaning": "Bir daha asla geri dönmeyecek olan bir insana, mekana veya hatıraya duyulan tatlı-acı derin melankoli.",
        "quote": "«Fado müziğinin can damarı: Sevilenin yokluğunun bizzat varlık haline gelmesi.»"
    },
    {
        "word": "Ubuntu",
        "culture": "🇿🇦 Sahra Altı Afrika (Bantu)",
        "meaning": "«Biz olduğumuz için ben varım»; bireyin varlığını toplumun refahı ve ortak merhametiyle tanımlayan hümanizma.",
        "quote": "«Bir insanın insanlığı diğer insanların insanlığına bağlıdır.» — Desmond Tutu"
    },
    {
        "word": "Toska (Тоска)",
        "culture": "🇷🇺 Rus & Doğu Slav",
        "meaning": "Herhangi bir somut sebebi olmayan, ruhun derinliklerinden gelen varoluşsal hüzün ve sonsuz manevi açlık.",
        "quote": "«Nabokov'un ifadesiyle: 'Hiçbir dile tek kelimeyle çevrilemeyen, ruhun sebepsiz sızısı.'»"
    },
    {
        "word": "Hygge",
        "culture": "🇩🇰 Danimarka & İskandinav",
        "meaning": "Mum ışığında, dostlarla, kasmadan, gösterişsiz ve sıcacık bir atmosferde anın huzurunu yakalama sanatı.",
        "quote": "«Kuzey soğuğuna inat, evin sıcaklığında samimiyet ve sükunet.»"
    },
    {
        "word": "Meraki (Μεράκι)",
        "culture": "🇬🇷 Yunan & Akdeniz",
        "meaning": "Bir işi, yemeği veya sanatı icra ederken içine ruhunu, tutkusunu ve sevgisini bütünüyle katmak.",
        "quote": "«Sıradan bir zeytinyağlı tabağına dahi aşkını üflemek.»"
    },
    {
        "word": "Guanxi (关系)",
        "culture": "🇨🇳 Çin",
        "meaning": "Sözleşmelerin ötesinde; karşılıklı ahlaki yükümlülük, güven, vefa ve derin ilişkiler ağı.",
        "quote": "«Hukuktan önce gelen bin yıllık ahlaki güven dokusu.»"
    },
    {
        "word": "Sisu",
        "culture": "🇫🇮 Fin",
        "meaning": "Tüm umutlar tükendiğinde, imkansız şartlar altında dahi pes etmeden sessizce direnme ve dayanma gücü.",
        "quote": "«Fin kışının dondurucu karanlığında bile geri adım atmayan irade.»"
    },
    {
        "word": "Tarab (طرب)",
        "culture": "🇪🇬 Arap & Yakın Doğu",
        "meaning": "Müziğin ve şiirin etkisiyle kendinden geçme, duygu fırtınasıyla ruhani vecd ve mest olma hali.",
        "quote": "«Ümmü Gülsüm'ün sesinde kitlelerin gözyaşlarıyla buluştuğu kolektif esrime.»"
    }
]

concept_cards = []
for c in iconic_concepts:
    concept_cards.append(f"""* **{c['word']}** ({c['culture']}): {c['meaning']}  
  > *{c['quote']}*""")

untranslatable_gallery_md = "\n\n".join(concept_cards)

# 6. Mutfak Felsefeleri & Sofra Adabı Özeti
gastronomy_highlights = """| Mutfak Kültürü | Temel Felsefe | Kutsal Sofra Ritüeli & Adabı | Ekmek / Karbonhidrat Kodu |
| :--- | :--- | :--- | :--- |
| 🇹🇷 **Türk & Anadolu** | Bereket, misafirperverlik ve Tanrı misafiri hakkı; nimete şükür. | Sofradan misafir doymadan kalkılmaz; ekmek yere düşerse öpülüp alına konur; çay ikramı sohbetin mührüdür. | Somun, Pide, Lavaş: Yeryüzünün bereketi |
| 🇯🇵 **Japon (Washoku)** | *Shun* (mevsimsellik), doğaya saygı, *Itadakimasu* (hayatını feda eden canlılara şükran). | Yemekten önce eller birleştirilip eğilinir; çubuklar asla dik batırılmaz (*Tsukitate-bashi* cenaze adetidir); çorba höpürdetilerek içilir (aşçıya saygı). | Gohan (Pirinç): Her tanesi bir emek |
| 🇫🇷 **Fransız (Haute & Terroir)** | *Art de Vivre* (Yaşama sanatı), *Terroir* (toprağın kimliği), gastronomi bir entelektüel eylemdir. | Yemek bir performans ve törendir; şarap ile yemek eşleşmesi zorunludur; sofra en az 2-3 saat sürer; ekmek tabağın soluna konur. | Baguette: Fransız cumhuriyet mirası |
| 🇮🇹 **İtalyan (Cucina Povera)** | Malzemenin saflığı, sadelik, aile birliği ve mevsiminde taze ürün. | Saat 11:00'den sonra Asla Cappuccino içilmez; makarnanın üzerine asla ketçap sıkılmaz; balıklı makarnaya peynir serpilmez; sofra kutsal aile meclisidir. | Ciabatta, Focaccia: Aile ocağının sıcaklığı |
| 🇨🇳 **Çin (Yin-Yang & Uyum)** | Yiyecek ilaçtır (*Shi Liao*); tatların dengesi (tatlı, ekşi, acı, tuzlu, umami); ortak paylaşılan döner masa. | Balığın başı masadaki en kıdemli veya onur konuğuna çevrilir; kase göğse yakın tutularak çubukla yenir; tabak tamamen temizlenmez (aşçı yetersiz doyurdu sanmasın diye). | Fan (Pirinç) & Mantou (Buharda Ekmek) |
| 🇮🇳 **Hint (Ayurvedik Denge)** | *Sattvik*, *Rajasik*, *Tamasik* enerji dengesi; yemek prana (yaşam gücü) taşır. | Yemek sağ el ile yenir (sol el temiz kabul edilmez); tabaktaki tüm lezzetler parmak uçlarıyla hissedilerek vücuda alınır (*Thali* geleneği). | Roti, Naan, Chapati: Ateşin kutsal bereketi |
| 🇲🇽 **Meksika (Mısır & Ata Ruhu)** | Mısır insanın özüdür (Maya Popol Vuh efsanesi); yemek atalarla kurulan canlı köprüdür. | Ölüler Günü'nde (*Día de los Muertos*) mezarlar ziyafet sofrasına çevrilir; yemek paylaşılmadan yenmez; sokak taquería'sı eşitlik alanıdır. | Tortilla: Bin yıllık kutsal mısır döngüsü |"""

# 7. Nezaket Kuralları ve İletişim Tarzları Özeti
etiquette_highlights = """| Kültürel Parametre | Yüksek Bağlamlı Kültürler (High-Context)<br/>*(Japonya, Çin, Türkiye, Arap Dünyası, Latin Amerika)* | Düşük Bağlamlı Kültürler (Low-Context)<br/>*(Almanya, İsviçre, ABD, İskandinavya, Hollanda)* |
| :--- | :--- | :--- |
| **İletişim Üslubu** | İmalı, zarif, satır araları yüklü, söylenmeyenler söylenenlerden daha mühimdir (*Haragei*). | Net, dolaysız, şeffaf, kelimeler lafzi anlamıyla anlaşılır; imaya yer yoktur. |
| **Hayır Deme Sanatı** | Doğrudan «Hayır» demek kabalık sayılır; «Düşünelim», «Bir bakalım», sessizlik veya tebessüm tercih edilir. | Doğrudan ve tereddütsüz «Nein» veya «No» denir; profesyonellik ve dürüstlük sayılır. |
| **Zaman Algısı (P-Time vs M-Time)** | Polikronik: İlişkiler ve insani muhabbet saatten önemlidir; esnek zaman anlayışı vardır. | Monokronik: Dakiklik kutsaldır; 5 dakika geç kalmak bile derin bir saygısızlık kabul edilir. |
| **Sosyal Mesafe (Proxemics)** | Yakın temas, sarılma, öpüşme ve samimi fiziksel temas normdur; mesafe sıcaklığı gösterir. | Geniş kişisel alan (1.5m); fiziksel temas profesyonel veya kamusal alanda hoş karşılanmaz. |
| **Kartvizit / Selamlaşma** | Kartvizit iki elle saygıyla tutulur ve incelenir (*Meishi*); selamlaşma statüye göre derinleşir. | Hızlıca cebe atılabilir; sıkı ve kuru bir el sıkışma kafidir. |"""

# 8. Jeopolitik ve İstihbarat Yönlendirme Matrisi (11 Özel Dosya)
intel_matrix_rows = [
    (
        "☢️ **Nükleer Cephanelikler & Triad**",
        "12,121 Nükleer Başlık, 9 Nükleer Güç, Kıtalararası Balistik Füzeler (ICBM), SSBN ve Stratejik Bombardıman Mimarisi",
        "[`geopolitics_and_intelligence/NUCLEAR_TRIAD_AND_STRATEGIC_ARSENALS.md`](geopolitics_and_intelligence/NUCLEAR_TRIAD_AND_STRATEGIC_ARSENALS.md)"
    ),
    (
        "⚔️ **Küresel Silah Ticareti & MIC Oligopolü**",
        "$2.4+ Trilyonluk Askeri Harcama, Lockheed, Raytheon, BAE Systems, Rostec; Demir Üçgen ve Döner Kapı Mekanizması",
        "[`geopolitics_and_intelligence/GLOBAL_ARMS_TRADE_AND_MIC_OLIGOPOLY.md`](geopolitics_and_intelligence/GLOBAL_ARMS_TRADE_AND_MIC_OLIGOPOLY.md)"
    ),
    (
        "🛡️ **Savunma Paktları & Askeri İttifaklar**",
        "NATO (Madde 5), CSTO (Madde 4), AUKUS, Quad, Rio Paktı, ANZUS; Müşterek Savunma Harcamaları ve Nükleer Şemsiye",
        "[`geopolitics_and_intelligence/DEFENSE_ALLIANCES_AND_SECURITY_PACTS.md`](geopolitics_and_intelligence/DEFENSE_ALLIANCES_AND_SECURITY_PACTS.md)"
    ),
    (
        "⚠️ **Finansal Yaptırımlar & Bypass Koridorları**",
        "Dondurulan $300B+ Rus Rezervi, OFAC Yaptırımları, İran/Venezuela/Kuzey Kore Ambargoları ve SPFS/CIPS/Takas Hatları",
        "[`geopolitics_and_intelligence/SANCTIONS_REGIMES_AND_BYPASS_CORRIDORS.md`](geopolitics_and_intelligence/SANCTIONS_REGIMES_AND_BYPASS_CORRIDORS.md)"
    ),
    (
        "⛏️ **Kritik Madenler & Rafinaj Tekelleri**",
        "Kobalt, Lityum, Nadir Toprak Elementleri (REE), Nikel, Galyum; Çin'in %70-90 Rafinaj Monopolü ve İhracat Kısıtlamaları",
        "[`geopolitics_and_intelligence/CRITICAL_RAW_MATERIALS_AND_REFINING_MONOPOLIES.md`](geopolitics_and_intelligence/CRITICAL_RAW_MATERIALS_AND_REFINING_MONOPOLIES.md)"
    ),
    (
        "🌐 **Denizaltı Kabloları & SIGINT İstasyonları**",
        "Dünya İnternetinin %99'u, 10 Kritik Boğaz Koridoru; FVEY Dinleme Merkezleri (Bude, Diego Garcia, Menwith Hill)",
        "[`geopolitics_and_intelligence/SUBSEA_CABLES_AND_GLOBAL_SIGINT_STATIONS.md`](geopolitics_and_intelligence/SUBSEA_CABLES_AND_GLOBAL_SIGINT_STATIONS.md)"
    ),
    (
        "💰 **Egemen Varlık Fonları (SWF) & Devlet Sermayesi**",
        "$12+ Trilyonluk Egemen Sermaye; Norveç NBIM, Çin CIC, BAE ADIA, Suudi PIF; Finansal Kaldıraç ve Ulusal Güvenlik Yatırımları",
        "[`geopolitics_and_intelligence/SOVEREIGN_WEALTH_FUNDS_AND_STATE_CAPITALISM.md`](geopolitics_and_intelligence/SOVEREIGN_WEALTH_FUNDS_AND_STATE_CAPITALISM.md)"
    ),
    (
        "🚢 **Küresel Gölge Tanker Filosu (Dark Fleet)**",
        "~850 Hayalet Petrol Tankeri; Gabon, Cook Adaları, Liberya Bayrakları; STS Denizde Aktarma Sahaları ve Sahte AIS Manipülasyonu",
        "[`geopolitics_and_intelligence/SHADOW_FLEET_MARITIME_AND_STS_HUBS.md`](geopolitics_and_intelligence/SHADOW_FLEET_MARITIME_AND_STS_HUBS.md)"
    ),
    (
        "⚓ **Deniz Darboğazları & Jeopolitik Kilit Noktaları**",
        "Hürmüz (21M v/g), Malakka (17M v/g), Babülmendep, Süveyş, Türk Boğazları, Panama; Küresel Ticaretin 8 Kırılgan Noktası",
        "[`geopolitics_and_intelligence/MARITIME_CHOKEPOINTS_AND_TRANSIT_VULNERABILITIES.md`](geopolitics_and_intelligence/MARITIME_CHOKEPOINTS_AND_TRANSIT_VULNERABILITIES.md)"
    ),
    (
        "⚔️ **Özel Askeri Şirketler (PMC) & Paramiliter Güçler**",
        "Wagner / Afrika Kolordusu, Constellis (Blackwater), Sadat, Executive Outcomes; Gri Bölge Harp Doktrini ve İnkar Edilebilirlik",
        "[`geopolitics_and_intelligence/PMC_MERCENARY_GROUPS_AND_PROXY_WARFARE.md`](geopolitics_and_intelligence/PMC_MERCENARY_GROUPS_AND_PROXY_WARFARE.md)"
    ),
    (
        "🕵️ **Küresel İstihbarat Teşkilatları & Kara Bütçeler**",
        "CIA, MI6, MİT, Mossad, SVR, MSS, BND, RAW; HUMINT/SIGINT Teşkilat Mimarisi, Kara Bütçeler ve Gizli Operasyon Yetkileri",
        "[`geopolitics_and_intelligence/GLOBAL_INTELLIGENCE_AGENCIES_AND_BLACK_BUDGETS.md`](geopolitics_and_intelligence/GLOBAL_INTELLIGENCE_AGENCIES_AND_BLACK_BUDGETS.md)"
    )
]

intel_matrix_table_md = "\n".join([
    f"| {col[0]} | {col[1]} | {col[2]} |"
    for col in intel_matrix_rows
])

master_readme_content = f"""# 🏛️ MEDENİYET ATLASI
### *Dünya Uluslarının Kültürel Kodları, Yaşam Felsefeleri, Medeniyet Havzaları ve Gerçek Güç Anatomisi Ansiklopedisi*

<p align="center">
  <img src="assets/images/hero_banner.jpg" alt="Medeniyet Atlası Hero Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Ansiklopedi-K%C3%BClt%C3%BCrel%20Kodlar%20%26%20Medeniyet-darkgreen?style=for-the-badge&logo=bookstack" alt="Encyclopedia">
  <img src="https://img.shields.io/badge/Kapsam-205%20%C3%9Clke%20%26%20B%C3%B6lge-blue?style=for-the-badge&logo=globe" alt="Coverage">
  <img src="https://img.shields.io/badge/Medeniyet%20Havzas%C4%B1-9%20B%C3%BCy%C3%BCk%20Havza-teal?style=for-the-badge" alt="Civilization">
  <img src="https://img.shields.io/badge/%C3%87evrilemeyen%20Kavramlar-50+%20Ruh%20Kavram%C4%B1-purple?style=for-the-badge" alt="Concepts">
  <img src="https://img.shields.io/badge/Gastronomi-D%C3%BCnya%20Sofra%20Felsefeleri-orange?style=for-the-badge" alt="Gastronomy">
  <img src="https://img.shields.io/badge/Ekonomik%20Arketip-8%20Makro%20G%C3%BC%C3%A7%20Blo%C4%9Fu-blueviolet?style=for-the-badge" alt="Economic Archetypes">
  <img src="https://img.shields.io/badge/G%C3%BC%C3%A7%20Anatomisi-4%20Katmanl%C4%B1%20Mimarisi-black?style=for-the-badge" alt="4-Layer">
  <img src="https://img.shields.io/badge/%C4%B0stihbarat%20Dosyalar%C4%B1-11%20Stratejik%20Rapor-darkred?style=for-the-badge" alt="Intelligence">
  <img src="https://img.shields.io/badge/Vaka%20Analizleri-12%20Adli%20Soru%C5%9Fturma-crimson?style=for-the-badge" alt="Case Studies">
  <img src="https://img.shields.io/badge/Do%C4%9Frulama-Admiralty%20Kodu%20B2+-success?style=for-the-badge" alt="Verification">
  <img src="https://img.shields.io/badge/Lisans-A%C3%A7%C4%B1k%20K%C3%BClt%C3%BCr%20(CC%20BY--SA%204.0)-lightgrey?style=for-the-badge" alt="License">
</p>

---

## 📑 İÇİNDEKİLER TABLOSU

1. [🏛️ Giriş ve Medeniyet Atlası Manifestosu](#️-giriş-ve-medeniyet-atlasi-manifestosu)
2. [🎭 Dünya Medeniyetleri ve Kültürel Kodlar Rehberi (Cultural DNA)](#-dünya-medeniyetleri-ve-kültürel-kodlar-rehberi-cultural-dna)
   - [🌐 9 Büyük Küresel Medeniyet Havzası](#-9-büyük-küresel-medeniyet-havzasi)
   - [🧬 20 Örnek Medeniyet Çapası: Ulusal Karakterler ve Yaşam Adabı](#-20-örnek-medeniyet-çapasi-ulusal-karakterler-ve-yaşam-adabi)
   - [📖 Çevrilemeyen Ruh Kavramları Galerisi](#-çevrilemeyen-ruh-kavramlari-galerisi)
   - [🍲 Dünya Gastronomi Felsefeleri & Sofra Ritüelleri](#-dünya-gastronomi-felsefeleri--sofra-ritüelleri)
   - [🧭 Küresel Nezaket Kuralları, İletişim Kodları ve Sosyal Tabular](#-küresel-nezaket-kurallari-iletişim-kodlari-ve-sosyal-tabular)
   - [📚 Medeniyet & Kültür Kütüphanesi Arşivi (/culture)](#-medeniyet--kültür-kütüphanesi-arşivi-culture)
3. [🗺️ 205 ÜLKELİK KÜRESEL ATLAS: TÜM DÜNYA ULUSLARI VE ALT İÇERİK REHBERİ](#️-205-ülkelik-küresel-atlas-tüm-dünya-uluslari-ve-alt-i̇çerik-rehberi)
   - [📍 Bölgesel Fihrist ve Hızlı Atlama](#-bölgesel-fihrist-ve-hizli-atlama)
   - [📑 205 Ülkelik Master Alt İçerik Navigasyon Tablosu](#-205-ülkelik-master-alt-i̇çerik-navigasyon-tablosu)
4. [📊 Ekonomik Modellere Göre 8 Küresel Güç Bloğu (/01_... - /08_...)](#-ekonomik-modellere-göre-8-küresel-güç-bloğu-01----08_)
5. [🏛️ Metodoloji: 4 Katmanlı Ülke ve Güç Mimarisi](#️-metodoloji-4-katmanli-ülke-ve-güç-mimarisi)
6. [🛡️ Doğrulama Standardı: NATO / Admiralty Kodu (B2+)](#️-doğrulama-standardi-nato--admiralty-kodu-b2)
7. [🌐 Gerçekçi Güç, Savunma ve İstihbarat Doktrini (/geopolitics_and_intelligence)](#-gerçekçi-güç-savunma-ve-istihbarat-doktrini-geopolitics_and_intelligence)
   - [🛰️ Küresel İstihbarat ve Stratejik Dosyalar Matrisi (11 Özel Rapor)](#️-küresel-istihbarat-ve-stratejik-dosyalar-matrisi-11-özel-rapor)
   - [💸 Kleptokrasi & Offshore Sermaye Kaçırma Döngüsü](#-kleptokrasi--offshore-sermaye-kaçirma-döngüsü)
   - [🧠 Bilişsel Savaş & Siber İstihbarat Matrisi (5GW)](#-bilişsel-savaş--siber-istihbarat-matrisi-5gw)
   - [🚢 Küresel Deniz Darboğazları & Jeopolitik Kilit Noktaları](#-küresel-deniz-darboğazlari--jeopolitik-kilit-noktalari)
8. [🗺️ Bölgesel Master Jeopolitik Güç Dosyaları (/regions)](#️-bölgesel-master-jeopolitik-güç-dosyalari-regions)
9. [📁 Derin Adli OSINT Vaka Analizleri (/dossiers)](#-derin-adli-osint-vaka-analizleri-dossiers)
10. [📚 Ansiklopedik Araştırma Dosyaları & Teori Külliyatı (/research)](#-ansiklopedik-araştirma-dosyalari--teori-külliyati-research)
11. [🔬 Metodoloji ve OSINT Araştırma Kılavuzları (/methodology)](#-metodoloji-ve-osint-araştirma-kilavuzlari-methodology)
12. [🛠️ CLI Terminal Aracı ile Kullanım (xray_cli.py)](#️-cli-terminal-araci-ile-kullanim-xray_clipy)
13. [🧪 Bütünlük ve Veri Doğrulama Testleri](#-bütünlük-ve-veri-doğrulama-testleri)
14. [⚖️ Etik, Hukuki Beyan ve Açık Kültür Lisansı](#️-etik-hukuki-beyan-ve-açik-kültür-lisansi)

---

## 🏛️ GİRİŞ VE MEDENİYET ATLASI MANİFESTOSU

> *"Bir ulusu gerçekten tanımak; onun yalnızca sınırlarını, başkentini ve bayrağını bilmek değildir. Bir ulusu tanımak; bin yıllık kolektif hafızasını, sevinçlerini ve yaslarını, sofrasındaki ekmeği bölüşme adabını, başka hiçbir dile tam çevrilemeyen ruh kavramlarını (Gönül, Ikigai, Gemütlichkeit, Saudade, Ubuntu), selamlaşma inceliklerini ve dünyaya bakış felsefesini öğrenmektir."*

Bu projenin **birincil ve en temel varoluş gayesi**; dünya üzerindeki 205 egemen ve jeopolitik ülkeyi tüm kültürel derinlikleri, medeniyet kodları, yaşam tarzları, mutfak gelenekleri, edebi mirası ve toplumsal karakterleriyle tanıtan **muazzam bir açık kaynaklı dünya ansiklopedisi** sunmaktır.

Dünya ulusları birbirine düşman soyut bayraklardan ibaret değildir; her biri binlerce yıllık coğrafi sınavlardan, göçlerden ve felsefi arayışlardan süzülmüş eşsiz birer kültürel hazinedir. Bu atlas, okuyucusuna bir Japon'un *Wabi-sabi* estetiğindeki dinginliği, bir Türk'ün *Gönül* ve *İmece* dilindeki derin cömertliği, bir Alman'ın *Gemütlichkeit* huzurunu, bir Slav'ın *Toska* melankolisini ve bir Afrikalının *Ubuntu* ("Biz olduğumuz için benim") dayanışmasını anlama kapısını aralar.

### ⚖️ Gerçekçilik Dengesi: Neden Derin Güç ve İstihbarat Katmanı da Var?
Bir ülkeyi yalnızca masalsı turizm broşürleriyle anlatmak, o ülkenin halkına ve tarihsel gerçeğine haksızlık etmektir. Bir ulusun gündelik hayatı ve kültürel dokusu ne kadar zengin olursa olsun; o toplum aynı zamanda **derin devlet mekanizmaları, askeri ittifaklar, oligarşik sermaye konsorsiyumları, enerji darboğazları ve istihbarat savaşları** gerçeğiyle kuşatılmıştır.

Bu nedenle bu ansiklopedi; **kültürü ve insanı merkeze koyan ana gövdesini**, adli bilişim ve OSINT disipliniyle hazırlanmış **derin güç anatomisi** ile dengeler. Tüm detaylı istihbari ve askeri veri setleri [`geopolitics_and_intelligence/`](geopolitics_and_intelligence/README.md) dizininde bağımsız araştırma dosyalarında toplanmış; ana omurgada ise bu dinamiklerin kültürel ve insani izdüşümleri öne çıkarılmıştır.

---

## 🎭 DÜNYA MEDENİYETLERİ VE KÜLTÜREL KODLAR REHBERİ (CULTURAL DNA)

<p align="center">
  <img src="assets/images/world_civilizations_cultural_realms.jpg" alt="Dünya Medeniyet Havzaları ve Kültürel Kodlar Kartografyası" width="90%">
</p>

İnsanlık tarihi, belirli coğrafi ve manevi havzalarda şekillenen büyük medeniyetlerin etkileşimidir. Bu bölümde dünya toplumlarının temel kültürel kodları, yaşam felsefeleri ve müşterek değerleri incelenmektedir:

### 🌐 9 Büyük Küresel Medeniyet Havzası
> 📖 *Genişletilmiş medeniyet havzaları felsefesi ve tarihi için: [`culture/CIVILIZATION_REALMS_AND_PHILOSOPHIES.md`](culture/CIVILIZATION_REALMS_AND_PHILOSOPHIES.md)*

| Medeniyet Havzası | Temel Felsefe & Toplumsal Ethos | Temsilci Ülkeler | Müşterek Erdemler & Değerler |
| :--- | :--- | :--- | :--- |
{realms_table_md}

---

### 🧬 20 Örnek Medeniyet Çapası: Ulusal Karakterler ve Yaşam Adabı
> 💡 *Her ülkenin kendi klasöründe (`01_culture_demographics/society_history.md`) tüm kültürel kodları, ritüelleri ve tabuları detaylıca işlenmiştir.*

| Ülke | Ulusal Karakter & Temel Ethos | Çevrilemeyen Ruh Kavramları | İletişim Tarzı | Gastronomi & Sofra Felsefesi |
| :--- | :--- | :--- | :--- | :--- |
{culture_table_md}

---

### 📖 ÇEVRİLEMEYEN RUH KAVRAMLARI GALERİSİ
> 📚 *50'den fazla küresel kavramın kökenbilimsel ve sosyolojik tahlili için: [`culture/UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md`](culture/UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md)*

<p align="center">
  <img src="assets/images/untranslatable_soul_concepts_wisdom.jpg" alt="Çevrilemeyen Ruh Kavramları ve Kültürel Bilgelik" width="90%">
</p>

Bir dilin sözlüğünde tek kelimeyle yer alıp başka hiçbir dünya diline doğrudan tercüme edilemeyen kavramlar, o milletin bin yıllık kolektif şuurunun ve yaşam tecrübesinin en saf kristalleridir:

{untranslatable_gallery_md}

---

### 🍲 DÜNYA GASTRONOMİ FELSEFELERİ & SOFRA RİTÜELLERİ
> 🍷 *Dünya mutfaklarının ritüelistik ve felsefi anatomisi için: [`culture/GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md`](culture/GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md)*

<p align="center">
  <img src="assets/images/global_gastronomy_table_rituals.jpg" alt="Dünya Gastronomi Felsefeleri ve Sofra Ritüelleri" width="90%">
</p>

Yemek, biyolojik bir ihtiyaçtan öte, bir medeniyetin doğayla kurduğu barışın, inanç sisteminin ve insani yakınlığının en somut ayinidir:

{gastronomy_highlights}

---

### 🧭 KÜRESEL NEZAKET KURALLARI, İLETİŞİM KODLARI VE SOSYAL TABULAR
> 🤝 *Kültürlerarası iletişim ve protokol rehberi için: [`culture/WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md`](culture/WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md)*

Farklı kültürlerde saygı ve hakaret kavramları taban tabana zıt şekillerde tezahür edebilir. Dünyayı doğru anlamak, bu görünmez kültürel sınırları bilmeyi gerektirir:

{etiquette_highlights}

---

### 📚 MEDENİYET & KÜLTÜR KÜTÜPHANESİ ARŞİVİ (/culture)

Kültürel zenginliğin derinlemesine tahlil edildiği özel araştırma dosyalarımız:

* 🏛️ [`culture/CIVILIZATION_REALMS_AND_PHILOSOPHIES.md`](culture/CIVILIZATION_REALMS_AND_PHILOSOPHIES.md): 9 büyük küresel havzanın tarihi, antropolojik gelişimi ve dünya görüşü.
* 📖 [`culture/UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md`](culture/UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md): 50+ küresel çevrilemeyen kavramın kökeni, anlamı ve günlük hayattaki yansıması.
* 🍲 [`culture/GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md`](culture/GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md): Sofra adabı, kutsal ekmek kültleri, çay/kahve seremonileri ve paylaşma ahlakı.
* 🧭 [`culture/WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md`](culture/WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md): Vücut dili, jestler, hediyeleşme adabı, sessizlik kültürü ve ölümcül sosyal tabular.
* 📚 [`culture/README.md`](culture/README.md): Kültür araştırmaları merkezi indeksi ve kaynakçası.

---

## 🗺️ 205 ÜLKELİK KÜRESEL ATLAS: TÜM DÜNYA ULUSLARI VE ALT İÇERİK REHBERİ

Bu bölümde dünyadaki **205 egemen ve jeopolitik entite** alfabetik ve bölgesel olarak listelenmiştir. Her bir satırdaki bağlantılar, o ülkenin doğrudan ilgili **alt içerik dosyalarına** (Medeniyet/Kültür, Gölge Güç/OSINT, Anayasal Düzen ve Makroekonomi) tek tıkla ulaşmanızı sağlar:

### 📍 Bölgesel Fihrist ve Hızlı Atlama

{regional_nav_md}

---

### 📑 205 Ülkelik Master Alt İçerik Navigasyon Tablosu

Aşağıdaki interaktif matriste yer alan her bağlantı doğrudan ilgili dosyanın derinliğine yönlendirir:
* **Ülke Adı:** Ülkenin ana istihbarat ve kültür özet raporunu açar (`countries/<ülke>/README.md`).
* **Ekonomik Model:** Ülkenin küresel işbölümündeki ekonomik bloğunu açar (`<blok>/<ülke>/README.md`).
* **🎭 Kültür & Tarih:** Kültürel kodları, çevrilemeyen ruh kavramlarını ve yaşam tarzını açar (`01_culture_demographics/society_history.md`).
* **🕵️ Gölge Güç:** Oligark ağlarını, derin klikleri ve kleptokrasi analizini açar (`04_shadow_power_osint/real_power_dynamics.md`).
* **🏛️ Anayasa:** Resmi rejim, parlamento ve yargı yapısını açar (`02_official_state/constitution_gov.md`).
* **📈 Makroekonomi:** GSYİH, dış ticaret ve kayıt dışı ekonomi verilerini açar (`03_official_economy/macroeconomics.json`).

| Ülke & Ana Dosya | ISO | Başkent | Ekonomik Model | 🎭 Kültür, Medeniyet & Yaşam | 🕵️ Gölge Güç & OSINT | 🏛️ Resmi Devlet | 📈 Makroekonomi |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- | :--- |
{atlas_table_md}

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

## 🏛️ METODOLOJİ: 4 KATMANLI ÜLKE VE GÜÇ MİMARİSİ

<p align="center">
  <img src="assets/images/4_layer_power_architecture.jpg" alt="Medeniyet Atlası 4 Katmanlı Ülke ve Güç Mimarisi" width="90%">
</p>

Repodaki istisnasız her ülke klasörü, birbirine bağlı ve disiplinlerarası **4 derin katmandan** meydana gelir:

### 🧩 Katmanların Analitik Ayrımı:
* **01. Medeniyet Kimliği, Kültür & Demografi (`01_culture_demographics/`):** Toplumun kültürel DNA'sı, çevrilemeyen ruh kavramları, yaşam ritüelleri, mutfak felsefesi, tabuları ve demografik yapısı (`society_history.md`, `demographics.csv`).
* **02. Resmi Devlet Mekanizması & Anayasa (`02_official_state/`):** Görünen yürütme, parlamenter veya başkanlık yapısı, anayasal kuvvetler ayrılığı illüzyonu, yargı teşkilatı ve resmi silahlı kuvvetler doktrini (`constitution_gov.md`).
* **03. Resmi Makroekonomi & Dış Ticaret (`03_official_economy/`):** Nominal ve SAGP GSYİH, cari denge, döviz rezervleri, dış borç stoku, bütçe açığı ve en büyük dış ticaret ortakları (`macroeconomics.json`).
* **04. Gölge Güç, Kleptokrasi & OSINT (`04_shadow_power_osint/`):** Gerçek güç odakları, askeri-istihbarat klikleri, oligark konsorsiyumları, hanedan tröstleri, offshore sermaye kaçış kanalları, basın sansür filtreleri ve algoritmik kontrol mekanizmaları (`real_power_dynamics.md`, `oligarch_network.csv`, `media_censorship_matrix.md`).

```mermaid
flowchart TD
    subgraph Katmanlar["Medeniyet Atlası 4 Katmanlı Ülke ve Güç Anatomisi"]
        L1["01. Kültür, Medeniyet Kimliği & Demografi<br/>(Kültürel DNA, yaşam felsefesi, sofra adabı, çevrilemeyen kavramlar)"]
        L2["02. Resmi Devlet Mekanizması & Anayasa<br/>(Görünen yürütme, parlamento, kanunlar, ordu bürokrasisi)"]
        L3["03. Resmi Makroekonomi & Dış Ticaret<br/>(GSYİH, ihracat-ithalat, döviz rezervleri, kamu borcu)"]
        L4["04. Gölge Güç, Kleptokrasi & OSINT<br/>(Askeri klikler, oligark ağları, offshore tröstler, medya tekelleri)"]
    end
    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 -.->|"Perde Arkasından Yürütmeyi Yönlendirir"| L2
    L4 -.->|"Kamu Bütçesini ve İhaleleri Gasp Eder"| L3
```

---

## 🛡️ DOĞRULAMA STANDARDI: NATO / ADMİRALTY KODU (B2+)

Medeniyet Atlası bünyesinde yer alan tüm istihbarat ve araştırma verileri, uluslararası askeri ve istihbarat doktrinlerinde kabul gören **Admiralty Kod (Stanag 2097)** metodolojisine göre çapraz kontrolden geçirilir. Projenin kabul eşiği **B2 (Genellikle Güvenilir / Muhtemelen Doğru)** düzeyidir:

| Kaynak Güvenilirliği (Harf) | Bilgi Doğruluğu (Rakam) | Medeniyet Atlası Kabul Eşiği |
| :--- | :--- | :---: |
| **A - Tamamen Güvenilir:** Şüpheye yer bırakmayan resmi tutanaklar, adli iddianameler, sızdırılmış orijinal belgeler. | **1 - Teyit Edilmiş:** Bağımsız birden fazla doğrulanabilir kaynak ve çapraz log kayıtları ile kanıtlanmış. | ✅ **A1** (Mutlak Delil) |
| **B - Genellikle Güvenilir:** Uluslararası denetim raporları (FATF, ICIJ, OCCRP), akademik araştırmalar, saygın araştırma merkezleri. | **2 - Muhtemelen Doğru:** En az iki bağımsız açık kaynak ve lojistik/finansal veriyle teyit edilmiş. | ✅ **B2** (Minimum Standart) |
| **C - Oldukça Güvenilir:** Yerel gazetecilik araştırmaları, sektörel raporlar. | **3 - Mümkün:** Mantıksal çıkarımlarla uyumlu fakat doğrudan adli belgesi olmayan. | ⚠️ Ek Teyit Gerekir |
| **D - Genellikle Güvenilmez:** Taraflı siyasi beyanlar, anonim sosyal medya iddiaları. | **4 - Şüpheli:** Doğrulanamayan veya çelişkili iddialar. | ❌ Reddedilir |

---

## 🌐 GERÇEKÇİ GÜÇ, SAVUNMA VE İSTİHBARAT DOKTRİNİ (/geopolitics_and_intelligence)

> *"Görünen hükümetin arkasında, halka karşı hiçbir bağlılığı olmayan ve hiçbir sorumluluk kabul etmeyen görünmez bir hükümet taht kurmuştur."*  
> — **Theodore Roosevelt** (ABD 26. Başkanı, 1912)

> *"Ticaret ve imalat dünyasında öyle bazı adamlar var ki, bir şeyden korkuyorlar. Biliyorlar ki bir yerlerde öyle organize, öyle sinsi, öyle uyanık, öyle kilitli ve öyle yaygın bir güç var ki, onu kınarken fısıltıyla bile konuşmamak en iyisi."*  
> — **Woodrow Wilson** (ABD 28. Başkanı, 1913)

> *"Washington'daki gerçek yöneticiler görünmezdir ve güçlerini perde arkasından kullanırlar."*  
> — **Felix Frankfurter** (ABD Yüksek Mahkeme Yargıcı, 1952)

> *"Derin siyaset, resmi siyasal sistemin kurallarını çiğneyen, ulusal güvenlik devleti bürokrasisi, organize suç örgütleri ve uluslararası finans konsorsiyumlarının gizli ittifakından doğan örtülü iktidardır."*  
> — **Prof. Peter Dale Scott** (*The Road to 9/11*)

Ulusların kaderini belirleyen gerçek güç odakları; resmi kabinelerden ziyade örtülü istihbarat paktlarında, hanedan varlık tröstlerinde, askeri-endüstriyel tedarik zincirlerinde, nükleer caydırıcılık doktrinlerinde ve denizaltı fiber hatlarında düğümlenmektedir.

Bu devasa veri külliyatı, projenin okunabilirliğini ve kültürel odağını korumak amacıyla [`geopolitics_and_intelligence/`](geopolitics_and_intelligence/README.md) dizini altındaki **11 derin araştırma dosyasına** paylaştırılmıştır:

### 🛰️ KÜRESEL İSTİHBARAT VE STRATEJİK DOSYALAR MATRİSİ (11 ÖZEL RAPOR)

<p align="center">
  <img src="assets/images/nuclear_triad_strategic_deterrence.jpg" alt="Küresel Stratejik Nükleer Triad ve Savunma Gücü Mimarisi" width="90%">
</p>

| Stratejik Güç Alanı | Kapsam & Öne Çıkan Göstergeler | Özel Araştırma Raporu |
| :--- | :--- | :--- |
{intel_matrix_table_md}

> 📁 *Tüm istihbari dosyaların detaylı indeks ve kaynakçası için: [`geopolitics_and_intelligence/README.md`](geopolitics_and_intelligence/README.md)*

---

### 💸 KLEPTOKRASİ & OFFSHORE SERMAYE KAÇIRMA DÖNGÜSÜ

<p align="center">
  <img src="assets/images/offshore_kleptocracy_network.jpg" alt="Global Offshore Kleptocracy and Capital Flight" width="90%">
</p>

Küresel kleptokrasi; kamu kaynaklarının ve maden imtiyazlarının siyasi elitler ve oligarklar tarafından gasp edilerek BVI, Delaware, İsviçre ve Lüksemburg üzerinden Batı finans merkezlerine (Londra, New York, Dubai) aktarılması döngüsüdür:

1. **Yerleştirme (Placement):** İhale komisyonları ve kaynak rantı paravan yerel şirketlere aktarılır.
2. **Katmanlama (Layering):** Shell şirketler, trust fonları ve sahte ticaret faturalarıyla (TBML) para onlarca ülkeye dağıtılarak izi kaybettirilir.
3. **Bütünleştirme (Integration):** Sermaye Batı borsalarındaki tahvillere, lüks gayrimenkullere ve özel jetlere dönüştürülerek meşrulaştırılır.

---

### 🧠 BİLİŞSEL SAVAŞ & SİBER İSTİHBARAT MATRİSİ (5GW)

<p align="center">
  <img src="assets/images/cognitive_warfare_surveillance.jpg" alt="Cognitive Warfare and Cyber Surveillance Matrix" width="90%">
</p>

5. Nesil Harp (5GW), insan zihnini, algoritmik akışları ve küresel dijital haberleşme altyapısını hedef alır:
* **Denizaltı Kablo Dinleme:** Dünya internet trafiğinin %99'u denizaltı fiber optik hatlarından akar; FVEY paktı küresel trafiği stratejik iniş istasyonlarında filtreler.
* **Sıfır-Tıklama Casus Yazılımlar (Zero-Click):** Pegasus ve Predator gibi askeri araçlar kullanıcı hiçbir linke tıklamadan cihazın mikrofon, kamera ve şifreli yazışmalarını gerçek zamanlı çeker.
* **Algoritmik Kitle Manipülasyonu:** Sosyal medya bot orduları ve psikometrik hedeflemeler kitlelerin duygusal tepkilerini polarize etmek için kullanılır.

---

### 🚢 KÜRESEL DENİZ DARBOĞAZLARI & JEOPOLİTİK KİLİT NOKTALARI

<p align="center">
  <img src="assets/images/geopolitical_chokepoints.jpg" alt="Geopolitical Chokepoints and Strategic Corridors" width="90%">
</p>

Dünya ticaretinin ve deniz yoluyla taşınan petrolün %60'ından fazlası daracık birkaç su yolundan (Hürmüz, Malakka, Babülmendep, Süveyş, Türk Boğazları, Panama, Danimarka Boğazları) geçmek zorundadır. Bu kilit geçitlerin herhangi birinde yaşanacak bir kriz, dünya ekonomisinde anında enflasyonist şok ve tedarik felci yaratır.

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

Tarihin en büyük kleptokratik, yolsuzluk, derin devlet ve siber istihbarat operasyonlarının adli bilişim ve finansal akış analizleri:

| Vaka Dosyası | Konu | Temel Bulgular & Metodoloji |
| :--- | :--- | :--- |
| 💸 [**CASE_STUDY_1MDB.md**](dossiers/CASE_STUDY_1MDB.md) | 1MDB Egemen Varlık Fonu Soygunu | $4.5 Milyar kamu kaynağının Goldman Sachs tahvil ihraçları ve BVI paravan şirketleri üzerinden aklanması; Hollywood filmleri ve mega yat alımları. |
| ⚖️ [**CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md**](dossiers/CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md) | Magnitsky & Rus Çamaşırhanesi | Moldova mahkeme sahte ilamları ve Danske Bank Estonya şubesi üzerinden $20+ milyar oligark parasının Avrupa'ya kaçırılması. |
| 🏗️ [**CASE_STUDY_ODEBRECHT_LAVA_JATO.md**](dossiers/CASE_STUDY_ODEBRECHT_LAVA_JATO.md) | Odebrecht & Lava Jato Rüşvet Karteli | 12 Latin Amerika ülkesinde devlet başkanlarına ve bakanlara $788M rüşvet dağıtmak için kurulan resmi "Yapılandırılmış Operasyonlar Bölümü". |
| 📱 [**CASE_STUDY_PEGASUS_PROJECT.md**](dossiers/CASE_STUDY_PEGASUS_PROJECT.md) | Pegasus Sıfır-Tıklama Siber Casusluk | NSO Group casus yazılımının Cemal Kaşıkçı cinayeti, 14 devlet başkanı ve 189 gazeteciye karşı adli telemetri analizi. |
| 🗄️ [**CASE_STUDY_PANDORA_PAPERS_AND_OFFSHORE_SECRECY.md**](dossiers/CASE_STUDY_PANDORA_PAPERS_AND_OFFSHORE_SECRECY.md) | Pandora Belgeleri & ABD Vergi Cennetleri | 11.9 Milyon belgenin analizi; South Dakota trust yasaları, Ürdün Kralı, Tony Blair ve küresel liderlerin $32 Trilyonluk gizli servet mimarisi. |
| 💥 [**CASE_STUDY_NORD_STREAM_SABOTAGE_AND_ENERGY_WARFARE.md**](dossiers/CASE_STUDY_NORD_STREAM_SABOTAGE_AND_ENERGY_WARFARE.md) | Kuzey Akım Boru Hattı Sabotajı | 26 Eylül 2022 Bornholm patlamaları; 2.3 Richter sismik analizi, saturasyon dalışı zorlukları, BALTOPS tatbikatı ve Almanya'nın sanayisizleşmesi. |
| 🗡️ [**CASE_STUDY_OPERATION_GLADIO_AND_STAY_BEHIND_NETWORKS.md**](dossiers/CASE_STUDY_OPERATION_GLADIO_AND_STAY_BEHIND_NETWORKS.md) | Gladio & NATO Gizli Orduları | 1990 Andreotti itirafı; Gerginlik Stratejisi (Strategia della tensione), Bologna katliamı, P2 Mason Locası, Banco Ambrosiano ve Kontrgerilla. |
| 🏦 [**CASE_STUDY_BCCI_THE_BANK_OF_CROOKS_AND_CLINICS.md**](dossiers/CASE_STUDY_BCCI_THE_BANK_OF_CROOKS_AND_CLINICS.md) | BCCI: İstihbarat & Suç Bankası | 78 ülkede faaliyet gösteren $20B'lık bankanın çöküşü; CIA Afganistan/Kontra örtülü fonları, Noriega kokain aklaması ve A.Q. Khan nükleer ağı. |
| 💻 [**CASE_STUDY_STUXNET_OLYMPIC_GAMES_CYBER_SABOTAGE.md**](dossiers/CASE_STUDY_STUXNET_OLYMPIC_GAMES_CYBER_SABOTAGE.md) | Stuxnet: İlk Askeri Siber Silah | NSA ve Unit 8200'ün Natanz nükleer tesisine sabotajı; 4 sıfır-gün açığı, Siemens PLC manipülasyonu ve 1.000 gaz santrifüjünün rezonansla imhası. |
| 🧠 [**CASE_STUDY_CAMBRIDGE_ANALYTICA_AND_PSYCHOGRAPHIC_WARFARE.md**](dossiers/CASE_STUDY_CAMBRIDGE_ANALYTICA_AND_PSYCHOGRAPHIC_WARFARE.md) | Cambridge Analytica & Psikografik Harp | SCL Group, 87 milyon Facebook profili izinsiz hasadı, OCEAN psikometrik puanlaması, Brexit ve 2016 ABD Seçimleri mikro hedefli karanlık reklamları. |
| 🐙 [**CASE_STUDY_PROMIS_SOFTWARE_AND_INSLAW_AFFAIR.md**](dossiers/CASE_STUDY_PROMIS_SOFTWARE_AND_INSLAW_AFFAIR.md) | PROMIS Yazılımı & Inslaw Skandalı ("The Octopus") | Inslaw yazılımının Adalet Bakanlığı tarafından gasp edilmesi; Michael Riconosciuto, Robert Maxwell & Mossad üzerinden 80+ ülkeye arka kapılı casus yazılım satışı; Danny Casolaro cinayeti. |
| 🦅 [**CASE_STUDY_OPERATION_CYBERSCOOP_AND_PROJECT_RAVEN.md**](dossiers/CASE_STUDY_OPERATION_CYBERSCOOP_AND_PROJECT_RAVEN.md) | Proje Raven (Project Raven) & DarkMatter | Eski NSA siber savaşçılarının BAE petro-monarşisine transferi; "Karma" sıfır-tık iPhone casusluk platformu, Katar Emiri, Türk bürokratlar ve Amerikalı gazetecilerin yasa dışı dinlenmesi. |

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
| 💵 [**DE_DOLLARIZATION_AND_GEOECONOMIC_CURRENCY_WARS.md**](research/DE_DOLLARIZATION_AND_GEOECONOMIC_CURRENCY_WARS.md) | Dedolarizasyon & Bretton Woods III | Rezervlerin dondurulması ($300B CBR), Zoltan Pozsar Dış Para (Outside Money) tezi, mBridge multi-CBDC ağı ve Petroyuan. |
| 🤖 [**AI_SURVEILLANCE_ALGORITHMIC_WARFARE_AND_PALANTIR_NEXUS.md**](research/AI_SURVEILLANCE_ALGORITHMIC_WARFARE_AND_PALANTIR_NEXUS.md) | Algoritmik Harp & Palantir Ağı | Project Maven, Palantir Gotham/AIP, İsrail Unit 8200 Lavender ve Habsora hedef üretim sistemleri, Clearview AI ve biyometri. |
| 💊 [**NARCO_KLEPTOCRACY_CARTEL_STATE_CONVERGENCE_AND_DRY_CORRIDORS.md**](research/NARCO_KLEPTOCRACY_CARTEL_STATE_CONVERGENCE_AND_DRY_CORRIDORS.md) | Narko-Devlet & Kartel Yakınsaması | Fentanil sentetik devrimi, Suriye Kaptagon rejimi (Mahir Esad), Venezuela Güneşler Karteli ve Çin Yeraltı Bankacılığı (CUBS). |
| 🧬 [**BIOLOGICAL_WARFARE_GENOMICS_AND_DEEP_BIOSECURITY.md**](research/BIOLOGICAL_WARFARE_GENOMICS_AND_DEEP_BIOSECURITY.md) | Biyolojik Harp & Genomik İstihbarat | Dual-Use (DURC) ikilemi, BSL-4 laboratuvarları (Fort Detrick, Wuhan, Vector), CRISPR patojen sentezi, BGI Group ve GENINT. |

---

## 🔬 METODOLOJİ VE OSINT ARAŞTIRMA KILAVUZLARI (/methodology)

Araştırmacılar, antropologlar, gazeteciler ve analistler için hazırlanan teknik kılavuzlar:

* 🏢 [**CORP_REGISTRY_RECONNAISSANCE.md**](methodology/CORP_REGISTRY_RECONNAISSANCE.md): BVI, Delaware, İngiltere Companies House, Lüksemburg RCS ve İsviçre ticaret sicillerinde paravan şirket sahipliği ve UBO (Nihai Faydalanıcı Mülkiyet) tespiti.
* 🌐 [**DATA_COLLECTION_GUIDE.md**](methodology/DATA_COLLECTION_GUIDE.md): Çok kaynaklı istihbarat toplama, uydu görüntüleri (Sentinel/Planet), gemi takip (AIS/MarineTraffic) ve uçuş radarı (ADS-B Exchange) entegrasyonu.
* 🛡️ [**OSINT_VERIFICATION.md**](methodology/OSINT_VERIFICATION.md): NATO Admiralty Kod standardı, dijital görüntü adli bilişimi, EXIF metadata analizi ve tersine görsel arama ile dezenformasyon filtreleme.

---

## 🛠️ CLI TERMİNAL ARACI İLE KULLANIM (xray_cli.py)

Tüm repoyu komut satırından hızlıca sorgulamak, kültürel kodları incelemek ve istihbarat analizi yapmak için `scripts/xray_cli.py` geliştirilmiştir:

```bash
# Bir ülkenin 4 katmanlı tam kültür ve güç profilini terminalde görüntüle (Türkçe isim/slug veya ISO kodu)
python scripts/xray_cli.py country turkiye
python scripts/xray_cli.py country almanya
python scripts/xray_cli.py country rusya

# Bir ülkenin kültürel kodlarını, çevrilemeyen kavramlarını ve yaşam tarzını incele
python scripts/xray_cli.py culture turkiye
python scripts/xray_cli.py culture japonya

# Küresel 9 büyük medeniyet havzasını listele
python scripts/xray_cli.py culture

# İki ülkeyi jeopolitik, kültürel ve makroekonomik olarak karşılaştır
python scripts/xray_cli.py compare turkiye japonya

# Ekonomik güç bloğuna göre ülkeleri filtrele ve analiz et
python scripts/xray_cli.py economy 01_ileri_sanayi_g7

# Küresel savunma paktları ve askeri ittifakları incele
python scripts/xray_cli.py alliances nato

# Yaptırım rejimleri ve bypass koridorlarını sorgula
python scripts/xray_cli.py sanctions rus

# Kritik hammadde ve maden rafinaj tekellerini listele
python scripts/xray_cli.py minerals ree

# Denizaltı fiber kabloları ve SIGINT istasyonlarını incele
python scripts/xray_cli.py cables bude

# Özel askeri şirketleri (PMC) ve faaliyet alanlarını listele
python scripts/xray_cli.py pmc

# Küresel deniz darboğazları ve transit risklerini listele
python scripts/xray_cli.py chokepoints

# İstihbarat teşkilatlarını ara ve bütçelerini incele
python scripts/xray_cli.py intel mossad

# Egemen varlık fonlarını (SWF) listele veya filtrele
python scripts/xray_cli.py swf norway

# Küresel gölge tanker filosunu (Dark Fleet) ve STS aktarma bölgelerini incele
python scripts/xray_cli.py darkfleet

# Nükleer cephanelikler, stratejik triad ve caydırıcılık sistemlerini sorgula
python scripts/xray_cli.py nuclear rus

# Silah ticareti pazarını ve savunma sanayii devlerini sorgula
python scripts/xray_cli.py armstrade lockheed

# Otomatik çok katmanlı derin keşif raporu üret ve dışa aktar
python scripts/deep_recon.py turkiye --export

# 12 derin adli vaka analizini listele
python scripts/xray_cli.py cases

# 12 derin araştırma tezini ve doktrin dosyalarını listele
python scripts/xray_cli.py research
```

---

## 🧪 BÜTÜNLÜK VE VERİ DOĞRULAMA TESTLERİ

Repodaki 205 ülkenin dosya yapısı, veri tutarlılığı, ekonomik gruplandırması, kültürel atlas kayıtları ve jeopolitik/istihbarat dosyaları otomatik birim testleriyle korunur:

```bash
python tests/test_integrity.py
```

---

## ⚖️ ETİK, HUKUKİ BEYAN VE AÇIK KÜLTÜR LİSANSI

1. **Açık Kaynak ve Kültürel Miras Güvencesi:** Bu repodaki tüm kültürel analizler, antropolojik tahliller ve istihbarat verileri; kamuya açık resmi hükümet kayıtları, uluslararası denetim raporları (BM, UNESCO, Dünya Bankası, IMF, FATF), mahkeme iddianameleri ve bağımsız uluslararası araştırmacı gazetecilik konsorsiyumları (ICIJ, OCCRP) tarafından yayımlanmış belgelere dayanır.
2. **Akademik & Eğitsel Amaç:** Bu çalışma, dünya halklarını kültürel zenginlikleriyle tanıtmayı, ulusların derin felsefi kodlarını aktarmayı ve egemen devletlerin örtülü güç dinamiklerini anlamayı amaçlayan bağımsız bir açık ansiklopedidir.
3. **Telif & Lisans:** Bu veritabanı, küresel barış, kültürlerarası anlayış ve şeffaflık amacıyla **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** lisansı altında açık kaynak olarak sunulmuştur.

---

<p align="center">
  <b>MEDENİYET ATLASI (CIVILIZATION ATLAS)</b> &copy; 2026 &bull; <i>Dünya uluslarını ruhlarıyla tanımak, gerçeği tüm katmanlarıyla anlamak.</i><br/>
  <i>«İnsan bilmediğinin düşmanıdır; tanıdıkça sever ve anlar.»</i>
</p>
"""

with open(BASE_DIR / "README.md", "w", encoding="utf-8") as f:
    f.write(master_readme_content.strip() + "\n")

print(f"[SUCCESS] Master README.md generated successfully! ({len(master_readme_content.splitlines())} lines)")
