# -*- coding: utf-8 -*-
"""
scripts/generate_web_atlas.py
Medeniyet Atlası - İnteraktif Web Atlası & Jeopolitik Dashboard Üreteci
205 ülkenin Kültürel DNA, Makroekonomi, Güç Matrisi, Nükleer Triad, İttifaklar ve Darboğazlar
verilerini birleştirerek bağımsız, sıfır-bağımlılıklı, çevrimdışı çalışabilen tek dosya index.html üretir.
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
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent

def build_web_atlas():
    print("[*] Veri setleri yükleniyor...")
    
    # 1. Temel Veri Setleri
    with open(BASE_DIR / "global_datasets" / "countries_registry.json", "r", encoding="utf-8") as f:
        countries = json.load(f)

    with open(BASE_DIR / "global_datasets" / "cultural_codes_and_civilizations_registry.json", "r", encoding="utf-8") as f:
        culture_data = json.load(f)

    with open(BASE_DIR / "global_datasets" / "global_power_matrix.json", "r", encoding="utf-8") as f:
        power_matrix = json.load(f).get("countries", [])

    with open(BASE_DIR / "global_datasets" / "defense_alliances_and_treaties.json", "r", encoding="utf-8") as f:
        alliances_data = json.load(f).get("alliances", [])

    with open(BASE_DIR / "global_datasets" / "chokepoints_registry.json", "r", encoding="utf-8") as f:
        chokepoints_data = json.load(f).get("chokepoints", [])

    with open(BASE_DIR / "global_datasets" / "nuclear_arsenals_and_triad_registry.json", "r", encoding="utf-8") as f:
        nuclear_data = json.load(f).get("nuclear_powers", [])

    with open(BASE_DIR / "global_datasets" / "critical_raw_materials_supply_chain.json", "r", encoding="utf-8") as f:
        minerals_data = json.load(f).get("minerals", [])

    with open(BASE_DIR / "global_datasets" / "geopolitical_crisis_scenarios.json", "r", encoding="utf-8") as f:
        crises_data = json.load(f).get("scenarios", [])

    with open(BASE_DIR / "global_datasets" / "sovereign_wealth_funds_registry.json", "r", encoding="utf-8") as f:
        swf_data = json.load(f).get("funds", [])

    # Sözlük indeksleri
    culture_by_code = {c.get("code"): c for c in culture_data.get("countries_cultural_dna", [])}
    power_by_code = {p.get("code"): p for p in power_matrix}

    # Birleşik 205 Ülke Profili
    print("[*] 205 ülkenin 4 katmanlı verileri konsolide ediliyor...")
    consolidated_countries = []
    
    for c in countries:
        code = c["code"]
        c_dir = BASE_DIR / c.get("economy_path", c.get("path", f"countries/{c['slug']}"))
        if not c_dir.exists():
            c_dir = BASE_DIR / c.get("path", f"countries/{c['slug']}")

        # Makroekonomi
        macro = {}
        macro_path = c_dir / "03_official_economy" / "macroeconomics.json"
        if macro_path.exists():
            try:
                with open(macro_path, "r", encoding="utf-8") as mf:
                    macro = json.load(mf)
            except Exception:
                pass

        # Oligarklar
        oligarchs = []
        oligarch_path = c_dir / "04_shadow_power_osint" / "oligarch_network.csv"
        if oligarch_path.exists():
            try:
                with open(oligarch_path, "r", encoding="utf-8") as of:
                    oligarchs = list(csv.DictReader(of))
            except Exception:
                pass

        # Kültür DNA
        dna = culture_by_code.get(code, {})
        # Güç Matrisi
        pwr = power_by_code.get(code, {})

        consolidated_countries.append({
            "slug": c["slug"],
            "name": c["name"],
            "code": code,
            "region": c["region"],
            "capital": c["capital"],
            "population": c["population"],
            "gdp_usd_b": c["gdp_usd_b"],
            "shadow_economy_pct": c["shadow_economy_pct"],
            "economy_group_id": c.get("economy_group_id", "06_orta_gelir_ve_ureticiler"),
            "economy_group_name": c.get("economy_group_name", "Orta Gelir Düzeyi"),
            "csfi": pwr.get("fragility_index_csfi", 50.0),
            "risk_tier": pwr.get("risk_tier", "Orta Risk"),
            "gdp_per_capita": pwr.get("gdp_per_capita_usd", macro.get("gdp_per_capita_usd", 0)),
            "cultural_dna": dna,
            "macroeconomics": macro,
            "oligarchs": oligarchs,
            "path": c.get("path", f"countries/{c['slug']}")
        })

    # Sanat Eserleri Kataloğu
    artworks = [
        {"file": "hero_banner.jpg", "title": "Medeniyet Atlası Başlangıç", "category": "Genel Mimari", "desc": "İnsanlığın 205 egemen ulusunun kültürel ve jeopolitik kartografyası."},
        {"file": "world_civilizations_cultural_realms.jpg", "title": "9 Büyük Küresel Medeniyet Havzası", "category": "Kültür & Medeniyet", "desc": "Doğu Asya'dan Akdeniz'e, Sahra Altı'ndan Latin Amerika'ya kadim havzalar."},
        {"file": "untranslatable_soul_concepts_wisdom.jpg", "title": "Çevrilemeyen Ruh Kavramları Galerisi", "category": "Kültürel Felsefe", "desc": "Gönül, Ikigai, Gemütlichkeit, Saudade, Toska ve Ubuntu bilgeliği."},
        {"file": "global_gastronomy_table_rituals.jpg", "title": "Dünya Gastronomi ve Sofra Ritüelleri", "category": "Gastronomi", "desc": "Ekmek kültleri, çay seremonileri ve sofra paylaşma adabı."},
        {"file": "intercultural_etiquette_and_greeting_rituals.jpg", "title": "Kültürlerarası Görgü ve Tabular", "category": "Toplumsal Normlar", "desc": "Yüksek ve düşük bağlamlı iletişim, jestler ve ölümcül sosyal tabular."},
        {"file": "global_folklore_mythology_epics.jpg", "title": "Dünya Mitolojileri ve Kurucu Destanlar", "category": "Edebiyat & Epos", "desc": "Gılgamış'tan Dede Korkut'a, Mahabharata'dan Popol Vuh'a 14 kurucu destan."},
        {"file": "world_sacred_architecture_monuments.jpg", "title": "Kutsal Mimari ve Şehir Felsefesi", "category": "Mimari", "desc": "İslam kubbelerinden Gotik ışığa, Doğu Asya pagodalarından çamur mabetlerine."},
        {"file": "global_music_instruments_sonic_heritage.jpg", "title": "Geleneksel Çalgılar ve Ses Haritası", "category": "Ses Mirası", "desc": "Neyden koraya, sitardan didgeridoo'ya 12 kadim çalgının manevi karakteri."},
        {"file": "world_festivals_and_sacred_rituals.jpg", "title": "Dünya Festivalleri ve Kutsal Ritüeller", "category": "Takvim Döngüleri", "desc": "Nevruz, Diwali, Hanami ve Ölüler Günü arınma şenlikleri."},
        {"file": "4_layer_power_architecture.jpg", "title": "4 Katmanlı Ülke ve Güç Anatomisi", "category": "Metodoloji", "desc": "Toplum, Resmi Devlet, Makroekonomi ve Gölge Güç OSINT mimarisi."},
        {"file": "nuclear_triad_strategic_deterrence.jpg", "title": "Stratejik Nükleer Triad ve Caydırıcılık", "category": "Savunma & Nükleer", "desc": "9 nükleer gücün 12.121 savaş başlığı ve ikinci vuruş kabiliyeti."},
        {"file": "global_defense_alliances_security.jpg", "title": "Savunma Paktları ve Güvenlik Mimarisi", "category": "Askeri İttifaklar", "desc": "NATO Madde 5, AUKUS, CSTO ve FVEY karşılıklı yardımlaşma omurgası."},
        {"file": "critical_raw_materials_semiconductors.jpg", "title": "Kritik Hammaddeler ve Çip Tedarik Zinciri", "category": "Jeoekonomi", "desc": "Nadir toprak elementleri, lityum, kobalt ve Çin'in rafinaj tekeli."},
        {"file": "subsea_cables_and_cyber_sigint_nexus.jpg", "title": "Denizaltı Fiber Kabloları ve SIGINT Ağı", "category": "Siber İstihbarat", "desc": "Dünya internetinin %97'sini taşıyan okyanus altı kablo hatları."},
        {"file": "geopolitical_chokepoints.jpg", "title": "Deniz Darboğazları ve Kilit Geçitler", "category": "Jeopolitik Transit", "desc": "Hürmüz, Malakka, Babülmendep ve Süveyş deniz ticareti boğum noktaları."},
        {"file": "offshore_kleptocracy_network.jpg", "title": "Kleptokrasi ve Offshore Sermaye Kaçırma", "category": "Gölge Sermaye", "desc": "Kamu kaynaklarının vergi cennetleri üzerinden aklanma rotası."},
        {"file": "cognitive_warfare_surveillance.jpg", "title": "Bilişsel Savaş ve Algoritmik Gözetim (5GW)", "category": "Bilişsel Harp", "desc": "Zero-click casus yazılımlar, algoritmik manipülasyon ve siber istihbarat."}
    ]

    # JSON verilerini dizeleştir
    dataset_bundle = {
        "countries": consolidated_countries,
        "realms": culture_data.get("civilization_realms", []),
        "alliances": alliances_data,
        "chokepoints": chokepoints_data,
        "nuclear": nuclear_data,
        "minerals": minerals_data,
        "swfs": swf_data,
        "crises": crises_data,
        "artworks": artworks,
        "stats": {
            "country_count": len(consolidated_countries),
            "total_population": sum(c["population"] for c in consolidated_countries),
            "total_gdp": sum(c["gdp_usd_b"] for c in consolidated_countries),
            "avg_shadow": sum(c["shadow_economy_pct"] for c in consolidated_countries) / len(consolidated_countries),
            "artwork_count": len(artworks),
            "realms_count": len(culture_data.get("civilization_realms", []))
        }
    }

    bundle_json_str = json.dumps(dataset_bundle, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="tr" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Medeniyet Atlası &bull; Küresel Kültür, Yaşam Felsefesi ve Güç Terminali</title>
  <meta name="description" content="205 Dünya Ulusunun Kültürel Kodları, Yaşam Felsefeleri, Medeniyet Havzaları ve Gerçek Güç Anatomisi İnteraktif Atlası">
  <!-- Tailwind CSS CDN with offline fallback styling -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#f0fdf4',
              500: '#22c55e',
              600: '#16a34a',
              700: '#15803d',
              900: '#14532d',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    /* Standalone / Offline base styles */
    body {{
      background-color: #0b0f19;
      color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}
    .glass-card {{
      background: rgba(18, 24, 38, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.2s ease-in-out;
    }}
    .glass-card:hover {{
      border-color: rgba(59, 130, 246, 0.4);
      transform: translateY(-2px);
    }}
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 600;
    }}
    /* Custom scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0b0f19;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e293b;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #334155;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col bg-[#0b0f19] text-slate-100 antialiased selection:bg-blue-600 selection:text-white">

  <!-- HEADER -->
  <header class="border-b border-slate-800 bg-[#0f172a]/90 backdrop-blur sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center space-x-3">
        <span class="text-3xl">🏛️</span>
        <div>
          <h1 class="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            MEDENİYET ATLASI
            <span class="text-xs px-2 py-0.5 rounded bg-blue-900/60 text-blue-300 border border-blue-700/50 font-mono">v2.0 OSINT</span>
          </h1>
          <p class="text-xs text-slate-400">205 Dünya Ulusunun Kültürel Kodları, Yaşam Felsefeleri ve Güç Anatomisi</p>
        </div>
      </div>

      <!-- Quick Metrics Bar -->
      <div class="flex flex-wrap items-center gap-2 text-xs">
        <div class="px-2.5 py-1 rounded-md bg-slate-800/80 border border-slate-700/60 text-slate-300">
          🌍 <span class="font-bold text-white" id="stat-countries">205</span> Ülke
        </div>
        <div class="px-2.5 py-1 rounded-md bg-slate-800/80 border border-slate-700/60 text-slate-300">
          👥 <span class="font-bold text-white">7.98 Milyar</span> Nüfus
        </div>
        <div class="px-2.5 py-1 rounded-md bg-slate-800/80 border border-slate-700/60 text-slate-300">
          💰 <span class="font-bold text-emerald-400">$105.6T</span> GSYİH
        </div>
        <div class="px-2.5 py-1 rounded-md bg-slate-800/80 border border-slate-700/60 text-slate-300">
          🎨 <span class="font-bold text-purple-400">17</span> Eser
        </div>
        <div class="px-2.5 py-1 rounded-md bg-slate-800/80 border border-slate-700/60 text-slate-300">
          🛡️ <span class="font-bold text-amber-400">B2+</span> Doğrulama
        </div>
      </div>
    </div>

    <!-- MAIN NAVIGATION TABS -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex space-x-1 sm:space-x-3 overflow-x-auto text-sm border-t border-slate-800/60 pt-2 pb-1.5">
      <button onclick="switchTab('explorer')" id="tab-btn-explorer" class="tab-btn px-3 py-1.5 rounded-md font-medium text-blue-400 bg-blue-950/60 border border-blue-800/50 flex items-center gap-1.5 transition">
        <span>🗺️</span> 205 Ülke Atlası
      </button>
      <button onclick="switchTab('compare')" id="tab-btn-compare" class="tab-btn px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800/50 flex items-center gap-1.5 transition">
        <span>⚖️</span> İkili Karşılaştırma
      </button>
      <button onclick="switchTab('culture')" id="tab-btn-culture" class="tab-btn px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800/50 flex items-center gap-1.5 transition">
        <span>🎭</span> Medeniyetler & Ruh Kavramları
      </button>
      <button onclick="switchTab('geopolitics')" id="tab-btn-geopolitics" class="tab-btn px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800/50 flex items-center gap-1.5 transition">
        <span>🛡️</span> Jeopolitik & Güç Doktrini
      </button>
      <button onclick="switchTab('simulator')" id="tab-btn-simulator" class="tab-btn px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800/50 flex items-center gap-1.5 transition">
        <span>⚡</span> Kriz & Şok Simülatörü
      </button>
      <button onclick="switchTab('gallery')" id="tab-btn-gallery" class="tab-btn px-3 py-1.5 rounded-md font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800/50 flex items-center gap-1.5 transition">
        <span>🖼️</span> Tematik Sanat Galerisi (17 Eser)
      </button>
    </div>
  </header>

  <!-- MAIN BODY -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full">

    <!-- ========================================== -->
    <!-- TAB 1: 🗺️ 205 COUNTRY EXPLORER -->
    <!-- ========================================== -->
    <div id="tab-explorer" class="tab-pane space-y-5">
      <!-- Search & Filters Header -->
      <div class="glass-card p-4 rounded-xl flex flex-wrap gap-3 items-center justify-between">
        <div class="relative flex-1 min-w-[260px]">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-400">🔍</span>
          <input type="text" id="search-input" oninput="renderCountries()" placeholder="Ülke adı, başkent, kod veya kavram ara (örn. Türkiye, Japonya, Ikigai, Gönül)..." class="w-full pl-9 pr-4 py-2 rounded-lg bg-slate-900 border border-slate-700/80 text-sm text-slate-100 placeholder-slate-400 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500">
        </div>

        <div class="flex flex-wrap items-center gap-2">
          <!-- Region Filter -->
          <select id="filter-region" onchange="renderCountries()" class="px-3 py-2 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-200 focus:outline-none focus:border-blue-500">
            <option value="all">🌍 Tüm Bölgeler</option>
            <option value="middle_east">🕌 Orta Doğu</option>
            <option value="europe">🏰 Avrupa</option>
            <option value="asia">🏯 Asya & Hint-Pasifik</option>
            <option value="americas">🌎 Amerika Kıtası</option>
            <option value="africa">🌍 Afrika</option>
            <option value="oceania">🏝️ Okyanusya</option>
          </select>

          <!-- Economic Block Filter -->
          <select id="filter-econ" onchange="renderCountries()" class="px-3 py-2 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-200 focus:outline-none focus:border-blue-500">
            <option value="all">📊 Tüm Ekonomik Bloklar</option>
            <option value="01_ileri_sanayi_g7">🏭 01 İleri Sanayi / G7</option>
            <option value="02_petro_ve_enerji_devleri">🛢️ 02 Petro-Devletler</option>
            <option value="03_gelismekte_olan_devler_ve_brics">🚀 03 BRICS & İmalat</option>
            <option value="04_offshore_ve_finansal_merkezler">💼 04 Offshore / Finans</option>
            <option value="05_kritik_maden_ve_hammadde">⛏️ 05 Maden & Emtia</option>
            <option value="06_orta_gelir_ve_ureticiler">📈 06 Orta Gelir / Bölgesel</option>
            <option value="07_kirilgan_ve_borc_krizindekiler">⚠️ 07 Kırılgan / Yaptırım</option>
            <option value="08_kucuk_ada_ve_turizm_ekonomileri">🏝️ 08 Ada & Turizm</option>
          </select>

          <!-- Civilizational Realm Filter -->
          <select id="filter-realm" onchange="renderCountries()" class="px-3 py-2 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-200 focus:outline-none focus:border-blue-500">
            <option value="all">🏛️ Tüm Medeniyet Havzaları</option>
            <option value="anatolian">🏺 Anadolu & Akdeniz</option>
            <option value="east_asian">🏯 Doğu Asya</option>
            <option value="germanic">🌲 Cermen & İskandinav</option>
            <option value="anglo">🦅 Anglo-Sakson</option>
            <option value="slavic">❄️ Slav & Avrasya</option>
            <option value="latin">🌵 Latin Amerika</option>
            <option value="middle_eastern">🕌 Orta Doğu & Fars</option>
            <option value="south_asian">🪷 Güney Asya</option>
            <option value="sub_saharan">☀️ Sahra Altı & Ubuntu</option>
          </select>

          <!-- CSV Export Button -->
          <button onclick="exportFilteredCSV()" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700/80 text-xs text-slate-200 font-medium flex items-center gap-1.5 transition" title="Filtrelenen listeyi CSV formatında indir">
            <span>📥</span> CSV İndir
          </button>

          <!-- Sort Order -->
          <select id="sort-select" onchange="renderCountries()" class="px-3 py-2 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-200 focus:outline-none focus:border-blue-500">
            <option value="name_asc">🔤 İsim (A - Z)</option>
            <option value="gdp_desc">💰 GSYİH (Yüksek &rarr; Düşük)</option>
            <option value="pop_desc">👥 Nüfus (Yüksek &rarr; Düşük)</option>
            <option value="shadow_asc">🛡️ Gölge Ekonomi (Düşük &rarr; Yüksek)</option>
            <option value="csfi_desc">⚠️ Kırılganlık CSFI (En Riskli)</option>
          </select>
        </div>
      </div>

      <!-- Counter -->
      <div class="flex items-center justify-between text-xs text-slate-400 px-1">
        <div>Eşleşen <span id="filtered-count" class="font-bold text-blue-400">0</span> egemen varlık gösteriliyor:</div>
        <div class="text-[11px] text-slate-500">Bir ülkenin kartına tıklayarak 4 katmanlı derin dosyasını inceleyin.</div>
      </div>

      <!-- Grid Cards -->
      <div id="countries-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <!-- Javascript renders country cards here -->
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 2: ⚖️ COMPARE ENGINE -->
    <!-- ========================================== -->
    <div id="tab-compare" class="tab-pane hidden space-y-6">
      <div class="glass-card p-5 rounded-xl space-y-4">
        <h2 class="text-lg font-bold text-white flex items-center gap-2">
          <span>⚖️</span> İkili Jeopolitik ve Kültürel Karşılaştırma Matrisi
        </h2>
        <p class="text-xs text-slate-400">İki ülkeyi yan yana seçerek makroekonomik güçlerini, kültürel DNA'larını, sofra adabını ve sosyal tabularını kıyaslayın.</p>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-blue-400 mb-1">1. Ülkeyi Seçin:</label>
            <select id="compare-c1" onchange="runComparison()" class="w-full px-3 py-2 rounded-lg bg-slate-900 border border-slate-700 text-sm text-slate-100">
              <!-- options dynamically filled -->
            </select>
          </div>
          <div>
            <label class="block text-xs font-semibold text-purple-400 mb-1">2. Ülkeyi Seçin:</label>
            <select id="compare-c2" onchange="runComparison()" class="w-full px-3 py-2 rounded-lg bg-slate-900 border border-slate-700 text-sm text-slate-100">
              <!-- options dynamically filled -->
            </select>
          </div>
        </div>
      </div>

      <div id="compare-results" class="space-y-4">
        <!-- Javascript renders comparison table here -->
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 3: 🎭 CIVILIZATIONS & SOUL CONCEPTS -->
    <!-- ========================================== -->
    <div id="tab-culture" class="tab-pane hidden space-y-8">
      <!-- 9 Havza -->
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <h2 class="text-lg font-bold text-white flex items-center gap-2">
            <span>🌐</span> 9 Büyük Küresel Medeniyet Havzası ve Kurucu Felsefeleri
          </h2>
          <span class="text-xs text-slate-400">Tarihsel ve manevi kökenler</span>
        </div>
        <div id="realms-grid" class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Javascript renders realms cards here -->
        </div>
      </div>

      <!-- Çevrilemeyen Kavramlar Arama Sözlüğü -->
      <div class="glass-card p-5 rounded-xl space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span>📖</span> Çevrilemeyen Ruh Kavramları Sözlüğü (Untranslatable Concepts)
            </h3>
            <p class="text-xs text-slate-400">Dillerde tek kelimeyle yer alıp başka dillere tam çevrilemeyen kolektif bilinç cevherleri.</p>
          </div>
          <input type="text" id="concept-search" oninput="renderConcepts()" placeholder="Kavram veya anlam ara (örn. Saudade, Wabi-sabi, Ubuntu)..." class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-xs text-slate-100 w-64">
        </div>
        
        <div id="concepts-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          <!-- Javascript renders concept cards here -->
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: 🛡️ GEOPOLITICS & DEFENSE -->
    <!-- ========================================== -->
    <div id="tab-geopolitics" class="tab-pane hidden space-y-8">
      <!-- Nükleer Güçler -->
      <div class="glass-card p-5 rounded-xl space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <span>☢️</span> Stratejik Nükleer Triad ve Küresel Cephanelikler (12.121 Başlık)
          </h3>
          <span class="text-xs px-2 py-0.5 rounded bg-red-950/80 text-red-300 border border-red-800/40">9 Nükleer Güç</span>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="border-b border-slate-800 text-slate-400 uppercase text-[10px]">
              <tr>
                <th class="py-2 px-3">Devlet</th>
                <th class="py-2 px-3">Toplam Başlık</th>
                <th class="py-2 px-3">Dağıtılmış</th>
                <th class="py-2 px-3">Triad Yapısı</th>
                <th class="py-2 px-3">Caydırıcılık Doktrini</th>
              </tr>
            </thead>
            <tbody id="nuclear-tbody" class="divide-y divide-slate-800/60 text-slate-300">
              <!-- Javascript renders nuclear rows -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Savunma Paktları -->
      <div class="glass-card p-5 rounded-xl space-y-3">
        <h3 class="text-base font-bold text-white flex items-center gap-2">
          <span>🛡️</span> Küresel Savunma Paktları ve Askeri İttifaklar
        </h3>
        <div id="alliances-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- Javascript renders alliances cards -->
        </div>
      </div>

      <!-- Darboğazlar ve Madenler 2 Sütun -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Darboğazlar -->
        <div class="glass-card p-5 rounded-xl space-y-3">
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <span>🚢</span> Kritik Deniz Darboğazları & Transit Riskleri
          </h3>
          <div id="chokepoints-list" class="space-y-2.5">
            <!-- Javascript renders chokepoints -->
          </div>
        </div>

        <!-- Kritik Madenler -->
        <div class="glass-card p-5 rounded-xl space-y-3">
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <span>⛏️</span> Kritik Hammaddeler ve Rafinaj Tekelleri
          </h3>
          <div id="minerals-list" class="space-y-2.5">
            <!-- Javascript renders minerals -->
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 5: 🖼️ ART GALLERY (17 ESER) -->
    <!-- ========================================== -->
    <div id="tab-gallery" class="tab-pane hidden space-y-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-lg font-bold text-white flex items-center gap-2">
            <span>🖼️</span> Medeniyet Atlası Tematik Sanat Eserleri Kataloğu
          </h2>
          <p class="text-xs text-slate-400">17 yüksek çözünürlüklü özgün görsel; medeniyet, kültür, istihbarat ve güç anatomisinin görsel haritasıdır.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-md bg-purple-950/80 text-purple-300 border border-purple-800/40 font-mono">17 / 17 Eser</span>
      </div>

      <div id="gallery-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        <!-- Javascript renders artworks cards -->
      </div>
    </div>


    <!-- ========================================== -->
    <!-- TAB 6: ⚡ JEOPOLİTİK KRİZ & ŞOK SİMÜLATÖRÜ -->
    <!-- ========================================== -->
    <div id="tab-simulator" class="tab-pane hidden space-y-6">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h2 class="text-lg font-bold text-white flex items-center gap-2">
            <span>⚡</span> Küresel Jeopolitik Kriz & Boğum Noktası Şok Simülatörü
          </h2>
          <p class="text-xs text-slate-400">Deniz boğazları tıkanmaları, kritik mineral ambargoları ve yarı iletken kesintilerinin 205 ülke üzerindeki zincirleme etkilerini test edin.</p>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="runShockSimulation()" class="px-3.5 py-1.5 rounded-lg bg-red-900/80 hover:bg-red-800 border border-red-700/60 text-red-100 text-xs font-bold flex items-center gap-1.5 transition shadow-lg shadow-red-950/40">
            <span>💥</span> Şok Simülasyonunu Çalıştır
          </button>
        </div>
      </div>

      <!-- Live Simulation Alert Box -->
      <div id="sim-alert-box" class="hidden p-4 rounded-xl border border-red-600/60 bg-red-950/40 text-xs space-y-2 text-red-200 transition-all">
        <!-- Rendered dynamically -->
      </div>

      <!-- Scenario Selector Buttons -->
      <div class="space-y-1.5">
        <label class="text-xs text-slate-400 font-semibold uppercase tracking-wider">Senaryo Seçimi:</label>
        <div id="scenario-selector" class="flex flex-wrap gap-2">
          <!-- Rendered by JS -->
        </div>
      </div>

      <!-- Active Scenario Details Card -->
      <div id="scenario-details-container" class="space-y-6">
        <!-- Rendered by JS -->
      </div>
    </div>

  </main>

  <!-- COUNTRY DETAIL MODAL -->
  <div id="country-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-3 sm:p-6 overflow-y-auto" onclick="closeCountryModal(event)">
    <div class="glass-card w-full max-w-4xl max-h-[90vh] rounded-2xl border border-slate-700/80 bg-[#0f172a] shadow-2xl flex flex-col overflow-hidden text-slate-200" onclick="event.stopPropagation()">
      <!-- Modal Header -->
      <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-900/60">
        <div class="flex items-center space-x-3">
          <span class="text-3xl" id="modal-flag">🌍</span>
          <div>
            <h3 class="text-lg font-bold text-white flex items-center gap-2" id="modal-title">Ülke Başlığı</h3>
            <p class="text-xs text-slate-400" id="modal-subtitle">Başkent & Bölge</p>
          </div>
        </div>
        <button onclick="closeModalDirect()" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition text-lg">&times;</button>
      </div>

      <!-- Modal Content Body -->
      <div class="p-6 overflow-y-auto space-y-6 text-sm flex-1" id="modal-body">
        <!-- Injected via Javascript -->
      </div>

      <!-- Modal Footer -->
      <div class="px-6 py-3 border-t border-slate-800 bg-slate-900/40 flex items-center justify-between text-xs text-slate-400">
        <div id="modal-path-info">Dosya: countries/...</div>
        <button onclick="closeModalDirect()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition font-medium">Kapat</button>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800 bg-[#0b0f19] py-6 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
      <div>
        <b>MEDENİYET ATLASI & GLOBAL X-RAY</b> &copy; 2026 &bull; Açık Kültür &bull; CC BY-SA 4.0
      </div>
      <div class="flex items-center space-x-4">
        <a href="README.md" class="text-slate-400 hover:text-slate-200 transition">README.md</a>
        <a href="culture/README.md" class="text-slate-400 hover:text-slate-200 transition">Kültür Kütüphanesi</a>
        <a href="geopolitics_and_intelligence/README.md" class="text-slate-400 hover:text-slate-200 transition">İstihbarat Dosyaları</a>
        <a href="https://github.com/bahattinyunus/medeniyet-atlasi" target="_blank" class="text-blue-400 hover:text-blue-300 transition">GitHub Deposu &rarr;</a>
      </div>
    </div>
  </footer>

  <!-- DATA & APP LOGIC -->
  <script>
    // Embedded consolidated dataset
    const DATA = {bundle_json_str};

    // Current State
    let currentTab = 'explorer';

    function switchTab(tabId) {{
      currentTab = tabId;
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(el => {{
        el.classList.remove('text-blue-400', 'bg-blue-950/60', 'border-blue-800/50');
        el.classList.add('text-slate-400');
      }});

      const targetPane = document.getElementById('tab-' + tabId);
      if (targetPane) targetPane.classList.remove('hidden');

      const targetBtn = document.getElementById('tab-btn-' + tabId);
      if (targetBtn) {{
        targetBtn.classList.add('text-blue-400', 'bg-blue-950/60', 'border-blue-800/50');
        targetBtn.classList.remove('text-slate-400');
      }}
    }}

    // Region name mapper
    function formatRegion(r) {{
      const map = {{
        'middle_east': '🕌 Orta Doğu',
        'europe': '🏰 Avrupa',
        'asia': '🏯 Asya & Hint-Pasifik',
        'americas': '🌎 Amerika Kıtası',
        'africa': '🌍 Afrika',
        'oceania': '🏝️ Okyanusya'
      }};
      return map[r] || r;
    }}

    // Economic badge color
    function getEconBadge(id) {{
      if (id.includes('g7')) return 'bg-blue-900/60 text-blue-300 border-blue-700/50';
      if (id.includes('petro')) return 'bg-amber-900/60 text-amber-300 border-amber-700/50';
      if (id.includes('brics')) return 'bg-emerald-900/60 text-emerald-300 border-emerald-700/50';
      if (id.includes('offshore')) return 'bg-purple-900/60 text-purple-300 border-purple-700/50';
      if (id.includes('maden')) return 'bg-orange-900/60 text-orange-300 border-orange-700/50';
      if (id.includes('kirilgan')) return 'bg-red-900/60 text-red-300 border-red-700/50';
      return 'bg-slate-800 text-slate-300 border-slate-700';
    }}

    // RENDER COUNTRIES GRID
    function renderCountries() {{
      const q = document.getElementById('search-input').value.toLowerCase().trim();
      const region = document.getElementById('filter-region').value;
      const econ = document.getElementById('filter-econ').value;
      const sortBy = document.getElementById('sort-select').value;

      let list = getFilteredCountries();

      // Sorting
      list.sort((a, b) => {{
        if (sortBy === 'name_asc') return a.name.localeCompare(b.name, 'tr');
        if (sortBy === 'gdp_desc') return (b.gdp_usd_b || 0) - (a.gdp_usd_b || 0);
        if (sortBy === 'pop_desc') return (b.population || 0) - (a.population || 0);
        if (sortBy === 'shadow_asc') return (a.shadow_economy_pct || 0) - (b.shadow_economy_pct || 0);
        if (sortBy === 'csfi_desc') return (b.csfi || 0) - (a.csfi || 0);
        return 0;
      }});

      document.getElementById('filtered-count').innerText = list.length;
      const container = document.getElementById('countries-grid');
      container.innerHTML = '';

      list.forEach(c => {{
        const card = document.createElement('div');
        card.className = 'glass-card p-4 rounded-xl cursor-pointer flex flex-col justify-between';
        card.onclick = () => openCountryModal(c.code);

        const words = (c.cultural_dna?.untranslatable_soul_concepts || []).slice(0, 3);
        const wordsHtml = words.map(w => `<span class="px-1.5 py-0.5 rounded bg-purple-950/70 border border-purple-800/40 text-[10px] text-purple-300 font-mono">${{w.word}}</span>`).join(' ');

        card.innerHTML = `
          <div>
            <div class="flex items-start justify-between gap-2 mb-2">
              <div>
                <h4 class="font-bold text-white text-base leading-tight">${{c.name}}</h4>
                <div class="text-[11px] text-slate-400">${{c.capital}} &bull; <span class="font-mono text-slate-300">${{c.code}}</span></div>
              </div>
              <span class="badge-pill border ${{getEconBadge(c.economy_group_id)}}">${{c.economy_group_id.substring(3).replace(/_/g, ' ').toUpperCase()}}</span>
            </div>

            <!-- Key metrics row -->
            <div class="grid grid-cols-3 gap-1.5 my-3 py-2 border-y border-slate-800/80 text-center text-xs">
              <div>
                <div class="text-[10px] text-slate-500 uppercase">GSYİH</div>
                <div class="font-semibold text-emerald-400">$${{(c.gdp_usd_b || 0).toLocaleString('en-US', {{maximumFractionDigits: 1}})}}B</div>
              </div>
              <div>
                <div class="text-[10px] text-slate-500 uppercase">Nüfus</div>
                <div class="font-semibold text-slate-200">${{(c.population || 0).toLocaleString('en-US')}}</div>
              </div>
              <div>
                <div class="text-[10px] text-slate-500 uppercase">Gölge</div>
                <div class="font-semibold text-amber-400">%${{c.shadow_economy_pct}}</div>
              </div>
            </div>

            <p class="text-xs text-slate-300 line-clamp-2 mb-2.5">
              ${{c.cultural_dna?.core_cultural_ethos || 'Kültürel ethos ve medeniyet kimliği kayıtlı.'}}
            </p>
          </div>

          <div>
            <div class="flex flex-wrap gap-1 mb-3">
              ${{wordsHtml}}
            </div>
            <div class="flex items-center justify-between text-[11px] text-blue-400 font-medium">
              <span>Röntgeni Aç &rarr;</span>
              <span class="text-slate-500 text-[10px]">${{formatRegion(c.region)}}</span>
            </div>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    // COUNTRY MODAL
    function openCountryModal(code) {{
      const c = DATA.countries.find(x => x.code === code);
      if (!c) return;

      document.getElementById('modal-title').innerText = `${{c.name}} (${{c.code}})`;
      document.getElementById('modal-subtitle').innerText = `${{c.capital}} &bull; ${{formatRegion(c.region)}} &bull; ${{c.economy_group_name}}`;
      document.getElementById('modal-path-info').innerText = `Konum: ${{c.path}}`;

      const dna = c.cultural_dna || {{}};
      const macro = c.macroeconomics || {{}};
      const oligarchs = c.oligarchs || [];

      let wordsHtml = '';
      if (dna.untranslatable_soul_concepts && dna.untranslatable_soul_concepts.length > 0) {{
        wordsHtml = dna.untranslatable_soul_concepts.map(w => `
          <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800">
            <div class="font-bold text-purple-300 text-sm font-mono">${{w.word}}</div>
            <div class="text-xs text-slate-300 mt-0.5">${{w.meaning}}</div>
          </div>
        `).join('');
      }} else {{
        wordsHtml = '<div class="text-xs text-slate-500">Kayıtlı kavram bulunamadı.</div>';
      }}

      let oligarchsHtml = '';
      if (oligarchs.length > 0) {{
        oligarchsHtml = `
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs border border-slate-800 rounded-lg overflow-hidden">
              <thead class="bg-slate-900 text-slate-400">
                <tr>
                  <th class="py-2 px-3">Kişi / Varlık</th>
                  <th class="py-2 px-3">Rol / Başlık</th>
                  <th class="py-2 px-3">Sektör</th>
                  <th class="py-2 px-3">Servet</th>
                  <th class="py-2 px-3">Siyasi Bağ</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800/80">
                ${{oligarchs.map(o => `
                  <tr>
                    <td class="py-2 px-3 font-semibold text-slate-200">${{o.person_or_entity}}</td>
                    <td class="py-2 px-3 text-slate-400">${{o.role_or_title || '-'}}</td>
                    <td class="py-2 px-3 text-slate-400">${{o.connected_sector || '-'}}</td>
                    <td class="py-2 px-3 text-emerald-400">${{o.estimated_wealth_usd_m && o.estimated_wealth_usd_m !== '0' ? '$' + o.estimated_wealth_usd_m + 'M' : '-'}}</td>
                    <td class="py-2 px-3 text-amber-300/80">${{o.political_connection || '-'}}</td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
        `;
      }} else {{
        oligarchsHtml = '<div class="text-xs text-slate-500">(Kayıtlı doğrudan oligark verisi bulunamadı)</div>';
      }}

            let crisesHtml = '';
      const matchedCrises = (DATA.crises || []).filter(s =>
        (s.most_vulnerable_countries || []).some(vc => vc.code === c.code || (vc.name && vc.name.toLowerCase() === c.name.toLowerCase()))
      );
      if (matchedCrises.length > 0) {{
        crisesHtml = `
          <div class="space-y-3">
            <h4 class="text-xs font-bold uppercase tracking-wider text-red-400 flex items-center gap-1.5">
              <span>⚡</span> Kritik Jeopolitik Darboğaz & Kriz Maruziyeti
            </h4>
            <div class="space-y-2">
              ${{matchedCrises.map(sc => {{
                const vc = sc.most_vulnerable_countries.find(x => x.code === c.code || (x.name && x.name.toLowerCase() === c.name.toLowerCase()));
                return `
                  <div class="p-3 rounded-xl bg-red-950/40 border border-red-800/60 flex items-center justify-between text-xs">
                    <div>
                      <div class="font-bold text-red-300 flex items-center gap-1.5">
                        <span>⚠️</span> ${{sc.title}}
                      </div>
                      <div class="text-[11px] text-slate-300 mt-0.5">Etkilenen Sektör: <span class="text-white">${{vc ? vc.sector : '-'}}</span></div>
                    </div>
                    <span class="px-2 py-1 rounded bg-red-900/80 text-white font-mono font-bold">%${{vc ? vc.dependency_pct : '0'}} Bağımlılık</span>
                  </div>
                `;
              }}).join('')}}
            </div>
          </div>
        `;
      }}

      document.getElementById('modal-body').innerHTML = `
        <!-- Section 1: Kültürel DNA -->
        <div class="space-y-3">
          <h4 class="text-xs font-bold uppercase tracking-wider text-blue-400 flex items-center gap-1.5">
            <span>🎭</span> 1. Kültürel DNA ve Medeniyet Kimliği
          </h4>
          <div class="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2 text-xs">
            <div><span class="text-slate-400 font-semibold">Medeniyet Sentezi:</span> <span class="text-slate-200">${{dna.civilization_crossroads || 'Kayıtlı sentez verisi yok'}}</span></div>
            <div><span class="text-slate-400 font-semibold">Temel Ulusal Ethos:</span> <span class="text-slate-200">${{dna.core_cultural_ethos || '-'}}</span></div>
            <div><span class="text-slate-400 font-semibold">İletişim Tarzı:</span> <span class="text-slate-200">${{dna.communication_style || '-'}}</span></div>
            <div><span class="text-slate-400 font-semibold">Mutfak Felsefesi:</span> <span class="text-slate-200">${{dna.gastronomic_philosophy || '-'}}</span></div>
            <div><span class="text-slate-400 font-semibold">Sosyal Tabular & Görgü:</span> <span class="text-slate-200">${{dna.social_taboos_and_etiquette || '-'}}</span></div>
          </div>
        </div>

        <!-- Section 2: Çevrilemeyen Ruh Kavramları -->
        <div class="space-y-3">
          <h4 class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-1.5">
            <span>📖</span> 2. Dilde Kristalleşen Çevrilemeyen Kavramlar
          </h4>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            ${{wordsHtml}}
          </div>
        </div>

        <!-- Section: Kriz Maruziyeti -->
        ${{crisesHtml}}

        <!-- Section 3: Makroekonomi -->
        <div class="space-y-3">
          <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
            <span>📊</span> 3. Makroekonomik Doku ve Dış Ticaret
          </h4>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
            <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-500">Nominal GSYİH</div>
              <div class="font-bold text-white text-sm">$${{(c.gdp_usd_b || 0).toLocaleString()}}B</div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-500">Kişi Başı Gelir</div>
              <div class="font-bold text-emerald-400 text-sm">$${{(c.gdp_per_capita || 0).toLocaleString()}}</div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-500">Gölge Ekonomi</div>
              <div class="font-bold text-amber-400 text-sm">%${{c.shadow_economy_pct}}</div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-500">CSFI Kırılganlık</div>
              <div class="font-bold text-red-400 text-sm">${{c.csfi}} (${{c.risk_tier.split(' ')[0]}})</div>
            </div>
          </div>
          <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-800 text-xs space-y-1">
            <div><span class="text-slate-400">Para Birimi:</span> ${{macro.currency || 'Bilinmiyor'}} &bull; <span class="text-slate-400">Enflasyon:</span> %${{macro.inflation_rate_pct ?? 'N/A'}}</div>
            <div><span class="text-slate-400">Ana İhracat Kalemleri:</span> ${{Array.isArray(macro.top_exports) ? macro.top_exports.join(', ') : '-'}}</div>
            <div><span class="text-slate-400">Başlıca Ticaret Ortakları:</span> ${{Array.isArray(macro.major_trading_partners) ? macro.major_trading_partners.join(', ') : '-'}}</div>
          </div>
        </div>

        <!-- Section 4: Oligarklar & Gölge Güç -->
        <div class="space-y-3">
          <h4 class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
            <span>🕶️</span> 4. Oligark & Gölge Sermaye Ağı (OSINT)
          </h4>
          ${{oligarchsHtml}}
        </div>
      `;

      document.getElementById('country-modal').classList.remove('hidden');
    }}

    function closeCountryModal(e) {{
      if (e.target.id === 'country-modal') closeModalDirect();
    }}

    function closeModalDirect() {{
      document.getElementById('country-modal').classList.add('hidden');
    }}

    // POPULATE COMPARE SELECTS
    function initCompareSelects() {{
      const c1 = document.getElementById('compare-c1');
      const c2 = document.getElementById('compare-c2');
      c1.innerHTML = '';
      c2.innerHTML = '';

      DATA.countries.slice().sort((a,b) => a.name.localeCompare(b.name, 'tr')).forEach(c => {{
        const opt1 = document.createElement('option');
        opt1.value = c.code;
        opt1.innerText = `${{c.name}} (${{c.code}})`;
        c1.appendChild(opt1);

        const opt2 = document.createElement('option');
        opt2.value = c.code;
        opt2.innerText = `${{c.name}} (${{c.code}})`;
        c2.appendChild(opt2);
      }});

      c1.value = 'TUR';
      c2.value = 'JPN';
      runComparison();
    }}

    function runComparison() {{
      const code1 = document.getElementById('compare-c1').value;
      const code2 = document.getElementById('compare-c2').value;
      const c1 = DATA.countries.find(x => x.code === code1);
      const c2 = DATA.countries.find(x => x.code === code2);
      if (!c1 || !c2) return;

      const container = document.getElementById('compare-results');
      const ratio = (c1.gdp_usd_b / Math.max(c2.gdp_usd_b, 0.01)).toFixed(1);

      container.innerHTML = `
        <div class="glass-card p-5 rounded-xl space-y-4">
          <div class="grid grid-cols-3 text-center border-b border-slate-800 pb-3">
            <div class="text-left font-bold text-slate-400 text-xs uppercase">Metrik</div>
            <div class="font-bold text-blue-400 text-base">${{c1.name}}</div>
            <div class="font-bold text-purple-400 text-base">${{c2.name}}</div>
          </div>

          <!-- Rows -->
          ${{renderCompareRow('Bölge', formatRegion(c1.region), formatRegion(c2.region))}}
          ${{renderCompareRow('Başkent', c1.capital, c2.capital)}}
          ${{renderCompareRow('Nüfus', c1.population.toLocaleString(), c2.population.toLocaleString())}}
          ${{renderCompareRow('Nominal GSYİH', '$' + c1.gdp_usd_b.toLocaleString() + 'B', '$' + c2.gdp_usd_b.toLocaleString() + 'B')}}
          ${{renderCompareRow('Kişi Başı Gelir', '$' + (c1.gdp_per_capita || 0).toLocaleString(), '$' + (c2.gdp_per_capita || 0).toLocaleString())}}
          ${{renderCompareRow('Gölge Ekonomi', '%' + c1.shadow_economy_pct, '%' + c2.shadow_economy_pct)}}
          ${{renderCompareRow('CSFI Kırılganlık', c1.csfi + ' (' + c1.risk_tier.split(' ')[0] + ')', c2.csfi + ' (' + c2.risk_tier.split(' ')[0] + ')')}}
          ${{renderCompareRow('İletişim Tarzı', c1.cultural_dna?.communication_style || '-', c2.cultural_dna?.communication_style || '-')}}
          ${{renderCompareRow('Mutfak Felsefesi', c1.cultural_dna?.gastronomic_philosophy || '-', c2.cultural_dna?.gastronomic_philosophy || '-')}}
          ${{renderCompareRow('Sosyal Tabular', c1.cultural_dna?.social_taboos_and_etiquette || '-', c2.cultural_dna?.social_taboos_and_etiquette || '-')}}
        </div>
      `;
    }}

    function renderCompareRow(label, v1, v2) {{
      return `
        <div class="grid grid-cols-3 py-2 border-b border-slate-800/50 text-xs">
          <div class="font-semibold text-slate-400">${{label}}</div>
          <div class="text-slate-200">${{v1}}</div>
          <div class="text-slate-200">${{v2}}</div>
        </div>
      `;
    }}

    // RENDER CIVILIZATION REALMS & CONCEPTS
    function renderCulture() {{
      const realmsGrid = document.getElementById('realms-grid');
      realmsGrid.innerHTML = '';
      DATA.realms.forEach(r => {{
        const card = document.createElement('div');
        card.className = 'glass-card p-4 rounded-xl space-y-2';
        card.innerHTML = `
          <div class="font-bold text-white text-sm">${{r.name}}</div>
          <div class="text-xs text-blue-300 font-medium">${{r.core_philosophy}}</div>
          <div class="text-[11px] text-slate-400 mt-2">
            <span class="text-slate-500 font-semibold">Temsilciler:</span> ${{r.representative_states.join(', ')}}
          </div>
        `;
        realmsGrid.appendChild(card);
      }});

      renderConcepts();
    }}

    function renderConcepts() {{
      const q = (document.getElementById('concept-search')?.value || '').toLowerCase().trim();
      const container = document.getElementById('concepts-grid');
      container.innerHTML = '';

      let allConcepts = [];
      DATA.countries.forEach(c => {{
        (c.cultural_dna?.untranslatable_soul_concepts || []).forEach(w => {{
          allConcepts.push({{
            country: c.name,
            code: c.code,
            word: w.word,
            meaning: w.meaning
          }});
        }});
      }});

      if (q) {{
        allConcepts = allConcepts.filter(x => x.word.toLowerCase().includes(q) || x.meaning.toLowerCase().includes(q) || x.country.toLowerCase().includes(q));
      }}

      allConcepts.slice(0, 30).forEach(item => {{
        const card = document.createElement('div');
        card.className = 'p-3 rounded-lg bg-slate-900/80 border border-slate-800/80 space-y-1';
        card.innerHTML = `
          <div class="flex items-center justify-between">
            <span class="font-bold text-purple-400 font-mono text-sm">${{item.word}}</span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400">${{item.country}}</span>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed">${{item.meaning}}</p>
        `;
        container.appendChild(card);
      }});
    }}

    // RENDER GEOPOLITICS
    function renderGeopolitics() {{
      // Nuclear Triad Table
      const nucTbody = document.getElementById('nuclear-tbody');
      nucTbody.innerHTML = '';
      DATA.nuclear.forEach(n => {{
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-800/30';
        tr.innerHTML = `
          <td class="py-2.5 px-3 font-semibold text-white">${{n.power}}</td>
          <td class="py-2.5 px-3 text-red-400 font-bold">${{n.total_warheads.toLocaleString()}}</td>
          <td class="py-2.5 px-3 text-amber-300">${{n.deployed_warheads.toLocaleString()}}</td>
          <td class="py-2.5 px-3 text-slate-400 text-[11px]">${{n.triad_status?.icbm_ground ? '✓ ICBM ' : ''}}${{n.triad_status?.ssbn_submarine ? '✓ SSBN ' : ''}}${{n.triad_status?.strategic_bombers ? '✓ Bombardıman' : ''}}</td>
          <td class="py-2.5 px-3 text-slate-400 text-[11px]">${{n.strategic_doctrine?.no_first_use ? 'İlk Kullanan Olmama (NFU)' : 'Önleyici / Esnek Mukabele'}}</td>
        `;
        nucTbody.appendChild(tr);
      }});

      // Alliances
      const allGrid = document.getElementById('alliances-grid');
      allGrid.innerHTML = '';
      DATA.alliances.forEach(a => {{
        const card = document.createElement('div');
        card.className = 'p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2 text-xs';
        card.innerHTML = `
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-sm">[${{a.id}}] ${{a.name}}</span>
            <span class="px-2 py-0.5 rounded bg-blue-900/50 text-blue-300 text-[10px] font-mono">${{a.established}} &bull; ${{a.member_count}} Üye</span>
          </div>
          <div class="text-slate-300"><span class="text-slate-500 font-semibold">Tetikleyici Madde:</span> ${{a.core_trigger_article}}</div>
          <div class="text-slate-400"><span class="text-slate-500 font-semibold">Ortak Bütçe:</span> $${{a.combined_military_spending_usd_b}} Milyar</div>
          <div class="text-[11px] text-slate-400"><span class="text-slate-500">Kilit Üyeler:</span> ${{a.key_members.join(', ')}}</div>
        `;
        allGrid.appendChild(card);
      }});

      // Chokepoints
      const chokeList = document.getElementById('chokepoints-list');
      chokeList.innerHTML = '';
      DATA.chokepoints.forEach(cp => {{
        const item = document.createElement('div');
        item.className = 'p-3 rounded-lg bg-slate-900/60 border border-slate-800 flex items-center justify-between text-xs';
        item.innerHTML = `
          <div>
            <div class="font-bold text-white">${{cp.name}} (${{cp.english_name}})</div>
            <div class="text-[11px] text-slate-400">${{cp.controlling_states.join(', ')}} &bull; Risk: ${{cp.geopolitical_risk_level}}</div>
          </div>
          <div class="text-right">
            <div class="font-bold text-emerald-400">${{cp.daily_petroleum_transit_barrels.toLocaleString()}} v/g</div>
            <div class="text-[10px] text-slate-500">Dünya petrolünün %${{cp.share_of_global_maritime_oil_pct}}</div>
          </div>
        `;
        chokeList.appendChild(item);
      }});

      // Minerals
      const minList = document.getElementById('minerals-list');
      minList.innerHTML = '';
      DATA.minerals.forEach(m => {{
        const item = document.createElement('div');
        item.className = 'p-3 rounded-lg bg-slate-900/60 border border-slate-800 flex items-center justify-between text-xs';
        item.innerHTML = `
          <div>
            <div class="font-bold text-white">${{m.name}} (${{m.id}})</div>
            <div class="text-[11px] text-slate-400">${{m.strategic_category}}</div>
          </div>
          <div class="text-right">
            <div class="font-bold text-amber-400">${{m.refining_monopoly.dominant_nation}} (%${{m.refining_monopoly.global_refining_share_pct}})</div>
            <div class="text-[10px] text-slate-500">Rafinaj Tekeli &bull; Risk: ${{m.geopolitical_risk_score}}/10</div>
          </div>
        `;
        minList.appendChild(item);
      }});
    }}

    // RENDER GALLERY (17 ESER)
    function renderGallery() {{
      const container = document.getElementById('gallery-grid');
      container.innerHTML = '';
      DATA.artworks.forEach((art, idx) => {{
        const card = document.createElement('div');
        card.className = 'glass-card rounded-xl overflow-hidden flex flex-col justify-between';
        card.innerHTML = `
          <div>
            <div class="relative overflow-hidden bg-slate-950 aspect-video">
              <img src="assets/images/${{art.file}}" alt="${{art.title}}" loading="lazy" class="w-full h-full object-cover transition-transform duration-300 hover:scale-105" onerror="this.parentElement.innerHTML='<div class=\\'flex items-center justify-center h-full text-slate-600 text-xs font-mono\\'>${{art.file}}</div>'">
              <span class="absolute top-2 right-2 px-2 py-0.5 rounded bg-black/70 backdrop-blur text-[10px] text-slate-300 font-mono">#${{idx + 1}}</span>
            </div>
            <div class="p-3.5 space-y-1.5">
              <span class="px-2 py-0.5 rounded bg-blue-950/70 border border-blue-800/40 text-[10px] text-blue-300 font-medium">${{art.category}}</span>
              <h4 class="font-bold text-white text-sm leading-tight">${{art.title}}</h4>
              <p class="text-xs text-slate-400 line-clamp-2">${{art.desc}}</p>
            </div>
          </div>
        `;
        container.appendChild(card);
      }});
    }}


    // Current Active Scenario
    let activeScenarioId = null;

    // Export Filtered Countries to CSV
    function exportFilteredCSV() {{
      const filtered = getFilteredCountries();
      if (!filtered.length) {{
        alert('Dışa aktarılacak ülke bulunamadı.');
        return;
      }}

      let csv = "name,code,region,capital,population,gdp_usd_b,gdp_per_capita,shadow_economy_pct,csfi,risk_tier,economy_group\n";
      filtered.forEach(c => {{
        const row = [
          `"${{c.name}}"`,
          `"${{c.code}}"`,
          `"${{c.region}}"`,
          `"${{c.capital}}"`,
          c.population || 0,
          c.gdp_usd_b || 0,
          c.gdp_per_capita || 0,
          c.shadow_economy_pct || 0,
          c.csfi || 0,
          `"${{c.risk_tier || ''}}"`,
          `"${{c.economy_group_name || ''}}"`
        ];
        csv += row.join(",") + "\n";
      }});

      const blob = new Blob(["\uFEFF" + csv], {{ type: "text/csv;charset=utf-8;" }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `medeniyet_atlasi_ulkeler_${{new Date().toISOString().slice(0, 10)}}.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }}

    // Helper to get currently filtered countries
    function getFilteredCountries() {{
      const q = (document.getElementById('search-input')?.value || '').toLowerCase().trim();
      const region = document.getElementById('filter-region')?.value || 'all';
      const econ = document.getElementById('filter-econ')?.value || 'all';
      const realm = document.getElementById('filter-realm')?.value || 'all';

      return DATA.countries.filter(c => {{
        if (region !== 'all' && c.region !== region) return false;
        if (econ !== 'all' && c.economy_group_id !== econ) return false;
        if (realm !== 'all') {{
          const cross = (c.cultural_dna?.civilization_crossroads || '').toLowerCase();
          const rname = (c.cultural_dna?.civilization_realm || '').toLowerCase();
          if (realm === 'anatolian' && !cross.includes('anadolu') && !cross.includes('akdeniz')) return false;
          if (realm === 'east_asian' && !cross.includes('asya') && !cross.includes('konfüçyüs') && !cross.includes('şinto')) return false;
          if (realm === 'germanic' && !cross.includes('cermen') && !cross.includes('iskandinav') && !cross.includes('alman')) return false;
          if (realm === 'anglo' && !cross.includes('anglo') && !cross.includes('amerikan')) return false;
          if (realm === 'slavic' && !cross.includes('slav') && !cross.includes('avrasya') && !cross.includes('rus')) return false;
          if (realm === 'latin' && !cross.includes('latin') && !cross.includes('ibero')) return false;
          if (realm === 'middle_eastern' && !cross.includes('orta doğu') && !cross.includes('fars') && !cross.includes('arap')) return false;
          if (realm === 'south_asian' && !cross.includes('dharmik') && !cross.includes('hint') && !cross.includes('hindu')) return false;
          if (realm === 'sub_saharan' && !cross.includes('ubuntu') && !cross.includes('sahra altı') && !cross.includes('afrika')) return false;
        }}
        if (q) {{
          const inName = c.name.toLowerCase().includes(q);
          const inCapital = (c.capital || '').toLowerCase().includes(q);
          const inCode = c.code.toLowerCase().includes(q);
          const inSlug = c.slug.toLowerCase().includes(q);
          const inEthos = (c.cultural_dna?.core_cultural_ethos || '').toLowerCase().includes(q);
          const inWords = (c.cultural_dna?.untranslatable_soul_concepts || []).some(w => w.word.toLowerCase().includes(q) || w.meaning.toLowerCase().includes(q));
          return inName || inCapital || inCode || inSlug || inEthos || inWords;
        }}
        return true;
      }});
    }}

    // Copy terminal CLI command to clipboard
    function copyCliBriefing(slug) {{
      const cmd = `python scripts/xray_cli.py briefing ${{slug}}`;
      navigator.clipboard.writeText(cmd).then(() => {{
        const btn = document.getElementById('copy-cli-btn');
        if (btn) {{
          const original = btn.innerHTML;
          btn.innerHTML = '<span>✅</span> Kopyalandı!';
          setTimeout(() => {{ btn.innerHTML = original; }}, 2000);
        }}
      }}).catch(() => {{
        alert('Komut: ' + cmd);
      }});
    }}

    // RENDER SIMULATOR
    function renderSimulator() {{
      const crises = DATA.crises || [];
      if (!crises.length) return;

      if (!activeScenarioId) {{
        activeScenarioId = crises[0].id;
      }}

      const selectorContainer = document.getElementById('scenario-selector');
      if (selectorContainer) {{
        selectorContainer.innerHTML = '';
        crises.forEach(s => {{
          const btn = document.createElement('button');
          const isActive = s.id === activeScenarioId;
          btn.className = `px-3 py-1.5 rounded-lg text-xs font-medium transition flex items-center gap-1.5 ${{isActive ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-900 border border-slate-800 text-slate-300 hover:bg-slate-800'}}`;
          btn.innerHTML = `<span>⚡</span> ${{s.title}}`;
          btn.onclick = () => {{
            activeScenarioId = s.id;
            renderSimulator();
          }};
          selectorContainer.appendChild(btn);
        }});
      }}

      const sc = crises.find(x => x.id === activeScenarioId) || crises[0];
      const container = document.getElementById('scenario-details-container');
      if (!container) return;

      const exposureKeys = Object.entries(sc.strategic_exposure || {{}});
      const exposureHtml = exposureKeys.map(([k, v]) => `
        <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-800">
          <div class="text-[10px] text-slate-400 uppercase tracking-wider">${{k.replace(/_/g, ' ')}}</div>
          <div class="font-bold text-white text-base mt-0.5 text-amber-300">${{v}}</div>
        </div>
      `).join('');

      const vulnHtml = (sc.most_vulnerable_countries || []).map(vc => `
        <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 flex items-center justify-between gap-3">
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <span class="font-bold text-white text-sm cursor-pointer hover:text-blue-400 transition" onclick="openCountryModal('${{vc.code}}')">${{vc.name}} (${{vc.code}})</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-red-950/80 text-red-300 border border-red-800/50 font-bold">%${{vc.dependency_pct}} Bağımlılık</span>
            </div>
            <div class="text-xs text-slate-400 mt-1">Sektör: <span class="text-slate-300">${{vc.sector}}</span></div>
            <div class="w-full bg-slate-800 h-1.5 rounded-full mt-2 overflow-hidden">
              <div class="bg-red-500 h-full rounded-full" style="width: ${{Math.min(100, vc.dependency_pct)}}%"></div>
            </div>
          </div>
          <button onclick="openCountryModal('${{vc.code}}')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] text-slate-300 transition">Röntgen &rarr;</button>
        </div>
      `).join('');

      const mitigationsHtml = (sc.mitigation_corridors || []).map(m => `
        <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1 text-xs">
          <div class="font-bold text-emerald-400 flex items-center justify-between">
            <span>🛣️ ${{m.route}}</span>
            ${{m.capacity_mbpd ? `<span class="text-slate-400 text-[11px] font-mono">${{m.capacity_mbpd}} mbpd</span>` : ''}}
          </div>
          <p class="text-slate-300">${{m.status}}</p>
        </div>
      `).join('');

      const secondaryHtml = (sc.secondary_impacts || []).map(si => `
        <li class="flex items-start gap-2">
          <span class="text-amber-400 font-bold">•</span>
          <span>${{si}}</span>
        </li>
      `).join('');

      container.innerHTML = `
        <!-- Scenario Master Card -->
        <div class="glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
            <div>
              <div class="flex items-center gap-2">
                <span class="px-2.5 py-0.5 rounded-full bg-red-950/80 text-red-300 border border-red-800/60 text-xs font-bold">${{sc.severity}}</span>
                <span class="text-xs text-slate-400 font-medium">${{sc.category}}</span>
              </div>
              <h3 class="text-xl font-bold text-white mt-1">${{sc.title}}</h3>
            </div>
            <div class="text-right text-xs">
              <div class="text-slate-400">Boğum / Lokasyon:</div>
              <div class="font-bold text-blue-300">${{sc.chokepoint || '-'}}</div>
            </div>
          </div>

          <div class="text-xs text-slate-300 leading-relaxed bg-slate-900/40 p-3 rounded-xl border border-slate-800/60">
            <span class="font-bold text-amber-400">Tetikleyici Dinamik:</span> ${{sc.core_trigger}}
          </div>

          <!-- Exposure Numbers -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            ${{exposureHtml}}
          </div>
        </div>

        <!-- 2 Columns: Vulnerable Countries vs Mitigations -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="space-y-3">
            <h4 class="text-xs font-bold uppercase tracking-wider text-red-400 flex items-center gap-1.5">
              <span>🎯</span> En Yüksek Maruziyete Sahip Ülkeler & Sektörler
            </h4>
            <div class="space-y-2.5">
              ${{vulnHtml}}
            </div>
          </div>

          <div class="space-y-4">
            <div class="space-y-3">
              <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                <span>🔄</span> Alternatif Lojistik ve İkmal Koridorları
              </h4>
              <div class="space-y-2.5">
                ${{mitigationsHtml}}
              </div>
            </div>

            <div class="space-y-2">
              <h4 class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                <span>⚠️</span> İkincil Küresel Sistemik Etkiler
              </h4>
              <ul class="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2 text-xs text-slate-300">
                ${{secondaryHtml}}
              </ul>
            </div>
          </div>
        </div>
      `;
    }}

    // Run dynamic shock simulation trigger
    function runShockSimulation() {{
      const crises = DATA.crises || [];
      const sc = crises.find(x => x.id === activeScenarioId) || crises[0];
      const box = document.getElementById('sim-alert-box');
      if (!box) return;

      const impactedCount = (sc.most_vulnerable_countries || []).length;
      box.classList.remove('hidden');
      box.innerHTML = `
        <div class="flex items-center justify-between">
          <div class="font-bold text-sm text-red-300 flex items-center gap-2">
            <span>🚨</span> CANLI SİMÜLASYON TETİKLENDİ: ${{sc.title.toUpperCase()}}
          </div>
          <button onclick="document.getElementById('sim-alert-box').classList.add('hidden')" class="text-slate-400 hover:text-white">&times;</button>
        </div>
        <p class="leading-relaxed">
          Sistemik domino etkisi hesaplandı: <b>${{impactedCount}} ana ithalatçı devlet</b> ilk 72 saat içinde kritik tedarik şokuna girmektedir.
          Denizcilik savaş riski sigorta primleri <b>%1200</b> fırlamış, alternatif koridor kapasitesi <b>%94 doluluk oranına</b> ulaşmıştır.
        </p>
        <div class="flex flex-wrap gap-2 pt-1">
          ${{(sc.most_vulnerable_countries || []).map(vc => `<span class="px-2 py-0.5 rounded bg-red-900/80 text-white font-mono text-[10px]">${{vc.name}}: %${{vc.dependency_pct}} Risk</span>`).join(' ')}}
        </div>
      `;
    }}

    // INITIALIZATION
    window.addEventListener('DOMContentLoaded', () => {{
      renderCountries();
      initCompareSelects();
      renderCulture();
      renderGeopolitics();
      renderGallery();
    }});
  </script>
</body>
</html>
"""

    output_path = BASE_DIR / "index.html"
    print(f"[*] HTML dosyası yazılıyor: {output_path}...")
    output_path.write_text(html_content, encoding="utf-8")
    print(f"[SUCCESS] index.html başarıyla üretildi! ({len(html_content):,} bayt)")

if __name__ == "__main__":
    build_web_atlas()
