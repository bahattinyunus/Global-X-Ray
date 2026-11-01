# -*- coding: utf-8 -*-
"""
scripts/generate_master_readme.py
Generates the comprehensive, quote-rich, authoritative master README.md for Global-X-Ray,
including the 5 high-impact thematic intelligence graphics, the 8 economic archetype blocks,
the 205-country atlas, regional dossiers, 7 deep forensic case studies, defense alliances,
sanction regimes, critical raw materials, subsea cables, and full OSINT methodology.
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

with open(BASE_DIR / "global_datasets" / "intelligence_agencies_registry.json", encoding="utf-8") as f:
    intel_registry = json.load(f)

with open(BASE_DIR / "global_datasets" / "chokepoints_registry.json", encoding="utf-8") as f:
    chokepoints_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "pmc_mercenary_groups.json", encoding="utf-8") as f:
    pmc_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "defense_alliances_and_treaties.json", encoding="utf-8") as f:
    alliances_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "sanctions_and_embargoes_registry.json", encoding="utf-8") as f:
    sanctions_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "critical_raw_materials_supply_chain.json", encoding="utf-8") as f:
    minerals_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "subsea_cables_and_sigint_stations.json", encoding="utf-8") as f:
    cables_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "sovereign_wealth_funds_registry.json", encoding="utf-8") as f:
    swf_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "shadow_fleet_maritime_registry.json", encoding="utf-8") as f:
    shadow_fleet_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "nuclear_arsenals_and_triad_registry.json", encoding="utf-8") as f:
    nuclear_data = json.load(f)

with open(BASE_DIR / "global_datasets" / "global_arms_trade_and_contractors.json", encoding="utf-8") as f:
    armstrade_data = json.load(f)

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

# 205 Ülkelik Atlas Tablosu (Ekonomik modellere göre yapılandırılmış)
atlas_rows = []
for c in countries_sorted:
    eco_id = c.get("economy_group_id", "06_orta_gelir_ve_ureticiler")
    eco_badge = economy_badges.get(eco_id, "🌐 Karma Model")
    eco_path = c.get("economy_path", f"06_orta_gelir_ve_ureticiler/{c['slug']}")
    link = f"[{c['name']} Dosyası]({eco_path}/README.md)"
    sh_str = f"%{c.get('shadow_economy_pct', 25.0)}"
    gdp_str = f"${c.get('gdp_usd_b', 0):,.1f}B"
    atlas_rows.append(f"| **{c['name']}** | {eco_badge} | `{c['code']}` | {c['capital']} | {link} | {gdp_str} | {sh_str} |")

atlas_table_md = "\n".join(atlas_rows)

# İstihbarat Teşkilatları Tablosu
intel_rows = []
for a in intel_registry["agencies"]:
    budget_str = a.get('estimated_annual_budget_usd', 'Bilinmiyor')
    intel_rows.append(f"| **{a['country']}** | {a['primary_foreign']} | {a['primary_signals']} | {a['primary_domestic']} | `{budget_str}` | {a['classification_level']} |")
intel_table_md = "\n".join(intel_rows)

# Boğazlar Tablosu
choke_rows = []
for cp in chokepoints_data["chokepoints"]:
    oil_str = f"{cp['daily_petroleum_transit_barrels']:,} v/g (%{cp['share_of_global_maritime_oil_pct']})"
    choke_rows.append(f"| **{cp['name']}** ({cp['english_name']}) | {cp['type']} | {', '.join(cp['controlling_states'])} | {oil_str} | {cp['geopolitical_risk_level']} |")
choke_table_md = "\n".join(choke_rows)

# PMC Tablosu
pmc_rows = []
for p in pmc_data["companies"]:
    pmc_rows.append(f"| **{p['name']}** | {p['country_of_origin']} | {p['estimated_manpower']} | {', '.join(p['active_theaters'])} | {p['legal_status']} |")
pmc_table_md = "\n".join(pmc_rows)

# Savunma Paktları Tablosu
alliance_rows = []
for al in alliances_data["alliances"]:
    alliance_rows.append(f"| **{al['id']}** | {al['name']} | `{al['established']}` | {al['member_count']} Üye | {al['core_trigger_article']} | ${al['combined_military_spending_usd_b']:,.0f}B |")
alliances_table_md = "\n".join(alliance_rows)

# Yaptırımlar Tablosu
sanctions_rows = []
for st in sanctions_data["targeted_states"]:
    sanctions_rows.append(f"| **{st['country']}** (`{st['code']}`) | {st['regime_type']} | {', '.join(st['primary_sanctioners'])} | ${st['frozen_assets_usd_b']}B | {st['circumvention_corridors'][0]} |")
sanctions_table_md = "\n".join(sanctions_rows)

# Kritik Madenler Tablosu
minerals_rows = []
for mn in minerals_data["minerals"]:
    top_p = ", ".join([f"{x['country']} (%{x['share_pct']})" for x in mn['top_mining_nations'][:2]])
    ref = f"{mn['refining_monopoly']['dominant_nation']} (%{mn['refining_monopoly']['global_refining_share_pct']})"
    minerals_rows.append(f"| **{mn['name']}** (`{mn['id']}`) | {mn['strategic_category']} | {top_p} | **{ref}** | {mn['geopolitical_risk_score']}/10 |")
minerals_table_md = "\n".join(minerals_rows)

# Denizaltı Kabloları Tablosu
cables_rows = []
for cb in cables_data["critical_cable_corridors"]:
    cables_rows.append(f"| **{cb['name']}** | {cb['connected_regions']} | {', '.join(cb['key_cables'][:3])} | {cb['vulnerability'][:70]}... | `{cb['geopolitical_risk']}` |")
cables_table_md = "\n".join(cables_rows)

# SIGINT İstasyonları Tablosu
sigint_rows = []
for sg in cables_data["global_sigint_interception_stations"]:
    sigint_rows.append(f"| **{sg['station_name']}** | {sg['country']} | {sg['operator']} | {sg['location']} |")
sigint_table_md = "\n".join(sigint_rows)

# Egemen Varlık Fonları (SWF) Tablosu
swf_rows = []
for sw in swf_data["funds"]:
    swf_rows.append(f"| **{sw['name']}** (`{sw['id']}`) | {sw['country']} | ${sw['assets_under_management_usd_b']:,.1f}B | {sw['funding_source'][:45]}... | {sw['geopolitical_leverage'][:65]}... |")
swf_table_md = "\n".join(swf_rows)

# Gölge Filo Bayrak Tablosu
darkfleet_flag_rows = []
for fl in shadow_fleet_data["flags_of_convenience"]:
    darkfleet_flag_rows.append(f"| **{fl['flag_state']}** (`{fl['code']}`) | {fl['registered_dark_vessels']} Gemi | {fl['risk_profile'][:80]}... |")
darkfleet_flags_md = "\n".join(darkfleet_flag_rows)

# Gölge Filo STS Tablosu
darkfleet_sts_rows = []
for st in shadow_fleet_data["sts_transfer_chokepoints"]:
    darkfleet_sts_rows.append(f"| **{st['zone_name']}** | {st['location']} | {st['operations']} |")
darkfleet_sts_md = "\n".join(darkfleet_sts_rows)

# Nükleer Güçler ve Stratejik Triad Tablosu
nuclear_rows = []
for p in nuclear_data["nuclear_powers"]:
    triad = p.get("triad_components", {})
    triad_status = "Tam Triad (Kara-Deniz-Hava)" if (triad.get("land_icbm") and triad.get("sea_ssbn") and triad.get("air_bomber")) else "Kısmi / İkili Caydırıcılık"
    nuclear_rows.append(f"| **{p['country']}** (`{p['code']}`) | {p['total_inventory']:,} | {p.get('deployed_strategic_warheads', '-')} | `{triad_status}` | {p['first_test_year']} | {p['nuclear_doctrine'][:75]}... |")
nuclear_table_md = "\n".join(nuclear_rows)

# Silah Sanayii ve Savunma Tröstleri Tablosu
armstrade_rows = []
for c in armstrade_data["top_prime_contractors"]:
    armstrade_rows.append(f"| **#{c['rank']} {c['company']}** | {c['country']} | ${c['defense_revenue_usd_b']}B | {c['flagship_systems'][:65]}... | {c['strategic_monopoly'][:60]}... |")
armstrade_table_md = "\n".join(armstrade_rows)

# Medeniyet Havzaları Tablosu
realms_rows = []
for r in culture_data["civilization_realms"]:
    realms_rows.append(f"| **{r['name']}** | {r['core_philosophy']} | `{', '.join(r['representative_states'])}` |")
realms_table_md = "\n".join(realms_rows)

# Kültürel Kodlar ve Ulusal DNA Tablosu
culture_rows = []
for c in culture_data["countries_cultural_dna"]:
    words = ", ".join([f"**{w['word']}**" for w in c.get("untranslatable_soul_concepts", [])[:3]])
    culture_rows.append(f"| **{c['country']}** (`{c['code']}`) | {c['core_cultural_ethos'][:65]}... | {words} | {c['communication_style'][:35]} | {c['gastronomic_philosophy'][:65]}... |")
culture_table_md = "\n".join(culture_rows)

master_readme_content = f"""# 🌍 DÜNYA MEDENİYETLERİ, KÜLTÜREL KODLAR & DERİN GÜÇ ATLASI
### *205 Ülkenin Kültürel DNA'sı, Yaşam Felsefesi, Medeniyet Havzaları ve Gerçek İktidar Anatomisi Ansiklopedisi*

