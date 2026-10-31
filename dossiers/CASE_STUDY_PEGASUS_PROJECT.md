# 🕵️ Vaka Analizi: Pegasus Projesi - Dijital Otokrasi ve Sıfır-Tıklama Siber İstihbarat

> "Pegasus turns your smartphone into a 24-hour surveillance device in your pocket. It reads your encrypted messages, turns on your microphone, tracks your GPS, and copies your passwords without you ever clicking a link."  
> — **Forbidden Stories & Amnesty International Security Lab (2021)**

> "In the 20th century, dictators needed secret police with listening vans outside your house. In the 21st century, they buy an Israeli software exploit and let Apple's own notification system deliver the spy into your bedroom."  
> — **Cyber-Intelligence OSINT Analysis**

---

## 1. Yönetici Özeti: NSO Group ve 50.000 Hedef Numara

Temmuz 2021'de 17 uluslararası medya kuruluşunun oluşturduğu **Forbidden Stories** konsorsiyumu ve **Uluslararası Af Örgütü Güvenlik Laboratuvarı**, İsrailli siber istihbarat şirketi **NSO Group** tarafından geliştirilen **Pegasus** casus yazılımının küresel çapta nasıl kötüye kullanıldığını ifşa etti.

Sızdırılan **50.000 telefon numarasından** oluşan hedef listesinde; en az 65 iş insanı, 85 insan hakları savunucusu, 189 gazeteci ve aralarında Fransa Cumhurbaşkanı Emmanuel Macron, Güney Afrika Devlet Başkanı Cyril Ramaphosa ve dönemin Pakistan Başbakanı İmran Han'ın da bulunduğu **14 devlet ve hükümet başkanı** yer almaktaydı.

---

## 2. Teknik Bilişim ve İstihbarat Mimarisi: Sıfır-Tıklama (Zero-Click)

Geleneksel oltalama (phishing) yöntemleri kullanıcının şüpheli bir linke tıklamasını gerektirirken, Pegasus **sıfır-tıklama (zero-click)** zaafiyetlerini kullanır:

```
[Saldırgan İstihbarat Servisi] 
           │
           ▼
[Görünmez iMessage / WhatsApp Bildirimi Gönderimi]
           │
           ▼
[CoreGraphics / WebKit PDF Ayrıştırıcı Taşması (FORCEDENTRY Zaafiyeti)]
           │
           ▼
[iOS Sandbox İhlali & Root/Kernel Yetkisi Elde Edilmesi]
           │
           ▼
[Şifreli Veri Çekimi (Signal, WhatsApp, Telegram, Kamera, Mikrofon)]
           │
           ▼
[Komuta Kontrol (C2) Sunucusuna Şifreli Telemetri Aktarımı]
```

---

## 3. Belgelenen İnsan Hakları İhlalleri ve Hedefler

1. **Cemal Kaşıkçı Cinayeti (2018):**
   - Suudi Arabistan muhalifi gazeteci Cemal Kaşıkçı'nın nişanlısı Hatice Cengiz'in, oğlu Abdullah'ın ve yakın çalışma arkadaşı Ömer Abdülaziz'in telefonlarına cinayet öncesinde ve sonrasında Pegasus yüklendiği adli bilişim raporlarıyla kanıtlandı.
2. **Meksika Narko-Siyaset İttifakı:**
   - Meksika hükümeti ve ordu istihbaratı (SEDENA), uyuşturucu kartellerinin cinayetlerini soruşturan bağımsız gazeteci Cecilio Pineda Birto'yu Pegasus ile takip etti; Pineda telefonunun izlenmesinden birkaç hafta sonra katledildi.
3. **Avrupa Birliği Skandalları:**
   - İspanya'da Katalan siyasetçilerin, Polonya'da muhalefet liderlerinin ve Yunanistan'da gazetecilerin bizzat ulusal istihbarat servisleri tarafından dinlendiği doğrulandı.
