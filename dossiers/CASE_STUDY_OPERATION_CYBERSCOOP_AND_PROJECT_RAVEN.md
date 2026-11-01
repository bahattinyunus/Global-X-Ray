# 🕵️ Vaka Analizi: Proje Raven (Project Raven) & DarkMatter - Emirlikler'in Eski NSA Paralı Siber Ordusu ve "Karma" Sıfır-Tık Operasyonu

> "You work for the United States government for a decade protecting freedom, and then you wake up in an Abu Dhabi skyscraper realizing you are helping a foreign monarchy hunt down political activists and monitor American journalists using top-secret zero-click exploits."  
> — **Lori Stroud**, *Eski NSA Siber Operatörü ve Project Raven İfşacısı (Whistleblower, 2019)*

> "Project Raven represents the ultimate privatization of military-grade cyber weapons. It proved that state-sponsored cyber warfare capabilities developed at Fort Meade can be bought off the shelf by petro-monarchies to conduct totalitarian surveillance worldwide."  
> — **Christopher Bing & Joel Schectman**, *Reuters Özel Araştırma Dosyası: 'Inside the UAE's Secret Hacking Team' (2019)*

---

## 1. Yönetici Özeti ve Operasyonun Arka Planı

**Project Raven (Kuzgun Projesi)**; Birleşik Arap Emirlikleri (BAE) Ulusal Elektronik Güvenlik Otoritesi (NESA) adına, ABD Ulusal Güvenlik Ajansı (NSA) ve CIA kökenli eski Amerikalı siber istihbarat operatörleri tarafından yürütülen son derece gizli bir ofansif siber casusluk programıdır.

İlk olarak 2009 yılında Maryland merkezli ABD savunma taşeronu **CyberPoint International** aracılığıyla meşru bir siber savunma danışmanlığı kılıfıyla başlatılan operasyon, kısa süre içinde BAE'nin istihbarat şirketi **DarkMatter** bünyesine aktarılmış ve küresel bir siber paralı asker (cyber mercenary) ordusuna dönüşmüştür.

Projenin en ölümcül silahı; hiçbir kullanıcı etkileşimi gerektirmeyen (zero-click), hedef kullanıcının haberi olmadan yalnızca arka planda bir iMessage göndererek iPhone cihazları tamamen ele geçiren **"Karma"** adlı sıfır-gün istismar zinciriydi. Proje kapsamında Katar Emiri'nden Türk bürokratlara, Nobel adayı insan hakları savunucularından Amerikalı gazetecilere kadar yüzlerce kişi yasa dışı olarak hedef alınmıştır.

---

## 2. Operasyonel Mimari ve Karma Sıfır-Tık Sızma Zinciri

```mermaid
sequenceDiagram
    autonumber
    participant Target as Hedef Telefon (iPhone / iOS)
    participant APNs as Apple Bildirim Sunuculari (APNs)
    participant Raven as Raven Kontrol Sunuculari (Abu Dabi Villa)
    participant Operatives as BAE / Eski NSA Siber Operatörleri
    participant DarkMatter as DarkMatter & NESA BAE Karargahı

    Operatives->>Raven: Hedef Telefon Numarası veya Apple ID Girilmesi
    Raven->>APNs: "Karma" Sıfır-Tık (Zero-Click) Exploit Taşıyan Gizli iMessage
    APNs->>Target: Arka Plan Bildirimi (Kullanıcı Ekranında Hiçbir Şey Görünmez)
    Target->>Target: iMessage Görüntü İşleme Kütüphanesi Açığı ile Bellek Taşması
    Target->>Raven: Arka Kapı Kurulumu & Şifreli Cihaz Anahtarlarının Sızdırılması
    Raven->>Target: Anlık İndirme: Konum, SMS, WhatsApp, Fotoğraflar, E-postalar, Ortam Dinleme
    Raven-->>DarkMatter: Günlük İstihbarat Raporu ve Hedef İzleme Kayıtları
    Note over Target,DarkMatter: Hedef asla tıklama yapmadı; cihaz tamamen klonlandı.
```

---

## 3. Temel Operasyonel Araçlar ve "Karma" İstismarının Anatomisi

1. **Karma Exploit Platformu (2016-2017):**
   * BAE, bu sıfır-tık saldırı kodunu yurt dışındaki gizli bir güvenlik firmasından (iddialara göre İsrailli veya Avrupalı bir broker) yüz binlerce dolar ödeyerek satın aldı.
   * Karma; kurbanın herhangi bir bağlantıya (link) tıklamasına ihtiyaç duymadan cihazı enfekte edebiliyordu. Bu özellik, hedefin şüphelenmesini imkansız kılıyordu.
   * Cihazdaki fotoğraflara, e-postalara, şifreli mesajlaşma uygulamalarına ve gerçek zamanlı GPS konum verilerine tam erişim sağlıyordu.
