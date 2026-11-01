# -*- coding: utf-8 -*-
"""
scripts/expand_cultural_registry.py
Expands cultural_codes_and_civilizations_registry.json from 20 to 40 anchor countries,
adding comprehensive Cultural DNA, untranslatable soul concepts, table rituals,
communication styles, and taboos.
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
DATASETS_DIR = BASE_DIR / "global_datasets"
REGISTRY_PATH = DATASETS_DIR / "cultural_codes_and_civilizations_registry.json"

NEW_COUNTRIES_DNA = [
    {
        "country": "Norveç",
        "code": "NOR",
        "capital": "Oslo",
        "civilization_crossroads": "İskandinav Fiyort Medeniyeti + Viking Denizcilik Mirası + Protestan Eşitlikçilik + Modern Refah Devleti.",
        "core_cultural_ethos": "Doğayla bütünleşme (Friluftsliv), mütevazı ve kimseyi kimseden üstün görmeyen eşitlikçilik (Janteloven), fiyortların sessizliğinde sükunet ve toplumsal güven.",
        "untranslatable_soul_concepts": [
            {
                "word": "Friluftsliv",
                "meaning": "Hava ne kadar dondurucu veya fırtınalı olursa olsun, doğanın bağrında özgürce açık havada yaşama ve ruhunu doğayla tazeleme felsefesi.",
                "cultural_significance": "«Kötü hava yoktur, yetersiz kıyafet vardır» düsturuyla Norveçlilerin doğayı kutsal bir arınma alanı olarak görmesi."
            },
            {
                "word": "Janteloven",
                "meaning": "«Kendini diğer insanlardan daha özel, daha akıllı veya üstün sanma» ilkesine dayanan gayriresmi toplumsal alçakgönüllülük yasası.",
                "cultural_significance": "Gösterişten ve kibirden nefret eden, herkesin eşit düzeyde kabul gördüğü İskandinav konsensüs kültürünün temeli."
            },
            {
                "word": "Koselig",
                "meaning": "Sıcak bir içecek, mum ışığı, samimi bir dost ve soğuk kış gecesinde paylaşılan iç ısıtıcı sükunet hali.",
                "cultural_significance": "Danimarka'nın Hygge'sine denk düşen, Norveç kışını yaşanabilir kılan derin sıcaklık hissi."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Hafta sonları teknolojiden ve şehirden uzaklaşıp elektriksiz dağ kulübelerine (Hytte) çekilme geleneği.",
            "17 Mayıs Ulusal Gün kutlamalarında geleneksel ulusal kıyafet olan Bunad giyme onuru.",
            "Çocukların sıfırın altındaki hava sıcaklıklarında dahi dışarıda açık havada uyutulması ve doğaya alıştırılması."
        ],
        "communication_style": "Düşük Bağlamlı (Low Context). Sakin, ölçülü, dolaysız ve yapmacık iltifatlardan uzak; gereksiz konuşmaktan ziyade sessizliğe saygı duyulur.",
        "gastronomic_philosophy": "Kuzey Denizi somonu, kurutulmuş morina balığı (Klippfisk), kahverengi keçi peyniri (Brunost) ve açık sandviçler (Smørbrød); doğallığın saflığı.",
        "social_taboos_and_etiquette": [
            "Maddi zenginlikle, lüks arabayla veya başarıyla övünmek aşırı derecede kınanır (Janteloven ihlali).",
            "Randevulara dakikası dakikasına uyulmalıdır; 5 dakika geç kalmak derin bir saygısızlık sayılır.",
            "Doğaya çöp bırakmak veya vahşi yaşama müdahale etmek affedilmez bir suç kabul edilir."
        ],
        "literary_and_artistic_archetypes": ["Henrik Ibsen", "Edvard Munch (Çığlık Tablosu)", "Knut Hamsun", "Sigrid Undset"]
    },
    {
        "country": "Portekiz",
        "code": "PRT",
        "capital": "Lizbon",
        "civilization_crossroads": "Atlantik Denizcilik Çağı + İber Yarımadası Mirası + Katolik Hüzün ve Fado Şiirselliği.",
        "core_cultural_ethos": "Gidenlerin ardından duyulan tatlı-acı melankoli (Saudade), kadere teslimiyet (Fado), okyanus ufuklarına duyulan ebedi hasret ve sıcak Akdeniz misafirperverliği.",
        "untranslatable_soul_concepts": [
            {
                "word": "Saudade",
                "meaning": "Bir daha asla geri dönmeyebilecek bir sevgiliye, mekana veya kaybedilmiş anılara duyulan derin, tatlı-acı varoluşsal melankoli.",
                "cultural_significance": "Fado müziğinin ruhudur; yokluğun bizzat mevcudiyet haline geldiği Portekiz ruhunun özü."
            },
            {
                "word": "Desassossego",
                "meaning": "Ruhun hiçbir dünyevi başarıyla tatmin olmayan, sürekli arayan, huzursuz ve metafizik içsel dalgalanma hali.",
                "cultural_significance": "Fernando Pessoa'nın «Huzursuzluğun Kitabı»nda felsefileştirdiği Portekiz entelektüel sancısı."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Tavernalarda tek bir Portekiz gitarı ve vokal eşliğinde mum ışığında icra edilen Fado geceleri.",
            "Akşamüstleri Pastel de Nata eşliğinde kahvehanelerde saatlerce süren edebiyat ve futbol sohbetleri.",
            "Haziran ayında Aziz Anthony şenliklerinde sokaklarda ızgara sardalya pişirilip dans edilmesi."
        ],
        "communication_style": "Yüksek Bağlamlı ve duygusal. İspanyollara kıyasla çok daha yumuşak başlı, nezaketli, ses tonunu yükseltmeyen ve kırıcı olmaktan kaçınan zarif üslup.",
        "gastronomic_philosophy": "365 farklı şekilde pişirilen tuzlu kurutulmuş morina balığı (Bacalhau), taze deniz mahsulleri, zeytinyağı ve Porto şarabı.",
        "social_taboos_and_etiquette": [
            "Portekizlileri İspanyollarla karıştırmak veya Portekizceye 'İspanyolcanın bir lehçesi' muamelesi yapmak ulusal onura ağır hakarettir.",
            "Fado söylenirken konuşmak veya gürültü yapmak kutsal bir ayini bozmak kadar büyük görgüsüzlüktür.",
            "Yemeğin sonunda hesabı tek tek kuruşu kuruşuna bölüşmeye çalışmak kabalık kabul edilir."
        ],
        "literary_and_artistic_archetypes": ["Luís de Camões", "Fernando Pessoa", "José Saramago", "Amália Rodrigues"]
    },
    {
        "country": "İrlanda",
        "code": "IRL",
        "capital": "Dublin",
        "civilization_crossroads": "Kelt Mitolojisi + Katolik Direniş ve Cemaat Ruhu + İrlanda Edebi Rönesansı.",
        "core_cultural_ethos": "Sözlü hikaye anlatıcılığı (Sean-nós), mizah ve müzikle dolu muhabbet (Craic), kederi şarkılarla gömme bilgeliği ve fırtınalı tarihe inat sarsılmaz cemaat dayanışması.",
        "untranslatable_soul_concepts": [
            {
                "word": "Craic",
                "meaning": "Yalnızca eğlence değil; zeka dolu espriler, canlı müzik, sıcak dedikodu ve dost meclisinde akan benzersiz muhabbet ortamı.",
                "cultural_significance": "İrlanda pub kültürünün kutsal ruhudur; «What's the craic?» gündelik selamlaşmanın ta kendisidir."
            },
            {
                "word": "Meitheal",
                "meaning": "Bir komşunun veya köyün hasadını kaldırmak, evini yapmak için tüm köylünün hiçbir ücret beklemeden imeceye koşması.",
                "cultural_significance": "Kelt kabile geleneğinden miras kalan, zor zamanlarda ortaya çıkan mutlak komşuluk dayanışması."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Geleneksel pub'larda gayda, keman ve bodhrán eşliğinde kendiliğinden gelişen canlı müzik seansları (Trad Sessions).",
            "Ölen bir yakın için yas tutmak yerine hayatını şarkılar, anılar ve viskiyle kutlayan taziye gecesi (Irish Wake).",
            "Gaelik futbolu ve hurling gibi antik Kelt sporlarının amatör ruhla köy düzeyinde coşkuyla oynanması."
        ],
        "communication_style": "Yüksek Bağlamlı, esprili ve hiciv dolu. Ciddiyet kisvesi altındaki kuruluktan nefret edilir; alaycı zeka (Banter) samimiyetin göstergesidir.",
        "gastronomic_philosophy": "İrlanda yahnisi (Irish Stew), soda ekmeği, siyah bira (Guinness) ve patates mirası (Colcannon); tok tutan, samimi ve sade sofra.",
        "social_taboos_and_etiquette": [
            "Pub'da grup halinde içilirken 'sıra alma' (Buying your round) kuralını atlamak sosyal olarak aforoz edilme sebebidir.",
            "İrlanda'yı İngiltere'nin bir parçası gibi görmek veya 'British Isles' terimini dikkatsizce kullanmak derin rahatsızlık yaratır.",
            "Büyük Kıtlık (Great Famine) travmasıyla alay etmek asla hoş görülmez."
        ],
        "literary_and_artistic_archetypes": ["James Joyce", "William Butler Yeats", "Samuel Beckett", "Oscar Wilde"]
    },
    {
        "country": "İsviçre",
        "code": "CHE",
        "capital": "Bern",
        "civilization_crossroads": "Alp Dağları Sığınağı + Dört Dilli Kantonlar Mozaiği (Almanca, Fransızca, İtalyanca, Romanş) + Doğrudan Demokrasi ve Bankacılık Gizliliği.",
        "core_cultural_ethos": "Hassasiyet ve dakiklik, mutlak tarafsızlık ve bağımsızlık, komşuluk huzurunu ve sessizliği kutsayan disiplin, doğrudan halk oylamasıyla (Referandum) yönetilme bilinci.",
        "untranslatable_soul_concepts": [
            {
                "word": "Heimat",
                "meaning": "Yalnızca doğulan ev değil; kişinin dilsel, coğrafi ve manevi olarak kök saldığı, güven içinde hissettiği Alp yurdu.",
                "cultural_significance": "Kantonel kimliğin ulusal kimlikten önce geldiği İsviçre aidiyetinin derin sığınağı."
            },
            {
                "word": "Zauberberg Hali",
                "meaning": "Dağların zirvesindeki sanatoryum havasında, dünyanın gürültüsünden ve savaşlarından yalıtılmış steril tefekkür hali.",
                "cultural_significance": "Thomas Mann'ın Büyülü Dağ romanında tasvir ettiği, İsviçre'nin tarafsız izole fanus psikolojisi."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Yılda 3-4 kez doğrudan anayasa maddelerini oylamak üzere sandığa gitme (Landsgemeinde) yurttaşlık ritüeli.",
            "Kışın karlı havada dostların tek bir tencere etrafında erimiş peynire ekmek bandırdığı Fondü seremonisi.",
            "Her yetişkin erkeğin evinde askeri tüfeğini ve teçhizatını sakladığı sivil milis ordusu hazırlığı."
        ],
        "communication_style": "Düşük Bağlamlı, son derece kibar, mesafeli ve formel. Tartışmalarda ses yükseltilmez; konsensüs ve kompromis (uzlaşı) kutsaldır.",
        "gastronomic_philosophy": "Peynir fondü, Raclette, Rösti (patates mücveri) ve dünyanın en rafine çikolataları; Alp sütü saflığı.",
        "social_taboos_and_etiquette": [
            "Pazar günleri veya akşam 22:00'den sonra gürültü yapmak (çim biçmek, cam şişe atmak) polis çağırma sebebidir.",
            "Kişisel finansal varlıkları, banka hesaplarını veya maaş miktarını sormak aşırı kaba bir tabudur.",
            "Trene veya otobüse binerken sırada bekleyenlerin önüne geçmek hoş karşılanmaz."
        ],
        "literary_and_artistic_archetypes": ["Friedrich Dürrenmatt", "Max Frisch", "Jean-Jacques Rousseau", "Carl Gustav Jung"]
    },
    {
        "country": "Hollanda",
        "code": "NLD",
        "capital": "Amsterdam",
        "civilization_crossroads": "Kuzey Denizi Ticaret Cumhuriyeti + Kalvinist Çalışma Ahlakı + Polder Modeli Mutabakatı.",
        "core_cultural_ethos": "Denizden toprak kazanmanın getirdiği kolektif uzlaşı (Polder Modeli), açık sözlülük (Directheid), hoşgörü, pragmatizm ve samimi sıcaklık (Gezelligheid).",
        "untranslatable_soul_concepts": [
            {
                "word": "Gezelligheid",
                "meaning": "Sıcak, neşeli, telaşsız, dostlarla birlikte olmaktan kaynaklanan ve mekanın samimiyetiyle taçlanan ortak mutluluk atmosferi.",
                "cultural_significance": "Hollanda yaşamının merkezidir; bir mekan veya buluşma 'gezellig' değilse eksik kalmış demektir."
            },
            {
                "word": "Poldermodel",
                "meaning": "Deniz taşmalarına karşı bentleri korumak için en uzlaşmaz düşmanların dahi masaya oturup ortak mutabakata varması geleneği.",
                "cultural_significance": "Hollanda siyasetinin ve iş dünyasının grevsiz, krizsiz konsensüs üretme metodolojisi."
            },
            {
                "word": "Uitwaaien",
                "meaning": "Fırtınalı veya rüzgarlı bir günde sahile veya kırlara çıkıp rüzgarın zihni temizlemesine izin verme yürüyüşü.",
                "cultural_significance": "Kuzey Denizi rüzgarıyla zihinsel arınma ritüeli."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Yağmur çamur dinlemeden her yere bisikletle (Omafiets) gitme ve eşitlikçi sokak kültürü.",
            "Evlerin perdelerini gece dahi kapatmama geleneği («Gizleyecek hiçbir günahımız yok» Kalvinist dürüstlük mirası).",
            "Kral Günü'nde (Koningsdag) tüm ülkenin turuncuya bürünüp sokaklarda ikinci el pazar açması."
        ],
        "communication_style": "Son derece Düşük Bağlamlı ve doğrudan (Dutch Directness). Kibarlık bahanesiyle gerçeği dolandırmak sahtekarlık sayılır; netlik dürüstlüğün zirvesidir.",
        "gastronomic_philosophy": "Kuyruğundan tutulup çiğ yutulan ringa balığı (Haring), Gouda/Edam tekerlek peynirleri ve karamel şuruplu Stroopwafel.",
        "social_taboos_and_etiquette": [
            "Randevusuz bir Hollandalının evine akşam yemeği saatinde (18:00) çat kapı gitmek; yemeğe davet edilmezsiniz.",
            "Fikrini dolaylı yollardan ima etmeye çalışmak; 'Ne demek istiyorsan açıkça söyle' tepkisi alırsınız.",
            "Sosyal statü veya markalarla hava atmak 'Normal yap, zaten yeterince delisin' atasözüyle alaya alınır."
        ],
        "literary_and_artistic_archetypes": ["Rembrandt van Rijn", "Vincent van Gogh", "Johannes Vermeer", "Erasmus"]
    },
    {
        "country": "Avusturya",
        "code": "AUT",
        "capital": "Viyana",
        "civilization_crossroads": "Habsburg İmparatorluk Görkemi + Orta Avrupa Barok Kültürü + Viyana Klasisizmi ve Kahvehane Entelektüalizmi.",
        "core_cultural_ethos": "İmparatorluk mirası zarafet, barok müzik estetiği, telaşsız yaşam zevki (Gemütlichkeit), kahvehanelerde saatlerce süren gazete okuma ve felsefe ritüeli.",
        "untranslatable_soul_concepts": [
            {
                "word": "Gemütlichkeit",
                "meaning": "Zamanın durduğu, garsonun acele ettirmediği, kadife koltuklarda sıcak bir kahve ve dost meclisinde paylaşılan dingin huzur.",
                "cultural_significance": "Viyana kahvehanelerinin UNESCO somut olmayan miras unvanı almasını sağlayan yaşam temposu."
            },
            {
                "word": "Schmäh",
                "meaning": "Tatlı dilli, hafif melankolik, ölümle dahi dalga geçebilen ince Viyana kara mizahı ve nüktedanlığı.",
                "cultural_significance": "Viyana sokaklarının ve edebiyatının trajedilere karşı geliştirdiği zarif alaycılık zırhı."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Viyana Kahvehanelerinde (Kaffeehaus) tek bir Melange sipariş edip saatlerce gazete okuma hakkı.",
            "Kış sezonunda imparatorluk saraylarında düzenlenen 400'den fazla geleneksel Vals Baloları (Wiener Opernball).",
            "Sonbaharda bağbozumu meyhanelerinde (Heuriger) genç şarap eşliğinde halk şarkıları dinleme geleneği."
        ],
        "communication_style": "Yüksek Bağlamlı ve son derece unvan odaklı. Karşındakine unvanıyla (Herr Doktor, Frau Magister) hitap etmek saygının ön şartıdır; doğrudan çatışmadan kaçınılır.",
        "gastronomic_philosophy": "İncecik dövülmüş tereyağlı Viyana Şnitseli (Wiener Schnitzel), Sachertorte çikolatalı pastası ve elmalı Strudel.",
        "social_taboos_and_etiquette": [
            "Bir Viyana kahvehanesinde hesabı ister istemez hemen kalkıp gitmek; garsonu acele ettirmek görgüsüzlüktür.",
            "Avusturyalıları 'bir tür Alman' olarak nitelendirmek ulusal kimliğe hakaret sayılır.",
            "Akademik veya mesleki unvanları hitapta kullanmamak kabalık kabul edilir."
        ],
        "literary_and_artistic_archetypes": ["Wolfgang Amadeus Mozart", "Sigmund Freud", "Stefan Zweig", "Gustav Klimt"]
    },
    {
        "country": "Polonya",
        "code": "POL",
        "capital": "Varşova",
        "civilization_crossroads": "Batı Slav Dünyası + Roma Katolik Kalesi + Tarihsel Bölünmeler ve Sarsılmaz Direniş Ruhu.",
        "core_cultural_ethos": "Boyun eğmeyen vatanseverlik, trajik tarihsel hafızaya rağmen romantik direniş iradesi, Katolik inanç bağlılığı ve sınır tanımayan cömert misafirperverlik.",
        "untranslatable_soul_concepts": [
            {
                "word": "Żal",
                "meaning": "Kaybedilen vatan topraklarına, şehitlere veya geçmişe duyulan; içinde hem öfke, hem asil bir keder hem de direniş barındıran derin hüzün.",
                "cultural_significance": "Chopin'in noktürnlerinin ve Polonya romantizminin kalbindeki duygu yükü."
            },
            {
                "word": "Załatwić",
                "meaning": "Bürokratik engelleri, imkansızlıkları kişisel ilişkiler ve pratik zekayla gayriresmi yoldan ustalıkla çözüvermek.",
                "cultural_significance": "Komünist kıtlık yıllarında hayatta kalmayı sağlayan dayanışma ve iş bitiricilik refleksi."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Noel arifesinde (Wigilia) sofrada beklenmedik bir yabancı misafir için daima boş bir tabak bırakılması.",
            "1 Kasım Tüm Azizler Günü'nde (Wszystkich Świętych) mezarlıkların milyonlarca mumla adeta bir ışık denizine dönüştürülmesi.",
            "Eve gelen misafire aç olup olmadığı sorulmadan doğrudan donatılmış bir sofra kurulması (Gość w dom, Bóg w dom)."
        ],
        "communication_style": "Orta Bağlamlı. Samimi, duygusal, tarihsel konularda tutkulu; kadınlara karşı eski usul centilmenlik (el öpme geleneği) devam eder.",
        "gastronomic_philosophy": "Mantı benzeri Pierogi, fermente çavdar çorbası (Żurek), lahana sarması (Gołąbki) ve Zubrówka bizon çimi votkası.",
        "social_taboos_and_etiquette": [
            "Polonya'yı 'Doğu Avrupa' olarak adlandırmak; kendilerini kesin bir dille 'Orta Avrupa' (Central Europe) olarak tanımlarlar.",
            "Katolik Kilisesi'ne veya Papa II. Jean Paul'e hakaret etmek toplumun büyük kesiminde infial yaratır.",
            "Eve girerken ayakkabıları çıkarmamak veya ev sahibinin terlik teklifini reddetmek kabalık sayılır."
        ],
        "literary_and_artistic_archetypes": ["Frédéric Chopin", "Adam Mickiewicz", "Stanisław Lem", "Wisława Szymborska"]
    },
    {
        "country": "Ukrayna",
        "code": "UKR",
        "capital": "Kiev",
        "civilization_crossroads": "Kievan Rus' Kadim Mirası + Dinyeper Kozak Hürriyet Ruhu + Bereketli Kara Topraklar (Çernozyom).",
        "core_cultural_ethos": "Özgürlük ve hür irade (Volya), baskıya boyun eğmeyen Kozak asiliği, bereketli toprağa duyulan sevgi, ağıt ve şarkılarla yoğrulmuş dayanıklılık.",
        "untranslatable_soul_concepts": [
            {
                "word": "Volya (Воля)",
                "meaning": "Yalnızca özgürlük değil; kişinin kendi kaderini tayin etme hakkı, zincir vurulamaz irade ve bağımsızlık aşkı.",
                "cultural_significance": "Ukrayna milli armasının (Tryzub) içine gizlendiğine inanılan milli varoluş parolası."
            },
            {
                "word": "Hromada (Громада)",
                "meaning": "Devletten bağımsız olarak yerel halkın kendi kaderini ve köyünü korumak için kurduğu organik cemaat birliği.",
                "cultural_significance": "Kriz ve savaş anlarında Ukrayna toplumunun anında kendi kendine organize olmasını sağlayan refleks."
            }
        ],
        "social_rituals_and_lifestyle": [
            "İşlemeli geleneksel gömlek olan Vyshynvanka giyme bayramı ve bunun bir milli kimlik zırhı kabul edilmesi.",
            "Paska ekmeği ve Pysanky (ustalıkla boyanmış paskalya yumurtaları) ile baharı karşılama ritüeli.",
            "Dinyeper nehri kıyısında şarkılar ve ateş etrafında toplanan İvan Kupala yaz dönümü gecesi."
        ],
        "communication_style": "Yüksek Bağlamlı ve samimi. İnsan ilişkilerinde sıcak, duygulu, misafirperver; kriz anlarında sarsılmaz bir kararlılık.",
        "gastronomic_philosophy": "Kırmızı pancarlı Borş çorbası (UNESCO Somut Olmayan Miras), sarımsaklı Pampushky ekmeği, Varenyky ve tuzlu domuz yağı (Salo).",
        "social_taboos_and_etiquette": [
            "Ukrayna'nın başına İngilizce 'the' takısı getirilmesi ('the Ukraine') veya Rusya'nın bir uzantısı gibi görülmesi ağır hakarettir.",
            "Holodomor (1932-33 Sovyet Büyük Kıtlığı) trajedisini inkar etmek veya küçümsemek.",
            "Eşik üzerinden el sıkışmak veya bir şey alıp vermek uğursuzluk sayılır."
        ],
        "literary_and_artistic_archetypes": ["Taras Şevçenko", "Lesya Ukrainka", "Nikolay Gogol", "İvan Franko"]
    },
    {
        "country": "Endonezya",
        "code": "IDN",
        "capital": "Cakarta",
        "civilization_crossroads": "17.000 Ada Mozaiği + İslamiyet + Hindu-Budist Nusantara Mirası + Animist Kökler.",
        "core_cultural_ethos": "Toplumsal uyum ve imece (Gotong Royong), ortak mutabakat ve istişare (Musyawarah & Mufakat), farklılıklar içinde birlik (Bhinneka Tunggal Ika) ve dingin tebessüm.",
        "untranslatable_soul_concepts": [
            {
                "word": "Gotong Royong",
                "meaning": "Bir köyün pirinç tarlasını hasat etmek, köprü yapmak veya felaketi atlatmak için tüm toplumun omuz omuza karşılıksız çalışması.",
                "cultural_significance": "Endonezya ulus felsefesinin (Pancasila) kalbidir; bireysel çıkardan önce kolektif varoluş gelir."
            },
            {
                "word": "Musyawarah",
                "meaning": "Oylama yapıp azınlığı ezmek yerine, herkesin içine sinene kadar günlerce süren sabırlı uzlaşı arayışı.",
                "cultural_significance": "Köy meclislerinden parlamentoya kadar uzanan geleneksel uzlaşmacı yönetim tarzı."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Gölge oyunu olan Wayang Kulit eşliğinde sabaha kadar süren ahlaki ve felsefi Mahabharata anlatıları.",
            "Gamelan orkestrasının hipnotik bronz gong melodileri eşliğinde tapınak dansları.",
            "Cuma günleri ve resmi törenlerde UNESCO tescilli Batik gömlekleri giyme zorunluluğu."
        ],
        "communication_style": "Aşırı Yüksek Bağlamlı. Doğrudan 'Hayır' denmez (Asam/Belum); çatışma ve öfke zafiyet sayılır, her durum tebessümle karşılanır.",
        "gastronomic_philosophy": "Karamelize hindistan cevizi sütlü baharatlı sığır eti (Rendang), Nasi Goreng, Satay şişleri ve acı biber ezmesi (Sambal).",
        "social_taboos_and_etiquette": [
            "Birinin başına dokunmak (çocuklar dahil) ruhun ikametgahına saygısızlık kabul edilir.",
            "Yemek yerken veya bir şey verirken sol eli kullanmak pis kabul edilir; mutlaka sağ el kullanılır.",
            "Topluluk içinde sesini yükseltmek veya birini utandırmak toplumsal uyumu dinamitlemek sayılır."
        ],
        "literary_and_artistic_archetypes": ["Pramoedya Ananta Toer", "Raden Saleh", "Chairil Anwar"]
    },
    {
        "country": "Vietnam",
        "code": "VNM",
        "capital": "Hanoi",
        "civilization_crossroads": "Pirinç Havzası Medeniyeti + Konfüçyüsçü Vefa + Budist Tevekkül + Sömürgeciliğe Karşı Bambu Direnci.",
        "core_cultural_ethos": "Bambu gibi esnek ama kırılmaz direnç (Bambu Diplomasisi), aileye ve atalara sınırsız hürmet (Hiếu), minnet ve vefa (Tình Nghĩa), sabırlı çalışkanlık.",
        "untranslatable_soul_concepts": [
            {
                "word": "Tình Nghĩa",
                "meaning": "Yalnızca sevgi değil; geçmişte yapılan bir iyiliğe, paylaşılan zorluklara duyulan ömür boyu süren ahlaki vefa borcu.",
                "cultural_significance": "Vietnam insan ilişkilerinin çimentosudur; çıkarlar bitse de Tình Nghĩa asla bitmez."
            },
            {
                "word": "Nhẫn",
                "meaning": "Büyük bir gaye uğruna acılara, hakaretlere ve zorluklara sabırla katlanma, öfkeyi içine gömme iradesi.",
                "cultural_significance": "Yüzyıllarca süren savaşlarda süper güçleri dize getiren Vietnam sabrının felsefi kökü."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Yeni Yıl (Tet) bayramında aile ocağında bir araya gelip ataların ruhuna Bánh Chưng pirinç keki sunulması.",
            "Küçük plastik taburelerde kaldırım kenarında içilen yoğun kıvamlı yoğunlaştırılmış sütlü buzlu kahve (Cà phê sữa đá).",
            "Su kuklası tiyatrosu (Múa rối nước) ile pirinç tarlalarındaki efsanelerin canlandırılması."
        ],
        "communication_style": "Yüksek Bağlamlı. Tevazu, yumuşak ses tonu ve yüzü koruma (Mặt) refleksi hakimdir; anlaşmazlıklar tebessümün ardına gizlenir.",
        "gastronomic_philosophy": "24 saat kaynatılan kemik sulu taze otlu erişte çorbası (Phở), Fransız bagetinden türeyen Bánh Mì ve fermente balık sosu (Nước mắm).",
        "social_taboos_and_etiquette": [
            "Yemek çubuklarını pirinç kasesine dik batırmak (cenaze tütsüsünü andırdığı için) ölümcül bir tabudur.",
            "Birinin omzuna dokunmak veya üzerinden atlamak o kişinin şansını çalmak sayılır.",
            "Yaşlılara iki elle bir şey uzatmamak veya başla selam vermemek saygısızlık kabul edilir."
        ],
        "literary_and_artistic_archetypes": ["Nguyễn Du (Kieu Destanı)", "Ho Chi Minh", "Bảo Ninh"]
    },
    {
        "country": "Tayland",
        "code": "THA",
        "capital": "Bangkok",
        "civilization_crossroads": "Theravada Budizmi + Siyam Krallık İhtişamı + Güler Yüzlüler Ülkesi Felsefesi.",
        "core_cultural_ethos": "Hayattan zevk alma sanatı (Sanuk), dünyevi dertleri akışa bırakma (Mai Pen Rai), içsel dinginlik ve karma dengesi, Kraliyet ve Budist Sangha'ya derin saygı.",
        "untranslatable_soul_concepts": [
            {
                "word": "Sanuk",
                "meaning": "Yapılan her işe, çalışmaya veya gündelik göreve oyunsu bir neşe ve keyif katma felsefesi.",
                "cultural_significance": "Taylandlılar bir işte 'Sanuk' yoksa o işi yapmaya değmeyeceğine inanır; gülümsemenin sırrıdır."
            },
            {
                "word": "Mai Pen Rai",
                "meaning": "«Önemli değil, dert etmeye değmez, akışına bırak»; kötü olaylar karşısında Budist tevekkül ve sükunet.",
                "cultural_significance": "Trafikte, krizde veya kayıpta öfkelenmek yerine iç huzuru koruma mekanizması."
            },
            {
                "word": "Kreng Jai",
                "meaning": "Kendi arzularından feragat ederek bir başkasını rahatsız etmeme, yük olmama veya utandırmama aşırı hassasiyeti.",
                "cultural_significance": "Toplumsal ilişkilerde çatışmayı sıfıra indiren nezaket filtresi."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Günde iki kez çalan milli marşta sokaktaki herkesin anında donup saygı duruşuna geçmesi.",
            "Nisan ayında Songkran su festivalinde sokaklarda günahları ve kötülükleri temizlemek için su savaşları yapılması.",
            "Her sabah keşişlere (Monk) diz çökerek yiyecek sunma (Almsgiving) ile liyakat ve sevap (Bun) kazanma."
        ],
        "communication_style": "Yüksek Bağlamlı ve son derece yumuşak. Cümle sonlarına eklenen 'Krap/Kha' saygı ekleri ve iki elin göğüste birleştirildiği 'Wai' selamı.",
        "gastronomic_philosophy": "Tatlı, ekşi, acı, tuzlu ve umaminin mükemmel dengesi; Tom Yum Goong çorbası, Pad Thai, yeşil köri ve mangolu yapışkan pirinç.",
        "social_taboos_and_etiquette": [
            "Kraliyet ailesi hakkında en ufak bir eleştiri veya espri yapmak (Lèse-majesté kanunu gereği hapis cezasıdır).",
            "Ayak tabanını bir insana veya Buda heykeline doğru uzatmak en ağır hakarettir (ayak bedenin en kirli yeridir).",
            "Bir Budist keşişe (özellikle kadınlar tarafından) doğrudan dokunmak dini tabudur."
        ],
        "literary_and_artistic_archetypes": ["Sunthorn Phu", "Kukrit Pramoj", "Ramakien Destanı"]
    },
    {
        "country": "Pakistan",
        "code": "PAK",
        "capital": "İslamabad",
        "civilization_crossroads": "İndus Vadisi Kadim Havzası + Babür İmparatorluk Mirası + Tasavvufi İslam + Urdu Şiir Geleneği.",
        "core_cultural_ethos": "Sınır tanımayan misafirperverlik (Mehman-nawazi), Tasavvuf tekkelerindeki ilahi aşk ve vecd (Qawwali), onur ve haysiyet kodu (Ghayrat), edebi incelik.",
        "untranslatable_soul_concepts": [
            {
                "word": "Mehmaan-Nawazi",
                "meaning": "Tanrı misafiri kapıya geldiğinde evin en kıymetli yemeğini ve yatağını ona sunma, canını ortaya koyma hürmeti.",
                "cultural_significance": "Kuzey dağlarından Karaçi'ye kadar bir yabancının asla aç ve açıkta kalamayacağı ahlaki kural."
            },
            {
                "word": "Ghayrat (غیرت)",
                "meaning": "Ailenin, inancın ve vatanın haysiyetini, namusunu ve mukaddesatını koruma konusundaki sarsılmaz hassasiyet.",
                "cultural_significance": "Toplumsal duruşu ve kabile dayanışmasını belirleyen temel ahlaki omurga."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Tasavvuf dergahlarında (Bülleh Şah, Lal Şahbaz Kalandar) dervişlerin dönerek vecd içinde dans ettiği Dhamal ayinleri.",
            "Nusret Fatih Ali Han ekolüyle icra edilen, saatlerce süren Qawwali ilahi geceleri.",
            "Şiir meclislerinde (Mushaira) şairlerin beyitlerine dinleyicilerin coşkuyla 'Vah vah!' nidalarıyla eşlik etmesi."
        ],
        "communication_style": "Yüksek Bağlamlı, saygı ve hitap unvanlarıyla (Aap, Janab, Sahib) örülü, sıcakkanlı ve duygusal üslup.",
        "gastronomic_philosophy": "Közde pişen ağır baharatlı etler (Nihari, Biryani, Chapli Kebab), tandır naan ekmeği ve safranlı kakuleli sütlü çay (Doodh Patti).",
        "social_taboos_and_etiquette": [
            "Dini değerlere, Hz. Peygamber'e veya Kur'an'a karşı saygısızlık toplumda asla tolere edilmez.",
            "Yaşlıların yanında bacak bacak üstüne atmak veya sigara içmek hürmetsizlik sayılır.",
            "İkram edilen çayı veya yemeği hiçbir meşru sebep yokken geri çevirmek ev sahibini derinden yaralar."
        ],
        "literary_and_artistic_archetypes": ["Muhammed İkbal", "Faiz Ahmed Faiz", "Nusret Fatih Ali Han", "Sadat Hasan Manto"]
    },
    {
        "country": "Suudi Arabistan",
        "code": "SAU",
        "capital": "Riyad",
        "civilization_crossroads": "İslam'ın Doğduğu Kutsal Topraklar + Necid Bedevi Onur Kodu + Hicaz Ticaret Kavşağı + 2030 Vizyonu Modernitesi.",
        "core_cultural_ethos": "Arap cömertliği (Kerem), sözün senet olduğu bedevi onuru (Şeref ve Mürüvvet), kabile meclisleri (Meclis), çöl sabrı ve İslami mukaddesat koruyuculuğu.",
        "untranslatable_soul_concepts": [
            {
                "word": "Karam (كرم)",
                "meaning": "Karşılık beklemeden, misafirin önüne sürüsünün en iyi devesini/koyununu kesip sunan sınırsız çöl cömertliği.",
                "cultural_significance": "Hatim et-Tai efsanesinden bu yana Arap karakterinin en yüce fazileti kabul edilen vasıf."
            },
            {
                "word": "Fazaa (فزعة)",
                "meaning": "Zor durumda kalan bir akraba veya yabancının imdadına hiçbir şey sormadan atılıp cansiperane yardım etme refleksi.",
                "cultural_significance": "Çölün amansız şartlarında hayatta kalmayı sağlayan kabilevi yardımlaşma andı."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Kakuleli sarı Arap kahvesinin (Gahwa) hurma eşliğinde fincan hafifçe sallanana kadar bitimsizce ikram edilmesi.",
            "Erkeklerin geleneksel kılıç dansı olan Ardah ile zafer ve birlik günlerini kutlaması.",
            "Kabile büyüklerinin, prenslerin ve halkın bir araya geldiği, dertlerin doğrudan lidere iletildiği Meclis toplantıları."
        ],
        "communication_style": "Yüksek Bağlamlı, iltifatlar, dualar ve şiirsel selamlaşmalarla yüklü; şeref ve aile mahremiyeti dokunulmazdır.",
        "gastronomic_philosophy": "Közde kuzu eti ve safranlı baharatlı basmati pirinciyle dev tepsilerde sunulan Kabsa, kuzu dolması ve Medine hurmaları.",
        "social_taboos_and_etiquette": [
            "Bir erkeğe karısının veya kızlarının adını doğrudan sormak (mahremiyet ihlali kabul edilir; 'Aile nasıl?' denir).",
            "Kahve fincanını sağ elle tutmamak veya kahveyi bitirdikten sonra fincanı hafifçe sallamadan masaya bırakmak.",
            "İslam dininin kutsallarına karşı lakayt veya saygısız tavır sergilemek."
        ],
        "literary_and_artistic_archetypes": ["Muallakat Şairleri (İmruü'l-Kays)", "Gazi el-Kusaybi", "Antarah ibn Shaddad"]
    },
    {
        "country": "Fas",
        "code": "MAR",
        "capital": "Rabat",
        "civilization_crossroads": "Mağrip Berberi (Amazigh) Kökleri + Endülüs İrfanı + Arap İslam Medeniyeti + Sahra Kervan Yolları.",
        "core_cultural_ethos": "Endülüs zarafetiyle harmanlanmış Berberi dayanıklılığı, labirent medina sokaklarındaki zanaat sabrı, nane çayı diplomasisi ve kadim saray terbiyesi.",
        "untranslatable_soul_concepts": [
            {
                "word": "Baraka (بركة)",
                "meaning": "Yalnızca bereket değil; kutsal mekanlardan, evliyalardan ve helal kazançtan toprağa ve insana yayılan manevi nur ve esenlik.",
                "cultural_significance": "Fas tasavvufi geleneğinde her zanaatın ve yemeğin temel gayesi olan ilahi lütuf."
            },
            {
                "word": "Hşuma (حشومة)",
                "meaning": "Ailenin, komşuların veya toplumun önünde utanılacak, edebe aykırı bir şey yapmaktan duyulan derin ar ve edep bilinci.",
                "cultural_significance": "Fas sosyal hayatında saygıyı ve ahlaki sınırları koruyan en güçlü toplumsal denetim."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Köpüklü Mağrip nane çayının (Atay) gümüş demlikten yarım metre yukarıdan ince bardaklara dökülme seremonisi.",
            "Haftalık bedensel ve ruhsal arınma merkezi olan geleneksel buharlı Hammam ritüeli.",
            "Cuma günleri namaz sonrası tüm ailenin dev toprak tabakta buharda pişmiş Kuskus etrafında toplanması."
        ],
        "communication_style": "Yüksek Bağlamlı, Fransızca, Arapça ve Berberice karışımı (Darija), şiirsel metaforlar ve dualarla bezeli sıcak üslup.",
        "gastronomic_philosophy": "Koni biçimli toprak kapta ağır ateşte pişen baharatlı erikli et Tagine'i, tatlı-tuzlu güvercin böreği Pastilla ve Cuma Kuskusu.",
        "social_taboos_and_etiquette": [
            "İkram edilen nane çayını reddetmek misafirperverliğe hakaret sayılır (En az üç bardak içmek adettendir).",
            "Ortak tabaktan yemek yerken kendi önünden değil de başkasının önünden lokma almak görgüsüzlüktür.",
            "Kraliyet ailesini veya devletin toprak bütünlüğünü (Batı Sahra meselesi) sorgulamak kesin tabudur."
        ],
        "literary_and_artistic_archetypes": ["İbn Battuta", "Tahar Ben Jelloun", "Fatima Mernissi"]
    },
    {
        "country": "Kolombiya",
        "code": "COL",
        "capital": "Bogota",
        "civilization_crossroads": "And Dağları İspanyol Mirası + Karayip Coşkusu + Pasifik Afrika Ritmi + Amazon Yerli Kabileleri.",
        "core_cultural_ethos": "Büyülü gerçekçilik (Realismo Mágico), acıları ve şiddet tarihini dansla ve müzikle şifalandırma gücü (Resiliencia), kahve dağlarının çalışkanlığı ve sıcak nezaket.",
        "untranslatable_soul_concepts": [
            {
                "word": "Querendón",
                "meaning": "Doğuştan aşırı şefkatli, etrafındakilere sevgi ve sıcaklık saçan, herkesi kucaklayan cömert insan karakteri.",
                "cultural_significance": "Kolombiyalıların yabancılara gösterdiği içten ve koşulsuz kucaklaşmanın ifadesi."
            },
            {
                "word": "Berraco",
                "meaning": "En büyük felaketlerin, yoksulluğun ve şiddetin altından cesaretle, yılmadan ve gülümseyerek kalkan dirençli insan.",
                "cultural_significance": "Narkotik savaşları ve çatışmaları geride bırakan Kolombiya halkının milli direniş sıfatı."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Sabahları dağ köylerinde sıcak Tinto (şeker kamışlı siyah kahve) eşliğinde başlayan sohbetler.",
            "Barranquilla Karnavalı ve Cali Salsa Festivallerinde sokakların devasa bir ritim tufanına dönmesi.",
            "Pazar günleri ailelerin nehir kenarlarında dev kazanlarda Sancocho çorbası pişirmesi (Paseo de Olla)."
        ],
        "communication_style": "Yüksek Bağlamlı ve son derece kibar. Bogota İspanyolcası dünyanın en temiz ve formel aksanı kabul edilir; 'Usted' saygı hitabı hakimdir.",
        "gastronomic_philosophy": "Fasulye, pilav, et, avokado ve muzdan oluşan doyurucu Bandeja Paisa, mısır ekmeği Arepa ve And kahvesi.",
        "social_taboos_and_etiquette": [
            "Pablo Escobar veya kokain kartelleri hakkında şaka yapmak veya Kolombiya'yı yalnızca uyuşturucuyla anmak derin bir hakarettir.",
            "Birisi size kahve (Tinto) ikram ettiğinde geri çevirmek kırıcı kabul edilir.",
            "Siyasetteki geçmiş şiddet dönemleri (La Violencia) hakkında yüzeysel ve yargılayıcı konuşmak tabudur."
        ],
        "literary_and_artistic_archetypes": ["Gabriel García Márquez (Yüzyıllık Yalnızlık)", "Fernando Botero", "Álvaro Mutis"]
    },
    {
        "country": "Şili",
        "code": "CHL",
        "capital": "Santiago",
        "civilization_crossroads": "And Dağları ile Büyük Okyanus Arasındaki İnce Şerit + Mapuche Yerli Direnci + İspanyol ve Cermen Göçü.",
        "core_cultural_ethos": "Şiir ve edebiyat aşkı (Los Poetas ülkesi), coğrafi izolasyonun getirdiği melankoli ve içe dönüklük, depremlere karşı sarsılmaz kolektif dayanışma, toprak ve deniz bağı.",
        "untranslatable_soul_concepts": [
            {
                "word": "Añoranza",
                "meaning": "And Dağları'nın devasa gölgesinde ve Pasifik'in kıyısında hisseden insanın uzak diyarlara ve geçmişe duyduğu derin hüzünlü hasret.",
                "cultural_significance": "Neruda ve Mistral şiirlerinin arkasındaki coğrafi yalnızlık duygusu."
            },
            {
                "word": "Chilenidad",
                "meaning": "Şilili olmanın getirdiği ortak karakter; depremlerle yıkılıp her defasında küllerinden yeniden doğan milli direnç.",
                "cultural_significance": "18 Eylül Ulusal Günlerinde (Fiestas Patrias) ortaya çıkan kolektif gurur."
            }
        ],
        "social_rituals_and_lifestyle": [
            "18 Eylül Fiestas Patrias'ta ramada adı verilen çadırlarda Cueca halk dansı yapıp empanada yemek.",
            "Pazar günleri aile boyu süren Asado (And usulü et ızgarası) ve Carmenere şarabı sohbetleri.",
            "Her şiddetli deprem sonrasında halkın paniklemeden birbirine yardım edip şehri temizlemesi refleksi."
        ],
        "communication_style": "Yüksek Bağlamlı, dünyanın en hızlı ve bol argo (Chilenismos - Weon, Cacha) içeren, metaforik ve melodik İspanyolcası.",
        "gastronomic_philosophy": "Fırında kıymalı üzümlü Empanada de Pino, mısır püreli Pastel de Choclo ve Pasifik deniz ürünleri (Centolla yengeci).",
        "social_taboos_and_etiquette": [
            "Pinochet diktatörlüğü ve askeri darbe dönemi hakkında taraflı ve hassasiyetsiz konuşmak toplumu derinden böler.",
            "Yemek masasında ellerin masanın üzerinde tutulmaması kabalık sayılır.",
            "Şili ile komşuları (Peru ve Bolivya) arasındaki Pasifik Savaşı mirası hakkında duyarsız şakalar yapmak."
        ],
        "literary_and_artistic_archetypes": ["Pablo Neruda", "Gabriela Mistral", "Isabel Allende", "Violeta Parra"]
    },
    {
        "country": "Peru",
        "code": "PER",
        "capital": "Lima",
        "civilization_crossroads": "İnka İmparatorluğu (Tahuantinsuyo) Mirası + And Quechua/Aymara Kültürü + İspanyol Kolonyal Zarafeti + Pasifik Gastronomi Devrimi.",
        "core_cultural_ethos": "Toprak Ana'ya (Pachamama) kutsal bağlılık, karşılıklı yardımlaşma ve manevi borç (Ayni), İnka taş işçiliğinin sabrı ve dünyanın en zengin biyo-çeşitlilik mutfağı.",
        "untranslatable_soul_concepts": [
            {
                "word": "Ayni",
                "meaning": "«Bugün bana, yarın sana»; karşılık beklemeden yapılan ama evrenin dengesi gereği mutlaka döneceğine inanılan kutsal karşılıklı yardımlaşma.",
                "cultural_significance": "And dağ köylerinde tarlaların sürülmesinden ev yapımına kadar toplumu ayakta tutan İnka ilkesi."
            },
            {
                "word": "Pachamama",
                "meaning": "Yalnızca doğa değil; bizzat yaşayan, besleyen, koruyan ve kendisine kurbanlar, şükranlar sunulan kutsal Toprak Ana tanrıçası.",
                "cultural_significance": "Yere bir damla içki dökmeden içki içilmeyen, doğayı sömürülecek nesne değil anne gören kozmoloji."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Toprağın altına kızgın taşlar gömülerek et, patates ve mısırın pişirildiği antik Pachamanca ziyafeti.",
            "Kuzey Andlarda Güneş Tanrısı İnti onuruna düzenlenen görkemli Inti Raymi kış dönümü festivali.",
            "Her lokantada ve evde yemeğe taze sıkılmış limon suyuyla pişirilen Ceviche ile başlanması."
        ],
        "communication_style": "Yüksek Bağlamlı, son derece kibar, And yerli dillerinin getirdiği yumuşak ve saygılı ses tonu.",
        "gastronomic_philosophy": "Limon suyu ve aji biberiyle pişen taze balık (Ceviche), 4000 çeşit patates, Wok tavasında pişen Lomo Saltado ve Pisco Sour.",
        "social_taboos_and_etiquette": [
            "İnka mirasını küçümsemek veya yerli Quechua/Aymara halkına karşı ayrımcı tavır sergilemek.",
            "Peru yemeklerini başka bir ülkenin (özellikle Şili'nin) mutfağıyla kıyaslayıp küçümsemek.",
            "Toprak Ana'ya (Pachamama) sunulan sembolik adaklara veya kutsal mekanlara (Apu dağları) saygısızlık."
        ],
        "literary_and_artistic_archetypes": ["Mario Vargas Llosa", "César Vallejo", "Garcilaso de la Vega (El Inca)"]
    },
    {
        "country": "Nijerya",
        "code": "NGA",
        "capital": "Abuja",
        "civilization_crossroads": "Batı Afrika'nın Devi + 250 Etnik Grup (Yoruba, Igbo, Hausa-Fulani) + Nollywood Yaratıcılığı + Afrobeats Küresel Kültürü.",
        "core_cultural_ethos": "Dur durak bilmeyen girişimci enerji (Hustle ruhu), saygı ve hiyerarşi, gösterişli ve canlı kutlamalar (Owambe), zorluklara meydan okuyan neşe ve zengin sözlü bilgelik.",
        "untranslatable_soul_concepts": [
            {
                "word": "Owambe",
                "meaning": "Göz alıcı ipek kumaşlar (Aso Ebi), canlı müzik, sonsuz yemek ve havaya para saçma geleneğiyle yapılan devasa Nijerya partisi.",
                "cultural_significance": "Sosyal bağların, zenginliğin paylaşılmasının ve hayatı kutlamanın en görkemli tezahürü."
            },
            {
                "word": "Wahala",
                "meaning": "Büyük karmaşa, dert, kaos veya bela; ancak Nijeryalıların espriyle ve tevekkülle karşılayıp altından kalktığı durum.",
                "cultural_significance": "«No Wahala» (Dert yok, hallederiz) gündelik hayatın gayriresmi sloganıdır."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Hafta sonu düğünlerinde tüm davetlilerin aynı renk ve desende özel dikim Aso Ebi kıyafeti giymesi.",
            "Büyüklerin önünde eğilerek veya yere diz çökerek selam verme (Yoruba Dobale geleneği).",
            "Nollywood sineması ve Afrobeats ritimleriyle mahalle sokaklarının adeta bir sahneye dönüşmesi."
        ],
        "communication_style": "Yüksek Bağlamlı, beden dili ve mimiklerle zenginleştirilmiş, atasözleriyle örülü, enerjik ve etkileyici Nijerya Pidgin İngilizcesi.",
        "gastronomic_philosophy": "Uğruna Gana ile tatlı rekabet yürütülen baharatlı Jollof Rice, dövülmüş manyok püresi (Pounded Yam) ve Egusi çorbası.",
        "social_taboos_and_etiquette": [
            "Bir büyüğe sol elle para veya hediye uzatmak en ağır hakaretlerden biridir; mutlaka iki el veya sağ el kullanılır.",
            "Büyüklere ismiyle hitap etmek yasaktır; mutlaka 'Auntie', 'Uncle' veya unvanıyla hitap edilir.",
            "Gözünün içine dik dik bakmak bazı geleneksel topluluklarda küstahlık ve meydan okuma sayılır."
        ],
        "literary_and_artistic_archetypes": ["Chinua Achebe (Ruhlar Parçalanıyor)", "Wole Soyinka (Nobel Edebiyat)", "Chimamanda Ngozi Adichie", "Fela Kuti"]
    },
    {
        "country": "Kenya",
        "code": "KEN",
        "capital": "Nairobi",
        "civilization_crossroads": "Doğu Afrika Svahili Sahili + Büyük Rift Vadisi Kabile Mirası (Kikuyu, Luo, Maasai) + İngiliz Kolonyal Etkisi.",
        "core_cultural_ethos": "Birlikte yükü kaldırma felsefesi (Harambee), vahşi doğa ve toprakla uyum, cemaat kararları ve istişare meclisi, sakin ve acelesiz Afrika zamanı (Pole Pole).",
        "untranslatable_soul_concepts": [
            {
                "word": "Harambee",
                "meaning": "«Hep birlikte asılalım, el birliğiyle kaldıralım»; bir çocuğun okul masrafı veya bir felaket için tüm köyün para ve emek toplaması.",
                "cultural_significance": "Kenya'nın resmi devlet armasında yer alan ve toplumu birbirine bağlayan milli dayanışma ilkesi."
            },
            {
                "word": "Pole Pole",
                "meaning": "«Yavaş yavaş, acele etmeden»; hayatın telaşla değil, sindire sindire ve doğanın ritmine saygı duyarak yaşanması gerektiği inancı.",
                "cultural_significance": "Svahili kültürünün stres ve modern panik karşısındaki zihinsel sığınağı."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Dünyanın ilk mobil para devrimi olan M-Pesa ile sokaktaki en küçük pazarcıdan taksiye kadar nakitsiz yardımlaşma.",
            "Maasai savaşçılarının zıplama dansı (Adumu) ile güç ve olgunluk kanıtlaması.",
            "Akşamları çay eşliğinde köy meclislerinde yaşlıların rehberliğinde sorunların çözülmesi."
        ],
        "communication_style": "Yüksek Bağlamlı ve son derece saygılı. Svahili dilinde selamlaşma dakikalarca sürebilir; hal hatır sormadan konuya girmek kabalıktır.",
        "gastronomic_philosophy": "Mısır unundan yapılan katı lapa (Ugali), ıspanak benzeri yeşillik Sukuma Wiki ve kömür ateşinde pişen kuzu/keçi eti Nyama Choma.",
        "social_taboos_and_etiquette": [
            "Selamlaşırken acele etmek veya el sıkışmayı hemen bırakmak soğukluk ve düşmanlık belirtisi sayılır.",
            "Sol elle selam vermek veya yemek yemek temiz kabul edilmez.",
            "Kabileler arası hassas dengeler hakkında saygısız ve önyargılı genellemeler yapmak tabudur."
        ],
        "literary_and_artistic_archetypes": ["Ngũgĩ wa Thiong'o", "Wangari Maathai (Nobel Barış Ödülü)", "Binyavanga Wainaina"]
    },
    {
        "country": "Avustralya",
        "code": "AUS",
        "capital": "Kanberra",
        "civilization_crossroads": "65.000 Yıllık Aborjin Düşzamanı (Dreamtime) + İngiliz Ceza Kolonisi ve Öncü Ruhu + Çok Kültürlü Pasifik Demokrasisi.",
        "core_cultural_ethos": "Sarsılmaz arkadaşlık ve yoldaşlık andı (Mateship), herkese eşit fırsat hakkı (Fair Go), otoriteye ve kibire karşı alaycılık (Tall Poppy Syndrome), açık hava sevgisi.",
        "untranslatable_soul_concepts": [
            {
                "word": "Mateship",
                "meaning": "Zorlu çöl şartlarında, savaşta veya gündelik hayatta bir arkadaşına koşulsuz sadakat, eşitlik ve güven duyma andı.",
                "cultural_significance": "Avustralya milli kimliğinin kutsal kavramıdır; Anzak ruhunun temelini oluşturur."
            },
            {
                "word": "Fair Go",
                "meaning": "Sosyal sınıfı, kökeni ne olursa olsun her insana eşit şans ve adil muamele gösterilmesi gerektiği inancı.",
                "cultural_significance": "Sınıfsal kibri ve hiyerarşik üstünlük taslamayı reddeden Avustralya eşitlikçiliği."
            },
            {
                "word": "Dreamtime (Jukurrpa)",
                "meaning": "Aborjin kozmolojisinde dünyanın, nehirlerin ve canlıların atalar ruhu tarafından şarkılarla yaratıldığı ezeli ve ebedi zaman boyutu.",
                "cultural_significance": "İnsan ile toprağın mülk değil akraba olduğu 65 bin yıllık yerli bilgelik."
            }
        ],
        "social_rituals_and_lifestyle": [
            "Hafta sonları parklarda ve sahillerde açık hava barbeküsü (Barbie) etrafında toplanma kültürü.",
            "25 Nisan Anzak Günü'nde (ANZAC Day) şafak vaktinde toplanarak savaşta ölenlerin anısına şafak ayini yapılması.",
            "Okyanus dalgalarıyla sörf yapma ve cankurtaran kulüplerinin (Surf Lifesaving) gönüllü sivil kahramanlığı."
        ],
        "communication_style": "Düşük Bağlamlı, gayriresmi ve kelimeleri kısaltmaya dayalı (Aussie Slang - Arvo, Brekkie, Maccas). Herkese 'Mate' denir; yapay saygı ifadelerinden hoşlanılmaz.",
        "gastronomic_philosophy": "Kömürde kanguru veya kuzu eti, mayalı tuzlu ekmek sürmesi Vegemite, Avustralya turtası (Meat Pie) ve Pavlova tatlısı.",
        "social_taboos_and_etiquette": [
            "Kendini başkalarından üstün görüp böbürlenmek ('Tall Poppy' olmak); toplum hemen o kişiyi alaya alarak hizaya çeker.",
            "Taksiye tek başına binerken arka koltuğa oturmak (şoförü hizmetkar gibi görmek sayılır; ön koltuğa oturulur).",
            "Aborjin halkının kutsal mekanlarına (Uluru gibi) saygısızca tırmanmak veya yerli mirası hiçe saymak."
        ],
        "literary_and_artistic_archetypes": ["Patrick White (Nobel)", "Banjo Paterson", "Henry Lawson", "Albert Namatjira"]
    }
]

def main():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_countries = {c["country"] for c in data.get("countries_cultural_dna", [])}
    added = 0
    for new_c in NEW_COUNTRIES_DNA:
        if new_c["country"] not in existing_countries:
            data.setdefault("countries_cultural_dna", []).append(new_c)
            added += 1

    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Added {added} new cultural DNA profiles! Total countries now: {len(data['countries_cultural_dna'])}")

if __name__ == "__main__":
    main()
