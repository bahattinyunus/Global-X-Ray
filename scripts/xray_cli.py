#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/xray_cli.py
Medeniyet Atlası (Civilization Atlas) - Kültürel Kodlar, Yaşam Felsefesi & Güç Terminali

Kullanım:
  python scripts/xray_cli.py country <ulke_adi_veya_kodu>
  python scripts/xray_cli.py culture [ulke_veya_medeniyet]
  python scripts/xray_cli.py compare-culture <ulke_1> <ulke_2>
  python scripts/xray_cli.py epics [arama]
  python scripts/xray_cli.py architecture [arama]
  python scripts/xray_cli.py music [arama] (dünya geleneksel çalgıları & ses mirası)
  python scripts/xray_cli.py festivals [arama] (dünya festivalleri & kutsal ritüeller)
  python scripts/xray_cli.py compare <ulke_1> <ulke_2>
  python scripts/xray_cli.py search <terim>
  python scripts/xray_cli.py top-shadow [sayi]
  python scripts/xray_cli.py top-gdp [sayi]
  python scripts/xray_cli.py intel [ulke_adi]
  python scripts/xray_cli.py pmc [arama]
  python scripts/xray_cli.py chokepoints [arama]
  python scripts/xray_cli.py alliances [pakt_kodu]
  python scripts/xray_cli.py sanctions [ulke_kodu]
  python scripts/xray_cli.py minerals [maden_id]
  python scripts/xray_cli.py cables [bolge_id]
  python scripts/xray_cli.py swf [fon_veya_ulke]
  python scripts/xray_cli.py darkfleet
  python scripts/xray_cli.py nuclear [ulke_veya_kod]
  python scripts/xray_cli.py armstrade [sirket_veya_ulke]
  python scripts/xray_cli.py recon <ulke_adi>
  python scripts/xray_cli.py research [konu]
  python scripts/xray_cli.py cases
  python scripts/xray_cli.py list [bolge]
  python scripts/xray_cli.py briefing <ulke_adi> (stratejik 4-katmanlı yönetici istihbarat brifingi)
  python scripts/xray_cli.py crisis-sim [senaryo_veya_ulke] (küresel jeopolitik kriz & darboğaz simülatörü)
  python scripts/xray_cli.py matrix [havza_adi] (9 küresel medeniyet havzası & güç matrisi)
  python scripts/xray_cli.py currency [kod_veya_ag] (rezerv paralar, de-dolarizasyon, CIPS/mBridge, altın)
  python scripts/xray_cli.py cyber [grup_veya_casus] (devlet destekli APT grupları & Pegasus/Predator casus yazılımları)
  python scripts/xray_cli.py audit <ulke_adi> (360° çok vektörlü stratejik egemenlik ve kırılganlık denetimi)
  python scripts/xray_cli.py rank [olcut] [limit] (guc ve kirilganlik siralamasi: csfi, gdp, shadow, percapita)
  python scripts/xray_cli.py export <ulke_adi> [--format md|json] [--out dosya_adi]
  python scripts/xray_cli.py graph <ulke_adi> (oligark ve iktidar sermaye agi mermaid grafigi)
  python scripts/xray_cli.py <komut> --json (makine tarafindan okunabilir JSON ciktisi)
  python scripts/xray_cli.py stats
  python scripts/xray_cli.py interactive (canlı interaktif sorgu kabuğu)
