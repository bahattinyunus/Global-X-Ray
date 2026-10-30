# 🤝 Katkıda Bulunma Rehberi (Contributing to Küresel Röntgen)

Küresel Röntgen projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Dünya genelinde şeffaflık, hesap verebilirlik ve bağımsız istihbarat analizini güçlendirmek için her katkı değerlidir.

---

## 🚀 Başlarken

1. Repoyu fork'layın:
   ```bash
   git clone https://github.com/arch-yunus/Global-X-Ray.git
   cd Global-X-Ray
   ```
2. Yeni bir dal (branch) açın:
   ```bash
   git checkout -b ulke/ulke-adi
   ```
3. İlgili ülkenin `regions/<bolge>/<ulke_adi>` klasöründe güncellemeleri yapın veya şablonu kullanarak eksik bir ülkeyi ekleyin.
4. `methodology/OSINT_VERIFICATION.md` kurallarına uygun olarak kaynak linklerini iliştirin.
5. Değişikliklerinizi commit edin ve Pull Request açın:
   ```bash
   git commit -m "feat(russia): 04_shadow_power oligark ağı ve yaptırım verileri güncellendi"
   git push origin ulke/ulke-adi
   ```

---

## 📌 PR (Pull Request) Standartları

- **Açıklayıcı Başlık:** Hangi ülke ve hangi katmanın güncellendiğini belirtin (`feat(turkey): medya sahipliği matrisi eklendi`).
- **Kaynak Gösterimi:** Katman 4 güncellemelerinde mutlaka rapor veya belge bağlantısı ekleyin.
- **Biçimlendirme Uyumu:** Markdown başlıklarını, JSON anahtar isimlerini ve CSV sütun düzenini bozmayın.

---

## ⚖️ Davranış Kuralları

- Tarafsız, analitik ve kanıta dayalı bir üslup kullanın.
- Herhangi bir siyasi parti veya devleti övmek veya yermek yerine somut olguları, ihale verilerini ve kurumsal ilişkileri listeleyin.
