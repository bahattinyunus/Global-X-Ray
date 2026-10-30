# 🔍 OSINT Doğrulama ve Teyit Standartları (OSINT Verification Standards)

**Küresel Röntgen** projesi, bilgi kirliliğini önlemek ve analiz kalitesini en üst düzeyde tutmak amacıyla katı bir istihbarat ve OSINT doğrulama protokolü uygular.

---

## 🏷️ Kaynak Güvenilirlik Sınıflandırması (Admiralty Code / NATO Standardı)

Veriler ve iddialar değerlendirilirken NATO standartlarındaki kaynak güvenilirlik matrisi esas alınır:

### Kaynak Güvenilirliği (Source Reliability)
- **A - Tamamen Güvenilir:** Bağımsız uluslararası denetçiler, resmi mahkeme kararları, teyitli veri sızıntıları (ICIJ veri tabanı).
- **B - Genellikle Güvenilir:** Saygın araştırmacı gazetecilik ağları (OCCRP, Bellingcat, ICIJ), akademik hakemli yayınlar.
- **C - Kısmen Güvenilir:** Yerel muhalif medya, tek taraflı sivil toplum raporları.
- **D - Şüpheli / Teyitsiz:** Sosyal medya paylaşımları, anonim ihbarlar.
- **E - Güvenilmez:** Doğrudan devlet kontrolündeki propaganda veya dezenformasyon bültenleri.

### Bilgi Doğruluğu (Information Credibility)
- **1 - Teyit Edilmiş (Confirmed):** Bağımsız birden fazla kaynak tarafından doğrulanmış.
- **2 - Muhtemelen Doğru (Probably True):** Mantıksal çerçeveyle örtüşen, kısmen doğrulanmış.
- **3 - Olası (Possibly True):** Doğrulayıcı kanıt bulunmayan ancak bağlamla çelişmeyen.
- **4 - Şüpheli (Doubtful):** Mantıksal tutarsızlıklar içeren.
- **5 - Olanaksız (Improbable):** Çürütülmüş veya kasıtlı çarpıtma.

> **Kural:** Repoda Katman 4 altında yer alacak iddialar en az **B2** (Genellikle Güvenilir kaynak + Muhtemelen Doğru bilgi) veya **A1** standardında olmalıdır.

---

## 🛡️ Teyit Adımları

1. **Çapraz Doğrulama (Triangulation):** Önemli bir yolsuzluk veya oligark-siyaset ilişkisi iddiası en az iki bağımsız kaynakça zikredilmelidir.
2. **Ticari Sicil ve Mülkiyet Doğrulaması:** Şirket ilişkileri ve ihale kazananları, ilgili ülkenin resmi ticaret sicil gazetesi veya sızdırılmış offshore veri tabanlarıyla eşleştirilmelidir.
3. **Mali İz Takibi:** Kara para aklama veya servet transferi iddialarında bankacılık düzenleyici kurumları (FinCEN dosyaları vb.) veya mahkeme iddianameleri referans verilmelidir.
4. **Metin İçi Alıntı Zorunluluğu:** 
   ```markdown
   Örnek format:
   - Şirket X, 2021 yılında 4.2 milyar dolarlık otoyol ihalesini rekabetsiz kazanmıştır [[1] OCCRP Investigation, 2022](https://www.occrp.org).
   ```

---

## ❌ Kabul Edilmeyen İçerikler

- Kaynak belirtilmemiş dedikodular ve anonim blog yazıları.
- Doğrudan nefret söylemi, ırkçı veya ayrımcı genellemeler.
- Çürütülmüş dezenformasyon anlatıları.
