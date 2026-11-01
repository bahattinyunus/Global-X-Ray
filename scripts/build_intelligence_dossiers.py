# -*- coding: utf-8 -*-
"""
scripts/build_intelligence_dossiers.py
Gathers all strategic, intelligence, military, and geoeconomic datasets into
dedicated, authoritative markdown dossiers under `geopolitics_and_intelligence/`.
"""

import sys
import json
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
GEO_DIR = BASE_DIR / "geopolitics_and_intelligence"
DATA_DIR = BASE_DIR / "global_datasets"

GEO_DIR.mkdir(exist_ok=True)

def load_data(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

# 1. Nuclear Triad
def build_nuclear():
    data = load_data("nuclear_arsenals_and_triad_registry.json")
    powers = data.get("nuclear_powers", [])
    overview = data.get("strategic_overview", {})
    sharing = data.get("nato_nuclear_sharing", {})
    
    rows = []
    for p in powers:
        triad = p.get("triad_components", {})
        triad_status = "Tam Triad (Kara-Deniz-Hava)" if (triad.get("land_icbm") and triad.get("sea_ssbn") and triad.get("air_bomber")) else "Kısmi / İkili Caydırıcılık"
        rows.append(f"| **{p['country']}** (`{p['code']}`) | {p['total_inventory']:,} | {p.get('deployed_strategic_warheads', '-')} | `{triad_status}` | {p['first_test_year']} | {p['nuclear_doctrine'][:80]}... |")
    
    bases_rows = []
    for b in sharing.get("bases", []):
        bases_rows.append(f"| **{b['base_name']}** | {b['country']} | ~{b['estimated_bombs']} Bomba | `{b['weapon_type']}` |")

    content = f"""# ☢️ Stratejik Nükleer Cephanelikler, Triad ve Caydırıcılık Sistemleri

> "{data.get('doctrine')}"

---

## 1. Stratejik Genel Bakış
* **Küresel Toplam Savaş Başlığı:** ~{overview.get('global_total_warheads', 0):,}
* **Konuşlu / Operasyonel Başlık:** ~{overview.get('deployed_operational_warheads', 0):,}
* **Nükleer Silaha Sahip Güç Sayısı:** {overview.get('nuclear_armed_states_count', 9)}
* **NATO Nükleer Paylaşım Ülkeleri:** {overview.get('nuclear_sharing_states_count', 5)}

---

## 2. 9 Nükleer Güç ve Stratejik Triad Envanteri

| Nükleer Güç | Toplam Cephanelik | Konuşlu Stratejik Başlık | Triad Yeteneği | İlk Test Yılı | Nükleer Doktrin & Angajman Şartı |
| :--- | :---: | :---: | :---: | :---: | :--- |
{chr(10).join(rows)}

---

## 3. NATO Nükleer Paylaşım Programı (B61 Bombaları)
{sharing.get('doctrine')}

| Üs Adı | Ev Sahibi Ülke | Tahmini Bomba Sayısı | Silah Türü & Atıcı Platform |
| :--- | :--- | :---: | :--- |
{chr(10).join(bases_rows)}

---

## 4. Asimetrik & Hipersonik Silahlar ve Otomatik Misilleme
* **Rusya (Perimeter / 'Ölü El'):** Komuta kademesi nükleer saldırıyla yok edilse dahi sismik ve radyasyon sensörleriyle otomatik misilleme fırlatan sistem; Avangard Mach 20+ HGV ve Poseidon nükleer torpidosu.
* **ABD (NC3 & Sentinel):** B-21 Raider yeni nesil stealth bombardıman uçağı, Columbia sınıfı nükleer denizaltılar ve Sentinel ICBM modernizasyonu.
* **Çin (Silo Tarlaları & FOBS):** Yumen ve Hami çöllerinde 300+ yeni ICBM silosu, DF-17 hipersonik füzeleri ve Kesirli Yörüngesel Bombardıman (FOBS) yeteneği.
"""
    with open(GEO_DIR / "NUCLEAR_TRIAD_AND_STRATEGIC_ARSENALS.md", "w", encoding="utf-8") as f:
        f.write(content)

# 2. Arms Trade & MIC
def build_armstrade():
    data = load_data("global_arms_trade_and_contractors.json")
    m_overview = data.get("market_overview", {})
    contractors = data.get("top_prime_contractors", [])
    exporters = data.get("top_exporters_vs_importers", {}).get("exporters", [])
    importers = data.get("top_exporters_vs_importers", {}).get("importers", [])
    
    c_rows = []
    for c in contractors:
        c_rows.append(f"| **#{c['rank']} {c['company']}** | {c['country']} | ${c['defense_revenue_usd_b']}B | {c['flagship_systems'][:65]}... | {c['strategic_monopoly'][:60]}... |")
        
    exp_rows = []
    for ex in exporters:
        exp_rows.append(f"| **{ex['country']}** | %{ex['share_pct']} | {', '.join(ex['primary_markets'])} |")
        
    imp_rows = []
    for im in importers:
        imp_rows.append(f"| **{im['country']}** | %{im['share_pct']} | {', '.join(im['primary_suppliers'])} |")

    content = f"""# ⚔️ Küresel Silah Ticareti ve Askeri-Endüstriyel Kompleks (MIC) Oligopolü

> "{data.get('doctrine')}"

---

## 1. Pazar Genel Bakışı
* **Yıllık Küresel Savunma Harcaması:** ${m_overview.get('global_defense_expenditure_usd_b', 0):,.1f} Milyar
* **İlk 100 Savunma Şirketi Cirosu:** ${m_overview.get('top_100_defense_revenue_usd_b', 0):,.1f} Milyar
* **ABD İhracat Payı:** %{m_overview.get('us_market_share_of_exports_pct')} | **Fransa:** %{m_overview.get('france_market_share_of_exports_pct')} | **Rusya:** %{m_overview.get('russia_market_share_of_exports_pct')}

---

## 2. Dünyanın En Büyük 12 Savunma Sanayii Yüklenicisi

| Savunma Yüklenicisi | Menşei | Savunma Cirosu | Amiral Platformlar & Füzeler | Stratejik Tekel & Pazar Hakimiyeti |
| :--- | :--- | :---: | :--- | :--- |
{chr(10).join(c_rows)}

---

## 3. Küresel Silah İhracatçıları ve İthalatçıları (SIPRI Verileri)

### 📤 En Büyük Silah İhracatçıları
| İhracatçı Ülke | Küresel Pazar Payı | Birincil İhracat Pazarları |
| :--- | :---: | :--- |
{chr(10).join(exp_rows)}

### 📥 En Büyük Silah İthalatçıları
| İthalatçı Ülke | Küresel Pazar Payı | Birincil Silah Tedarikçileri |
| :--- | :---: | :--- |
{chr(10).join(imp_rows)}
"""
    with open(GEO_DIR / "GLOBAL_ARMS_TRADE_AND_MIC_OLIGOPOLY.md", "w", encoding="utf-8") as f:
        f.write(content)

# 3. Defense Alliances
def build_alliances():
    data = load_data("defense_alliances_and_treaties.json")
    alliances = data.get("alliances", [])
    rows = []
    for al in alliances:
        rows.append(f"| **{al['id']}** | {al['name']} | `{al['established']}` | {al['member_count']} Üye | {al['core_trigger_article']} | ${al['combined_military_spending_usd_b']:,.0f}B |")
        
    content = f"""# 🛡️ Savunma Paktları, Askeri İttifaklar ve Güvenlik Mimarisi

Devletlerin sınır güvenliğini ve ortak savunma doktrinini belirleyen çok taraflı ve ikili askeri paktlar:

| Pakt Kodu | İttifak Tam Adı | Kuruluş | Kapsam | Temel Tetikleyici Karşılıklı Yardım Maddesi | Askeri Bütçe |
| :--- | :--- | :---: | :---: | :--- | :---: |
{chr(10).join(rows)}

---

## Pakt Detayları ve Jeopolitik İşlevleri
1. **NATO (Kuzey Atlantik Antlaşması Örgütü):** Madde 5 kolektif savunma maddesi; ABD nükleer şemsiyesi ve Avrupa güvenlik omurgası.
2. **CSTO (KGAÖ):** Rusya liderliğinde eski Sovyet cumhuriyetleri kolektif güvenlik paktı; Madde 4 kolektif müdahale maddesi.
3. **AUKUS:** ABD, İngiltere ve Avustralya nükleer tahrikli denizaltı ve yapay zeka/kuantum paktı.
4. **SCO (Şanghay İşbirliği Örgütü):** Çin ve Rusya liderliğinde Avrasya siyasi, askeri ve terörle mücadele platformu.
5. **QUAD:** ABD, Japonya, Hindistan ve Avustralya deniz güvenliği ve Hint-Pasifik çevreleme diyaloğu.
"""
    with open(GEO_DIR / "DEFENSE_ALLIANCES_AND_SECURITY_PACTS.md", "w", encoding="utf-8") as f:
        f.write(content)

# 4. Sanctions Regimes
def build_sanctions():
    data = load_data("sanctions_and_embargoes_registry.json")
    targets = data.get("targeted_states", [])
    rows = []
    for st in targets:
        rows.append(f"| **{st['country']}** (`{st['code']}`) | {st['regime_type']} | {', '.join(st['primary_sanctioners'])} | ${st['frozen_assets_usd_b']}B | {st['circumvention_corridors'][0]} |")

    content = f"""# ⚠️ Finansal Yaptırım Rejimleri ve Yaptırım Aşma Koridorları

Küresel rezerv para birimlerinin (USD, EUR) silahlaştırılması, dondurulan merkez bankası rezervleri ve hedef ülkelerin karşı tedbirleri:

| Hedef Ülke | Yaptırım Rejiminin Kapsamı | Uygulayan Güçler | Dondurulan Rezerv | Birincil Bypass & Kaçınma Koridoru |
| :--- | :--- | :--- | :---: | :--- |
{chr(10).join(rows)}

---

## Finansal Silahlanma ve Dedolarizasyon
* **Rezerv Güvenliği:** Rusya-Ukrayna savaşı sonrası \$300B Rus MB rezervinin dondurulması, küresel merkez bankalarının altın ve yerel para cinsinden ikili takas sistemlerine (mBridge, SPFS, CIPS) geçişini hızlandırdı.
* **Kripto ve Gölge Bankacılık:** İran ve Kuzey Kore gibi ülkeler, yaptırımları aşmak için devlet destekli kripto borsaları, Hawala ağları ve paravan şirketler zinciri kullanmaktadır.
"""
    with open(GEO_DIR / "SANCTIONS_REGIMES_AND_BYPASS_CORRIDORS.md", "w", encoding="utf-8") as f:
        f.write(content)

# 5. Critical Minerals
def build_minerals():
    data = load_data("critical_raw_materials_supply_chain.json")
    minerals = data.get("minerals", [])
    rows = []
    for mn in minerals:
        top_p = ", ".join([f"{x['country']} (%{x['share_pct']})" for x in mn['top_mining_nations'][:2]])
        ref = f"{mn['refining_monopoly']['dominant_nation']} (%{mn['refining_monopoly']['global_refining_share_pct']})"
        rows.append(f"| **{mn['name']}** (`{mn['id']}`) | {mn['strategic_category']} | {top_p} | **{ref}** | {mn['geopolitical_risk_score']}/10 |")

    content = f"""# ⛏️ Kritik Madenler, Tedarik Zincirleri ve Küresel Rafinaj Tekelleri

Yapay zeka çipleri, bataryalar, elektrikli araçlar ve gelişmiş savunma mühimmatı için hayati olan stratejik hammaddeler:

| Maden / Element | Stratejik Kullanım Kategorisi | En Büyük Maden Üreticileri | Küresel Rafinaj Tekeli | Jeopolitik Risk |
| :--- | :--- | :--- | :--- | :---: |
{chr(10).join(rows)}

---

## Rafinaj Tekeli Asimetrisi
* Madenler dünyanın farklı ülkelerinde (Kongo'da kobalt, Şili'de lityum) çıkarılsa dahi; ham cevherin işlenmesi ve saflaştırılmasında **Çin %60-90 arası küresel tekel** kurmuştur.
* Bu durum, Tayvan Boğazı veya Güney Çin Denizi krizlerinde Batı sanayisini anında hammadde krizine sürükleyecek asimetrik bir şantaj kaldıracıdır.
"""
    with open(GEO_DIR / "CRITICAL_RAW_MATERIALS_AND_REFINING_MONOPOLIES.md", "w", encoding="utf-8") as f:
        f.write(content)

# 6. Subsea Cables & SIGINT
def build_cables():
    data = load_data("subsea_cables_and_sigint_stations.json")
    cables = data.get("critical_cable_corridors", [])
    sigint = data.get("global_sigint_interception_stations", [])
    
    cb_rows = []
    for cb in cables:
        cb_rows.append(f"| **{cb['name']}** | {cb['connected_regions']} | {', '.join(cb['key_cables'][:3])} | {cb['vulnerability'][:70]}... | `{cb['geopolitical_risk']}` |")
        
    sg_rows = []
    for sg in sigint:
        sg_rows.append(f"| **{sg['station_name']}** | {sg['country']} | {sg['operator']} | {sg['location']} |")

    content = f"""# 🌐 Küresel Denizaltı Fiber Optik Kabloları ve SIGINT Dinleme İstasyonları

Dünya internet trafiğinin ve finansal transferlerinin (SWIFT) %97'si uydulardan değil, okyanus tabanındaki fiber kablolardan akar.

---

## 1. Kritik Denizaltı Kablo Koridorları
| Koridor Adı | Bağlanan Bölgeler | Kilit Kablo Hatları | Fiziksel Zaafiyet & Tehdit | Risk Seviyesi |
| :--- | :--- | :--- | :--- | :---: |
{chr(10).join(cb_rows)}

---

## 2. Küresel SIGINT Dinleme ve Casusluk İstasyonları
Five Eyes (FVEY) ve müttefik istihbarat servislerinin denizaltı kablolarını doğrudan dinleme tesisleri:

| İstasyon Adı | Ev Sahibi Ülke | Operatör Teşkilat | Stratejik Coğrafi Konum |
| :--- | :--- | :--- | :--- |
{chr(10).join(sg_rows)}
"""
    with open(GEO_DIR / "SUBSEA_CABLES_AND_GLOBAL_SIGINT_STATIONS.md", "w", encoding="utf-8") as f:
        f.write(content)

# 7. Sovereign Wealth Funds
def build_swf():
    data = load_data("sovereign_wealth_funds_registry.json")
    funds = data.get("funds", [])
    rows = []
    for sw in funds:
        rows.append(f"| **{sw['name']}** (`{sw['id']}`) | {sw['country']} | ${sw['assets_under_management_usd_b']:,.1f}B | {sw['funding_source'][:45]}... | {sw['geopolitical_leverage'][:65]}... |")

    content = f"""# 💰 Küresel Egemen Varlık Fonları (SWF) ve Devlet Sermayesi

Petrodolar fazlaları, dış ticaret artıları ve kamu varlıklarının toplandığı $12+ Trilyonluk küresel devlet sermayesi havuzları:

| Fon Adı | Ülke | Yönetilen Varlık (AUM) | Finansman Kaynağı | Jeopolitik Kaldıraç |
| :--- | :--- | :---: | :--- | :--- |
{chr(10).join(rows)}

---

## Stratejik Etki
* Norveç Petrol Fonu (NBIM), Çin Yatırım Kurumu (CIC) ve Suudi Kamu Yatırım Fonu (PIF); küresel borsaların, teknoloji devlerinin, limanların ve altyapıların en büyük hissedarları haline gelmiştir.
"""
    with open(GEO_DIR / "SOVEREIGN_WEALTH_FUNDS_AND_STATE_CAPITALISM.md", "w", encoding="utf-8") as f:
        f.write(content)

# 8. Shadow Fleet
def build_shadow_fleet():
    data = load_data("shadow_fleet_maritime_registry.json")
    flags = data.get("flags_of_convenience", [])
    sts = data.get("sts_transfer_chokepoints", [])
    metrics = data.get("fleet_metrics", {})
    
    fl_rows = []
    for fl in flags:
        fl_rows.append(f"| **{fl['flag_state']}** (`{fl['code']}`) | {fl['registered_dark_vessels']} Gemi | {fl['risk_profile'][:80]}... |")
        
    st_rows = []
    for st in sts:
        st_rows.append(f"| **{st['zone_name']}** | {st['location']} | {st['operations']} |")

    content = f"""# 🚢 Küresel Gölge Tanker Filosu (Dark Fleet) ve Yaptırım Kaçırma Koridorları

G7 tavan fiyatını, denizcilik sigorta yasaklarını ve petrol ambargolarını aşmak için kurulan ~{metrics.get('estimated_active_vessels', 850)} hayalet tankerin mimarisi.

* **Küresel Tanker Tonaj Payı:** %{metrics.get('share_of_global_tanker_tonnage_pct')}
* **Ortalama Gemi Yaşı:** {metrics.get('average_vessel_age_years')} Yıl
* **Birincil Kargo Çıkışları:** {', '.join(metrics.get('primary_cargo_origins', []))}

---

## 1. Öne Çıkan Kolaylık Bayrakları (Flags of Convenience)
| Bayrak Devleti | Tescilli Gölge Gemi Sayısı | Risk Profili & Zaafiyet Analizi |
| :--- | :---: | :--- |
{chr(10).join(fl_rows)}

---

## 2. Deniz Üstü Gemiden Gemiye (STS) Petrol Aktarma Merkezleri
| Aktarma Sahası (STS Zone) | Coğrafi Lokasyon | Operasyonel Taktik & Kamuflaj |
| :--- | :--- | :--- |
{chr(10).join(st_rows)}
"""
    with open(GEO_DIR / "SHADOW_FLEET_MARITIME_AND_STS_HUBS.md", "w", encoding="utf-8") as f:
        f.write(content)

# 9. Chokepoints
def build_chokepoints():
    data = load_data("chokepoints_registry.json")
    chokepoints = data.get("chokepoints", [])
    rows = []
    for cp in chokepoints:
        oil_str = f"{cp['daily_petroleum_transit_barrels']:,} v/g (%{cp['share_of_global_maritime_oil_pct']})"
        rows.append(f"| **{cp['name']}** ({cp['english_name']}) | {cp['type']} | {', '.join(cp['controlling_states'])} | {oil_str} | {cp['geopolitical_risk_level']} |")

    content = f"""# 🚢 Küresel Deniz Darboğazları ve Jeopolitik Kilit Noktaları

Dünya ticaretinin hacimce %80'inden fazlası, petrol taşımacılığının ise %60'ı okyanuslar ve deniz yolları üzerinden gerçekleşir. Ancak bu devasa küresel akış, coğrafyanın dayattığı birkaç dar boğaz ve yapay kanaldan geçmek zorundadır. Alfred Thayer Mahan'ın "Deniz Gücünün Tarihe Etkisi" kuramında belirttiği üzere: **«Darboğazları kontrol eden güç, dünya ticaretinin şah damarını ve rakiplerinin enerji arzını kontrol eder.»**

---

## ⚓ Kritik Boğazlar ve Kanallar Matrisi

| Boğaz / Kanal | Türü | Kıyıdaş & Kontrol Eden Güçler | Günlük Petrol Transiti & Küresel Pay | Jeopolitik Risk Seviyesi |
| :--- | :--- | :--- | :---: | :---: |
{chr(10).join(rows)}

---

## 🎯 Stratejik Darboğazların Derin Güvenlik ve Asimetrik Tehdit Analizi

### 1. Hürmüz Boğazı: Dünyanın Enerji Şah Damarı
* **Jeopolitik Konum:** Basra Körfezi'ni Umman Denizi ve Hint Okyanusu'na bağlayan en dar noktası 39 km genişliğindeki doğal geçit.
* **Stratejik Önemi:** Suudi Arabistan, Irak, BAE, Kuveyt, Katar (LNG ihracatının %20'si) ve İran'ın petrol ihracatı buradan geçer.
* **Tehdit Senaryoları:** İran Devrim Muhafızları Deniz Kuvvetleri (IRGCN) asimetrik sürat tekneleri, mayınlama ve kıyı seyir füzeleri. Boğazın 24 saat kapanması petrol fiyatlarını anında $150+/varil seviyesine fırlatır.

### 2. Malakka Boğazı & "Malakka İkilemi"
* **Jeopolitik Konum:** Malay Yarımadası ile Sumatra Adası arasında 800 km uzunluğunda, Singapur açıklarında sadece 2.8 km genişliğe inen koridor.
* **Stratejik Önemi:** Çin, Japonya ve Güney Kore'nin enerji ithalatının %80'i buradan akar.
* **Çin'in "Malakka İkilemi":** Olası bir Tayvan krizinde Malakka'nın abluka altına alınması durumunda Çin ekonomisinin akaryakıt kıtlığına düşme riski.

### 3. Babülmendep & Süveyş Kanalı: Kızıldeniz Asimetrik Kuşatması
* **Jeopolitik Konum:** Kızıldeniz'in güney çıkışı (Yemen-Cibuti arası 29 km) ve kuzey çıkışı (193 km uzunluğundaki Süveyş Kanalı).
* **Kızıldeniz Krizi:** Husi güçlerinin İHA ve balistik füzeleri, ticari gemileri Ümit Burnu rotasına yönlendirmiş, navlun maliyetlerini 3 katına çıkarmıştır.

### 4. Türk Boğazları ve Montrö Rejimi (1936)
* **Jeopolitik Konum:** Karadeniz'i Akdeniz'e bağlayan İstanbul ve Çanakkale boğazları.
* **Montrö Boğazlar Sözleşmesi Gücü:** Türkiye'nin boğazlar üzerindeki tam egemenliği ve savaş zamanında Karadeniz'e kıyıdaş olmayan ülkelerin savaş gemilerine geçişi kapatma yetkisi Karadeniz'in küresel savaşa dönüşmesini engelleyen nihai kalkandır.
"""
    with open(GEO_DIR / "MARITIME_CHOKEPOINTS_AND_TRANSIT_VULNERABILITIES.md", "w", encoding="utf-8") as f:
        f.write(content)

# 10. PMCs
def build_pmc():
    data = load_data("pmc_mercenary_groups.json")
    companies = data.get("companies", [])
    rows = []
    for p in companies:
        rows.append(f"| **{p['name']}** | {p['country_of_origin']} | {p['estimated_manpower']} | {', '.join(p['active_theaters'])} | {p['legal_status']} |")

    content = f"""# ⚔️ Özel Askeri Şirketler (PMC) ve Paramiliter Şebekeler

Modern hibrit harp doktrininde devletler; resmi ordularının hukuki ve siyasi sorumluluğunu üstlenmeksizin, vekil savaşlarını yürütmek, maden ve enerji imtiyazlarını korumak ve örtülü operasyonlar icra etmek için **Özel Askeri Şirketleri (PMC)** ve paramiliter ağları kullanmaktadır.

Niccolò Machiavelli'nin "Hükümdar" (1532) eserinde uyardığı gibi: **«Paralı askerler sadakatsiz, disiplinsiz ve muhteristir. Barış zamanında onlar sizi soyar, savaş zamanında düşman sizi mahveder.»** Günümüz küresel jeopolitiğinde PMC'ler, makul inkar edilebilirlik (plausible deniability) sağlayan stratejik devlet aygıtlarıdır.

---

## 🪖 Küresel Özel Askeri Şirketler ve Paramiliter Ağlar Matrisi

| Şirket / Şebeke | Menşei | Tahmini İnsan Gücü | Aktif Harekât Sahaları | Hukuki Statü & İlişki Biçimi |
| :--- | :--- | :---: | :--- | :--- |
{chr(10).join(rows)}

---

## 🎯 Stratejik Kullanım Modelleri

### 1. Rusya ve "Afrika Kolordusu" Modeli (Eski Wagner Grubu)
* Mali, Orta Afrika Cumhuriyeti, Burkina Faso ve Nijer'de darbe sonrası maden imtiyazları (altın, lityum) karşılığı rejim koruması.
* Prigozhin isyanı sonrası doğrudan GRU kontrolüne devredilmiştir.

### 2. ABD Modeli: İhale Tabanlı Savunma Alt-Yükleniciliği
* Irak ve Afganistan'da lojistik, VIP ve üs koruma taşeronluğu. Constellis (Blackwater/Academi) üzerinden Pentagon ihaleleri.
"""
    with open(GEO_DIR / "PMC_MERCENARY_GROUPS_AND_PROXY_WARFARE.md", "w", encoding="utf-8") as f:
        f.write(content)

# 11. Intelligence Agencies
def build_intel():
    data = load_data("intelligence_agencies_registry.json")
    agencies = data.get("agencies", [])
    rows = []
    for a in agencies:
        budget_str = a.get('estimated_annual_budget_usd', 'Bilinmiyor')
        rows.append(f"| **{a['country']}** | {a['primary_foreign']} | {a['primary_signals']} | {a['primary_domestic']} | `{budget_str}` | {a['classification_level']} |")

    content = f"""# 🕵️ Küresel İstihbarat Teşkilatları ve Örtülü Bütçeler

Dünya jeopolitiğine yön veren dış istihbarat, sinyal istihbaratı ve iç güvenlik servisleri:

| Ülke | Dış İstihbarat (HUMINT) | Sinyal İstihbaratı (SIGINT) | İç Güvenlik / Karşı İstihbarat | Tahmini Yıllık Bütçe | Operasyonel Sınıflandırma |
| :--- | :--- | :--- | :--- | :--- | :--- |
{chr(10).join(rows)}
"""
    with open(GEO_DIR / "GLOBAL_INTELLIGENCE_AGENCIES_AND_BLACK_BUDGETS.md", "w", encoding="utf-8") as f:
        f.write(content)

# Master README for geopolitics
def build_geo_index():
    content = """# 🌐 Medeniyet Atlası: Jeopolitik Güç, Savunma ve İstihbarat Külliyatı (/geopolitics_and_intelligence)

Bu dizin, egemen devletlerin kültürel kimliklerinin arkasında işleyen **askeri, nükleer, istihbari, siber ve jeoekonomik güç mimarisini** adli bilişim ve OSINT disipliniyle belgeleyen stratejik araştırma dosyalarını içerir.

---

## 📑 Stratejik Dosya Dizini

| Dosya | Konu | Temel Kapsam & Veri Seti |
| :--- | :--- | :--- |
| ☢️ [**NUCLEAR_TRIAD_AND_STRATEGIC_ARSENALS.md**](NUCLEAR_TRIAD_AND_STRATEGIC_ARSENALS.md) | Stratejik Nükleer Triad | 9 Nükleer gücün 12.121 savaş başlığı, ICBM, SSBN denizaltıları, Rus Perimeter (Ölü El) ve NATO nükleer paylaşım üsleri. |
| ⚔️ [**GLOBAL_ARMS_TRADE_AND_MIC_OLIGOPOLY.md**](GLOBAL_ARMS_TRADE_AND_MIC_OLIGOPOLY.md) | Silah Ticareti & MIC Tekelleri | $2.44T savunma bütçesi, en büyük 12 savunma tröstü (Lockheed, Raytheon, Rostec vb.) ve SIPRI ihracat/ithalat dengeleri. |
| 🛡️ [**DEFENSE_ALLIANCES_AND_SECURITY_PACTS.md**](DEFENSE_ALLIANCES_AND_SECURITY_PACTS.md) | Savunma Paktları & İttifaklar | NATO Madde 5, CSTO, AUKUS, QUAD, ŞİÖ karşılıklı yardım maddeleri ve askeri güç dengesi. |
| ⚠️ [**SANCTIONS_REGIMES_AND_BYPASS_CORRIDORS.md**](SANCTIONS_REGIMES_AND_BYPASS_CORRIDORS.md) | Finansal Yaptırımlar & Bypass | $300B+ dondurulan rezervler, SWIFT ambargoları, Hawala ve kripto kaçınma koridorları. |
| ⛏️ [**CRITICAL_RAW_MATERIALS_AND_REFINING_MONOPOLIES.md**](CRITICAL_RAW_MATERIALS_AND_REFINING_MONOPOLIES.md) | Kritik Madenler & Çin Tekeli | Kobalt, lityum, nadir toprak elementleri madenciliği ve %60-90 Çin rafinaj tekeli. |
| 🌐 [**SUBSEA_CABLES_AND_GLOBAL_SIGINT_STATIONS.md**](SUBSEA_CABLES_AND_GLOBAL_SIGINT_STATIONS.md) | Denizaltı Fiber Hatları & SIGINT | Dünya internet trafiğinin %97'sini taşıyan okyanus altı kablolar ve Five Eyes dinleme istasyonları. |
| 💰 [**SOVEREIGN_WEALTH_FUNDS_AND_STATE_CAPITALISM.md**](SOVEREIGN_WEALTH_FUNDS_AND_STATE_CAPITALISM.md) | Egemen Varlık Fonları (SWF) | Norveç NBIM, Çin CIC, Suudi PIF dahil $12+ Trilyonluk devlet sermayesi ve jeopolitik kaldıraç. |
| 🚢 [**SHADOW_FLEET_MARITIME_AND_STS_HUBS.md**](SHADOW_FLEET_MARITIME_AND_STS_HUBS.md) | Gölge Tanker Filosu (Dark Fleet) | Yaptırım kaçıran ~850 hayalet tanker, kolaylık bayrakları (Gabon, Cook Adaları) ve açık deniz STS aktarma noktaları. |
| ⚓ [**MARITIME_CHOKEPOINTS_AND_TRANSIT_VULNERABILITIES.md**](MARITIME_CHOKEPOINTS_AND_TRANSIT_VULNERABILITIES.md) | Deniz Darboğazları & Kilit Noktalar | Hürmüz, Malakka, Babülmendep, Süveyş ve Türk Boğazları petrol ve ticaret transiti risk haritası. |
| 🪖 [**PMC_MERCENARY_GROUPS_AND_PROXY_WARFARE.md**](PMC_MERCENARY_GROUPS_AND_PROXY_WARFARE.md) | Özel Askeri Şirketler (PMC) | Wagner/Afrika Kolordusu, Constellis/Blackwater, Sadat, Executive Outcomes ve vekil savaşları. |
| 🕵️ [**GLOBAL_INTELLIGENCE_AGENCIES_AND_BLACK_BUDGETS.md**](GLOBAL_INTELLIGENCE_AGENCIES_AND_BLACK_BUDGETS.md) | İstihbarat Teşkilatları & Bütçeler | CIA, MI6, Mossad, MİT, GRU, MSS operasyonel doktrinleri ve gizli kara bütçeler. |

---

> 💡 *Ayrıca tarihi derin devlet operasyonları ve siber istihbarat sabotajları için:* [**dossiers/**](../dossiers/README.md)
"""
    with open(GEO_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    build_nuclear()
    build_armstrade()
    build_alliances()
    build_sanctions()
    build_minerals()
    build_cables()
    build_swf()
    build_shadow_fleet()
    build_chokepoints()
    build_pmc()
    build_intel()
    build_geo_index()
    print("[SUCCESS] All 12 geopolitics & intelligence dossiers built successfully in geopolitics_and_intelligence/")
