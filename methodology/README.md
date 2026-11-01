# 🔬 Metodoloji ve OSINT Araştırma Kılavuzları (/methodology)

> *"Bir iddianın değeri, onu destekleyen delilin doğrulanabilirlik derecesi kadardır. İstihbarat analizinde inançlar değil, kanıt zinciri ve çapraz teyit esastır."*

Bu dizin, **Medeniyet Atlası** projesinde kullanılan açık kaynak istihbaratı (OSINT), şirket sicil taramaları, siber telemetri ve adli veri doğrulama yönergelerini içerir.

---

## 📑 Metodolojik Kılavuzlar

| Kılavuz Dosyası | Alanı | Temel İçerik & Yöntem |
| :--- | :--- | :--- |
| 🏢 [**CORP_REGISTRY_RECONNAISSANCE.md**](CORP_REGISTRY_RECONNAISSANCE.md) | **Şirket Sicil Taraması & UBO Tespiti** | Britanya Virjin Adaları (BVI), Delaware, İngiltere Companies House, Lüksemburg RCS, İsviçre ve Panama ticaret sicillerinde paravan şirketlerin Nihai Faydalanıcı Mülkiyet (Ultimate Beneficial Ownership) tespiti yöntemleri. |
| 🌐 [**DATA_COLLECTION_GUIDE.md**](DATA_COLLECTION_GUIDE.md) | **Çok Kaynaklı Veri Toplama Yönergesi** | Uydu görüntüleri (Copernicus Sentinel / Planet Labs), gemi takip telemetrisi (AIS / MarineTraffic), uçuş radarı (ADS-B Exchange), gümrük konşimentoları (ImportGenius) ve siber iz sürme teknikleri. |
| 🛡️ [**OSINT_VERIFICATION.md**](OSINT_VERIFICATION.md) | **NATO / Admiralty Doğrulama Standardı** | STANAG 2097 Admiralty Kod değerlendirme matrisi (A1'den F6'ya); dijital görüntü adli bilişimi (EXIF metadata, ELA analizi), tersine görsel arama ve dezenformasyon filtreleme protokolleri. |

---

## 🎯 NATO Admiralty Doğrulama Standardı Özeti

Medeniyet Atlası'na entegre edilen tüm kritik iddialar ve adli bulgular **en az B2 (Genellikle Güvenilir / Muhtemelen Doğru)** düzeyinde olmak zorundadır:

* **Kaynak Güvenilirliği:** A (Tamamen Güvenilir) &bull; B (Genellikle Güvenilir) &bull; C (Oldukça Güvenilir)
* **Bilgi Doğruluğu:** 1 (Teyit Edilmiş) &bull; 2 (Muhtemelen Doğru) &bull; 3 (Mümkün)
