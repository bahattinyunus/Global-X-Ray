# -*- coding: utf-8 -*-
"""
scripts/build_culture_dossiers.py
Generates the rich encyclopedic cultural dossiers under `culture/`:
- UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md
- GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md
- WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md
- CIVILIZATION_REALMS_AND_PHILOSOPHIES.md
- README.md
"""

import sys
import json
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
CULTURE_DIR = BASE_DIR / "culture"
DATA_DIR = BASE_DIR / "global_datasets"

CULTURE_DIR.mkdir(exist_ok=True)

with open(DATA_DIR / "cultural_codes_and_civilizations_registry.json", "r", encoding="utf-8") as f:
    culture_data = json.load(f)

# 1. Untranslatable Concepts Encyclopedia
def build_untranslatable():
    countries = culture_data.get("countries_cultural_dna", [])
    rows = []
    for c in countries:
        for w in c.get("untranslatable_soul_concepts", []):
            rows.append(f"| **{w['word']}** | {c['country']} (`{c['code']}`) | {w['meaning']} |")

    content = f"""# 📖 Çevrilemeyen Ruh Kavramları Ansiklopedisi (The Untranslatable Soul Words)

> "Dil, varlığın evidir. Bir ulusun en derin felsefesi, başka hiçbir dile tam olarak tercüme edilemeyen kelimelerinde kristalleşir."  
> — **Martin Heidegger**

Dünya dillerinde yalnızca bir kelimeyle ifade edilen ancak arkasında bin yıllık kolektif hafızayı, sevinçleri, kederleri ve yaşam felsefesini barındıran kavramlar atlası:

---

## 🌍 Küresel Kavramlar Tablosu

| Kavram | Köken Ülke | Kültürel & Felsefi Anlamı |
| :--- | :--- | :--- |
{chr(10).join(rows)}

---

## 🔍 Öne Çıkan Kavramların Derinlemesine Çözümlemesi

### 🇹🇷 1. Gönül (Türkçe)
* Kalp (biyolojik organ) veya zihin (akıl) kelimelerinden tamamen farklıdır. Sevginin, kırılganlığın, affetmenin ve manevi arzuların taht kurduğu içsel kutsal mekandır. Bir insanın "gönlüne girmek" en büyük başarı, "gönül kırmak" ise Kâbe'yi yıkmak kadar ağır bir günahtır.

### 🇯🇵 2. Mono no Aware (Japonca)
* "Nesnelerin ve olayların geçiciliğine duyulan derin dokunaklı hüzün." Özellikle baharda açıp bir iki hafta içinde dökülen kiraz çiçeklerinin (sakura) güzelliği, geçici olduğu için bu denli kıymetlidir. Fanilik acı değil, estetik bir derinliktir.

### 🇩🇪 3. Gemütlichkeit (Almanca)
* Sıcak, güvenli, telaşsız ve samimi bir aidiyet duygusu. Dostlarla tahta bir masada oturup acele etmeden bir şeyler içerken hissedilen o huzurlu dinginlik.

### 🇧🇷 4. Saudade (Portekizce / Brezilya)
* Kaybedilen veya uzakta kalan bir sevgiye, çocukluğa, memlekete duyulan derin, nostaljik sızı. İçinde hem acı hem de geçmişte onu yaşamış olmanın tatlı minneti bulunur.

### 🇪🇸 5. Sobremesa (İspanyolca)
* Yemek bittikten sonra tabaklar boşalsa bile saatlerce masadan kalkmadan, kahve veya içecek eşliğinde dostlarla yapılan o derin, neşeli ve kahkahalı sohbet dönemi.

### 🇿🇦 6. Ubuntu (Zuluca / Xhosaca)
* "Umuntu ngumuntu ngabantu" ("Ben, biz olduğumuz için benim"). İnsanlığın birbirine görünmez bağlarla kenetlendiği, bir bireyin acısının tüm toplumun acısı olduğu inancı.

### 🇷🇺 7. Toska (Rusça)
* Vladimir Nabokov'un ifadesiyle: "Hiçbir belirgin sebebi olmayan, insanın göğsünü sıkıştıran, sonsuz bozkırlara ve ruhun derinliklerine bakan büyük manevi sızı ve metafizik hasret."
"""
    with open(CULTURE_DIR / "UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md", "w", encoding="utf-8") as f:
        f.write(content)

