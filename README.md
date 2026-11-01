<p align="center">
  <img src="assets/images/hero_banner.jpg" alt="Medeniyet Atlası & Global X-Ray" width="100%">
</p>

# 🌐 Global X-Ray & Medeniyet Atlası
> **205 Dünya Ulusunun Kültürel Kodları, Yaşam Felsefeleri ve 4 Katmanlı Güç Anatomisi**

<p align="center">
  <a href="countries/README.md"><img src="https://img.shields.io/badge/Uluslar-205%20%C3%9Clke-blue.svg?style=flat-square" alt="205 Countries"></a>
  <a href="culture/README.md"><img src="https://img.shields.io/badge/K%C3%BClt%C3%BCr-9%20Medeniyet%20Havzas%C4%B1-teal.svg?style=flat-square" alt="9 Realms"></a>
  <a href="economies/README.md"><img src="https://img.shields.io/badge/Ekonomi-8%20G%C3%BC%C3%A7%20Blo%C4%9Fu-purple.svg?style=flat-square" alt="8 Economic Blocks"></a>
  <a href="geopolitics_and_intelligence/README.md"><img src="https://img.shields.io/badge/%C4%B0stihbarat-11%20Stratejik%20Rapor-darkred.svg?style=flat-square" alt="Intelligence"></a>
  <a href="#-do%C4%9Frulama-ve-standart"><img src="https://img.shields.io/badge/Do%C4%9Frulama-Admiralty%20B2+-success.svg?style=flat-square" alt="Admiralty Code"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Lisans-CC%20BY--SA%204.0-lightgrey.svg?style=flat-square" alt="License"></a>
</p>

---

## 📌 Genel Bakış

**Global X-Ray**, dünya üzerindeki 205 egemen ulusu ve de-facto entiteyi iki temel eksende inceleyen açık kaynaklı bir küresel araştırma külliyatıdır:

1. **Kültürel DNA & Toplumsal Ruh ([`/culture`](culture/README.md)):** Ulusların diline, mutfak felsefesine, çevrilemeyen kolektif kavramlarına (*Gönül, Ikigai, Ubuntu, Toska*), kurucu destanlarına ve yaşam adabına odaklanır.
2. **Gerçek Güç & Jeopolitik Anatomi ([`/geopolitics_and_intelligence`](geopolitics_and_intelligence/README.md)):** Resmi retoriğin arkasındaki nükleer kapasiteleri, savunma paktlarını, kritik maden tekellerini, denizaltı kablo hatlarını ve oligarşik sermaye ağlarını analiz eder.

---

## 🏛️ 4 Katmanlı Analiz Metodolojisi

Her ülke, spekülasyonlardan arındırılmış ve **NATO / Admiralty B2+** standardında çapraz doğrulanmış 4 analitik katman üzerinden incelenir:

```
[ÜLKE ADI] /
├── 01_culture_demographics/  ──► Katman 1: Sosyo-Kültürel DNA, Toplum Tarihi ve Demografi
├── 02_official_state/        ──► Katman 2: Resmi Anayasal Rejim, Yargı ve Yönetim Yapısı
├── 03_official_economy/      ──► Katman 3: Resmi Makroekonomi, Dış Ticaret ve Göstergeler
└── 04_shadow_power_osint/    ──► Katman 4: Gölge Güç, Oligarşik Ağlar ve Medya/Sansür
```

---

## 📂 Dizin ve Modül Haritası

Detaylı raporlar, monografiler ve veri setleri ilgili alt dizinlerin kendi kılavuzlarında yer almaktadır:

| Modül | Dizin | Kapsam & İçerik |
| :--- | :--- | :--- |
| 🗺️ **205 Ülke Atlası** | [**`countries/`**](countries/README.md) | 205 ülkenin 4 katmanlı tüm monografi dosyaları ve master navigasyon tablosu. |
| 🎭 **Kültür Kütüphanesi** | [**`culture/`**](culture/README.md) | 9 Medeniyet Havzası, 205 ülkenin kültürel DNA matrisi, gastronomi, destanlar ve görgü kuralları. |
| 📊 **Ekonomik Güç Blokları** | [**`economies/`**](economies/README.md) | İleri Sanayi G7, Petro-Devletler, BRICS, Offshore Merkezler dahil 8 yapısal küresel blok. |
| 🌐 **Stratejik İstihbarat** | [**`geopolitics_and_intelligence/`**](geopolitics_and_intelligence/README.md) | Nükleer triad, silah ticareti, yaptırımlar, gölge filo, denizaltı kabloları ve boğazlar. |
| 🌍 **Bölgesel Raporlar** | [**`regions/`**](regions/README.md) | Orta Doğu, Avrupa, Asya, Amerika, Afrika ve Okyanusya jeopolitik güç dengeleri. |
| 📁 **Adli OSINT Vakaları** | [**`dossiers/`**](dossiers/README.md) | 1MDB, Nord Stream, Pegasus, Gladio, Troika Laundromat dahil 12 derin vaka incelemesi. |
| 📚 **Teori & Araştırma** | [**`research/`**](research/README.md) | Derin devlet teorileri, dedolarizasyon, bilişsel harp ve algoritmik istihbarat tezleri. |
| 🔬 **Metodoloji Kılavuzu** | [**`methodology/`**](methodology/README.md) | Paravan şirket tespiti (UBO), uydu/gemi takibi ve açık kaynak istihbaratı doğrulama rehberi. |
| 📊 **Küresel Veri Setleri** | [**`global_datasets/`**](global_datasets/README.md) | Ham CSV/JSON veri setleri (askeri üsler, offshore cennetleri, boğazlar, SWF fonları). |

---

## 🛠️ CLI Kullanımı (xray_cli.py)

Tüm repoyu ve veri tabanını terminalden hızlıca sorgulamak için `xray_cli.py` aracını kullanabilirsiniz:

```bash
# Ülkenin 4 katmanlı tam profilini incele
python scripts/xray_cli.py country turkiye

# Kültürel kodları ve çevrilemeyen kavramları görüntüle
python scripts/xray_cli.py culture japonya

# İki ülkeyi kültürel DNA ve sofra felsefesi açısından karşılaştır
python scripts/xray_cli.py compare-culture turkiye japonya

# Ekonomik bloğa göre ülkeleri listele
python scripts/xray_cli.py economy 01_ileri_sanayi_g7

# Savunma paktları, yaptırımlar veya deniz darboğazlarını sorgula
python scripts/xray_cli.py alliances nato
python scripts/xray_cli.py chokepoints

# 12 adli vaka analizini ve araştırma tezlerini listele
python scripts/xray_cli.py cases
python scripts/xray_cli.py research
```

---

## 🧪 Bütünlük Testleri

Repodaki 205 ülkenin hiyerarşik yapısı, veri tutarlılığı ve standartları otomatik testlerle denetlenir:

```bash
python -m unittest discover tests
```

---

## ⚖️ Lisans

Bu proje ve veri setleri [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](LICENSE) lisansı ile sunulmaktadır.
