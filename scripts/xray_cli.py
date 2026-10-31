#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/xray_cli.py
Küresel Röntgen (Global X-Ray) - Komut Satırı İstihbarat & Analiz Terminali

Kullanım:
  python scripts/xray_cli.py country <ulke_adi_veya_kodu>
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
  python scripts/xray_cli.py cases
  python scripts/xray_cli.py list [bolge]
  python scripts/xray_cli.py stats
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
DOSSIERS_DIR = BASE_DIR / "dossiers"

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
    for f in files:
        print(f"  • {f.name:<45} -> dossiers/{f.name}")
    print("=" * 80)

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
    print("📊 KÜRESEL RÖNTGEN - EKONOMİK ARKETİPLER VE GÜÇ BLOKLARI")
    print("=" * 70)
    for gid, data in sorted(groups.items()):
        total_gdp = sum(c.get("gdp_usd_b", 0) for c in data["countries"])
        avg_sh = sum(c.get("shadow_economy_pct", 0) for c in data["countries"]) / len(data["countries"])
        print(f"\n🏛️ [{gid}] {data['name']}")
        print(f"   Kapsam: {len(data['countries'])} Ülke | Toplam GSYİH: ${total_gdp:,.1f}B | Ort. Gölge: %{avg_sh:.1f}")
        c_names = [f"{c['name']} ({c['code']})" for c in sorted(data["countries"], key=lambda x: x["name"])]
        print(f"   Üyeler: {', '.join(c_names)}")
    print("=" * 70)

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
    elif cmd in ["economy", "ekonomik", "eko"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_economy_groups(q)
    elif cmd in ["top-shadow", "golge"]:
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 15
        top_shadow(limit)
    elif cmd in ["top-gdp", "ekonomi"]:
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 15
        top_gdp(limit)
    elif cmd in ["intel", "istihbarat"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_intel(q)
    elif cmd in ["pmc", "parali-asker"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_pmcs(q)
    elif cmd in ["chokepoints", "bogaz", "bogazlar"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_chokepoints(q)
    elif cmd in ["cases", "vaka", "dossiers"]:
        show_case_studies()
    elif cmd in ["alliances", "ittifak", "pakt"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_alliances(q)
    elif cmd in ["sanctions", "yaptirim", "ambargo"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_sanctions(q)
    elif cmd in ["minerals", "maden", "hammadde"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_minerals(q)
    elif cmd in ["cables", "kablo", "sigint"]:
        q = sys.argv[2] if len(sys.argv) > 2 else None
        show_cables(q)
    elif cmd in ["stats", "istatistik"]:
        show_stats()
    elif cmd in ["list", "liste"]:
        reg = load_registry()
        print(f"📋 Toplam {len(reg)} Ülke Kayıtlı:")
        for c in reg:
            print(f"  • {c['name']:<25} ({c['code']}) - {c['region']}")
    else:
        show_country(cmd)

if __name__ == "__main__":
    main()