# 2. Global Gastronomy & Table Rituals
def build_gastronomy():
    countries = culture_data.get("countries_cultural_dna", [])
    rows = []
    for c in countries:
        rows.append(f"| **{c['country']}** (`{c['code']}`) | {c['gastronomic_philosophy']} |")

    content = f"""# 🍲 Dünya Mutfakları, Gastronomi Felsefesi ve Sofra Ritüelleri

> "Bana ne yediğini söyle, sana kim olduğunu söyleyeyim."  
> — **Jean Anthelme Brillat-Savarin** (*Le Physiologie du Goût*, 1825)

Yemek; yalnızca biyolojik bir karın doyurma eylemi değil, bir toplumun doğayla kurduğu ilişkinin, ikram geleneğinin ve medeniyet hafızasının en somut göstergesidir.

---

## 🍽️ 20 Medeniyetin Sofra ve Mutfak Felsefesi

| Ülke / Medeniyet | Gastronomi Felsefesi & Sofra Adabı |
| :--- | :--- |
{chr(10).join(rows)}

---

## 🌾 Temel Mutfak Ekolleri ve Kültürel Kutsallar

1. **Ekmek ve Bereket Kültürü (Anadolu & Akdeniz):** Ekmek nimettir; yere düşerse öpülüp başa konur. Sofra, ailenin ve misafirin ortak dualarla birleştiği kutsal bir çemberdir.
2. **Washoku & Doğallık (Japonya - UNESCO Mirası):** Malzemenin doğallığını bozmadan, mevsimselliğine (Shun) saygı duyarak sunma sanatı. Yemekte renk, koku ve geometrik sunum felsefesi.
3. **Ayurveda & Baharat Simyası (Hindistan):** Baharatlar tatlandırıcı değil, bedenin ve zihnin dengesini kuran tıbbi şifa kaynaklarıdır.
4. **Fermantasyon & Dayanıklılık (Kore):** Zorlu kış şartlarına karşı sebzeleri toprağın altında fermente ederek (Kimchi, Gochujang) yaşatma bilgeliği.
5. **Ateş & Paylaşım Kültürü (Latin Amerika & Afrika):** Asado ve Braai; etin açık ateşte saatlerce pişirilmesi bahanesiyle tüm mahallenin ve ailenin gün boyu bir arada şarkılarla toplanmasıdır.
"""
    with open(CULTURE_DIR / "GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md", "w", encoding="utf-8") as f:
        f.write(content)

