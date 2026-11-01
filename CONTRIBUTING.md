# 🤝 Katkıda Bulunma Rehberi (Contributing to Medeniyet Atlası)

**Medeniyet Atlası** projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Dünya genelinde kültürleri derinlemesine tanımak, medeniyet kodlarını keşfetmek, çevrilemeyen ruh kavramlarını derlemek ve şeffaf/bağımsız bir güç analizi sunmak için her katkı değerlidir.

---

## 🚀 Katkı Alanları

Medeniyet Atlası'na dört ana eksende katkı sunabilirsiniz:
1. **Kültür, Sanat & Yaşam Felsefesi (Katman 1):** Ülkelerin gündelik yaşam ritüelleri, dilsel ruh kavramları, gastronomi felsefeleri, mimari mirasları ve görgü kuralları (`01_culture_demographics/`).
2. **Resmi Devlet & Anayasal Düzen (Katman 2):** Anayasa maddeleri, kuvvetler ayrılığı yapısı ve seçim mevzuatı (`02_official_state/`).
3. **Resmi Makroekonomi & Ticaret (Katman 3):** GSYİH, ihracat-ithalat kalemleri, kamu borcu ve döviz rezervleri (`03_official_economy/`).
4. **Gölge Güç, Kleptokrasi & OSINT (Katman 4):** Oligarşik sermaye konsorsiyumları, medya tekelleri ve gölge ekonomi dinamikleri (`04_shadow_power_osint/`).

---

## 🛠️ Başlarken

1. Depoyu fork'layın ve klonlayın:
   ```bash
   git clone https://github.com/bahattinyunus/medeniyet-atlasi.git
   cd medeniyet-atlasi
   ```
2. Yeni bir çalışma dalı (branch) oluşturun:
   ```bash
   git checkout -b ulke/ulke-adi
   ```
3. İlgili ülkenin veya kültür dosyasının dizininde düzenlemelerinizi yapın.
4. Katman 4 veya istihbarat verisi ekliyorsanız, [`methodology/OSINT_VERIFICATION.md`](methodology/OSINT_VERIFICATION.md) gereğince **en az B2** (Genellikle Güvenilir / Muhtemelen Doğru) standardında kaynak bağlantısı sağlayın.
5. Otomatik bütünlük testlerini çalıştırın:
   ```bash
   python tests/test_integrity.py
   ```
6. Değişikliklerinizi commit edin ve Pull Request açın:
   ```bash
   git commit -m "feat(japonya): 01_culture Wabi-sabi ve zanaat felsefesi genişletildi"
   git push origin ulke/ulke-adi
   ```

---

## 📌 PR (Pull Request) İlkeleri

- **Açıklayıcı Başlık:** Hangi ülke, kültür veya veri setinin güncellendiğini açıkça belirtin.
- **Kaynak Teyidi:** Adli veya makroekonomik güncellemelerde resmi rapor veya uluslararası denetim bağlantısı ekleyin.
- **Biçimlendirme Uyumu:** Markdown başlık yapısını, JSON şemalarını ve CSV formatını bozmayın.
- **Üslup & Tarafsızlık:** Tarafsız, ansiklopedik, kültürel zenginliğe hürmetkar ve kanıta dayalı bir dil kullanın.
