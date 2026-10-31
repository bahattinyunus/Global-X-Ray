#!/usr/bin/env python3
"""
scripts/xray_cli.py
Küresel Röntgen (Global X-Ray) - Komut Satırı İstihbarat & Analiz Terminali
Kullanım:
  python scripts/xray_cli.py country <ulke_adi_veya_kodu>
  python scripts/xray_cli.py compare <ulke_1> <ulke_2>
  python scripts/xray_cli.py graph <ulke_adi>
  python scripts/xray_cli.py stats
  python scripts/xray_cli.py search <terim>
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

def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def find_country(query: str):
    registry = load_registry()
    q = query.lower().strip()
    for c in registry:
        if c["slug"] == q or c["name"].lower() == q or c["code"].lower() == q:
            return c
    # Kısmi eşleşme
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
    readme_path = c_dir / "README.md"
    macro_path = c_dir / "03_official_economy" / "macroeconomics.json"
    shadow_path = c_dir / "04_shadow_power_osint" / "real_power_dynamics.md"
    oligarch_path = c_dir / "04_shadow_power_osint" / "oligarch_network.csv"

    print("=" * 70)
    print(f"🌍 KÜRESEL RÖNTGEN RAPORU: {c['name'].upper()} ({c['code']})")
    print("=" * 70)
    print(f"• Bölge: {c['region'].replace('_', ' ').title()}")
    print(f"• Başkent: {c['capital']}")
    print(f"• Nüfus: {c['population']:,}")
    print(f"• Nominal GSYH: ${c['gdp_usd_b']:.1f} Milyar")
    print(f"• Gölge / Kayıt Dışı Ekonomi: %{c['shadow_economy_pct']}")
    print("-" * 70)

    if macro_path.exists():
        with open(macro_path, "r", encoding="utf-8") as f:
            m = json.load(f)
            print("📊 EKONOMİ VE TİCARET:")
            print(f"  Para Birimi: {m.get('currency')}")
            print(f"  Kişi Başı Gelir: ${m.get('gdp_per_capita_usd'):,}")
            print(f"  Enflasyon: %{m.get('inflation_rate_pct')}")
            print(f"  Ana İhracat: {', '.join(m.get('top_exports', []))}")
            print(f"  Ticaret Ortakları: {', '.join(m.get('major_trading_partners', []))}")
        print("-" * 70)

    if oligarch_path.exists():
        print("🕶️ OLİGARK & GÜÇ AĞI:")
        with open(oligarch_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                wealth = f" (${row.get('estimated_wealth_usd_m')}M)" if row.get('estimated_wealth_usd_m') != "0" else ""
                print(f"  • {row.get('person_or_entity')} {wealth}")
                print(f"    Rol: {row.get('role_or_title')} | Sektör: {row.get('connected_sector')}")
                print(f"    Siyasi Bağ: {row.get('political_connection')}")
        print("-" * 70)

    print(f"[!] Detaylı inceleme için: {c['slug']}/ (Kök Dizin)")

def compare_countries(q1: str, q2: str):
    c1 = find_country(q1)
    c2 = find_country(q2)
    if not c1 or not c2:
        print(f"[-] Ülkelerden biri veya ikisi bulunamadı ({q1}, {q2})")
        return

    print("=" * 75)
    print(f"⚖️ JEOPOLİTİK KARŞILAŞTIRMA: {c1['name'].upper()} vs {c2['name'].upper()}")
    print("=" * 75)
    header = f"{'Metrik':<28} | {c1['name'][:20]:<20} | {c2['name'][:20]:<20}"
    print(header)
    print("-" * 75)
    print(f"{'Bölge':<28} | {c1['region']:<20} | {c2['region']:<20}")
    print(f"{'Başkent':<28} | {c1['capital']:<20} | {c2['capital']:<20}")
    pop1 = f"{c1['population']:,}"
    pop2 = f"{c2['population']:,}"
    gdp1 = f"${c1['gdp_usd_b']:.1f}B"
    gdp2 = f"${c2['gdp_usd_b']:.1f}B"
    sh1 = f"%{c1['shadow_economy_pct']}"
    sh2 = f"%{c2['shadow_economy_pct']}"
    print(f"{'Nüfus':<28} | {pop1:<20} | {pop2:<20}")
    print(f"{'Nominal GSYH (Milyar $)':<28} | {gdp1:<20} | {gdp2:<20}")
    print(f"{'Gölge Ekonomi Oranı (%)':<28} | {sh1:<20} | {sh2:<20}")
    print("=" * 75)

def show_stats():
    registry = load_registry()
    total_pop = sum(c["population"] for c in registry)
    total_gdp = sum(c["gdp_usd_b"] for c in registry)
    avg_shadow = sum(c["shadow_economy_pct"] for c in registry) / len(registry)
    
    # En yüksek gölge ekonomi
    highest_shadow = sorted(registry, key=lambda x: x["shadow_economy_pct"], reverse=True)[:5]
    # En büyük ekonomiler
    top_gdp = sorted(registry, key=lambda x: x["gdp_usd_b"], reverse=True)[:5]

    print("=" * 70)
    print("🌐 KÜRESEL RÖNTGEN DÜNYA İSTATİSTİKLERİ")
    print("=" * 70)
    print(f"• Kayıtlı Ülke Sayısı: {len(registry)}")
    print(f"• Haritalanan Dünya Nüfusu: {total_pop:,}")
    print(f"• Küresel Nominal GSYH: ${total_gdp:,.1f} Milyar")
    print(f"• Dünya Ortalama Gölge Ekonomi: %{avg_shadow:.1f}")
    print("-" * 70)
    print("🔥 En Yüksek Tahmini Gölge / Kayıt Dışı Ekonomi Oranları:")
    for i, c in enumerate(highest_shadow, 1):
        print(f"  {i}. {c['name']} ({c['region']}): %{c['shadow_economy_pct']}")
    print("-" * 70)
    print("💰 Dünyanın En Büyük 5 Ekonomisi:")
    for i, c in enumerate(top_gdp, 1):
        print(f"  {i}. {c['name']}: ${c['gdp_usd_b']:,.1f} Milyar")
    print("=" * 70)

def search_text(term: str):
    t = term.lower()
    matches = []
    for path in (BASE_DIR / "regions").rglob("*.md"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().lower()
                if t in content:
                    parts = path.parts
                    country = parts[parts.index("regions") + 2]
                    filename = path.name
                    matches.append((country, filename, str(path.relative_to(BASE_DIR))))
        except Exception:
            pass

    print(f"[*] '{term}' için arama sonuçları ({len(matches)} eşleşme):")
    seen_countries = set()
    for country, filename, rel in matches[:25]:
        print(f"  • [{country}] -> {rel}")
        seen_countries.add(country)
    if len(matches) > 25:
        print(f"  ...ve {len(matches) - 25} ek sonuç.")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "country" and len(sys.argv) > 2:
        show_country(sys.argv[2])
    elif cmd == "compare" and len(sys.argv) > 3:
        compare_countries(sys.argv[2], sys.argv[3])
    elif cmd == "stats":
        show_stats()
    elif cmd == "search" and len(sys.argv) > 2:
        search_text(sys.argv[2])
    elif cmd == "graph" and len(sys.argv) > 2:
        c = find_country(sys.argv[2])
        if c:
            csv_path = BASE_DIR / c["path"] / "04_shadow_power_osint" / "oligarch_network.csv"
            from network_graph_gen import generate_mermaid_network
            print(generate_mermaid_network(csv_path))
        else:
            print("[-] Ülke bulunamadı.")
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