<p align="center">
  <img src="assets/images/hero_banner.jpg" alt="Global X-Ray Hero Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Ansiklopedi-K%C3%BClt%C3%BCrel%20Kodlar%20%26%20Medeniyet-darkgreen?style=for-the-badge&logo=bookstack" alt="Encyclopedia">
  <img src="https://img.shields.io/badge/Kapsam-205%20%C3%9Clke%20%26%20B%C3%B6lge-blue?style=for-the-badge&logo=globe" alt="Coverage">
  <img src="https://img.shields.io/badge/Medeniyet%20Havzas%C4%B1-9%20K%C3%BCresel%20Kutup-teal?style=for-the-badge" alt="Civilization">
  <img src="https://img.shields.io/badge/Ekonomik%20Arketip-8%20Makro%20G%C3%BC%C3%A7%20Blo%C4%9Fu-blueviolet?style=for-the-badge" alt="Economic Archetypes">
  <img src="https://img.shields.io/badge/G%C3%BC%C3%A7%20Anatomisi-4%20Katmanl%C4%B1%20Derin%20Devlet-black?style=for-the-badge" alt="4-Layer">
  <img src="https://img.shields.io/badge/Vaka%20Analizleri-12%20Adli%20Soru%C5%9Fturma-crimson?style=for-the-badge" alt="Case Studies">
  <img src="https://img.shields.io/badge/N%C3%BCkleer%20Triad-12%2C121%20Ba%C5%9Fl%C4%B1k%20Kayd%C4%B1-darkred?style=for-the-badge" alt="Nuclear Triad">
  <img src="https://img.shields.io/badge/Silah%20Ticareti-$2.4T%20Savunma%20Oligopol%C3%BC-firebrick?style=for-the-badge" alt="Arms Trade">
  <img src="https://img.shields.io/badge/Egemen%20Varl%C4%B1k-$12+%20Trilyon%20SWF-forestgreen?style=for-the-badge" alt="SWF">
  <img src="https://img.shields.io/badge/G%C3%B6lge%20Filo-850%20Dark%20Tanker-maroon?style=for-the-badge" alt="Shadow Fleet">
  <img src="https://img.shields.io/badge/Do%C4%9Frulama-Admiralty%20Kodu%20B2+-success?style=for-the-badge" alt="Verification">
  <img src="https://img.shields.io/badge/Lisans-A%C3%A7%C4%B1k%20K%C3%BClt%C3%BCr%20(CC%20BY--SA%204.0)-purple?style=for-the-badge" alt="License">
