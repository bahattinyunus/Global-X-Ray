# 📋 Ülke Şablonu (Country Profile Template)

Her ülke klasörü aşağıdaki hiyerarşik yapıya ve dosya içeriği formatına uygun olarak doldurulmalıdır:

```text
📂 [ulke_adi]
 ┣ 📜 README.md
 ┣ 📂 01_culture_demographics
 ┃ ┣ 📜 society_history.md
 ┃ ┗ 📊 demographics.csv
 ┣ 📂 02_official_state
 ┃ ┗ 📜 constitution_gov.md
 ┣ 📂 03_official_economy
 ┃ ┗ 📊 macroeconomics.json
 ┗ 📂 04_shadow_power_osint
   ┣ 📜 real_power_dynamics.md
   ┣ 📊 oligarch_network.csv
   ┗ 📜 media_censorship_matrix.md
```

---

## 1. README.md (Ülke Yönetici Özeti)
```markdown
# 🌍 [Ülke Adı] - Küresel Röntgen Özeti

## 📌 Genel Bakış
- **Resmi Ad:**
- **Başkent:**
- **Bölge:**
- **Nüfus:**
- **Yönetim Biçimi:**
- **Resmi Lider(ler):**
- **Fiili (De Facto) Güç Odağı:**

## ⚠️ Röntgen Risk Skoru
- **Oligarşik Yoğunlaşma:** [Düşük / Orta / Yüksek / Kritik]
- **Yolsuzluk Algı Endeksi Sırası:**
- **Basın Özgürlüğü Durumu:**
- **Gölge Ekonomi Oranı Tahmini:**
```

---

## 2. 01_culture_demographics/demographics.csv
```csv
metric,value,unit,year,source
total_population,0,people,2024,World Bank
urban_population_pct,0,percent,2024,World Bank
median_age,0,years,2024,UN Data
literacy_rate_pct,0,percent,2024,UNESCO
dominant_ethnic_group,Unknown,string,2024,Official Census
dominant_religion,Unknown,string,2024,Pew Research
```

---

## 3. 03_official_economy/macroeconomics.json
```json
{
  "country": "Country Name",
  "currency": "CUR",
  "gdp_nominal_billion_usd": 0.0,
  "gdp_per_capita_usd": 0,
  "inflation_rate_pct": 0.0,
  "unemployment_rate_pct": 0.0,
  "top_exports": [],
  "top_imports": [],
  "major_trading_partners": [],
  "debt_to_gdp_pct": 0.0
}
```

---

## 4. 04_shadow_power_osint/oligarch_network.csv
```csv
person_or_entity,role_or_title,connected_sector,political_connection,estimated_wealth_usd_m,source_investigation
"Örnek Holding","Altyapı Tekeli","İnşaat / Enerji","İktidar İhale Ağı",2500,"OCCRP Laundromat 2023"
```
