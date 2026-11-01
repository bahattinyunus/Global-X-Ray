#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/deep_recon.py
Medeniyet Atlası Çok Katmanlı Kültür & Derin Güç Keşif Motoru (Deep Reconnaissance Engine)

Kullanım:
  python scripts/deep_recon.py <ulke_adi_veya_kodu>
  python scripts/deep_recon.py --export <ulke_adi>
"""

import sys
import json
import csv
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "global_datasets"

def load_json(filename):
    p = DATASETS_DIR / filename
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def run_deep_recon(query, export_md=False):
    registry = load_json("countries_registry.json")
    intel_data = load_json("intelligence_agencies_registry.json")
    choke_data = load_json("chokepoints_registry.json")
    alliances_data = load_json("defense_alliances_and_treaties.json")
    sanctions_data = load_json("sanctions_and_embargoes_registry.json")
    minerals_data = load_json("critical_raw_materials_supply_chain.json")
    swf_data = load_json("sovereign_wealth_funds_registry.json")
    cables_data = load_json("subsea_cables_and_sigint_stations.json")
    shadow_fleet_data = load_json("shadow_fleet_maritime_registry.json")
    culture_data = load_json("cultural_codes_and_civilizations_registry.json")

    # Ülkeyi bul
    q = query.lower().strip()
    target = None
    for c in registry:
        if c["slug"] == q or c["code"].lower() == q or c["name"].lower() == q:
            target = c
            break
    if not target:
        for c in registry:
            if q in c["slug"] or q in c["name"].lower():
                target = c
                break

    if not target:
        print(f"[-] Ülke bulunamadı: '{query}'")
        return

    # Dosya yolları
    c_path = BASE_DIR / target.get("economy_path", f"countries/{target['slug']}")
    if not c_path.exists():
        c_path = BASE_DIR / f"countries/{target['slug']}"

    # İttifaklar
    member_alliances = []
    for a in alliances_data.get("alliances", []):
        if target["code"] in a.get("key_members", []):
            member_alliances.append(f"{a['id']} ({a['name']})")

    # Yaptırımlar
    target_sanctions = None
    for s in sanctions_data.get("targeted_states", []):
        if s["code"] == target["code"]:
            target_sanctions = s
            break

    # İstihbarat Teşkilatı
    agency_info = None
    for ag in intel_data.get("agencies", []):
        ag_c = ag["country"].lower()
        if ag_c in [target["name"].lower(), target["slug"].lower()] or target["slug"] in ag_c or target["code"].lower() in ag_c:
            agency_info = ag
            break

    # Darboğazlar
    controlled_chokepoints = []
    for cp in choke_data.get("chokepoints", []):
        if any(target["name"].lower() in cs.lower() for cs in cp.get("controlling_states", [])):
            controlled_chokepoints.append(f"{cp['name']} ({cp['daily_petroleum_transit_barrels']:,} v/g)")

    # Kritik Madenler
    mined_minerals = []
    refined_minerals = []
    for mn in minerals_data.get("minerals", []):
        for prod in mn.get("top_mining_nations", []):
            if target["name"].lower() in prod.get("country", "").lower():
                mined_minerals.append(f"{mn['name']} (%{prod['share_pct']} pay)")
        if target["name"].lower() in mn.get("refining_monopoly", {}).get("dominant_nation", "").lower():
            refined_minerals.append(f"{mn['name']} (Rafinaj: %{mn['refining_monopoly']['global_refining_share_pct']})")

    # Egemen Varlık Fonu (SWF)
    country_swfs = []
    for sw in swf_data.get("funds", []):
        if sw.get("code") == target["code"]:
            country_swfs.append(f"{sw['name']} (${sw['assets_under_management_usd_b']}B AUM)")

    # SIGINT İstasyonları
    sigint_stations = []
    for st in cables_data.get("global_sigint_interception_stations", []):
        if target["name"].lower() in st.get("country", "").lower():
            sigint_stations.append(f"{st['station_name']} ({st['operator']})")

    # Kültürel Kodlar
    target_culture = None
    for cd in culture_data.get("countries_cultural_dna", []):
        if cd.get("code") == target["code"] or target["name"].lower() in cd.get("country", "").lower():
            target_culture = cd
            break

    # Rapor çıktısı
    lines = []
    lines.append("=" * 80)
    lines.append(f"🎯 MEDENİYET ATLASI DERİN KEŞİF RAPORU (DEEP RECON)")
    lines.append(f"   HEDEF: {target['name'].upper()} ({target['code']}) &bull; BAŞKENT: {target['capital'].upper()}")
    lines.append("=" * 80)
    if target_culture:
        lines.append("🎭 MEDENİYET KİMLİĞİ VE KÜLTÜREL KODLAR:")
        lines.append(f"   [+] Medeniyet Havzası: {target_culture.get('civilization_crossroads')}")
        lines.append(f"   [+] Ulusal Karakter:   {target_culture.get('core_cultural_ethos')}")
        lines.append(f"   [+] İletişim Tarzı:    {target_culture.get('communication_style')}")
        words = [f"{w['word']} ({w['meaning'][:40]}...)" for w in target_culture.get("untranslatable_soul_concepts", [])[:3]]
        lines.append(f"   [+] Kilit Kavramlar:   {'; '.join(words)}")
        lines.append("-" * 80)
    lines.append(f"• Doğrulama Kodu:         NATO / Admiralty B2+ (Genellikle Güvenilir / Teyitli)")
    lines.append(f"• Ekonomik Güç Bloğu:     {target.get('economy_group_name', 'Bilinmiyor')} [{target.get('economy_group_id', '')}]")
    lines.append(f"• Coğrafi Bölge:          {target['region'].upper()}")
    lines.append(f"• Nominal GSYİH:          ${target.get('gdp_usd_b', 0):,.1f} Milyar USD")
    lines.append(f"• Nüfus:                  {target.get('population', 0):,} Kişi")
    lines.append(f"• Kayıt Dışı / Gölge:     %{target.get('shadow_economy_pct', 25.0)} (Risk Seviyesi: {'YÜKSEK' if target.get('shadow_economy_pct', 0) > 30 else 'ORTA'})")
    lines.append("-" * 80)
    lines.append("🛡️ ASKERİ PAKTLAR & GÜVENLİK İTTİFAKLARI:")
    if member_alliances:
        for ma in member_alliances:
            lines.append(f"   [+] {ma}")
    else:
        lines.append("   [-] Resmi küresel pakt kaydı yok (Bağımsız / Tarafsız / Bölgesel Paktlar)")

    lines.append("-" * 80)
    lines.append("⚠️ FİNANSAL YAPTIRIMLAR & ABLUKA STATÜSÜ:")
    if target_sanctions:
        lines.append(f"   [!] AKTİF YAPTIRIM REJİMİ: {target_sanctions['regime_type']}")
        lines.append(f"   [!] Dondurulan Rezervler: ${target_sanctions['frozen_assets_usd_b']} Milyar")
        lines.append(f"   [!] Bypass Koridoru: {target_sanctions['circumvention_corridors'][0]}")
    else:
        lines.append("   [+] Doğrudan kapsamlı çok taraflı finansal yaptırım altında değil.")

    lines.append("-" * 80)
    lines.append("🕵️ İSTİHBARAT & GÖZETİM TEŞKİLATI:")
    if agency_info:
        lines.append(f"   • Dış İstihbarat (HUMINT): {agency_info['primary_foreign']}")
        lines.append(f"   • Sinyal İstihbaratı:     {agency_info['primary_signals']}")
        lines.append(f"   • İç Güvenlik:            {agency_info['primary_domestic']}")
        lines.append(f"   • Tahmini Yıllık Bütçe:   {agency_info.get('estimated_annual_budget_usd', 'Bilinmiyor')}")
    else:
        lines.append("   [-] Küresel istihbarat teşkilatı kaydı listelenmemiş.")
    if sigint_stations:
        lines.append(f"   • Ev Sahipliği Yaptığı SIGINT Merkezleri: {', '.join(sigint_stations)}")

    lines.append("-" * 80)
    lines.append("🚢 STRATEJİK DENİZ DARBOĞAZLARI & KORİDORLAR:")
    if controlled_chokepoints:
        for ccp in controlled_chokepoints:
            lines.append(f"   [⚓] {ccp}")
    else:
        lines.append("   [-] Doğrudan kontrol edilen küresel kilit darboğaz bulunmuyor.")

    lines.append("-" * 80)
    lines.append("⛏️ KRİTİK HAMMADDE & RAFİNAJ TEKELLERİ:")
    if mined_minerals or refined_minerals:
        if mined_minerals:
            lines.append(f"   • Maden Üretimi: {', '.join(mined_minerals)}")
        if refined_minerals:
            lines.append(f"   • Rafinaj Tekeli: {', '.join(refined_minerals)}")
    else:
        lines.append("   [-] Kritik yarı iletken/enerji madeni tekel kontrolü yok.")

    lines.append("-" * 80)
    lines.append("💰 EGEMEN VARLIK FONLARI (SWF):")
    if country_swfs:
        for swf_entry in country_swfs:
            lines.append(f"   [🏛️] {swf_entry}")
    else:
        lines.append("   [-] Kayıtlı $50B+ küresel egemen varlık fonu bulunmuyor.")

    lines.append("-" * 80)
    lines.append(f"📁 4 KATMANLI ARŞİV DOSYALARI DİZİNİ:")
    lines.append(f"   • Klasör Yolu: {c_path}")
    lines.append(f"   • Katman 1 (Toplum):       {c_path / '01_culture_demographics'}")
    lines.append(f"   • Katman 2 (Resmi Devlet): {c_path / '02_official_state'}")
    lines.append(f"   • Katman 3 (Makroekonomi): {c_path / '03_official_economy'}")
    lines.append(f"   • Katman 4 (Gölge Güç):    {c_path / '04_shadow_power_osint'}")
    lines.append("=" * 80)

    report_text = "\n".join(lines)
    print(report_text)

    if export_md:
        out_file = BASE_DIR / f"RECON_{target['slug'].upper()}.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(report_text + "\n")
        print(f"\n[+] Rapor başarıyla dışa aktarıldı: {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    export = False
    args = sys.argv[1:]
    if "--export" in args:
        export = True
        args.remove("--export")
    
    query = " ".join(args)
    run_deep_recon(query, export_md=export)