</p>

---

## 📑 İÇİNDEKİLER TABLOSU

1. [🏛️ Giriş ve Ana Misyon: Dünya Uluslarını ve Kültürel Kodlarını Tanımak](#️-giriş-ve-ana-misyon-dünya-uluslarini-ve-kültürel-kodlarini-tanimak)
2. [🎭 Dünya Medeniyetleri ve Kültürel Kodlar Rehberi (Cultural DNA)](#-dünya-medeniyetleri-ve-kültürel-kodlar-rehberi-cultural-dna)
3. [🌐 Küresel Röntgen Doktrini: Gerçekçi Güç ve Derin Devlet Anatomisi](#-küresel-röntgen-doktrini-gerçekçi-güç-ve-derin-devlet-anatomisi)
4. [📊 Ekonomik Modellere Göre 8 Küresel Güç Bloğu (/01_... - /08_...)](#-ekonomik-modellere-göre-8-küresel-güç-bloğu-01----08_)
5. [🏛️ Metodoloji: 4 Katmanlı Ülke ve Güç Mimarisi](#️-metodoloji-4-katmanli-ülke-ve-güç-mimarisi)
6. [🛡️ Doğrulama Standardı: NATO / Admiralty Kodu (B2+)](#️-doğrulama-standardi-nato--admiralty-kodu-b2)
7. [💸 Kleptokrasi & Offshore Sermaye Kaçırma Döngüsü](#-kleptokrasi--offshore-sermaye-kaçirma-döngüsü)
8. [🧠 Bilişsel Savaş & Siber İstihbarat Matrisi (5GW)](#-bilişsel-savaş--siber-istihbarat-matrisi-5gw)
9. [🚢 Küresel Deniz Darboğazları & Jeopolitik Kilit Noktaları](#-küresel-deniz-darboğazlari--jeopolitik-kilit-noktalari)
10. [🌐 Küresel Denizaltı Fiber Kablolar & SIGINT İstasyonları](#-küresel-denizalti-fiber-kablolar--sigint-istasyonlari)
11. [🛡️ Savunma Paktları, Askeri İttifaklar & Nükleer Şemsiye](#️-savunma-paktlari-askeri-ittifaklar--nükleer-şemsiye)
12. [⚠️ Finansal Yaptırım Rejimleri & Bypass Koridorları](#️-finansal-yaptirim-rejimleri--bypass-koridorlari)
13. [⛏️ Kritik Madenler & Küresel Rafinaj Tekelleri](#️-kritik-madenler--küresel-rafinaj-tekelleri)
14. [💰 Küresel Egemen Varlık Fonları (SWF) & Devlet Sermayesi](#-küresel-egemen-varlik-fonlari-swf--devlet-sermayesi)
15. [🚢 Küresel Gölge Tanker Filosu (Dark Fleet) & Yaptırım Kaçırma](#-küresel-gölge-tanker-filosu-dark-fleet--yaptirim-kaçirma)
16. [☢️ Küresel Nükleer Cephanelikler & Stratejik Nükleer Triad](#️-küresel-nükleer-cephanelikler--stratejik-nükleer-triad)
17. [⚔️ Küresel Silah Ticareti & Savunma Sanayii Tröstleri (MIC)](#️-küresel-silah-ticareti--savunma-sanayii-tröstleri-mic)
18. [🗺️ Bölgesel Master Jeopolitik Güç Dosyaları (/regions)](#️-bölgesel-master-jeopolitik-güç-dosyalari-regions)
19. [📁 Derin Adli OSINT Vaka Analizleri (/dossiers)](#-derin-adli-osint-vaka-analizleri-dossiers)
20. [⚔️ Özel Askeri Şirketler (PMC) & Paramiliter Şebekeler](#️-özel-askeri-şirketler-pmc--paramiliter-şebekeler)
21. [🕵️ Küresel İstihbarat Teşkilatları & Güç Mimarisi](#️-küresel-istihbarat-teşkilatlari--güç-mimarisi)
22. [📚 Ansiklopedik Araştırma Dosyaları & Teori Külliyatı (/research)](#-ansiklopedik-araştirma-dosyalari--teori-külliyati-research)
23. [🗺️ 205 Ülkelik Küresel Atlas İndeksi (Ekonomik Modelleriyle)](#️-205-ülkelik-küresel-atlas-indeksi-ekonomik-modelleriyle)
24. [🔬 Metodoloji ve OSINT Araştırma Kılavuzları (/methodology)](#-metodoloji-ve-osint-araştirma-kilavuzlari-methodology)
25. [🛠️ CLI Terminal Aracı ile Kullanım (xray_cli.py)](#️-cli-terminal-araci-ile-kullanim-xray_clipy)
26. [🧪 Bütünlük ve Veri Doğrulama Testleri](#-bütünlük-ve-veri-doğrulama-testleri)
27. [⚖️ Etik, Hukuki Beyan ve Açık İstihbarat Lisansı](#️-etik-hukuki-beyan-ve-açik-istihbarat-lisansi)

---

## 🏛️ GİRİŞ VE ANA MİSYON: DÜNYA ULUSLARINI VE KÜLTÜREL KODLARINI TANIMAK

> *"Bir ulusu gerçekten tanımak; onun yalnızca sınırlarını, başkentini ve bayrağını bilmek değildir. Bir ulusu tanımak; bin yıllık kolektif hafızasını, sevinçlerini ve yaslarını, sofrasındaki ekmeği bölüşme adabını, başka hiçbir dile tam çevrilemeyen ruh kavramlarını (Gönül, Ikigai, Gemütlichkeit, Saudade, Ubuntu), selamlaşma inceliklerini ve dünyaya bakış felsefesini öğrenmektir."*

Bu projenin **birincil ve en temel varoluş gayesi**; dünya üzerindeki 205 egemen ve jeopolitik ülkeyi tüm kültürel derinlikleri, medeniyet kodları, yaşam tarzları, mutfak gelenekleri, edebi mirası ve toplumsal karakterleriyle tanıtan **muazzam bir açık kaynaklı dünya ansiklopedisi** sunmaktır.

Dünya ulusları birbirine düşman soyut bayraklardan ibaret değildir; her biri binlerce yıllık coğrafi sınavlardan, göçlerden ve felsefi arayışlardan süzülmüş eşsiz birer kültürel hazinedir. Bu atlas, okuyucusuna bir Japon'un *Wabi-sabi* estetiğindeki dinginliği, bir Türk'ün *Gönül* ve *İmece* dilindeki derin cömertliği, bir Alman'ın *Gemütlichkeit* huzurunu, bir Slav'ın *Toska* melankolisini ve bir Afrikalının *Ubuntu* ("Biz olduğumuz için benim") dayanışmasını anlama kapısını aralar.

### ⚖️ Gerçekçilik Dengesi: Neden Derin Devlet ve Güç Katmanı da Var?
Bir ülkeyi yalnızca masalsı turizm broşürleriyle anlatmak, o ülkenin halkına ve tarihsel gerçeğine haksızlık etmektir. Bir ulusun gündelik hayatı ve kültürel dokusu ne kadar zengin olursa olsun; o toplum aynı zamanda **derin devlet mekanizmaları, askeri ittifaklar, oligarşik sermaye konsorsiyumları, enerji darboğazları ve istihbarat savaşları** gerçeğiyle kuşatılmıştır.

Bu nedenle bu ansiklopedi; **kültürü ve insanı merkeze koyan ana gövdesini**, adli bilişim ve OSINT disipliniyle hazırlanmış **derin güç anatomisi** ile dengeler. Böylece okuyucu hem bir ülkenin ruhunu tanır hem de o ülkenin üzerinde dönen küresel satrancı tüm çıplaklığıyla kavrar.

---

## 🎭 DÜNYA MEDENİYETLERİ VE KÜLTÜREL KODLAR REHBERİ (CULTURAL DNA)

İnsanlık tarihi, belirli coğrafi ve manevi havzalarda şekillenen büyük medeniyetlerin etkileşimidir (`global_datasets/cultural_codes_and_civilizations_registry.json`):

### 🌐 9 Büyük Küresel Medeniyet Havzası
| Medeniyet Havzası | Temel Felsefe & Toplumsal Ethos | Temsilci Ülkeler |
| :--- | :--- | :--- |
{realms_table_md}

### 🧬 Örnek Medeniyet Çapaları: Ulusal Karakterler ve Yaşam Adabı
| Ülke | Ulusal Karakter & Temel Ethos | Çevrilemeyen Ruh Kavramları | İletişim Tarzı | Gastronomi & Sofra Felsefesi |
| :--- | :--- | :--- | :--- | :--- |
{culture_table_md}

---

## 🌐 KÜRESEL RÖNTGEN DOKTRİNİ: GERÇEKÇİ GÜÇ VE DERİN DEVLET ANATOMİSİ

> *"Görünen hükümetin arkasında, halka karşı hiçbir bağlılığı olmayan ve hiçbir sorumluluk kabul etmeyen görünmez bir hükümet taht kurmuştur. Bu görünmez hükümeti yok etmek, yozlaşmış iş dünyası ile yozlaşmış siyaset arasındaki kirli ittifakı bozmak, günümüzün ilk görevidir."*  
> — **Theodore Roosevelt** (ABD 26. Başkanı, 1912 İlerleme Partisi Platformu)

> *"Ticaret ve imalat dünyasında öyle bazı adamlar var ki, bir şeyden korkuyorlar. Biliyorlar ki bir yerlerde öyle organize, öyle sinsi, öyle uyanık, öyle kilitli ve öyle yaygın bir güç var ki, onu kınarken fısıltıyla bile konuşmamak en iyisi."*  
> — **Woodrow Wilson** (ABD 28. Başkanı, *The New Freedom*, 1913)

> *"Kitlelerin organize alışkanlıklarının ve kanaatlerinin bilinçli ve akıllıca manipülasyonu, demokratik bir toplumun önemli bir unsurudur. Toplumun bu görülmeyen mekanizmasını manipüle edenler, ülkemizin gerçek yönetici gücü olan görünmez bir hükümet teşkil ederler."*  
> — **Edward L. Bernays** (*Propaganda*, 1928)

> *"Washington'daki gerçek yöneticiler görünmezdir ve güçlerini perde arkasından kullanırlar."*  
> — **Felix Frankfurter** (ABD Yüksek Mahkeme Yargıcı, 1952)

> *"Egemen, olağanüstü hale karar verendir. Hukuk düzeni, anayasanın askıya alındığı gri alanda doğar ve korunur."*  
> — **Carl Schmitt** (*Siyasi İlahiyat*, 1922)

> *"Derin siyaset, resmi siyasal sistemin kurallarını çiğneyen, ulusal güvenlik devleti bürokrasisi, organize suç örgütleri ve uluslararası finans konsorsiyumlarının gizli ittifakından doğan örtülü iktidardır."*  
> — **Prof. Peter Dale Scott** (*The Road to 9/11: Wealth, Empire, and the Future of America*)

> *"İktidar seçkinleri; dev şirketlerin, askeri kliklerin ve federal yürütmenin zirvesindeki yöneticilerden oluşur. Bunlar sıradan insanların hayatını doğrudan belirleyen kararları kapalı kapılar ardında alır."*  
> — **C. Wright Mills** (*The Power Elite*, 1956)

> *"Eğer savaşlar yalanlarla başlatılabiliyorsa, barış gerçeklerle inşa edilebilir."*  
> — **Julian Assange** (WikiLeaks Kurucusu, 2011)

---

## 🌐 KÜRESEL RÖNTGEN MANİFESTOSU VE DOKTRİNİ

Geleneksel ansiklopediler, diplomatik bültenler ve ana akım medya; devletleri resmi anayasaları, meclis tutanakları, seçim bültenleri ve kamuya açıklanan makroekonomik göstergeleri üzerinden resmeder. Ancak tarihsel gerçeklik şudur: **Egemen devletlerin kaderini belirleyen gerçek güç odakları; resmi kabinelerden ziyade örtülü istihbarat paktlarında, hanedan varlık tröstlerinde, askeri-endüstriyel tedarik zincirlerinde ve offshore bankacılık ağlarında kümelenmiştir.**

**Küresel Röntgen (Global X-Ray)**; devletlerin anayasal maskelerini kaldırarak gerçek güç anatomilerini ortaya koyan, **205 egemen ve jeopolitik entiteyi** 4 derin katmanda adli bilişim ve OSINT disipliniyle haritalandıran **dünyanın en kapsamlı açık kaynak istihbarat atlasıdır**.

### 🔍 Doktrinin 3 Temel İlkesi:
1. **İllüzyonun Yıkımı (Constitutional Decoupling):** Resmi anayasa ile fiili iktidar mekanizması arasındaki uçurumu belgelemek; yürütmenin arkasındaki derin klikleri somut kanıtlarla görünür kılmak.
2. **Finansal İz Sürme (Follow the Forensic Ledger):** Kleptokratik sermaye kaçışını, paravan kabuk şirketleri (shell companies), vergi cennetlerini ve kayıt dışı para transferlerini şeffaflaştırmak.
3. **Bilişsel Bağımsızlık (Cognitive Sovereignty):** Devletlerin ve küresel tröstlerin kitleleri yönlendirmek için kurduğu algoritmik ve medyatik sansür mimarisini deşifre etmek.

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

## 🏛️ METODOLOJİ: 4 KATMANLI DERİN DEVLET MİMARİSİ

<p align="center">
  <img src="assets/images/4_layer_power_architecture.jpg" alt="4 Layer Power Architecture" width="90%">
</p>

Repodaki istisnasız her ülke klasörü, birbirine bağlı ve disiplinlerarası **4 derin katmandan** meydana gelir:

### 🧩 Katmanların Analitik Ayrımı:
* **01. Kültür, Etnik Denge & Demografi (`01_culture_demographics/`):** Toplumun tarihsel travmaları, mezhepsel ve kabilevi fay hatları, göç dalgaları ve demografik kırılganlıklar (`society_history.md`, `demographics.csv`).
* **02. Resmi Devlet Mekanizması & Anayasa (`02_official_state/`):** Görünen yürütme, parlamenter veya başkanlık yapısı, anayasal kuvvetler ayrılığı illüzyonu, yargı teşkilatı ve resmi silahlı kuvvetler doktrini (`constitution_gov.md`).
* **03. Resmi Makroekonomi & Dış Ticaret (`03_official_economy/`):** Nominal ve SAGP GSYİH, cari denge, döviz rezervleri, dış borç stoku, bütçe açığı ve en büyük dış ticaret ortakları (`macroeconomics.json`).
* **04. Gölge Güç, Kleptokrasi & OSINT (`04_shadow_power_osint/`):** Gerçek güç odakları, askeri-istihbarat cuntaları, oligark konsorsiyumları, hanedan tröstleri, offshore sermaye kaçış kanalları, basın sansür filtreleri ve algoritmik kontrol mekanizmaları (`real_power_dynamics.md`, `oligarch_network.csv`, `media_censorship_matrix.md`).

```mermaid
flowchart TD
    subgraph Katmanlar["Global X-Ray 4 Katmanlı Güç Anatomisi"]
        L1["01. Kültür, Etnik Denge & Demografi<br/>(Tarihsel travmalar, mezhepsel fay hatları, kabile dinamikleri)"]
        L2["02. Resmi Devlet Mekanizması & Anayasa<br/>(Görünen yürütme, parlamento, kanunlar, ordu bürokrasisi)"]
        L3["03. Resmi Makroekonomi & Dış Ticaret<br/>(GSYİH, ihracat-ithalat, döviz rezervleri, kamu borcu)"]
        L4["04. Gölge Güç, Kleptokrasi & OSINT<br/>(Askeri klikler, oligark ağları, offshore tröstler, medya tekelleri)"]
    end
    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 -.->|"Perde Arkasından Yönetir ve Yönlendirir"| L2
    L4 -.->|"Kamu Bütçesini ve İhaleleri Gasp Eder"| L3
```

---

## 🛡️ DOĞRULAMA STANDARDI: NATO / ADMİRALTY KODU (B2+)

Global X-Ray bünyesinde yer alan tüm istihbarat ve araştırma verileri, uluslararası askeri ve istihbarat doktrinlerinde kabul gören **Admiralty Kod (Stanag 2097)** metodolojisine göre çapraz kontrolden geçirilir. Projenin kabul eşiği **B2 (Genellikle Güvenilir / Muhtemelen Doğru)** düzeyidir:

| Kaynak Güvenilirliği (Harf) | Bilgi Doğruluğu (Rakam) | Global X-Ray Kabul Eşiği |
| :--- | :--- | :---: |
| **A - Tamamen Güvenilir:** Şüpheye yer bırakmayan resmi tutanaklar, adli iddianameler, sızdırılmış orijinal belgeler. | **1 - Teyit Edilmiş:** Bağımsız birden fazla doğrulanabilir kaynak ve çapraz log kayıtları ile kanıtlanmış. | ✅ **A1** (Mutlak Delil) |
| **B - Genellikle Güvenilir:** Uluslararası denetim raporları (FATF, ICIJ, OCCRP), akademik araştırmalar, saygın araştırma merkezleri. | **2 - Muhtemelen Doğru:** En az iki bağımsız açık kaynak ve lojistik/finansal veriyle teyit edilmiş. | ✅ **B2** (Minimum Standart) |
| **C - Oldukça Güvenilir:** Yerel gazetecilik araştırmaları, sektörel raporlar. | **3 - Mümkün:** Mantıksal çıkarımlarla uyumlu fakat doğrudan adli belgesi olmayan. | ⚠️ Ek Teyit Gerekir |
| **D - Genellikle Güvenilmez:** Taraflı siyasi beyanlar, anonim sosyal medya iddiaları. | **4 - Şüpheli:** Doğrulanamayan veya çelişkili iddialar. | ❌ Reddedilir |

---

## 💸 KLEPTOKRASİ & OFFSHORE SERMAYE KAÇIRMA DÖNGÜSÜ

<p align="center">
  <img src="assets/images/offshore_kleptocracy_network.jpg" alt="Global Offshore Kleptocracy and Capital Flight" width="90%">
</p>

Küresel kleptokrasi; az gelişmiş ve gelişmekte olan ülkelerdeki kamu kaynaklarının, maden ve enerji imtiyazlarının siyasi elitler ve oligarklar tarafından gasp edilerek batı finans merkezlerine aktarılması döngüsüdür:

1. **Yerleştirme (Placement):** Kamu ihalelerinden alınan rüşvetler, gümrük kaçakçılığı ve enerji imtiyaz komisyonları paravan yerel şirketler üzerinden sisteme sokulur.
2. **Katmanlama (Layering):** British Virgin Islands (BVI), Cayman Adaları, Panama, Seyşeller ve Delaware'de kurulan iç içe geçmiş kabuk şirketler (shell companies) ve isimsiz trust fonları üzerinden para onlarca ülkeye transfer edilir (Ticaret Temelli Para Aklama - TBML, Sahte Faturalandırma, Mirror Trading).
3. **Bütünleştirme (Integration):** Aklanmış ve kaynağı gizlenmiş sermaye; Londra, New York, Cenevre ve Dubai'de lüks gayrimenkullere, mega yatlara, futbol kulüplerine ve batı borsalarındaki tahvillere dönüştürülerek meşrulaştırılır.

```mermaid
sequenceDiagram
    autonumber
    actor Kleptokrat as Otokrat / Siyasi Klik
    participant Varlık as Kamu İhalesi & Doğal Kaynak Gaspı
    participant Paravan as BVI / Delaware / Panama Kabuk Şirket
    participant Banka as İsviçre / Londra / Dubai Bankası
    participant RealEstate as Londra / NY / Dubai Gayrimenkulü & SWF

    Kleptokrat->>Varlık: Kamu bütçesinden komisyon & Kaynak gaspı
    Varlık->>Paravan: Sahte danışmanlık faturası & Transfer fiyatlandırması
    Paravan->>Banka: Katmanlama (Layering) & İsimsiz Trust hesabı
    Banka->>RealEstate: Entegrasyon: Lüks gayrimenkul, özel jet, batı hissesi
    Note over Kleptokrat,RealEstate: Sermaye tamamen aklanır ve batı hukuk güvencesine kavuşur.
```

---

## 🧠 BİLİŞSEL SAVAŞ & SİBER İSTİHBARAT MATRİSİ (5GW)

<p align="center">
  <img src="assets/images/cognitive_warfare_surveillance.jpg" alt="Cognitive Warfare and Cyber Surveillance Matrix" width="90%">
</p>

5. Nesil Harp (5GW), fiziksel sınırlardan ziyade insan zihnini, algoritmik akışları ve küresel dijital haberleşme altyapısını hedef alır:

* **Denizaltı Fiber Kabloları Dinleme İstasyonları:** Dünya internet trafiğinin %99'u okyanus tabanındaki fiber kablolardan akar. FVEY (Beş Göz Paktı) üyesi ülkeler (ABD, İngiltere, Kanada, Avustralya, Yeni Zelanda); Bude, Cornwall, Diego Garcia ve Hawaii dinleme istasyonları vasıtasıyla küresel veri trafiğini filtreler.
* **Sıfır-Tıklama Casus Yazılımlar (Zero-Click Spyware):** NSO Group (Pegasus) ve Intellexa (Predator) gibi askeri siber istihbarat araçları; hedefin hiçbir bağlantıya tıklamasına gerek kalmadan iOS/Android cihazlara sızarak kamera, mikrofon, şifreli mesajlar ve konum verilerini gerçek zamanlı dışarı aktarır.
* **Algoritmik Kitle Manipülasyonu:** Sosyal medya algoritmalarının duygusal polarizasyon motorları ve bot çiftlikleri, seçim sonuçlarını ve toplumsal infialleri manipüle etmek için organize psikolojik harekât (PSYOP) silahı olarak kullanılır.

---

## 🚢 KÜRESEL DENİZ DARBOĞAZLARI & JEOPOLİTİK KİLİT NOKTALARI

<p align="center">
  <img src="assets/images/geopolitical_chokepoints.jpg" alt="Geopolitical Chokepoints and Strategic Corridors" width="90%">
</p>

Dünya ticaretinin ve deniz yoluyla taşınan petrolün %60'ından fazlası daracık birkaç su yolundan geçmek zorundadır (`global_datasets/chokepoints_registry.json`):

| Boğaz / Kanal | Tip | Kıyıdaş Devletler | Günlük Petrol Transiti | Jeopolitik Risk Seviyesi |
| :--- | :--- | :--- | :--- | :--- |
{choke_table_md}

---

## 🌐 KÜRESEL DENİZALTI FİBER KABLOLAR & SIGINT İSTASYONLARI

Dünya internet trafiğinin ve SWIFT bankacılık mesajlarının aktığı denizaltı omurgaları ve dinleme merkezleri (`global_datasets/subsea_cables_and_sigint_stations.json`):

### 🌊 Kritik Denizaltı Kablo Koridorları
| Koridor Adı | Bağlantı Alanı | Örnek Hatlar | Zaafiyet & Sabotaj Riski | Risk |
| :--- | :--- | :--- | :--- | :---: |
{cables_table_md}

### 📡 Küresel Sinyal İstihbaratı (SIGINT) Dinleme Merkezleri
| İstasyon Adı | Ev Sahibi Ülke | İşleten Teşkilat / İttifak | Lokasyon |
| :--- | :--- | :--- | :--- |
{sigint_table_md}

---

## 🛡️ SAVUNMA PAKTLARI, ASKERİ İTTİFAKLAR & NÜKLEER ŞEMSİYE

Küresel güvenlik mimarisini belirleyen çok taraflı ve ikili savunma paktları (`global_datasets/defense_alliances_and_treaties.json`):

| Pakt Kodu | İttifak Tam Adı | Kuruluş | Kapsam | Temel Tetikleyici Karşılıklı Yardım Maddesi | Askeri Bütçe |
| :--- | :--- | :---: | :---: | :--- | :---: |
{alliances_table_md}

---

## ⚠️ FİNANSAL YAPTIRIM REJİMLERİ & BYPASS KORİDORLARI

Küresel rezerv para (USD) bağımlılığının silah olarak kullanılması ve hedef ülkelerin karşı tedbirleri (`global_datasets/sanctions_and_embargoes_registry.json`):

| Hedef Ülke | Yaptırım Rejiminin Kapsamı | Uygulayan Güçler | Dondurulan Rezerv | Birincil Bypass & Kaçınma Koridoru |
| :--- | :--- | :--- | :---: | :--- |
{sanctions_table_md}

---

## ⛏️ KRİTİK MADENLER & KÜRESEL RAFİNAJ TEKELLERİ

Enerji dönüşümünün, yapay zeka çiplerinin ve savunma sanayisinin hammadde boğazları (`global_datasets/critical_raw_materials_supply_chain.json`):

| Maden / Element | Stratejik Kullanım Kategorisi | En Büyük Maden Üreticileri | Küresel Rafinaj Tekeli | Jeopolitik Risk |
| :--- | :--- | :--- | :--- | :---: |
{minerals_table_md}

---

## 💰 KÜRESEL EGEMEN VARLIK FONLARI (SWF) & DEVLET SERMAYESİ

Küresel petrodolar fazlaları, dış ticaret artıları ve stratejik kamu işletmelerinin konsolide edildiği $12+ Trilyonluk egemen sermaye havuzları (`global_datasets/sovereign_wealth_funds_registry.json`):

| Fon Adı | Ülke | Yönetilen Varlık (AUM) | Finansman Kaynağı | Jeopolitik Kaldıraç |
| :--- | :--- | :---: | :--- | :--- |
{swf_table_md}

---

## 🚢 KÜRESEL GÖLGE TANKER FİLOSU (DARK FLEET) & YAPTIRIM KAÇIRMA

G7 tavan fiyatını ve denizcilik sigorta yasaklarını aşarak Rusya, İran ve Venezuela petrolünü taşıyan ~850 hayalet tankerin mimarisi (`global_datasets/shadow_fleet_maritime_registry.json`):

### 🚩 Öne Çıkan Kolaylık Bayrakları (Flags of Convenience)
| Bayrak Devleti | Tescilli Gölge Gemi Sayısı | Risk Profili & Zaafiyet Analizi |
| :--- | :---: | :--- |
{darkfleet_flags_md}

### ⚓ Deniz Üstü Gemiden Gemiye (STS) Petrol Aktarma Merkezleri
| Aktarma Sahası (STS Zone) | Coğrafi Lokasyon | Operasyonel Taktik & Kamuflaj |
| :--- | :--- | :--- |
{darkfleet_sts_md}

---

## ☢️ KÜRESEL NÜKLEER CEPHANELİKLER & STRATEJİK NÜKLEER TRİAD

Nükleer silahlar ve stratejik nükleer triad (ICBM, SSBN, Stratejik Bombardıman); egemen devletlerin nihai güvenlik garantisi ve karşılıklı garantili imha (MAD) dengesinin temelidir (`global_datasets/nuclear_arsenals_and_triad_registry.json`):

| Nükleer Güç | Toplam Cephanelik | Konuşlu Stratejik Başlık | Triad Yeteneği | İlk Test Yılı | Nükleer Doktrin & Angajman Şartı |
| :--- | :---: | :---: | :---: | :---: | :--- |
{nuclear_table_md}

---

## ⚔️ KÜRESEL SİLAH TİCARETİ & SAVUNMA SANAYİİ TRÖSTLERİ (MIC)

Askeri-Endüstriyel Kompleks (MIC); küresel savunma bütçelerini, vekil savaşlarını ve jeopolitik nüfuzu yönlendiren devasa bir oligopol yapısıdır (`global_datasets/global_arms_trade_and_contractors.json`):

| Savunma Yüklenicisi | Menşei | Savunma Cirosu | Amiral Platformlar & Füzeler | Stratejik Tekel & Küresel Pazar Hakimiyeti |
| :--- | :--- | :---: | :--- | :--- |
{armstrade_table_md}

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

## ⚔️ ÖZEL ASKERİ ŞİRKETLER (PMC) & PARAMİLİTER ŞEBEKELER

Devletlerin resmi ordu sorumluluğunu üstlenmeden vekil savaşlarında, maden sahaları korumasında ve örtülü operasyonlarda kullandığı askeri yükleniciler (`global_datasets/pmc_mercenary_groups.json`):

| Şirket / Şebeke | Menşei | Tahmini İnsan Gücü | Aktif Harekât Sahaları | Hukuki Statü |
| :--- | :--- | :---: | :--- | :--- |
{pmc_table_md}

---

## 🕵️ KÜRESEL İSTİHBARAT TEŞKİLATLARI & GÜÇ MİMARİSİ

Dünya jeopolitiğine yön veren istihbarat teşkilatlarının teşkilat yapısı, tahmini bütçeleri ve operasyonel uzmanlıkları (`global_datasets/intelligence_agencies_registry.json`):

| Ülke | Dış İstihbarat (HUMINT) | Sinyal İstihbaratı (SIGINT) | İç Güvenlik / Karşı İstihbarat | Tahmini Yıllık Bütçe | Operasyonel Sınıflandırma |
| :--- | :--- | :--- | :--- | :--- | :--- |
{intel_table_md}

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

## 🗺️ 205 ÜLKELİK KÜRESEL ATLAS İNDEKSİ (EKONOMİK MODELLERİYLE)

Aşağıdaki tabloda projedeki tüm bağımsız ülkeler listelenmiştir. Her bağlantı doğrudan kök dizindeki ilgili **ekonomik blok klasörü** altındaki detaylı istihbarat profiline yönlendirir:

| Ülke | Ekonomik Model | ISO | Başkent | Rapor Bağlantısı | GSYİH (USD) | Kayıt Dışı (%) |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: |
{atlas_table_md}

---

## 🔬 METODOLOJİ VE OSINT ARAŞTIRMA KILAVUZLARI (/methodology)

Araştırmacılar, gazeteciler ve analistler için hazırlanan teknik OSINT kılavuzları:

* 🏢 [**CORP_REGISTRY_RECONNAISSANCE.md**](methodology/CORP_REGISTRY_RECONNAISSANCE.md): BVI, Delaware, İngiltere Companies House, Lüksemburg RCS ve İsviçre ticaret sicillerinde paravan şirket sahipliği ve UBO (Nihai Faydalanıcı Mülkiyet) tespiti.
* 🌐 [**DATA_COLLECTION_GUIDE.md**](methodology/DATA_COLLECTION_GUIDE.md): Çok kaynaklı istihbarat toplama, uydu görüntüleri (Sentinel/Planet), gemi takip (AIS/MarineTraffic) ve uçuş radarı (ADS-B Exchange) entegrasyonu.
* 🛡️ [**OSINT_VERIFICATION.md**](methodology/OSINT_VERIFICATION.md): NATO Admiralty Kod standardı, dijital görüntü adli bilişimi, EXIF metadata analizi ve tersine görsel arama ile dezenformasyon filtreleme.

---

## 🛠️ CLI TERMİNAL ARACI İLE KULLANIM (xray_cli.py)

Tüm repoyu komut satırından hızlıca sorgulamak ve çapraz istihbarat analizi yapmak için `scripts/xray_cli.py` geliştirilmiştir:

```bash
# Bir ülkenin 4 katmanlı tam istihbarat ve kültür profilini terminalde görüntüle
python scripts/xray_cli.py country turkey

# Bir ülkenin kültürel kodlarını, çevrilemeyen kavramlarını ve yaşam tarzını incele
python scripts/xray_cli.py culture turkey

# Küresel 9 büyük medeniyet havzasını listele
python scripts/xray_cli.py culture

# İki ülkeyi jeopolitik, askeri ve makroekonomik olarak karşılaştır
python scripts/xray_cli.py compare turkey iran

# Ekonomik güç bloğuna göre ülkeleri filtrele ve analiz et
python scripts/xray_cli.py economy 02_petro_ve_enerji_devleri

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
python scripts/deep_recon.py turkey --export

# 12 derin adli vaka analizini listele
python scripts/xray_cli.py cases

# 12 derin araştırma tezini ve doktrin dosyalarını listele
python scripts/xray_cli.py research

# Belirli bir araştırma konusunu ara (örn. dedolarizasyon / biyolojik)
python scripts/xray_cli.py research dollar

# En yüksek kayıt dışı / gölge ekonomi oranına sahip ülkeleri sırala
python scripts/xray_cli.py top-shadow 15

# Küresel makroekonomik sistem istatistiklerini özetle
python scripts/xray_cli.py stats
```

---

## 🧪 BÜTÜNLÜK VE VERİ DOĞRULAMA TESTLERİ

Repodaki 205 ülkenin dosya yapısı, veri tutarlılığı, ekonomik gruplandırması ve JSON şemaları otomatik birim testleriyle korunur:

```bash
python tests/test_integrity.py
```

---

## ⚖️ ETİK, HUKUKİ BEYAN VE AÇIK İSTİHBARAT LİSANSI

1. **Açık Kaynak İstihbarat (OSINT) Güvencesi:** Bu repodaki tüm veriler; kamuya açık resmi hükümet kayıtları, uluslararası denetim raporları (BM, Dünya Bankası, IMF, FATF), mahkeme iddianameleri ve bağımsız uluslararası araştırmacı gazetecilik konsorsiyumları (ICIJ, OCCRP) tarafından yayımlanmış belgelere dayanır.
2. **Akademik & Araştırma Amacı:** Bu çalışma, egemen devletlerin iç ve dış politikalarını, sermaye kaçış kanallarını ve derin güç dinamiklerini anlamaya yönelik bağımsız bir akademik ve araştırmacı gazetecilik çalışmasıdır.
3. **Telif & Lisans:** Bu veritabanı, küresel şeffaflık ve kamu yararı amacıyla **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** lisansı altında açık kaynak olarak sunulmuştur.

---

<p align="center">
  <b>KÜRESEL RÖNTGEN (GLOBAL X-RAY)</b> &copy; 2026 &bull; <i>Hakikat, gizlenenlerin toplamıdır.</i><br/>
  <i>"Veritas vos liberabit." (Gerçek sizi özgür kılacaktır.)</i>
</p>
"""

with open(BASE_DIR / "README.md", "w", encoding="utf-8") as f:
    f.write(master_readme_content.strip() + "\n")

print(f"[SUCCESS] Master README.md generated successfully! ({len(master_readme_content.splitlines())} lines)")