2. **Kapsam Genişlemesi ve Hedef Profilleme:**
   * **Katar Krizi (2017):** BAE ve Suudi Arabistan'ın Katar'a abluka uyguladığı dönemde, Katar Emiri Şeyh Tamim bin Hamad Al Thani, Katar Dışişleri Bakanı ve kraliyet ailesi mensuplarının telefonları Karma ile dinlendi.
   * **Türkiye ve Müslüman Kardeşler:** Türkiye ve Katar arasındaki askeri ittifak nedeniyle Türk bürokratlar, diplomatlar ve bölgedeki muhalif ağlar izleme listesine alındı.
   * **İnsan Hakları Savunucuları:** Emirlik rejimini eleştiren insan hakları aktivisti **Ahmed Mansoor** ("Bir Milyon Dolarlık Muhalif"), Karma ve Pegasus yazılımlarıyla yıllarca takip edildi ve 2017'de tutuklanarak 10 yıl hapis cezasına çarptırıldı.
3. **"Amerikalıların İzlenmesi" ve Kriz Anı:**
   * Operasyonun dönüm noktası, Amerikalı operatörlere kendi vatandaşlarını (ABD pasaportlu gazeteciler, insan hakları çalışanları ve diplomatlar) hedef alma talimatının verilmesi oldu. Bu durum, ABD İhracat Kontrol Kanunu (ITAR) ve Bilgisayar Dolandırıcılığı ve Kötüye Kullanımı Yasası'nın (CFAA) doğrudan ihlali anlamına geliyordu.

---

## 4. İfşa Süreci ve Hukuki Hesaplaşma

| Aşama / Olay | Detaylar ve Gelişmeler | Hukuki ve Jeopolitik Netice |
| :--- | :--- | :--- |
| **Lori Stroud'un İfşası** | Eski NSA ajanı Lori Stroud, ekibin Amerikalıları izlediğini fark edip delilleri toplayarak projeden ayrıldı ve durumu FBI'a bildirdi. | FBI karşı-istihbarat soruşturması başlattı. |
| **Reuters Küresel Araştırması (Ocak 2019)** | Christopher Bing ve Joel Schectman'ın *"Inside the UAE's secret hacking team of American mercenaries"* başlıklı yazı dizisi operasyonu tüm kod adlarıyla kamuoyuna duyurdu. | BAE'nin siber paralı asker operasyonu uluslararası bir skandala dönüştü. |
| **ABD Adalet Bakanlığı (DOJ) Anlaşması (Eylül 2021)** | Projenin tepe yöneticisi eski NSA/savunma taşeronu 3 Amerikalı (*Marc Baier, Ryan Adams, Daniel Gericke*), federal mahkemede suçlamaları kabul etti. | **1.68 Milyon Dolar** ceza ödemeyi, ABD güvenlik yetkilerini tamamen devretmeyi ve gelecekte siber istihbarat yapmamayı kabul ettiler (Deferred Prosecution Agreement). |
| **DarkMatter'ın Tasfiyesi ve CPX Dönüşümü** | DarkMatter uluslararası kara listelere ve yaptırım baskılarına maruz kalınca kapatıldı; kadroları **G42** ve **CPX (Cyber Perimeter X)** adlı yeni holdingler altında yeniden yapılandırıldı. | BAE'nin yapay zeka ve siber gözetim yatırımları G42 (Group 42) çatısına taşındı. |

---

## 5. Siber Jeopolitiğe Etkisi ve Alınan Dersler

1. **İstihbarat Gücünün Özelleşmesi (Privatization of State Espionage):**
   - Project Raven; en gelişmiş devlet istihbarat eğitimini almış personelin, yüksek maaş teklif eden otokratik petro-monarşilere kolaylıkla satılabileceğini kanıtladı.
2. **Sıfır-Tık (Zero-Click) Devri:**
   - Siber gözetim sektörünün geleneksel oltalama (phishing) taktiklerinden çıkıp, doğrudan işletim sistemi çekirdeklerini hedef alan görünmez sıfır-tık silahlarına geçtiğini tescilledi.
3. **Yaptırımlar ve İhracat Rejimi Dönüşümü:**
   - ABD Ticaret Bakanlığı, bu skandalın ardından DarkMatter ve NSO Group gibi ticari siber gözetim firmalarını Varlık Listesi'ne (Entity List) alarak Amerikan menşeli yazılım ve donanım satışını yasakladı.

---

## 6. Araştırma ve Teftiş Kaynakları

* **Reuters Soruşturma Serisi (2019):** Christopher Bing & Joel Schectman, *"Project Raven: UAE Hacking Operation"*, Reuters Investigates.
* **ABD Adalet Bakanlığı (DOJ) Resmi Tebliği (14 Eylül 2021):** *Three Former U.S. Intelligence Community and Military Personnel Agree to Pay More Than \$1.68 Million to Resolve Criminal Charges for Assisting UAE in Unauthorized Cyber Operations*.
* **Citizen Lab Analizleri (Toronto Üniversitesi):** *The Million Dollar Dissident: NSO Group's Pegasus and DarkMatter Spyware Targets in the UAE* (Bill Marczak & John Scott-Railton).
* **Kitap:** Nicole Perlroth, *This Is How They Tell Me the World Ends: The Cyberweapons Arms Race*, Bloomsbury (2021).