# 3. Etiquette & Taboos
def build_etiquette():
    countries = culture_data.get("countries_cultural_dna", [])
    rows = []
    for c in countries:
        rows.append(f"| **{c['country']}** (`{c['code']}`) | {c['social_taboos_and_etiquette']} | {c['communication_style']} |")

    content = f"""# 🚫 Küresel Görgü Kuralları, İletişim Kodları ve Sosyal Tabular (Do's & Don'ts)

Farklı kültürlerde saygı ifadesi olan bir davranış, başka bir coğrafyada en ağır hakaret sayılabilir. Yabancı bir ülkede saygın ve görgülü bir misafir olmanın altın anahtarları:

---

## 🌐 20 Ülkenin Sosyal Tabuları ve İletişim Kodları

| Ülke | Görgü Kuralları & Sosyal Tabular (Kaçınılması Gerekenler) | İletişim Tarzı (High/Low Context) |
| :--- | :--- | :--- |
{chr(10).join(rows)}

---

## 🧭 İletişim Tarzı Ayrımı: Yüksek Bağlam (High Context) vs Düşük Bağlam (Low Context)

* **Yüksek Bağlamlı Toplumlar (Japonya, Türkiye, Çin, İran, Arap Dünyası):**
  - Sözcüklerin doğrudan anlamından ziyade beden dili, ses tonu, ortamın havası ve geçmiş ilişkiler önemlidir.
  - "Hayır" doğrudan denmez; dolaylı yollardan ima edilir. Muhatabın yüzünü kaybetmemesi (Mianzi) esastır.
* **Düşük Bağlamlı Toplumlar (Almanya, İsveç, ABD, Hollanda):**
  - Mesaj doğrudan, net, rasyonel ve şeffaftır. Ne söyleniyorsa anlamı odur.
  - İmalı konuşmak belirsizlik ve amatörlük sayılır; doğrudan geri bildirim saygının gereğidir.
"""
    with open(CULTURE_DIR / "WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(content)

# 4. Civilizations & Philosophies
def build_civilizations():
    realms = culture_data.get("civilization_realms", [])
    rows = []
    for r in realms:
        rows.append(f"| **{r['name']}** | {r['core_philosophy']} | `{', '.join(r['representative_states'])}` |")

    content = f"""# 🏛️ Küresel Medeniyet Havzaları ve Tarihsel Düşünce Külliyatı

İnsanlık tarihi, belirli coğrafi iklimlerde ve manevi köklerde filizlenen büyük medeniyetlerin birikimidir:

---

## 🌐 9 Büyük Küresel Medeniyet Havzası

| Medeniyet Havzası | Temel Felsefe & Toplumsal Ethos | Temsilci Ülkeler |
| :--- | :--- | :--- |
{chr(10).join(rows)}

---

## 🌿 Medeniyetlerin Yaşam Felsefeleri

1. **Anadolu & Akdeniz Havzası:** Kavşak medeniyeti. Bozkır hürriyeti, İslam tasavvufu (Yunus Emre, Mevlana) ve Roma/Bizans idari mirası. Temelinde "İnsanı yaşat ki devlet yaşasın" ve "Gönül Çerağı" vardır.
2. **Doğu Asya Sinik Havzası:** Konfüçyüs'ün sosyal nizamı, Laozi'nin Tao (Yol) dengesi ve Budist sabır. Birey toplumun içinde eriyerek ahengi (Wa) sağlar.
3. **Cermen-İskandinav Havzası:** Aydınlanma aklı, Protestan iş ahlakı, doğayla bütünleşen Lagom dengesi ve toplum sözleşmesine dayalı sarsılmaz güven.
4. **Anglo-Sakson Havzası:** Locke, Smith ve Mill'in bireysel hürriyet felsefesi; pragmatizm, hukuk devleti ve girişimcilik cesareti.
5. **Slav-Avrasya Havzası:** Sonsuz bozkırların geniş ruhu (Dusha), Ortodoks tefekkürü, çilekeş dayanıklılık ve metafizik arayışlar.
6. **Latin Amerika Havzası:** Büyülü gerçekçilik (Gabriel García Márquez), yerli şamanik doğa bağı ve Akdeniz'in sıcak sokak neşesi.
7. **Orta Doğu & Fars Havzası:** İrfan, şiir, zarafet (Ta'arof), Cömertlik (Kerem) ve kadim İpek Yolu ticaret ahlakı.
8. **Güney Asya Dharmik Havzası:** Karma, Dharma ve Moksha kozmolojisi; kainattaki tüm canlılara saygı (Ahimsa) ve sonsuz çoğulculuk.
9. **Sahra Altı Afrika Ubuntu Havzası:** İnsanın topluluk içinde var olduğu, ritmik müzik, dans ve sözlü tarih geleneğiyle yaşayan kolektif insan sevgisi.
"""
    with open(CULTURE_DIR / "CIVILIZATION_REALMS_AND_PHILOSOPHIES.md", "w", encoding="utf-8") as f:
        f.write(content)

# 5. Master README for culture
def build_culture_index():
    content = """# 🏛️ Medeniyet Atlası: Kültür, Yaşam Felsefesi ve Medeniyetler Külliyatı (/culture)

Bu dizin, dünya uluslarının **kültürel kodlarını, çevrilemeyen ruh kavramlarını, mutfak felsefelerini, görgü kurallarını ve kadim medeniyet havzalarını** derinlemesine inceleyen ansiklopedik referans kütüphanesidir.

---

## 📑 Kültürel Dosya Dizini

| Dosya | Konu | Temel Kapsam & İçerik |
| :--- | :--- | :--- |
| 📖 [**UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md**](UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md) | Çevrilemeyen Ruh Kavramları | Türkçe *Gönül, Hüzün, İmece*, Japonca *Ikigai, Wabi-sabi*, Almanca *Gemütlichkeit*, Portekizce *Saudade*, Zuluca *Ubuntu* dahil 50+ derin kavram. |
| 🍲 [**GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md**](GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md) | Mutfaklar & Sofra Adabı | Anadolu bereket sofrası, Japon Washoku felsefesi, Hint Ayurveda baharatları, Kore fermantasyon sanatı ve Latin Amerika Asado ritüeli. |
| 🚫 [**WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md**](WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md) | Görgü Kuralları & Tabular | 20 ülkenin do's and don'ts listesi, ayakkabı kuralları, hediyeleşme adabı ve Yüksek Bağlam (High Context) vs Düşük Bağlam iletişimi. |
| 🏛️ [**CIVILIZATION_REALMS_AND_PHILOSOPHIES.md**](CIVILIZATION_REALMS_AND_PHILOSOPHIES.md) | 9 Büyük Medeniyet Havzası | Anadolu-Akdeniz, Doğu Asya, Cermen-İskandinav, Anglo-Sakson, Slav-Avrasya, Latin Amerika, Orta Doğu, Güney Asya ve Afrika medeniyet felsefeleri. |

---

> 💡 *Ayrıca her ülkenin kendi kültürel ve demografik dosyası için ilgili ülke klasöründeki `01_culture_demographics/society_history.md` dosyasını inceleyebilirsiniz.*
"""
    with open(CULTURE_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    build_untranslatable()
    build_gastronomy()
    build_etiquette()
    build_civilizations()
    build_culture_index()
    print("[SUCCESS] All cultural encyclopedic dossiers built successfully in culture/")