"""

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
PMC_PATH = BASE_DIR / "global_datasets" / "pmc_mercenary_groups.json"
CHOKE_PATH = BASE_DIR / "global_datasets" / "chokepoints_registry.json"
ALLIANCES_PATH = BASE_DIR / "global_datasets" / "defense_alliances_and_treaties.json"
SANCTIONS_PATH = BASE_DIR / "global_datasets" / "sanctions_and_embargoes_registry.json"
MINERALS_PATH = BASE_DIR / "global_datasets" / "critical_raw_materials_supply_chain.json"
CABLES_PATH = BASE_DIR / "global_datasets" / "subsea_cables_and_sigint_stations.json"
SWF_PATH = BASE_DIR / "global_datasets" / "sovereign_wealth_funds_registry.json"
DARKFLEET_PATH = BASE_DIR / "global_datasets" / "shadow_fleet_maritime_registry.json"
NUCLEAR_PATH = BASE_DIR / "global_datasets" / "nuclear_arsenals_and_triad_registry.json"
ARMSTRADE_PATH = BASE_DIR / "global_datasets" / "global_arms_trade_and_contractors.json"
CULTURE_PATH = BASE_DIR / "global_datasets" / "cultural_codes_and_civilizations_registry.json"
CRISIS_PATH = BASE_DIR / "global_datasets" / "geopolitical_crisis_scenarios.json"
CURRENCY_PATH = BASE_DIR / "global_datasets" / "currency_hegemony_and_dedollarization.json"
CYBER_PATH = BASE_DIR / "global_datasets" / "cognitive_warfare_and_cyber_arsenals.json" 
DOSSIERS_DIR = BASE_DIR / "dossiers"
RESEARCH_DIR = BASE_DIR / "research"

OUTPUT_JSON = False

def load_currency():
    if CURRENCY_PATH.exists():
        with open(CURRENCY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def load_cyber():
    if CYBER_PATH.exists():
        with open(CYBER_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def load_crises():
    if CRISIS_PATH.exists():
        with open(CRISIS_PATH, "r", encoding="utf-8") as f:
            return json.load(f).get("scenarios", [])
    return []

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
        
    c_dir = BASE_DIR / c.get("economy_path", c.get("path", f"countries/{c['slug']}"))
    if not c_dir.exists():
        c_dir = BASE_DIR / c.get("path", f"countries/{c['slug']}")
    macro_path = c_dir / "03_official_economy" / "macroeconomics.json"
    shadow_path = c_dir / "04_shadow_power_osint" / "real_power_dynamics.md"
    oligarch_path = c_dir / "04_shadow_power_osint" / "oligarch_network.csv"

    if OUTPUT_JSON:
        c_dna = None
        if CULTURE_PATH.exists():
            with open(CULTURE_PATH, "r", encoding="utf-8") as f:
                c_dna_list = json.load(f).get("countries_cultural_dna", [])
            c_dna = next((x for x in c_dna_list if x.get("code") == c["code"] or x.get("country").lower() == c["name"].lower()), None)
        m = {}
        if macro_path.exists():
            with open(macro_path, "r", encoding="utf-8") as f:
                m = json.load(f)
        oligarchs_data = []
        if oligarch_path.exists():
            with open(oligarch_path, "r", encoding="utf-8") as f:
                oligarchs_data = list(csv.DictReader(f))
        print(json.dumps({
            "country": c,
            "cultural_dna": c_dna,
            "macroeconomics": m,
            "oligarchs": oligarchs_data
        }, ensure_ascii=False, indent=2))
        return

    print("=" * 80)
    print(f"🏛️ MEDENİYET ATLASI RAPORU: {c['name'].upper()} ({c['code']})")
    print("=" * 80)
    print(f"• Bölge: {c['region'].replace('_', ' ').title()}")
    print(f"• Başkent: {c['capital']}")
    print(f"• Nüfus: {c['population']:,}")
    print(f"• Nominal GSYH: ${c['gdp_usd_b']:,.1f} Milyar")
    print(f"• Gölge / Kayıt Dışı Ekonomi: %{c['shadow_economy_pct']}")
    print("-" * 75)

    if CULTURE_PATH.exists():
        with open(CULTURE_PATH, "r", encoding="utf-8") as f:
            c_dna_list = json.load(f).get("countries_cultural_dna", [])
        c_dna = next((x for x in c_dna_list if x.get("code") == c["code"] or x.get("country").lower() == c["name"].lower()), None)
        if c_dna:
            print("🎭 MEDENİYET KİMLİĞİ VE KÜLTÜREL KODLAR:")
            print(f"  Medeniyet Havzası: {c_dna.get('civilization_crossroads')}")
            print(f"  Ulusal Karakter:   {c_dna.get('core_cultural_ethos')}")
            print(f"  İletişim Tarzı:    {c_dna.get('communication_style')}")
            words = [f"{w['word']} ({w['meaning'][:40]}...)" for w in c_dna.get("untranslatable_soul_concepts", [])[:3]]
            if words:
                print(f"  Kilit Kavramlar:   {'; '.join(words)}")
            print("-" * 75)

    if macro_path.exists():
        with open(macro_path, "r", encoding="utf-8") as f:
            m = json.load(f)
            print("📊 EKONOMİ VE TİCARET:")
            print(f"  Para Birimi: {m.get('currency')}")
            print(f"  Kişi Başı Gelir: ${m.get('gdp_per_capita_usd'):,}")
            print(f"  Enflasyon: %{m.get('inflation_rate_pct')}")
            print(f"  Kamu Borcu / GSYH: %{m.get('debt_to_gdp_pct', 'N/A')}")
            print(f"  Dış Borç: ${m.get('external_debt_billion_usd', 'N/A')}B")
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

def show_pmcs(query=None):
    if not PMC_PATH.exists():
        print("[-] PMC veritabanı bulunamadı.")
        return
    with open(PMC_PATH, "r", encoding="utf-8") as f:
        pmcs = json.load(f).get("companies", [])
    if query:
        q = query.lower()
        pmcs = [p for p in pmcs if q in p["name"].lower() or q in p["country_of_origin"].lower()]
    print(f"⚔️ ÖZEL ASKERİ ŞİRKETLER (PMC) VERİTABANI ({len(pmcs)} Şirket):")
    print("=" * 80)
    for p in pmcs:
        print(f"[{p['name']} ({p['country_of_origin']})]")
        print(f"  • Hukuki Statü:  {p['legal_status']}")
        print(f"  • Tahmini Güç:   {p['estimated_manpower']}")
        print(f"  • Aktif Sahalar: {', '.join(p['active_theaters'])}")
        print(f"  • Gelir Modeli:  {', '.join(p['primary_revenue_sources'])}")
        print("-" * 80)

def show_chokepoints(query=None):
    if not CHOKE_PATH.exists():
        print("[-] Boğazlar veritabanı bulunamadı.")
        return
    with open(CHOKE_PATH, "r", encoding="utf-8") as f:
        cps = json.load(f).get("chokepoints", [])
    if query:
        q = query.lower()
        cps = [c for c in cps if q in c["name"].lower() or q in c["english_name"].lower()]
    print(f"🚢 STRATEJİK DENİZ DARBOĞAZLARI & KANALLAR ({len(cps)} Boğaz):")
    print("=" * 80)
    for c in cps:
        print(f"[{c['name']} / {c['english_name']}] - {c['type']}")
        print(f"  • Kontrol Eden Devletler: {', '.join(c['controlling_states'])}")
        print(f"  • Günlük Petrol Transiti: {c['daily_petroleum_transit_barrels']:,} varil/gün (%{c['share_of_global_maritime_oil_pct']})")
        print(f"  • Yıllık Gemi Geçişi:    {c['annual_vessel_transits']:,}")
        print(f"  • Tehdit Vektörleri:     {', '.join(c['asymmetric_threats'])}")
        print(f"  • Risk Seviyesi:         {c['geopolitical_risk_level']}")
        print("-" * 80)

def show_alliances(query=None):
    if not ALLIANCES_PATH.exists():
        print("[-] Askeri ittifaklar veritabanı bulunamadı.")
        return
    with open(ALLIANCES_PATH, "r", encoding="utf-8") as f:
        alliances = json.load(f).get("alliances", [])
    if query:
        q = query.lower()
        alliances = [a for a in alliances if q in a["id"].lower() or q in a["name"].lower() or q in a["english_name"].lower()]
    print(f"🛡️ KÜRESEL ASKERİ İTTİFAKLAR & SAVUNMA PAKTLARI ({len(alliances)} Pakt):")
    print("=" * 80)
    for a in alliances:
        print(f"[{a['id']}] {a['name']}")
        print(f"  • Kuruluş & Merkez:   {a['established']} / {a['headquarters']} ({a['member_count']} Üye)")
        print(f"  • Tetikleyici Madde:  {a['core_trigger_article']}")
        print(f"  • Nükleer Doktrin:    {a['nuclear_doctrine']}")
        print(f"  • Kilit Üyeler:       {', '.join(a['key_members'])}")
        print(f"  • Stratejik Odak:     {a['strategic_focus']}")
        print(f"  • Ortak Bütçe:        ${a['combined_military_spending_usd_b']} Milyar")
        print("-" * 80)

def show_sanctions(query=None):
    if not SANCTIONS_PATH.exists():
        print("[-] Yaptırımlar veritabanı bulunamadı.")
        return
    with open(SANCTIONS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    states = data.get("targeted_states", [])
    if query:
        q = query.lower()
        states = [s for s in states if q in s["country"].lower() or q in s["code"].lower()]
    print(f"⚠️ KÜRESEL YAPTIRIM REJİMLERİ & BYPASS KORİDORLARI ({len(states)} Hedef Rejim):")
    print("=" * 80)
    for s in states:
        print(f"[{s['country']} ({s['code']})] - {s['regime_type']}")
        print(f"  • Yaptırım Uygulayanlar: {', '.join(s['primary_sanctioners'])}")
        print(f"  • Dondurulan Varlıklar:  ${s['frozen_assets_usd_b']} Milyar")
        print("  • Temel Kısıtlamalar:")
        for r in s['core_restrictions']:
            print(f"    - {r}")
        print("  • Bypass & Kaçınma Koridorları:")
        for c in s['circumvention_corridors']:
            print(f"    * {c}")
        print("-" * 80)

def show_minerals(query=None):
    if not MINERALS_PATH.exists():
        print("[-] Kritik madenler veritabanı bulunamadı.")
        return
    with open(MINERALS_PATH, "r", encoding="utf-8") as f:
        minerals = json.load(f).get("minerals", [])
    if query:
        q = query.lower()
        minerals = [m for m in minerals if q in m["id"].lower() or q in m["name"].lower()]
    print(f"⛏️ KRİTİK HAMMADDELER VE RAFİNAJ TEKELLERİ ({len(minerals)} Maden/Element):")
    print("=" * 80)
    for m in minerals:
        print(f"[{m['id']}] {m['name']} - Kategori: {m['strategic_category']} (Risk: {m['geopolitical_risk_score']}/10)")
        print(f"  • Kullanım Alanı:  {m['critical_applications']}")
        top_producers = [f"{t['country']} (%{t['share_pct']})" for t in m['top_mining_nations']]
        print(f"  • Üretici Güçler:  {', '.join(top_producers)}")
        ref = m['refining_monopoly']
        print(f"  • Rafinaj Tekeli:  {ref['dominant_nation']} (%{ref['global_refining_share_pct']})")
        print(f"  • Analitik Tehdit: {ref['vulnerability_analysis']}")
        print("-" * 80)

def show_cables(query=None):
    if not CABLES_PATH.exists():
        print("[-] Denizaltı kabloları veritabanı bulunamadı.")
        return
    with open(CABLES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    corridors = data.get("critical_cable_corridors", [])
    stations = data.get("global_sigint_interception_stations", [])
    if query:
        q = query.lower()
        corridors = [c for c in corridors if q in c["id"].lower() or q in c["name"].lower()]
        stations = [s for s in stations if q in s["station_name"].lower() or q in s["country"].lower()]
    print(f"🌐 DENİZALTI FİBER KABLOLAR & SIGINT İSTASYONLARI:")
    print("=" * 80)
    for c in corridors:
        print(f"[Kablo Koridoru: {c['name']}] (Risk: {c['geopolitical_risk']})")
        print(f"  • Bağlantı:   {c['connected_regions']}")
        print(f"  • Kilit Hatlar: {', '.join(c['key_cables'])}")
        print(f"  • Kırılganlık:  {c['vulnerability']}")
        print("-" * 80)
    for s in stations:
        print(f"[SIGINT İstasyonu: {s['station_name']} ({s['country']})]")
        print(f"  • İşleten:    {s['operator']} / {s['location']}")
        print(f"  • Kapasite:   {s['capabilities']}")
        print("-" * 80)

def show_case_studies():
    if not DOSSIERS_DIR.exists():
        print("[-] Vaka analizleri klasörü bulunamadı.")
        return
    files = list(DOSSIERS_DIR.glob("*.md"))
    print(f"📁 DERİN ADLİ OSINT VAKA ANALİZLERİ ({len(files)} Dosya):")
    print("=" * 80)
    for f in sorted(files, key=lambda x: x.name):
        print(f"  • {f.name:<55} -> dossiers/{f.name}")
    print("=" * 80)

def show_research(query=None):
    if not RESEARCH_DIR.exists():
        print("[-] Araştırma dosyaları klasörü bulunamadı.")
        return
    files = list(RESEARCH_DIR.glob("*.md"))
    if query:
        q = query.lower()
        files = [f for f in files if q in f.name.lower()]
    print(f"📚 ANSİKLOPEDİK ARAŞTIRMA TEZLERİ & DOKTRİN DOSYALARI ({len(files)} Dosya):")
    print("=" * 80)
    for f in sorted(files, key=lambda x: x.name):
        size_kb = f.stat().st_size / 1024
        print(f"  • {f.name:<55} ({size_kb:,.1f} KB) -> research/{f.name}")
    print("=" * 80)

def show_swfs(query=None):
    if not SWF_PATH.exists():
        print("[-] Egemen varlık fonları veritabanı bulunamadı.")
        return
    with open(SWF_PATH, "r", encoding="utf-8") as f:
        funds = json.load(f).get("funds", [])
    if query:
        q = query.lower()
        funds = [fn for fn in funds if q in fn["name"].lower() or q in fn["country"].lower() or q in fn["id"].lower()]
    print(f"💰 KÜRESEL EGEMEN VARLIK FONLARI (SWF) ({len(funds)} Fon):")
    print("=" * 80)
    for fn in funds:
        print(f"[{fn['id']}] {fn['name']} ({fn['country']})")
        print(f"  • Varlık Hacmi (AUM): ${fn['assets_under_management_usd_b']:,.1f} Milyar USD")
        print(f"  • Fon Kaynağı:        {fn['funding_source']}")
        print(f"  • Yönetim Modeli:     {fn['governance_model']}")
        print(f"  • Stratejik Varlık:   {fn['strategic_holdings']}")
        print(f"  • Jeopolitik Kaldıraç:{fn['geopolitical_leverage']}")
        print("-" * 80)

def show_darkfleet(query=None):
    if not DARKFLEET_PATH.exists():
        print("[-] Gölge filo veritabanı bulunamadı.")
        return
    with open(DARKFLEET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    metrics = data.get("fleet_metrics", {})
    flags = data.get("flags_of_convenience", [])
    sts = data.get("sts_transfer_chokepoints", [])
    print("🚢 KÜRESEL GÖLGE TANKER FİLOSU (DARK FLEET) & STS TRANSFERLERİ:")
    print("=" * 80)
    print(f"• Aktif Gölge Tanker Sayısı:  ~{metrics.get('estimated_active_vessels')} Gemi")
    print(f"• Küresel Tanker Tonaj Payı:  %{metrics.get('share_of_global_tanker_tonnage_pct')}")
    print(f"• Ortalama Gemi Yaşı:         {metrics.get('average_vessel_age_years')} Yıl")
    print(f"• Yük Menşeleri:              {', '.join(metrics.get('primary_cargo_origins', []))}")
    print(f"• Ana Rotalar:                {', '.join(metrics.get('primary_destinations', []))}")
    print("-" * 80)
    print("🚩 ÖNE ÇIKAN KOLAYLIK BAYRAKLARI (Flags of Convenience):")
    for fl in flags:
        print(f"  [{fl['flag_state']}] - {fl['registered_dark_vessels']} Gemi | {fl['risk_profile']}")
    print("-" * 80)
    print("⚓ DENİZ ÜSTÜ GEMİDEN GEMİYE (STS) AKTARIM KORİDORLARI:")
    for s in sts:
        print(f"  [{s['zone_name']}] - {s['location']}")
        print(f"    * {s['operations']}")
    print("=" * 80)

def show_nuclear(query=None):
    if not NUCLEAR_PATH.exists():
        print("[-] Nükleer cephanelik veritabanı bulunamadı.")
        return
    with open(NUCLEAR_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    powers = data.get("nuclear_powers", [])
    overview = data.get("strategic_overview", {})
    
    if query:
        q = query.lower()
        powers = [p for p in powers if q in p["country"].lower() or q in p["code"].lower() or q in p.get("nuclear_doctrine", "").lower()]
        
    print("☢️ KÜRESEL NÜKLEER CEPHANELİKLER & STRATEJİK TRİAD REGİSTRİ:")
    print("=" * 85)
    print(f"• Küresel Toplam Savaş Başlığı:       ~{overview.get('global_total_warheads', 0):,}")
    print(f"• Konuşlu ve Operasyonel Başlık:      ~{overview.get('deployed_operational_warheads', 0):,}")
    print(f"• Nükleer Silaha Sahip Güç Sayısı:    {overview.get('nuclear_armed_states_count', 9)}")
    print("=" * 85)
    for p in powers:
        print(f"\n🚀 [{p['code']}] {p['country'].upper()} (İlk Test: {p.get('first_test_year')})")
        print(f"  • Toplam Envanter:        {p['total_inventory']:,} Başlık (Konuşlu: {p.get('deployed_strategic_warheads', 'N/A')})")
        triad = p.get("triad_components", {})
        if triad:
            print(f"  • Kara (ICBM):            {triad.get('land_icbm', 'Mevcut değil')}")
            print(f"  • Deniz (SSBN):           {triad.get('sea_ssbn', 'Mevcut değil')}")
            print(f"  • Hava (Bombardıman):     {triad.get('air_bomber', 'Mevcut değil')}")
        if p.get("hypersonic_and_asymmetric"):
            print(f"  • Asimetrik/Hipersonik:   {'; '.join(p['hypersonic_and_asymmetric'][:2])}")
        if p.get("early_warning_and_dead_hand"):
            print(f"  • Erken Uyarı / Ölü El:   {p['early_warning_and_dead_hand']}")
        print(f"  • Doktrin:                {p.get('nuclear_doctrine')}")
        print("-" * 85)

def show_armstrade(query=None):
    if not ARMSTRADE_PATH.exists():
        print("[-] Silah ticareti ve savunma sanayii veritabanı bulunamadı.")
        return
    with open(ARMSTRADE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    contractors = data.get("top_prime_contractors", [])
    m_overview = data.get("market_overview", {})
    
    if query:
        q = query.lower()
        contractors = [c for c in contractors if q in c["company"].lower() or q in c["country"].lower() or q in c.get("flagship_systems", "").lower()]
        
    print("⚔️ KÜRESEL SİLAH TİCARETİ & SAVUNMA SANAYİİ TRÖSTLERİ:")
    print("=" * 85)
    print(f"• Küresel Yıllık Askeri Harcama:    ${m_overview.get('global_defense_expenditure_usd_b', 0):,.1f} Milyar")
    print(f"• İlk 100 Savunma Şirketi Cirosu:   ${m_overview.get('top_100_defense_revenue_usd_b', 0):,.1f} Milyar")
    print(f"• İhracat Pazar Payları:            ABD %{m_overview.get('us_market_share_of_exports_pct')} | Fransa %{m_overview.get('france_market_share_of_exports_pct')} | Rusya %{m_overview.get('russia_market_share_of_exports_pct')}")
    print("=" * 85)
    for c in contractors:
        print(f"\n🏢 #{c['rank']} {c['company']} ({c['country']})")
        print(f"  • Savunma Hasılatı:  ${c['defense_revenue_usd_b']} Milyar USD")
        print(f"  • Amiral Sistemler:  {c['flagship_systems']}")
        print(f"  • Stratejik Tekel:   {c['strategic_monopoly']}")
        print("-" * 85)

def show_culture(query=None):
    if not CULTURE_PATH.exists():
        print("[-] Kültürel kodlar veritabanı bulunamadı.")
        return
    with open(CULTURE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    realms = data.get("civilization_realms", [])
    countries_dna = data.get("countries_cultural_dna", [])

    if not query:
        print("=" * 85)
        print("🏛️ KÜRESEL MEDENİYETLER VE KÜLTÜREL KODLAR REHBERİ")
        print("=" * 85)
        print(f"Toplam {len(realms)} Büyük Medeniyet Havzası ve {len(countries_dna)} Detaylı Kültürel Profil:\n")
        for r in realms:
            print(f"📍 [{r['name']}]")
            print(f"   Felsefe: {r['core_philosophy']}")
            print(f"   Temsilci Ülkeler: {', '.join(r['representative_states'])}\n")
        print("=" * 85)
        print("[!] Belirli bir ülkenin kültürel kodlarını incelemek için: python scripts/xray_cli.py culture <ulke>")
        return

    q = query.lower().strip()
    c_reg = find_country(q)
    target_code = c_reg["code"].lower() if c_reg else ""

    matched = None
    for c in countries_dna:
        if (target_code and c.get("code", "").lower() == target_code) or \
           q in c["country"].lower() or q in c["code"].lower() or q in c["capital"].lower():
            matched = c
            break

    if not matched:
        matched_realms = [r for r in realms if q in r["name"].lower() or q in r["id"].lower()]
        if matched_realms:
            for r in matched_realms:
                print("=" * 85)
                print(f"🏛️ MEDENİYET HAVZASI: {r['name'].upper()}")
                print("=" * 85)
                print(f"• Temel Felsefe:   {r['core_philosophy']}")
                print(f"• Temsilci Ülkeler: {', '.join(r['representative_states'])}")
                print("=" * 85)
            return
        print(f"[-] '{query}' için kültürel profil veya medeniyet havzası bulunamadı.")
        return

    print("=" * 85)
    print(f"🎭 KÜLTÜREL KODLAR VE ULUSAL KARAKTER: {matched['country'].upper()} ({matched['code']})")
    print("=" * 85)
    print(f"• Medeniyet Kavşağı:       {matched['civilization_crossroads']}")
    print(f"• Ulusal Karakter & Ethos: {matched['core_cultural_ethos']}")
    print(f"• İletişim Tarzı:          {matched['communication_style']}")
    print("-" * 85)
    print("✨ ÇEVRİLEMEYEN RUH KAVRAMLARI (Untranslatable Concepts):")
    for w in matched.get("untranslatable_soul_concepts", []):
        print(f"  • {w['word']}: {w['meaning']}")
    print("-" * 85)
    print("☕ GÜNDELİK HAYAT VE SOSYAL RİTÜELLER:")
    print(f"  {matched['social_rituals_and_lifestyle']}")
    print("-" * 85)
    print("🍲 MUTFAK FELSEFESİ & GASTRONOMİ:")
    print(f"  {matched['gastronomic_philosophy']}")
    print("-" * 85)
    print("🚫 GÖRGÜ KURALLARI VE SOSYAL TABULAR (Do's & Don'ts):")
    print(f"  {matched['social_taboos_and_etiquette']}")
    print("-" * 85)
    print("📚 EDEBİYAT, SANAT VE MİMARİ MİRAS:")
    print(f"  {matched['literary_and_artistic_archetypes']}")
    print("=" * 85)

def show_epics(query=None):
    epics_file = BASE_DIR / "culture" / "GLOBAL_FOLKLORE_MYTHOLOGY_AND_EPICS.md"
    if not epics_file.exists():
        print("[-] Destanlar külliyatı bulunamadı.")
        return
    with open(epics_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print("=" * 85)
    print("📜 DÜNYA MİTOLOJİLERİ VE KURUCU DESTANLAR KÜLLİYATI")
    print("=" * 85)
    
    table_rows = []
    in_table = False
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("| Destan"):
            in_table = True
            continue
        if in_table and line_s.startswith("| :---"):
            continue
        if in_table and line_s.startswith("|"):
            parts = [p.strip() for p in line_s.split("|")[1:-1]]
            if len(parts) >= 5:
                table_rows.append({
                    "epic": parts[0].replace("**", ""),
                    "civ": parts[1],
                    "hero": parts[2],
                    "theme": parts[3],
                    "legacy": parts[4]
                })
        elif in_table and not line_s.startswith("|"):
            in_table = False

    if query:
        q = query.lower()
        table_rows = [r for r in table_rows if q in r["epic"].lower() or q in r["civ"].lower() or q in r["hero"].lower() or q in r["theme"].lower()]
        
    for r in table_rows:
        print(f"\n📖 {r['epic']} ({r['civ']})")
        print(f"  • Baş Kahraman / Figür:   {r['hero']}")
        print(f"  • Temel Felsefe & İkilem: {r['theme']}")
        print(f"  • Edebi & Manevi Miras:   {r['legacy']}")
        print("-" * 85)
    print(f"\n[!] Detaylı felsefi analiz için bkz: culture/GLOBAL_FOLKLORE_MYTHOLOGY_AND_EPICS.md")

def show_architecture(query=None):
    arch_file = BASE_DIR / "culture" / "WORLD_ARCHITECTURE_AND_SACRED_SPACES.md"
    if not arch_file.exists():
        print("[-] Mimari külliyatı bulunamadı.")
        return
    with open(arch_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("=" * 85)
    print("🏛️ DÜNYA MİMARİSİ, ŞEHİR FELSEFESİ VE KUTSAL MEKANLAR KÜLLİYATI")
    print("=" * 85)

    table_rows = []
    in_table = False
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("| Mimari Ekol"):
            in_table = True
            continue
        if in_table and line_s.startswith("| :---"):
            continue
        if in_table and line_s.startswith("|"):
            parts = [p.strip() for p in line_s.split("|")[1:-1]]
            if len(parts) >= 5:
                table_rows.append({
                    "school": parts[0].replace("**", ""),
                    "geo": parts[1],
                    "materials": parts[2],
                    "philosophy": parts[3].replace("**", ""),
                    "masterpieces": parts[4]
                })
        elif in_table and not line_s.startswith("|"):
            in_table = False

    if query:
        q = query.lower()
        table_rows = [r for r in table_rows if q in r["school"].lower() or q in r["geo"].lower() or q in r["philosophy"].lower() or q in r["masterpieces"].lower()]

    for r in table_rows:
        print(f"\n🏰 {r['school']} ({r['geo']})")
        print(f"  • Malzeme & Strüktür:  {r['materials']}")
        print(f"  • Mekan Felsefesi:     {r['philosophy']}")
        print(f"  • Başyapıt Örnekleri:  {r['masterpieces']}")
        print("-" * 85)
    print(f"\n[!] Detaylı şehir meydanları ve mekan felsefesi için bkz: culture/WORLD_ARCHITECTURE_AND_SACRED_SPACES.md")

def show_music(query=None):
    music_file = BASE_DIR / "culture" / "GLOBAL_MUSIC_INSTRUMENTS_AND_SONIC_HERITAGE.md"
    if not music_file.exists():
        print("[-] Müzik mirası külliyatı bulunamadı.")
        return
    with open(music_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("=" * 85)
    print("🎵 DÜNYA MÜZİK MİRASI VE GELENEKSEL ÇALGILAR KÜLLİYATI")
    print("=" * 85)

    table_rows = []
    in_table = False
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("| Geleneksel Çalgı"):
            in_table = True
            continue
        if in_table and line_s.startswith("| :---"):
            continue
        if in_table and line_s.startswith("|"):
            parts = [p.strip() for p in line_s.split("|")[1:-1]]
            if len(parts) >= 5:
                table_rows.append({
                    "instrument": parts[0].replace("**", ""),
                    "geo": parts[1],
                    "materials": parts[2],
                    "spirit": parts[3].replace("**", ""),
                    "meaning": parts[4]
                })
        elif in_table and not line_s.startswith("|"):
            in_table = False

    if query:
        q = query.lower()
        table_rows = [r for r in table_rows if q in r["instrument"].lower() or q in r["geo"].lower() or q in r["spirit"].lower() or q in r["meaning"].lower()]

    for r in table_rows:
        print(f"\n🎻 {r['instrument']} ({r['geo']})")
        print(f"  • Aile & Malzeme:    {r['materials']}")
        print(f"  • Manevi Karakter:   {r['spirit']}")
        print(f"  • Kültürel Anlamı:   {r['meaning']}")
        print("-" * 85)
    print(f"\n[!] Detaylı ses felsefesi için bkz: culture/GLOBAL_MUSIC_INSTRUMENTS_AND_SONIC_HERITAGE.md")

def show_festivals(query=None):
    fest_file = BASE_DIR / "culture" / "WORLD_FESTIVALS_CALENDARS_AND_RITUALS.md"
    if not fest_file.exists():
        print("[-] Festivaller külliyatı bulunamadı.")
        return
    with open(fest_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("=" * 85)
    print("🎆 DÜNYA FESTİVALLERİ VE KUTSAL RİTÜELLER KÜLLİYATI")
    print("=" * 85)

    table_rows = []
    in_table = False
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("| Festival / Bayram"):
            in_table = True
            continue
        if in_table and line_s.startswith("| :---"):
            continue
        if in_table and line_s.startswith("|"):
            parts = [p.strip() for p in line_s.split("|")[1:-1]]
            if len(parts) >= 5:
                table_rows.append({
                    "name": parts[0].replace("**", ""),
                    "geo": parts[1],
                    "time": parts[2],
                    "philosophy": parts[3].replace("**", ""),
                    "ritual": parts[4]
                })
        elif in_table and not line_s.startswith("|"):
            in_table = False

    if query:
        q = query.lower()
        table_rows = [r for r in table_rows if q in r["name"].lower() or q in r["geo"].lower() or q in r["philosophy"].lower() or q in r["ritual"].lower()]

    for r in table_rows:
        print(f"\n🎭 {r['name']} ({r['geo']})")
        print(f"  • Zaman & Süre:      {r['time']}")
        print(f"  • Temel Felsefe:     {r['philosophy']}")
        print(f"  • Kutsal Ritüeller:  {r['ritual']}")
        print("-" * 85)
    print(f"\n[!] Detaylı takvim döngüleri için bkz: culture/WORLD_FESTIVALS_CALENDARS_AND_RITUALS.md")

def compare_culture(q1: str, q2: str):
    if not CULTURE_PATH.exists():
        print("[-] Kültürel kodlar veritabanı bulunamadı.")
        return
    with open(CULTURE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    countries_dna = data.get("countries_cultural_dna", [])

    def match_dna(q):
        ql = q.lower().strip()
        c_reg = find_country(ql)
        target_code = c_reg["code"].lower() if c_reg else ""
        for c in countries_dna:
            if (target_code and c.get("code", "").lower() == target_code) or \
               ql in c["country"].lower() or ql in c["code"].lower() or ql in c["capital"].lower():
                return c
        return None

    dna1 = match_dna(q1)
    dna2 = match_dna(q2)

    if not dna1 or not dna2:
        print(f"[-] Karşılaştırılacak ülkelerden biri veya ikisi kültürel DNA veritabanında bulunamadı: ({q1}, {q2})")
        return

    print("=" * 90)
    print(f"🎭 MEDENİYET VE KÜLTÜREL DNA KARŞILAŞTIRMASI")
    print(f"   {dna1['country'].upper()} ({dna1['code']}) vs {dna2['country'].upper()} ({dna2['code']})")
    print("=" * 90)
    print(f"• Medeniyet Havzası:")
    print(f"  [{dna1['country']}]: {dna1['civilization_crossroads']}")
    print(f"  [{dna2['country']}]: {dna2['civilization_crossroads']}")
    print("-" * 90)
    print(f"• Temel Kültürel Ethos & Karakter:")
    print(f"  [{dna1['country']}]: {dna1['core_cultural_ethos']}")
    print(f"  [{dna2['country']}]: {dna2['core_cultural_ethos']}")
    print("-" * 90)
    print(f"• İletişim Tarzı & Sosyal Etkileşim:")
    print(f"  [{dna1['country']}]: {dna1['communication_style']}")
    print(f"  [{dna2['country']}]: {dna2['communication_style']}")
    print("-" * 90)
    print(f"• Çevrilemeyen Ruh Kavramları:")
    c1_words = ", ".join([w['word'] + ' (' + w['meaning'][:40] + '...)' for w in dna1.get('untranslatable_soul_concepts', [])])
    c2_words = ", ".join([w['word'] + ' (' + w['meaning'][:40] + '...)' for w in dna2.get('untranslatable_soul_concepts', [])])
    print(f"  [{dna1['country']}]: {c1_words}")
    print(f"  [{dna2['country']}]: {c2_words}")
    print("-" * 90)
    print(f"• Sofra Ritüelleri ve Mutfak:")
    print(f"  [{dna1['country']}]: {dna1['gastronomic_philosophy']}")
    print(f"  [{dna2['country']}]: {dna2['gastronomic_philosophy']}")
    print("-" * 90)
    print(f"• Sosyal Tabular & Görgü:")
    print(f"  [{dna1['country']}]: {dna1['social_taboos_and_etiquette']}")
    print(f"  [{dna2['country']}]: {dna2['social_taboos_and_etiquette']}")
    print("=" * 90)


def show_rank(query=None, limit=20, sort_by="csfi"):
    matrix_data = load_matrix()
    if not matrix_data:
        print("[-] Power matrix verisi yüklenemedi.")
        return

    filtered = list(matrix_data)
    if query:
        q = query.lower().strip()
        if q in ["gdp", "gsyh"]:
            sort_by = "gdp"
        elif q in ["shadow", "golge"]:
            sort_by = "shadow"
        elif q in ["percapita", "kisi-basi"]:
            sort_by = "percapita"
        elif q in ["csfi", "kirilganlik", "risk"]:
            sort_by = "csfi"
        else:
            filtered = [x for x in matrix_data if q in x.get("region", "").lower() or q in x.get("name", "").lower() or q in x.get("code", "").lower() or q in x.get("risk_tier", "").lower()]

    if sort_by == "gdp":
        filtered.sort(key=lambda x: x.get("gdp_usd_b", 0), reverse=True)
        metric_title = "Nominal GSYİH ($B)"
    elif sort_by == "shadow":
        filtered.sort(key=lambda x: x.get("shadow_economy_pct", 0), reverse=True)
        metric_title = "Gölge Ekonomi (%)"
    elif sort_by == "percapita":
        filtered.sort(key=lambda x: x.get("gdp_per_capita_usd", 0), reverse=True)
        metric_title = "Kişi Başı Gelir ($)"
    else:
        filtered.sort(key=lambda x: x.get("fragility_index_csfi", 0), reverse=True)
        metric_title = "CSFI Kırılganlık İndeksi"

    if limit and limit > 0:
        filtered = filtered[:limit]

    if OUTPUT_JSON:
        print(json.dumps(filtered, ensure_ascii=False, indent=2))
        return

    print("=" * 90)
    print(f"📊 KÜRESEL GÜÇ & KIRILGANLIK MATRİSİ SIRALAMASI ({metric_title})")
    print("=" * 90)
    print(f"{'Sıra':<5} | {'Ülke':<24} | {'Kod':<5} | {'Bölge':<14} | {'CSFI':<7} | {'GSYH ($B)':<10} | {'Gölge (%)':<9}")
    print("-" * 90)
    for idx, c in enumerate(filtered, start=1):
        csfi_val = f"{c.get('fragility_index_csfi', 0):.1f}"
        gdp_val = f"${c.get('gdp_usd_b', 0):,.1f}"
        shadow_val = f"%{c.get('shadow_economy_pct', 0):.1f}"
        print(f"{idx:<5} | {c.get('name', ''):<24} | {c.get('code', ''):<5} | {c.get('region', ''):<14} | {csfi_val:<7} | {gdp_val:<10} | {shadow_val:<9}")
    print("=" * 90)

def export_country_dossier(query: str, fmt="md", output_file=None):
    c = find_country(query)
    if not c:
        print(f"[-] Ülke bulunamadı: '{query}'")
        return

    c_dir = BASE_DIR / c.get("economy_path", c.get("path", f"countries/{c['slug']}"))
    if not c_dir.exists():
        c_dir = BASE_DIR / c.get("path", f"countries/{c['slug']}")

    c_dna = None
    if CULTURE_PATH.exists():
        with open(CULTURE_PATH, "r", encoding="utf-8") as f:
            c_dna_list = json.load(f).get("countries_cultural_dna", [])
        c_dna = next((x for x in c_dna_list if x.get("code") == c["code"] or x.get("country").lower() == c["name"].lower()), None)

    macro = {}
    macro_path = c_dir / "03_official_economy" / "macroeconomics.json"
    if macro_path.exists():
        with open(macro_path, "r", encoding="utf-8") as f:
            macro = json.load(f)

    oligarchs = []
    oligarch_path = c_dir / "04_shadow_power_osint" / "oligarch_network.csv"
    if oligarch_path.exists():
        with open(oligarch_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            oligarchs = list(reader)

    def read_layer_file(rel):
        p = c_dir / rel
        if p.exists():
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                return f.read().strip()
        return ""

    society_text = read_layer_file("01_culture_demographics/society_history.md")
    state_text = read_layer_file("02_official_state/constitution_gov.md")
    power_text = read_layer_file("04_shadow_power_osint/real_power_dynamics.md")
    media_text = read_layer_file("04_shadow_power_osint/media_censorship_matrix.md")

    if fmt == "json" or OUTPUT_JSON:
        export_payload = {
            "metadata": c,
            "cultural_dna": c_dna,
            "macroeconomics": macro,
            "oligarchs": oligarchs,
            "society_history": society_text,
            "constitution_gov": state_text,
            "real_power_dynamics": power_text,
            "media_censorship_matrix": media_text
        }
        res_str = json.dumps(export_payload, ensure_ascii=False, indent=2)
    else:
        lines = [
            f"# 🏛️ MEDENİYET ATLASI DERİN ÜLKE DOSYASI: {c['name'].upper()} ({c['code']})",
            "",
            f"> *Resmi Başkent:* **{c['capital']}** | *Bölge:* **{c['region'].replace('_', ' ').title()}** | *Nüfus:* **{c['population']:,}**",
            f"> *Nominal GSYİH:* **${c['gdp_usd_b']:,.1f} Milyar** | *Gölge Ekonomi Oranı:* **%{c['shadow_economy_pct']}**",
            "",
            "---",
            "",
            "## 🎭 1. KÜLTÜREL KODLAR VE MEDENİYET KİMLİĞİ",
        ]
        if c_dna:
            lines.extend([
                f"* **Medeniyet Havzası:** {c_dna.get('civilization_crossroads')}",
                f"* **Temel Ulusal Ethos:** {c_dna.get('core_cultural_ethos')}",
                f"* **İletişim Tarzı:** {c_dna.get('communication_style')}",
                f"* **Mutfak Felsefesi:** {c_dna.get('gastronomic_philosophy')}",
                f"* **Görgü Kuralları ve Tabular:** {c_dna.get('social_taboos_and_etiquette')}",
                "",
                "### 📖 Çevrilemeyen Ruh Kavramları:"
            ])
            for w in c_dna.get("untranslatable_soul_concepts", []):
                lines.append(f"* **{w.get('word')}**: {w.get('meaning')} *(Kültürel Bağlam: {w.get('cultural_context')})*")
        
        if society_text:
            lines.extend(["", "### 📜 Toplumsal Tarih ve Kültürel Bellek:", "", society_text])

        lines.extend([
            "",
            "---",
            "",
            "## ⚖️ 2. RESMİ DEVLET VE ANAYASAL YAPI",
            "",
            state_text if state_text else "Resmi anayasal bilgi bulunamadı.",
            "",
            "---",
            "",
            "## 📊 3. MAKROEKONOMİK DOKU VE DIŞ TİCARET",
            "",
            f"* **Para Birimi:** {macro.get('currency', 'N/A')}",
            f"* **Kişi Başı Gelir:** ${macro.get('gdp_per_capita_usd', 0):,}",
            f"* **Enflasyon Oranı:** %{macro.get('inflation_rate_pct', 'N/A')}",
            f"* **Kamu Borcu / GSYH:** %{macro.get('debt_to_gdp_pct', 'N/A')}",
            f"* **Dış Borç:** ${macro.get('external_debt_billion_usd', 'N/A')}B",
            f"* **Ana İhracat Kalemleri:** {', '.join(macro.get('top_exports', []))}",
            f"* **Başlıca Ticaret Ortakları:** {', '.join(macro.get('major_trading_partners', []))}",
            "",
            "---",
            "",
            "## 🕶️ 4. ÖRTÜLÜ GÜÇ DİNAMİKLERİ, OLİGARKLAR VE BASIN ÖZGÜRLÜĞÜ",
            "",
            "### 👑 Oligark ve Hanedan Sermaye Ağı:"
        ])
        if oligarchs:
            for o in oligarchs:
                wealth = f" (${o.get('estimated_wealth_usd_m')}M)" if o.get('estimated_wealth_usd_m') != "0" else ""
                lines.append(f"* **{o.get('person_or_entity')}**{wealth} — *Rol:* {o.get('role_or_title')} | *Sektör:* {o.get('connected_sector')} | *Siyasi Bağ:* {o.get('political_connection')}")
        else:
            lines.append("*(Kayıtlı doğrudan oligark verisi bulunamadı)*")

        if power_text:
            lines.extend(["", "### 🕵️ Gerçek Güç Dinamikleri ve Derin Ağlar:", "", power_text])
        if media_text:
            lines.extend(["", "### 📡 Medya Sansür ve Algoritmik Gözetim Matrisi:", "", media_text])

        res_str = "\n".join(lines)

    if output_file:
        out_p = Path(output_file)
        with open(out_p, "w", encoding="utf-8") as f:
            f.write(res_str)
        print(f"[+] Ülke dosyası başarıyla kaydedildi: {out_p.resolve()}")
    else:
        print(res_str)

def show_crisis_sim(query=None):
    crises = load_crises()
    if not crises:
        print("[-] Kriz senaryoları veri seti bulunamadı!")
        return

    if OUTPUT_JSON:
        if query:
            q = query.lower().strip()
            matched = [s for s in crises if q in s["id"].lower() or q in s["title"].lower() or q in s.get("chokepoint", "").lower() or any(q == c["code"].lower() or q in c["name"].lower() for c in s.get("most_vulnerable_countries", []))]
            print(json.dumps(matched, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(crises, ensure_ascii=False, indent=2))
        return

    if not query:
        print("=" * 90)
        print("⚡ MEDENİYET ATLASI - KÜRESEL JEOPOLİTİK KRİZ & DARBOĞAZ SİMÜLATÖRÜ")
        print("=" * 90)
        print(f"{'Senaryo ID':<26} | {'Kategori':<24} | {'Risk / Şiddet':<20} | {'Boğum Noktası'}")
        print("-" * 90)
        for s in crises:
            print(f"{s['id']:<26} | {s['category'][:23]:<24} | {s['severity']:<20} | {s.get('chokepoint', '')}")
        print("=" * 90)
        print("💡 Detay için: python scripts/xray_cli.py crisis-sim <senaryo_id_veya_ulke>")
        print("   Örnek: python scripts/xray_cli.py crisis-sim hormuz_blockade")
        print("   Örnek: python scripts/xray_cli.py crisis-sim turkiye")
        return

    q = query.lower().strip()
    matched_scenario = next((s for s in crises if q == s["id"].lower() or q in s["title"].lower() or q in s.get("chokepoint", "").lower()), None)
    
    if matched_scenario:
        s = matched_scenario
        print("=" * 80)
        print(f"🚨 KRİZ SENARYOSU: {s['title'].upper()}")
        print("=" * 80)
        print(f"• ID:                    {s['id']}")
        print(f"• Kategori:              {s['category']}")
        print(f"• Tehdit Seviyesi:       {s['severity']}")
        print(f"• Boğum / Odak Noktası:  {s.get('chokepoint', '')} ({s.get('location', '')})")
        print(f"• Tetikleyici Unsur:     {s['core_trigger']}")
        print("\n📈 Stratejik Etki ve Maruziyet:")
        for k, v in s.get("strategic_exposure", {}).items():
            print(f"  - {k.replace('_', ' ').title()}: {v}")
        print("\n🎯 En Yüksek Kırılganlığa Sahip Ülkeler:")
        for c in s.get("most_vulnerable_countries", []):
            print(f"  • {c['name']} ({c['code']}): %{c['dependency_pct']} bağımlılık — [{c['sector']}]")
        print("\n🔄 Alternatif Bypass ve İkmal Koridorları:")
        for m in s.get("mitigation_corridors", []):
            cap = f" ({m['capacity_mbpd']} mbpd)" if m.get('capacity_mbpd') else ""
            print(f"  • {m['route']}{cap}: {m['status']}")
        print("\n⚠️ İkincil Dalga Etkileri:")
        for sec in s.get("secondary_impacts", []):
            print(f"  - {sec}")
        print("=" * 80)
        return

    # Country query match
    country_matches = []
    for s in crises:
        for c in s.get("most_vulnerable_countries", []):
            if q == c["code"].lower() or q in c["name"].lower():
                country_matches.append((s, c))
                break

    if country_matches:
        country_name = country_matches[0][1]["name"]
        print("=" * 80)
        print(f"🎯 {country_name.upper()} İÇİN JEOPOLİTİK KRİZ VE ŞOK MARUZİYET ANALİZİ")
        print("=" * 80)
        print(f"Bu ülke toplam {len(country_matches)} kritik küresel darboğaz ve kriz senaryosuna doğrudan maruz kalmaktadır:\n")
        for s, c in country_matches:
            print(f"⚡ [{s['id']}] {s['title']}")
            print(f"   Boğum: {s.get('chokepoint', '')} | Seviye: {s['severity']}")
            print(f"   Doğrudan Bağımlılık / Risk: %{c['dependency_pct']} — Sektör: {c['sector']}")
            print(f"   Tetikleyici: {s['core_trigger']}")
            mit = s.get('mitigation_corridors', [{}])[0].get('route', 'Yok')
            print(f"   Alternatif Koridor: {mit}\n")
        print("=" * 80)
    else:
        print(f"[-] Eşleşen kriz senaryosu veya etkilenen ülke bulunamadı: '{query}'")

def show_briefing(query: str):
    c = find_country(query)
    if not c:
        print(f"[-] Ülke bulunamadı: '{query}'")
        return

    code = c["code"]
    c_dir = BASE_DIR / c.get("economy_path", c.get("path", f"countries/{c['slug']}"))
    if not c_dir.exists():
        c_dir = BASE_DIR / c.get("path", f"countries/{c['slug']}")

    # 1. Cultural DNA
    c_dna = {}
    if CULTURE_PATH.exists():
        with open(CULTURE_PATH, "r", encoding="utf-8") as f:
            c_dna_list = json.load(f).get("countries_cultural_dna", [])
        c_dna = next((x for x in c_dna_list if x.get("code") == code or x.get("country", "").lower() == c["name"].lower()), {})

    # 2. Power matrix
    matrix = load_matrix()
    pwr = next((x for x in matrix if x.get("code") == code or x.get("slug") == c["slug"]), {})

    # 3. Macroeconomics
    macro = {}
    macro_path = c_dir / "03_official_economy" / "macroeconomics.json"
    if macro_path.exists():
        try:
            with open(macro_path, "r", encoding="utf-8") as f:
                macro = json.load(f)
        except Exception:
            pass

    # 4. Oligarchs
    oligarchs = []
    oligarch_path = c_dir / "04_shadow_power_osint" / "oligarch_network.csv"
    if oligarch_path.exists():
        try:
            with open(oligarch_path, "r", encoding="utf-8") as f:
                oligarchs = list(csv.DictReader(f))
        except Exception:
            pass

    # 5. Alliances & Treaties
    member_alliances = []
    if ALLIANCES_PATH.exists():
        try:
            with open(ALLIANCES_PATH, "r", encoding="utf-8") as f:
                alliances = json.load(f).get("alliances", [])
                for a in alliances:
                    key_mems = a.get("key_members", a.get("members", []))
                    if code in key_mems or c["name"] in key_mems or any(str(m).lower() == code.lower() for m in key_mems):
                        member_alliances.append(f"{a.get('name')} [{a.get('id', '')}]")
        except Exception:
            pass

    # 6. Nuclear Status
    nuclear_info = None
    if NUCLEAR_PATH.exists():
        try:
            with open(NUCLEAR_PATH, "r", encoding="utf-8") as f:
                npowers = json.load(f).get("nuclear_powers", [])
                for n in npowers:
                    if n.get("code") == code or c["name"].lower() in n.get("country", "").lower():
                        nuclear_info = n
                        break
        except Exception:
            pass

    # 7. Intel agency
    intel_agency = None
    intel_data = load_intel()
    for ag in intel_data.get("agencies", []):
        if ag.get("country", "").lower() == c["name"].lower() or ag.get("iso2", "").lower() == code[:2].lower() or code in ag.get("country", ""):
            intel_agency = ag
            break

    # 8. Crisis exposure
    crises = load_crises()
    exposed_crises = []
    for s in crises:
        for vc in s.get("most_vulnerable_countries", []):
            if vc.get("code") == code or c["name"].lower() in vc.get("name", "").lower():
                exposed_crises.append({"scenario_id": s["id"], "title": s["title"], "dependency_pct": vc.get("dependency_pct"), "sector": vc.get("sector")})

    if OUTPUT_JSON:
        briefing_obj = {
            "country": c,
            "cultural_dna": c_dna,
            "power_matrix": pwr,
            "macroeconomics": macro,
            "alliances": member_alliances,
            "nuclear": nuclear_info,
            "intel_agency": intel_agency,
            "oligarchs": oligarchs,
            "crisis_exposures": exposed_crises
        }
        print(json.dumps(briefing_obj, ensure_ascii=False, indent=2))
        return

    # Terminal Dashboard Display
    print("=" * 80)
    print(f"📑 STRATEJİK İSTİHBARAT & MEDENİYET BRİFİNGİ: {c['name'].upper()} ({code})")
    print("=" * 80)
    print(f"🏛️  Devlet Kimliği:      {c['name']} | Başkent: {c['capital']} | Bölge: {c['region']}")
    print(f"👥  Nüfus:               {c['population']:,} Kişi")
    print(f"💰  Ekonomi Büyüklüğü:   GSYİH: ${c['gdp_usd_b']:,.1f} Milyar | Kişi Başı: ${pwr.get('gdp_per_capita_usd', macro.get('gdp_per_capita_usd', 0)):,}")
    print(f"🕵️  Gölge Ekonomi:       %{c['shadow_economy_pct']} | Kırılganlık (CSFI): {pwr.get('fragility_index_csfi', 'N/A')} ({pwr.get('risk_tier', 'Bilinmiyor')})")
    print(f"🏷️  Ekonomik Blok:       {c.get('economy_group_name', 'Orta Gelir Düzeyi')} [{c.get('economy_group_id', '-')}]")
    print("-" * 80)

    print("🎭 KÜLTÜREL DNA VE RUH DOKUSU:")
    crossroads = c_dna.get('civilization_crossroads', c_dna.get('civilization_realm', 'Kayıtlı Havza Bilgisi Bulunmuyor'))
    print(f"   • Medeniyet Havzası:    {crossroads}")
    ethos = c_dna.get('core_cultural_ethos', c_dna.get('core_ethos', 'Bilinmiyor'))
    print(f"   • Temel Karakter & Ruh: {ethos}")
    
    concepts = c_dna.get('untranslatable_soul_concepts', [])
    if concepts and isinstance(concepts, list):
        concepts_formatted = []
        for it in concepts[:3]:
            if isinstance(it, dict):
                w = it.get('word', '')
                m = it.get('meaning', '')
                concepts_formatted.append(f"'{w}': {m}")
            elif isinstance(it, str):
                concepts_formatted.append(it)
        if concepts_formatted:
            print(f"   • Ruh Kavramları:       {'; '.join(concepts_formatted)}")

    rituals = c_dna.get('social_rituals_and_lifestyle')
    if rituals:
        print(f"   • Yaşam & Ritüeller:    {rituals[:180]}...")
    comm = c_dna.get('communication_style')
    if comm:
        print(f"   • İletişim Karakteri:   {comm}")
    taboos = c_dna.get('social_taboos_and_etiquette')
    if taboos:
        print(f"   • Tabular & Görgü:      {taboos[:180]}...")
    print("-" * 80)

    print("🛡️ SAVUNMA, İTTİFAK VE İSTİHBARAT MİMARİSİ:")
    alliances_str = ", ".join(member_alliances) if member_alliances else "Bağımsız / Bağlantısız"
    print(f"   • Savunma Paktları:     {alliances_str}")
    if nuclear_info:
        print(f"   • Nükleer Statü:        ☢️ AKTİF NÜKLEER GÜÇ ({nuclear_info.get('total_warheads', 0)} Savaş Başlığı, Triad: {nuclear_info.get('triad_status', 'Yok')})")
    else:
        print("   • Nükleer Statü:        Nükleer Silahı Bulunmayan Devlet (NPT Rejimi)")
    if intel_agency:
        p_for = intel_agency.get('primary_foreign', '')
        p_sig = intel_agency.get('primary_signals', '')
        bgt = intel_agency.get('estimated_annual_budget_usd', '')
        print(f"   • Dış İstihbarat:       {p_for}")
        if p_sig:
            print(f"   • Sinyal/SIGINT:        {p_sig}")
        if bgt:
            print(f"   • Tahmini Bütçe:        ${bgt}")
    print("-" * 80)

    print("👑 OLİGARKİ VE İKTİDAR SERMAYESİ:")
    if oligarchs:
        for idx, o in enumerate(oligarchs[:4], 1):
            wealth = f" (${o.get('estimated_wealth_usd_m')}M)" if o.get('estimated_wealth_usd_m') != "0" else ""
            print(f"   {idx}. {o.get('person_or_entity')}{wealth} | Rol: {o.get('role_or_title')} | Sektör: {o.get('connected_sector')}")
        if len(oligarchs) > 4:
            print(f"   ... ve {len(oligarchs)-4} diğer kilit güç odağı (detay: xray_cli.py graph {c['slug']})")
    else:
        print("   *(Doğrudan kayıtlı oligark ağı verisi bulunamadı)*")
    print("-" * 80)

    print("⚡ JEOPOLİTİK KRİZ & BOĞUM NOKTASI MARUZİYETİ:")
    if exposed_crises:
        for ec in exposed_crises:
            print(f"   ⚠️ [{ec['scenario_id']}] {ec['title']}")
            print(f"      Bağımlılık Oranı: %{ec['dependency_pct']} — Kritik Sektör: {ec['sector']}")
    else:
        print("   ✅ Doğrudan küresel kriz senaryolarında yüksek tekil kırılganlık tespit edilmedi.")
    print("=" * 80)

def show_civilization_matrix(realm_query=None):
    if not CULTURE_PATH.exists():
        print("[-] Kültür veri seti bulunamadı!")
        return

    with open(CULTURE_PATH, "r", encoding="utf-8") as f:
        cdata = json.load(f)

    realms = cdata.get("civilization_realms", [])
    dnas = cdata.get("countries_cultural_dna", [])
    registry = load_registry()
    countries_by_code = {c["code"]: c for c in registry}

    aggregated = []
    for r in realms:
        rid = r.get("id")
        rname = r.get("name")
        rep_states = r.get("representative_states", [])
        
        # Match countries
        c_objs = []
        for c in registry:
            if c["name"] in rep_states or any(rs.lower() in c["name"].lower() for rs in rep_states):
                c_objs.append(c)

        pop = sum(c.get("population", 0) for c in c_objs)
        gdp = sum(c.get("gdp_usd_b", 0) for c in c_objs)
        avg_sh = sum(c.get("shadow_economy_pct", 0) for c in c_objs) / len(c_objs) if c_objs else 0

        aggregated.append({
            "id": rid,
            "name": rname,
            "core_philosophy": r.get("core_philosophy", ""),
            "representative_states": rep_states,
            "matched_country_count": len(c_objs),
            "sample_population": pop,
            "sample_gdp_usd_b": round(gdp, 1),
            "avg_shadow_economy_pct": round(avg_sh, 1)
        })

    if OUTPUT_JSON:
        if realm_query:
            rq = realm_query.lower()
            filtered = [x for x in aggregated if rq in x["id"].lower() or rq in x["name"].lower()]
            print(json.dumps(filtered, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(aggregated, ensure_ascii=False, indent=2))
        return

    print("=" * 88)
    print("🏛️  MEDENİYET ATLASI - 9 KÜRESEL MEDENİYET HAVZASI & FELSEFİ ÖZET")
    print("=" * 88)
    print(f"{'Medeniyet Havzası':<35} | {'Örnek Devletler':<35} | {'Ort. Gölge'}")
    print("-" * 88)
    for a in aggregated:
        if realm_query and (realm_query.lower() not in a["id"].lower() and realm_query.lower() not in a["name"].lower()):
            continue
        states_str = ", ".join(a['representative_states'][:4])
        sh_str = f"%{a['avg_shadow_economy_pct']:.1f}" if a['avg_shadow_economy_pct'] > 0 else "-"
        print(f"{a['name'][:34]:<35} | {states_str[:34]:<35} | {sh_str}")
        print(f"  └─ Felsefe: {a['core_philosophy'][:100]}...\n")
    print("=" * 88)
    print("💡 Detay için: python scripts/xray_cli.py culture <ulke_veya_havza>")

def show_currency(query=None):
    data = load_currency()
    if not data:
        print("[-] Para birimleri ve de-dolarizasyon veri seti bulunamadı!")
        return

    if OUTPUT_JSON:
        if query:
            q = query.lower().strip()
            res = {
                "currencies": [c for c in data.get("global_reserve_currencies", []) if q in c["code"].lower() or q in c["currency"].lower()],
                "networks": [n for n in data.get("alternative_clearing_networks", []) if q in n["id"].lower() or q in n["name"].lower()],
                "gold_buyers": [g for g in data.get("top_central_bank_gold_buyers_metric_tons", []) if q in g["country"].lower() or q in g["code"].lower()],
                "treasury_holders": [t for t in data.get("top_us_treasury_holders_usd_b", []) if q in t["country"].lower() or q in t["code"].lower()]
            }
            print(json.dumps(res, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    if not query:
        print("=" * 88)
        print("💱 MEDENİYET ATLASI - KÜRESEL REZERV PARA BİRİMLERİ & HEGEMONYA")
        print("=" * 88)
        print(f"{'Kod':<6} | {'Para Birimi':<30} | {'Rezerv Payı':<12} | {'SWIFT Payı':<12} | {'Hegemonya Sütunu'}")
        print("-" * 88)
        for c in data.get("global_reserve_currencies", []):
            print(f"{c['code']:<6} | {c['currency'][:28]:<30} | %{c['fx_reserves_share_pct']:<11.1f} | %{c['swift_payment_share_pct']:<11.1f} | {c['hegemonic_pillar'][:45]}...")
        print("\n🌐 ALTERNATİF SINIR ÖTESİ TAKAS VE MESAJLAŞMA AĞLARI (DE-DOLARİZASYON):")
        print(f"{'Ağ ID':<12} | {'Öncü Devlet / Çatı':<28} | {'Katılımcı':<12} | {'Yıllık Hacim'}")
        print("-" * 88)
        for n in data.get("alternative_clearing_networks", []):
            print(f"{n['id']:<12} | {n['lead_country'][:27]:<28} | {n['participant_banks']} Banka    | ${n['annual_transaction_volume_trillion_usd']}T")

        print("\n🥇 EN ÇOK ALTIN REZERVİ BİRİKTİREN MERKEZ BANKALARI:")
        for g in data.get("top_central_bank_gold_buyers_metric_tons", []):
            print(f"  • {g['country']:<20}: {g['total_gold_tonnage']} Ton (Rezervlerin %{g['pct_of_total_reserves']}'i) | Yıllık Alım: +{g['recent_annual_purchases_tons']} Ton")
        print("=" * 88)
        print("💡 Detay için: python scripts/xray_cli.py currency <usd|cny|gold|cips|mbridge>")
        return

    q = query.lower().strip()
    matched_curr = next((c for c in data.get("global_reserve_currencies", []) if q == c["code"].lower() or q in c["currency"].lower()), None)
    if matched_curr:
        c = matched_curr
        print("=" * 80)
        print(f"💵 REZERV PARA DETAYI: {c['currency'].upper()}")
        print("=" * 80)
        print(f"• İhraç Eden:          {c['issuing_entity']}")
        print(f"• Küresel Rezerv Payı:  %{c['fx_reserves_share_pct']}")
        print(f"• SWIFT İşlem Payı:    %{c['swift_payment_share_pct']}")
        print(f"• Hegemonik Dayanak:   {c['hegemonic_pillar']}")
        print(f"• Yapısal Riskler:     {c['vulnerability_points']}")
        print("=" * 80)
        return

    matched_net = next((n for n in data.get("alternative_clearing_networks", []) if q == n["id"].lower() or q in n["name"].lower()), None)
    if matched_net:
        n = matched_net
        print("=" * 80)
        print(f"🌐 ALTERNATİF TAKAS AĞI: {n['name'].upper()}")
        print("=" * 80)
        print(f"• Kod:                 {n['id']}")
        print(f"• Öncü Ülke / Çatı:    {n['lead_country']}")
        print(f"• Merkez:              {n['headquarters']}")
        print(f"• Üye / Katılımcı:     {n['participant_banks']} Banka ({n['direct_countries']} Ülke)")
        print(f"• Yıllık İşlem Hacmi:  ${n['annual_transaction_volume_trillion_usd']} Trilyon")
        print(f"• Stratejik Misyon:    {n['purpose']}")
        print("=" * 80)
        return

    print(f"[-] Eşleşen para birimi veya takas ağı bulunamadı: '{query}'")

def show_cyber(query=None):
    data = load_cyber()
    if not data:
        print("[-] Siber ve bilişsel harp veri seti bulunamadı!")
        return

    if OUTPUT_JSON:
        if query:
            q = query.lower().strip()
            res = {
                "apt_units": [a for a in data.get("apt_units", []) if q in a["id"].lower() or q in a["alias"].lower() or q in a["sponsoring_state"].lower()],
                "spyware_cartel": [s for s in data.get("commercial_spyware_cartel", []) if q in s["vendor"].lower() or q in s["flagship_spyware"].lower() or q in s["country"].lower()]
            }
            print(json.dumps(res, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    if not query:
        print("=" * 90)
        print("🛰️ MEDENİYET ATLASI - DEVLET DESTEKLİ SİBER HARP BİRLİKLERİ (APT) & CASUS YAZILIMLAR")
        print("=" * 90)
        print(f"{'Grup ID':<16} | {'Yaygın Takma Ad':<28} | {'Bağlı Devlet':<20} | {'Teşkilat'}")
        print("-" * 90)
        for a in data.get("apt_units", []):
            print(f"{a['id']:<16} | {a['alias'][:26]:<28} | {a['sponsoring_state'][:19]:<20} | {a['affiliated_agency'][:22]}")

        print("\n🕵️ TİCARİ CASUS YAZILIM TRÖSTLERİ (COMMERCIAL SURVEILLANCE VENDORS):")
        print(f"{'Üretici Şirket':<26} | {'Casus Yazılım':<18} | {'Menşe Ülke':<20} | {'Saldırı Vektörü'}")
        print("-" * 90)
        for s in data.get("commercial_spyware_cartel", []):
            print(f"{s['vendor'][:24]:<26} | {s['flagship_spyware']:<18} | {s['country'][:18]:<20} | {s['infection_vector'][:22]}")
        print("=" * 90)
        print("💡 Detay için: python scripts/xray_cli.py cyber <apt28|lazarus|pegasus|predator>")
        return

    q = query.lower().strip()
    matched_apt = next((a for a in data.get("apt_units", []) if q == a["id"].lower() or q in a["alias"].lower() or q in a["sponsoring_state"].lower()), None)
    if matched_apt:
        a = matched_apt
        print("=" * 80)
        print(f"👾 DEVLET DESTEKLİ SİBER TEHDİT GRUBU: {a['id']} ({a['alias']})")
        print("=" * 80)
        print(f"• Destekleyen Devlet:    {a['sponsoring_state']}")
        print(f"• Bağlı Teşkilat:        {a['affiliated_agency']}")
        print(f"• Hedef Sektörler:       {a['target_sectors']}")
        print(f"• İmzalı Siber Silahlar: {', '.join(a['signature_tools'])}")
        print("\n🎯 Bilinen Büyük Siber Operasyonlar:")
        for op in a.get("notable_operations", []):
            print(f"  • {op}")
        print("=" * 80)
        return

    matched_spy = next((s for s in data.get("commercial_spyware_cartel", []) if q in s["vendor"].lower() or q in s["flagship_spyware"].lower() or q in s["country"].lower()), None)
    if matched_spy:
        s = matched_spy
        print("=" * 80)
        print(f"📱 TİCARİ CASUS YAZILIM: {s['flagship_spyware'].upper()} ({s['vendor']})")
        print("=" * 80)
        print(f"• Menşe Ülke:         {s['country']}")
        print(f"• Bulaşma Vektörü:    {s['infection_vector']}")
        print(f"• İstihbarat Gücü:    {s['capabilities']}")
        print(f"• Hukuki/OFAC Durumu: {s['legal_sanctions']}")
        print("=" * 80)
        return

    print(f"[-] Eşleşen siber grup veya casus yazılım bulunamadı: '{query}'")

def show_audit(query: str):
    c = find_country(query)
    if not c:
        print(f"[-] Ülke bulunamadı: '{query}'")
        return

    code = c["code"]
    c_dir = BASE_DIR / c.get("economy_path", c.get("path", f"countries/{c['slug']}"))
    if not c_dir.exists():
        c_dir = BASE_DIR / c.get("path", f"countries/{c['slug']}")

    # Power matrix
    pwr = next((x for x in load_matrix() if x.get("code") == code or x.get("slug") == c["slug"]), {})
    # Macro
    macro = {}
    macro_path = c_dir / "03_official_economy" / "macroeconomics.json"
    if macro_path.exists():
        try:
            with open(macro_path, "r", encoding="utf-8") as f:
                macro = json.load(f)
        except Exception:
            pass

    # Press freedom
    press_score = c.get("press_score", "N/A")
    # US Treasury holding
    curr_data = load_currency()
    treasury_entry = next((t for t in curr_data.get("top_us_treasury_holders_usd_b", []) if t.get("code") == code or t.get("country", "").lower() == c["name"].lower()), None)
    gold_entry = next((g for g in curr_data.get("top_central_bank_gold_buyers_metric_tons", []) if g.get("code") == code or c["name"].lower() in g.get("country", "").lower()), None)

    # Chokepoints
    choke_data = []
    if CHOKE_PATH.exists():
        try:
            with open(CHOKE_PATH, "r", encoding="utf-8") as f:
                chokes = json.load(f).get("chokepoints", [])
                for ch in chokes:
                    deps = ch.get("dependent_countries", [])
                    ctrl = ch.get("controlling_states", [])
                    if code in deps or c["name"] in deps or code in ctrl or c["name"] in ctrl:
                        choke_data.append(ch.get("name"))
        except Exception:
            pass

    # Crisis exposure
    crises = load_crises()
    exposed_crises = []
    for s in crises:
        for vc in s.get("most_vulnerable_countries", []):
            if vc.get("code") == code or c["name"].lower() in vc.get("name", "").lower():
                exposed_crises.append(f"{s['title']} (%{vc.get('dependency_pct')})")

    # Cyber / APT alignment
    cyber_data = load_cyber()
    state_apts = [a["alias"] for a in cyber_data.get("apt_units", []) if c["name"].lower() in a.get("sponsoring_state", "").lower()]

    if OUTPUT_JSON:
        audit_payload = {
            "country": c,
            "csfi_fragility": pwr.get("fragility_index_csfi"),
            "risk_tier": pwr.get("risk_tier"),
            "shadow_economy_pct": c["shadow_economy_pct"],
            "press_freedom_score": press_score,
            "us_treasury_holdings_usd_b": treasury_entry.get("holdings_usd_b") if treasury_entry else None,
            "gold_reserves_tonnage": gold_entry.get("total_gold_tonnage") if gold_entry else None,
            "chokepoints_exposure": choke_data,
            "crisis_vulnerabilities": exposed_crises,
            "state_cyber_units": state_apts
        }
        print(json.dumps(audit_payload, ensure_ascii=False, indent=2))
        return

    print("=" * 80)
    print(f"🔍 360° STRATEJİK & ADLİ EGEMENLİK DENETİMİ (AUDIT): {c['name'].upper()} ({code})")
    print("=" * 80)
    print(f"📊 Kırılganlık Derecesi (CSFI):    {pwr.get('fragility_index_csfi', 'N/A')} ({pwr.get('risk_tier', 'Belirsiz')})")
    print(f"🕵️ Gölge Ekonomi & Kleptokrasi:    %{c['shadow_economy_pct']} (Kayıt dışı sermaye risk düzeyi)")
    print(f"📡 Basın & Sansür Skoru:          {press_score}/100")
    if treasury_entry:
        print(f"💵 ABD Hazine Tahvili Rezervi:     ${treasury_entry['holdings_usd_b']} Milyar (Küresel pay: %{treasury_entry['share_pct']})")
    if gold_entry:
        print(f"🥇 Parasal Altın Rezervleri:       {gold_entry['total_gold_tonnage']} Ton (Toplam rezervin %{gold_entry['pct_of_total_reserves']}'si)")
    print(f"🚢 Kritik Deniz Darboğazları:      {', '.join(choke_data) if choke_data else 'Doğrudan bağımlılık tespit edilmedi'}")
    print(f"⚡ Maruz Kalınan Kriz Senaryoları: {', '.join(exposed_crises) if exposed_crises else 'Doğrudan tekil kriz maruziyeti yok'}")
    print(f"👾 Milli Siber Harp Güçleri:       {', '.join(state_apts) if state_apts else 'Doğrudan kayıtlı APT birimi bulunmuyor'}")
    print("=" * 80)

def show_stats():
    registry = load_registry()
    total_gdp = sum(c.get("gdp_usd_b", 0) for c in registry)
    total_pop = sum(c.get("population", 0) for c in registry)
    avg_shadow = sum(c.get("shadow_economy_pct", 0) for c in registry) / len(registry)
    
    images_dir = BASE_DIR / "assets" / "images"
    image_count = len(list(images_dir.glob("*.jpg"))) if images_dir.exists() else 0
    dossiers_count = len(list(DOSSIERS_DIR.glob("CASE_STUDY_*.md"))) if DOSSIERS_DIR.exists() else 0
    research_count = len([f for f in RESEARCH_DIR.glob("*.md") if f.name != "README.md"]) if RESEARCH_DIR.exists() else 0
    geo_dir = BASE_DIR / "geopolitics_and_intelligence"
    geo_count = len([f for f in geo_dir.glob("*.md") if f.name != "README.md"]) if geo_dir.exists() else 0
    culture_dir = BASE_DIR / "culture"
    culture_count = len([f for f in culture_dir.glob("*.md") if f.name != "README.md"]) if culture_dir.exists() else 0

    if OUTPUT_JSON:
        stats_dict = {
            "country_count": len(registry),
            "total_population": total_pop,
            "total_gdp_usd_b": round(total_gdp, 2),
            "average_shadow_economy_pct": round(avg_shadow, 2),
            "artwork_images_count": image_count,
            "forensic_case_studies_count": dossiers_count,
            "research_theses_count": research_count,
            "geopolitics_dossiers_count": geo_count,
            "culture_dossiers_count": culture_count,
            "economic_blocks_count": 8
        }
        print(json.dumps(stats_dict, ensure_ascii=False, indent=2))
        return

    print("=" * 65)
    print("🌐 MEDENİYET ATLASI - SİSTEM VE VERİ TABANI İSTATİSTİKLERİ")
    print("=" * 65)
    print(f"• Kayıtlı Toplam Varlık Sayısı:     {len(registry)} Ülke & Bölge")
    print(f"• Toplam Dünya Nüfusu:              {total_pop:,}")
    print(f"• Toplam Dünya GSYH'si:             ${total_gdp:,.1f} Milyar (~${total_gdp/1000:.1f} Trilyon)")
    print(f"• Ortalama Gölge Ekonomi Oranı:     %{avg_shadow:.2f}")
    print(f"• Yüksek Çözünürlüklü İllüstrasyon: {image_count} Tematik Eser")
    print(f"• Kültür Kütüphanesi Raporları:     {culture_count} İhtisas Dosyası")
    print(f"• Jeopolitik & Güç Raporları:       {geo_count} Stratejik Rapor")
    print(f"• Adli Vaka OSINT İncelemeleri:     {dossiers_count} Soruşturma Dosyası")
    print(f"• Doktrin & Araştırma Tezleri:      {research_count} Akademik Tez")
    print("=" * 65)

def show_economy_groups(query=None):
    registry = load_registry()
    groups = {}
    for c in registry:
        gid = c.get("economy_group_id", "06_orta_gelir_ve_ureticiler")
        gname = c.get("economy_group_name", "Orta Gelir Düzeyi ve Bölgesel Üreticiler")
        if gid not in groups:
            groups[gid] = {"name": gname, "countries": []}
        groups[gid]["countries"].append(c)

    if query:
        q = query.lower()
        matched_groups = {k: v for k, v in groups.items() if q in k.lower() or q in v["name"].lower()}
        if not matched_groups:
            print(f"[-] Eşleşen ekonomik blok bulunamadı: '{query}'")
            return
        groups = matched_groups

    print("=" * 70)
    print("📊 MEDENİYET ATLASI - EKONOMİK ARKETİPLER VE GÜÇ BLOKLARI")
    print("=" * 70)
    for gid, data in sorted(groups.items()):
        total_gdp = sum(c.get("gdp_usd_b", 0) for c in data["countries"])
        avg_sh = sum(c.get("shadow_economy_pct", 0) for c in data["countries"]) / len(data["countries"])
        print(f"\n🏛️ [{gid}] {data['name']}")
        print(f"   Kapsam: {len(data['countries'])} Ülke | Toplam GSYİH: ${total_gdp:,.1f}B | Ort. Gölge: %{avg_sh:.1f}")
        c_names = [f"{c['name']} ({c['code']})" for c in sorted(data["countries"], key=lambda x: x["name"])]
        print(f"   Üyeler: {', '.join(c_names)}")
    print("=" * 70)

def dispatch_command(args):
    global OUTPUT_JSON
    if not args:
        print(__doc__)
        return

    clean_args = []
    for a in args:
        if a.lower() == "--json":
            OUTPUT_JSON = True
        else:
            clean_args.append(a)
    args = clean_args

    if not args:
        print(__doc__)
        return

    cmd = args[0].lower()

    if cmd in ["interactive", "shell", "kabuk"]:
        interactive_shell()
    elif cmd in ["country", "ulke", "c"] and len(args) > 1:
        show_country(" ".join(args[1:]))
    elif cmd in ["graph", "ag", "sema", "mermaid"] and len(args) > 1:
        from network_graph_gen import generate_mermaid_network, find_country_csv
        csv_p, c_name = find_country_csv(" ".join(args[1:]))
        if csv_p:
            if OUTPUT_JSON:
                with open(csv_p, "r", encoding="utf-8") as f:
                    print(json.dumps(list(csv.DictReader(f)), ensure_ascii=False, indent=2))
            else:
                print(f"📊 {c_name} Oligark & Siyaset Güç Ağı (Mermaid Grafiği):\n")
                print(generate_mermaid_network(csv_p, c_name))
        else:
            print(f"[-] Ülke veya ağ dosyası bulunamadı: {' '.join(args[1:])}")
    elif cmd in ["culture", "kultur", "medeniyet", "kod"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_culture(q)
    elif cmd in ["compare-culture", "kultur-karsilas", "karsilas-kultur"] and len(args) > 2:
        compare_culture(args[1], args[2])
    elif cmd in ["epics", "destanlar", "destan", "mitoloji"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_epics(q)
    elif cmd in ["architecture", "mimari", "mimar"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_architecture(q)
    elif cmd in ["music", "muzik", "calgi", "enstruman"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_music(q)
    elif cmd in ["festivals", "festivaller", "bayramlar", "rituel"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_festivals(q)
    elif cmd in ["compare", "karsilas", "vs"] and len(args) > 2:
        compare_countries(args[1], args[2])
    elif cmd in ["search", "ara", "s"] and len(args) > 1:
        search_term(" ".join(args[1:]))
    elif cmd in ["economy", "ekonomik", "eko"]:
        q = args[1] if len(args) > 1 else None
        show_economy_groups(q)
    elif cmd in ["top-shadow", "golge"]:
        limit = int(args[1]) if len(args) > 1 else 15
        top_shadow(limit)
    elif cmd in ["top-gdp", "ekonomi"]:
        limit = int(args[1]) if len(args) > 1 else 15
        top_gdp(limit)
    elif cmd in ["intel", "istihbarat"]:
        q = args[1] if len(args) > 1 else None
        show_intel(q)
    elif cmd in ["pmc", "parali-asker"]:
        q = args[1] if len(args) > 1 else None
        show_pmcs(q)
    elif cmd in ["chokepoints", "bogaz", "bogazlar"]:
        q = args[1] if len(args) > 1 else None
        show_chokepoints(q)
    elif cmd in ["cases", "vaka", "dossiers"]:
        show_case_studies()
    elif cmd in ["research", "arastirma", "tez"]:
        q = args[1] if len(args) > 1 else None
        show_research(q)
    elif cmd in ["swf", "fon", "varlik-fonu"]:
        q = args[1] if len(args) > 1 else None
        show_swfs(q)
    elif cmd in ["darkfleet", "tanker", "golge-filo"]:
        q = args[1] if len(args) > 1 else None
        show_darkfleet(q)
    elif cmd in ["nuclear", "nukleer"]:
        q = args[1] if len(args) > 1 else None
        show_nuclear(q)
    elif cmd in ["armstrade", "silah", "savunma"]:
        q = args[1] if len(args) > 1 else None
        show_armstrade(q)
    elif cmd in ["recon", "kesif", "dossier"] and len(args) > 1:
        from deep_recon import run_deep_recon
        run_deep_recon(" ".join(args[1:]))
    elif cmd in ["alliances", "ittifak", "pakt"]:
        q = args[1] if len(args) > 1 else None
        show_alliances(q)
    elif cmd in ["sanctions", "yaptirim", "ambargo"]:
        q = args[1] if len(args) > 1 else None
        show_sanctions(q)
    elif cmd in ["minerals", "maden", "hammadde"]:
        q = args[1] if len(args) > 1 else None
        show_minerals(q)
    elif cmd in ["cables", "kablo", "sigint"]:
        q = args[1] if len(args) > 1 else None
        show_cables(q)
    elif cmd in ["stats", "istatistik"]:
        show_stats()
    elif cmd in ["list", "liste"]:
        reg = load_registry()
        print(f"📋 Toplam {len(reg)} Ülke Kayıtlı:")
        for c in reg:
            print(f"  • {c['name']:<25} ({c['code']}) - {c['region']}")
    elif cmd in ["rank", "siralama", "guc-siralamasi"]:
        q = args[1] if len(args) > 1 else None
        lim = 20
        if len(args) > 2:
            try:
                lim = int(args[2])
            except ValueError:
                pass
        elif len(args) > 1 and args[1].isdigit():
            lim = int(args[1])
            q = None
        show_rank(q, limit=lim)
    elif cmd in ["briefing", "brifing", "rapor"] and len(args) > 1:
        show_briefing(" ".join(args[1:]))
    elif cmd in ["crisis-sim", "sim", "kriz", "kriz-sim"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_crisis_sim(q)
    elif cmd in ["currency", "para", "dedollar", "rezerv"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_currency(q)
    elif cmd in ["cyber", "siber", "apt", "casus"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_cyber(q)
    elif cmd in ["audit", "denetim"] and len(args) > 1:
        show_audit(" ".join(args[1:]))
    elif cmd in ["matrix", "civilization-matrix", "realms", "havzalar", "medeniyet-matrisi"]:
        q = " ".join(args[1:]) if len(args) > 1 else None
        show_civilization_matrix(q)
    elif cmd in ["export", "disa-aktar"] and len(args) > 1:
        country_q = args[1]
        fmt = "md"
        out_f = None
        idx = 2
        while idx < len(args):
            if args[idx] in ["--format", "-f"] and idx + 1 < len(args):
                fmt = args[idx + 1].lower()
                idx += 2
            elif args[idx] in ["--out", "-o"] and idx + 1 < len(args):
                out_f = args[idx + 1]
                idx += 2
            else:
                idx += 1
        export_country_dossier(country_q, fmt=fmt, output_file=out_f)
    elif cmd in ["help", "--help", "-h", "yardim", "?"]:
        print(__doc__)
    else:
        show_country(cmd)

def interactive_shell():
    print("=" * 80)
    print("🏛️  MEDENİYET ATLASI - İNTERAKTİF KOMUT SATIRI KABUĞU (SHELL)")
    print("   Ülkeleri, kültürleri, destanları ve güç dinamiklerini canlı sorgulayın.")
    print("   Örnekler: 'briefing turkiye', 'crisis-sim hormuz_blockade', 'matrix', 'epics'")
    print("   Çıkmak için: 'exit', 'quit' veya 'q' yazabilirsiniz.")
    print("=" * 80)
    while True:
        try:
            line = input("\n[Medeniyet-Atlasi] > ").strip()
            if not line:
                continue
            if line.lower() in ["exit", "quit", "q", "cikis"]:
                print("İyi günler!")
                break
            parts = line.split()
            dispatch_command(parts)
        except (KeyboardInterrupt, EOFError):
            print("\nÇıkış yapıldı.")
            break

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    dispatch_command(sys.argv[1:])

if __name__ == "__main__":
    main()