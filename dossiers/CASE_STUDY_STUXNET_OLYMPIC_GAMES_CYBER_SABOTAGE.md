# 🕵️ Vaka Analizi: Stuxnet & Olympic Games Operasyonu - İlk Askeri Siber Silah ve Kritik Altyapı Sabotajı

> "Stuxnet was the first weapon made entirely of code that caused physical destruction in the physical world. It crossed the digital Rubicon; cyberspace ceased to be just an espionage domain and became a kinetic battlespace."  
> — **Kim Zetter**, *Countdown to Zero Day: Stuxnet and the Launch of the World's First Digital Weapon* (2014)

> "There are only two countries on earth capable of writing code this sophisticated: the United States and Israel. And they were not doing it as an academic experiment; they were doing it to delay an atomic bomb without dropping a single Tomahawk cruise missile."  
> — **Ralph Langner**, *Alman Endüstriyel Siber Güvenlik Uzmanı (Stuxnet PLC Kodunu İlk Çözen Mühendis)*

---

## 1. Yönetici Özeti ve Operasyonun Arka Planı

**Operation Olympic Games (Olimpiyat Oyunları Operasyonu)**; Amerika Birleşik Devletleri (NSA - Özel Erişim Operasyonları / TAO ve CIA) ile İsrail (Birim 8200 ve Mossad) ortaklığıyla başlatılan, tarihin ilk askeri sınıf dijital ve kinetik siber silah operasyonudur.

Operasyonun birincil hedefi; İran'ın İsfahan eyaletinde yer altında inşa edilen ve nükleer silah yapımında kullanılabilecek zenginleştirilmiş uranyum üreten **Natanz Nükleer Zenginleştirme Tesisi**'ndeki IR-1 gaz santrifüjlerini fiziksel olarak imha etmekti.

İnternetten tamamen izole edilmiş (Air-Gapped) bu tesise sızmayı başaran zararlı yazılım (**Stuxnet / Kod Adı: *Myrtus***); santrifüjleri kontrol eden endüstriyel bilgisayarları (PLC) ele geçirmiş, yaklaşık **1.000 adet santrifüjün rezonans frekansı kırılmasıyla parçalanmasını** sağlamış ve İran'ın nükleer programını en az 18-24 ay geriye atmıştır.

---

## 2. Siber Silahın Mimari ve Bulaşma Akışı

```mermaid
sequenceDiagram
    autonumber
    participant Intel as NSA / Unit 8200 (Olympic Games Lab)
    participant Contractor as İranlı Mühendislik Şirketi (Hedef Taşeron)
    participant NatanzPC as Natanz SCADA Operatör Bilgisayarı (Windows)
    participant SiemensPLC as Siemens Simatic S7-300 PLC (Endüstriyel Kontrolör)
    participant Centrifuge as IR-1 Gaz Santrifüjleri (Uranyum Kaskatları)

    Intel->>Contractor: 4 Adet Sıfır-Gün (Zero-Day) Açığı & Çalınmış Dijital Sertifikalı USB
    Contractor->>NatanzPC: Hava Boşluğu (Air-Gap) Aşımı: Mühendisin virüslü USB'yi takması
    NatanzPC->>NatanzPC: LNK açığı (CVE-2010-2568) ile kod yürütme & Rootkit gizlenmesi
    NatanzPC->>SiemensPLC: Siemens Step7 yazılımı manipülasyonu & PLC kod enjeksiyonu
    SiemensPLC->>Centrifuge: Dönüş Hızı Sabotajı: 1.064 Hz'den 1.410 Hz'e çıkartma & 2 Hz'e düşürme
    SiemensPLC-->>NatanzPC: Sahte Telemetri Gönderimi: Kontrol ekranlarında "Her Şey Normal" gösterimi
    Note over Centrifuge: Karbon fiber rotorlar rezonans titreşimiyle patlar; tesis çalışanları arızayı anlayamaz.
```

---

## 3. Teknik Üstünlükler ve Adli Bilişim Bulguları

1. **Eşi Benzeri Görülmemiş Sıfır-Gün (Zero-Day) Konsantrasyonu:**
   - Stuxnet, aynı anda **4 farklı bilinmeyen Microsoft Windows sıfır-gün açığını** (CVE-2010-2568 LNK dosyası yürütme, CVE-2010-2729 Yazıcı Kuyruğu açığı, iki adet çekirdek ayrıcalık yükseltme açığı) barındırıyordu. Siber silah pazarında bu açıkların toplam maliyeti ve geliştirme süresi yalnızca süper güç devlet laboratuvarlarınca finanse edilebilecek boyuttaydı.
2. **Çalınmış Dijital Sertifikalar:**
   - Yazılımın Windows işletim sisteminde şüphe çekmeden yüklenmesi için Tayvan'ın önde gelen yarı iletken firmaları **Realtek** ve **JMicron**'a ait meşru özel dijital imzalar çalınarak Stuxnet ikili dosyalarına gömülmüştü.
3. **Endüstriyel Sabotaj Mühendisliği (PLC Manipülasyonu):**
   - Stuxnet, yalnızca Finlandiya menşeli *Vacon* ve İran menşeli *Fararo Paya* frekans dönüştürücü sürücülere bağlı Siemens Simatic S7-300 PLC'leri hedef alıyordu. Başka hiçbir endüstriyel sisteme zarar vermeyerek kendisini hedefe kilitli bir "akıllı torpido" gibi sınırlandırmıştı.
4. **Kusursuz Aldatma (The Replay Attack):**
   - Santrifüjlerin dönüş hızını aşırı artırıp ardından aniden düşürerek mekanik rezonansla parçalanmalarına yol açarken, kontrol odasındaki monitörlere daha önce kaydedilmiş normal basınç ve titreşim verilerini yayınlıyordu. İranlı nükleer bilimciler santrifüjlerin sabotajla değil, malzeme hatası nedeniyle patladığını düşündüler.

---

## 4. Deşifre Oluş ve Siber Jeopolitiğin Doğuşu

* **Virüsün Yayılması:** Yazılıma 2009-2010 yıllarında eklenen aşırı agresif yayılma protokolü nedeniyle Stuxnet Natanz dışına sızdı; Belarus merkezli siber güvenlik firması *VirusBlokAda* tarafından Haziran 2010'da tespit edildi.
* **Hibrit Savaş Eşiğinin Aşılması:** Stuxnet, siber operasyonların konvansiyonel hava bombardımanına (örneğin İsrail'in 1981 Osirak veya 2007 El-Kibar saldırıları) ihtiyaç duymadan nükleer tesisleri felç edebileceğini kanıtladı.
* **Misillemeler Çağı:** Operasyonun ardından İran; siber kapasitesini hızla geliştirerek 2012 yılında Suudi Arabistan petrol devi **Saudi Aramco**'ya yönelik Shamoon siber saldırısını düzenledi (35.000 bilgisayarın sabit diski silindi) ve ABD bankacılık sistemine yönelik kitlesel DDoS saldırıları (*Operation Ababil*) başlattı.
