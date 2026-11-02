# 🛠️ Geliştirici ve Analist Komut Satırı Araçları (/scripts)

> *"Büyük veri havuzları ancak güçlü ve ergonomik sorgu araçlarıyla anlam kazanır."*

Bu dizin, **Medeniyet Atlası** veri tabanını komut satırından sorgulamak, ülkeleri kültürel ve jeopolitik olarak karşılaştırmak, otomatik keşif raporları üretmek ve proje belgelerini derlemek için geliştirilmiş Python motorlarını içerir.

---

## 📑 Komut Dosyaları Kataloğu

| Araç | Açıklama | Örnek Çalıştırma |
| :--- | :--- | :--- |
| 💻 [**`xray_cli.py`**](xray_cli.py) | **Merkezi CLI Terminal Sorgu Motoru** | `python scripts/xray_cli.py country turkiye`<br/>`python scripts/xray_cli.py rank gdp 10`<br/>`python scripts/xray_cli.py export almanya --format md`<br/>`python scripts/xray_cli.py stats --json` |
| 🎯 [**`deep_recon.py`**](deep_recon.py) | **Çok Katmanlı Derin Keşif Motoru** | `python scripts/deep_recon.py almanya`<br/>`python scripts/deep_recon.py --export turkiye` |
| 📚 [**`build_culture_dossiers.py`**](build_culture_dossiers.py) | **Kültür Kütüphanesi Derleme Motoru** | `python scripts/build_culture_dossiers.py` |
| 📄 [**`generate_master_readme.py`**](generate_master_readme.py) | **Master README.md Otomasyon Motoru** | `python scripts/generate_master_readme.py` |
| 🧬 [**`enrich_country_cultural_files.py`**](enrich_country_cultural_files.py) | **Ülke Kültür Katmanı Senkronizasyonu** | `python scripts/enrich_country_cultural_files.py` |

---

## 💻 `xray_cli.py` Hızlı Kullanım Rehberi

```bash
# Bir ülkenin 4 katmanlı tam profilini terminalde görüntüle
python scripts/xray_cli.py country almanya

# Bir ülkenin kültürel kodlarını ve çevrilemeyen kavramlarını incele
python scripts/xray_cli.py culture japonya

# İki ülkeyi kültürel DNA, sofra ritüelleri ve tabular açısından karşılaştır
python scripts/xray_cli.py compare-culture turkiye almanya

# Küresel güç ve kırılganlık matrisini sırala (csfi, gdp, shadow, percapita)
python scripts/xray_cli.py rank gdp 15
python scripts/xray_cli.py rank shadow 20

# Bir ülkenin tüm katmanlarını ve kültürel DNA'sını tek bir rapor olarak dışa aktar
python scripts/xray_cli.py export turkiye --format md --out REPOR_TURKIYE.md
python scripts/xray_cli.py export japonya --format json

# Makine tarafından okunabilir JSON çıktısı al (--json bayrağı)
python scripts/xray_cli.py stats --json
python scripts/xray_cli.py country fransa --json
python scripts/xray_cli.py alliances nato --json

# 14 büyük kurucu dünya destanını sorgula
python scripts/xray_cli.py epics

# Dünya kutsal mimari ekollerini ve şehir felsefesini sorgula
python scripts/xray_cli.py architecture

# Dünya geleneksel çalgılarını ve ses mirasını sorgula
python scripts/xray_cli.py music

# Dünya festivalleri ve kutsal ritüellerini sorgula
python scripts/xray_cli.py festivals

# Stratejik nükleer triad ve cephanelikleri incele
python scripts/xray_cli.py nuclear usa

# İstihbarat servislerini ve operasyonlarını incele
python scripts/xray_cli.py intel mit

# Canlı interaktif sorgu kabuğunu (shell) başlat
python scripts/xray_cli.py interactive
```
