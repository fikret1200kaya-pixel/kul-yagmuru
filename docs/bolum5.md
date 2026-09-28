# 5. Bölüm — Büyük Fırın (tasarım)

Tasarım belgesindeki özetin (5.1–5.6, Seçim 5 ve Seçim 6) adım adım hâli. Vurgu rengi **ateş turuncusu**, oyundaki tek "tehlikeli" sıcak renk. Tohum **Tomurcuk** evresinde kalır ama bölüm sonunda tomurcuk ilk kez aralanır. Yeni güç: **Polen**. Görseller `docs/gorsel_tarifleri_bolum5.md`'de listelidir.

## Hikâye akışı
1. Lunaparkın arka kapısından çıkan yol, şehrin kalbindeki devasa **Büyük Fırın**'a varır. Kapıda, göğüslerinde kömür haznesi olan ateşçi robotlardan oluşan uzun bir sıra içeri girer.
2. **Ateşçi Kapısı** yalnızca ateşçi numarası olanları alır. Numara, Lehim'in göğüs kapağının iç yüzüne kazılıdır: Prolog'daki Bahçıvan'ın ayağının dibinde duran kömür kapağındaki işaretin aynısı. Lehim kendi geçmişini kullanarak içeri sızar.
3. İçeride Kül Toplayıcılar dolaşır. Tohum, havalandırmadan gelen sıcak rüzgârla **Polen** gücünü kazanır: polen, Toplayıcıların koku sensörünü şaşırtır.
4. **Kömür Bandı**nda yakalanmış bitki kırıntıları, kırık makineler ve (Seçim 2'de bırakıldıysa) kafeste **Pırpır** Fırın'a doğru ilerler → **Seçim 5**.
5. Bandın yanındaki raylarda paslı, yeşil boyası solmuş bir tren durur: seraya son tohum yükünü taşıyan tren. **Düdük** yanındaysa treni tanır, sessizce yanına oturur; bu, onun hikâyesinin kapanışıdır.
6. **Körük Salonu**'nda dev körükler sıcak hava üfler; Düdük'ün 1. Bölüm'deki ritmiyle geçilir.
7. **Ocakbaşı'nın Salonu**: kocaman, yorgun, yaşlı yönetici. Kötü değil, korkmuştur: Fırın sönerse şehrin öleceğine inanır. Yüzleşme bir dövüş değildir: toplanan hafıza çizimleri Fırın'ın projeksiyon camına dizilir ve Ocakbaşı ne yakıldığını görür.
8. **Seçim 6: Fırın'a ne olacak?** Bölüm, Lehim'in Fırın'ın tepesinden seranın kırık kubbesini ilk kez yakından görmesiyle biter.

## Sahneler
| Kod | Sahne | Çıkışlar |
|---|---|---|
| 5a | Ateşçi Kapısı | kapı → Kömür Bandı |
| 5b | Kömür Bandı | geri → Kapı, ileri → Körük Salonu |
| 5c | Körük Salonu | geri → Bant, ileri → Ocakbaşı'nın Salonu |
| 5d | Ocakbaşı'nın Salonu | geri → Körük Salonu, çatı merdiveni → bölüm sonu |

## Tohum sürükleme: Işık, Kök, Nilüfer, Sarmaşık ve Polen
Polen, havalandırma ızgarasına ya da açık bir havaya bırakılınca altın renkli bir toz bulutu olarak yayılır ve rüzgârla sürüklenir. Bulut, Toplayıcıları kendine çeker (yeşil kokusu). Güç kullanmak bedavadır.

## Yardımcılar ve önceki seçimler
- **Düdük** (Seçim 1'de ısıtıldıysa): yeşil treni görür. Körük Salonu'nda ritmi kendisi çalar. Düdük yoksa ritim oyuncunun hafızasına kalır; Tamir Defteri gösterir.
- **Pırpır** katıldıysa: Kömür Bandı'nda makasın kolunu yukarıdan çeker (Seçim 5'in üçüncü yolu kolaylaşır). Pırpır Fırın'a götürüldüyse (Seçim 2, B): bantta kafeste ilerler ve **son bir şans** vardır; kurtarılmazsa kaybedilir.
- **Kepçe** katıldıysa: 5.6 Isı Hattı'nda ağır boru vanasını çevirir.
- **Nota** kurulduysa (Seçim 4, A veya üçüncü yol): 5.5'te Ocakbaşı'na seranın açılış şarkısını çalar; ikna bir adım kolaylaşır.
- **Hafıza çizimleri**: 5.5'te ne kadar çok çizim varsa projeksiyon dizisi o kadar kolay tamamlanır.

## Bulmacalar
### 5.1 Ateşçi Kapısı (gözlem + hafıza)
- Kapının yanındaki kilitte yan yana **üç çubuk sayacı** vardır (her biri 0–9 arası çentik gösterir; rakam yok, çentik çizgileri).
- Ateşçiler sırayla göğüs kapaklarını kilide dayar ve kapı açılır. Lehim dayayınca kilit reddeder: cam kapaklı göğsü tanınmaz.
- Lehim göğüs kapağını açar (kendine dokun) ve iç yüzünde kazılı çentikleri görür: **4 çentik, 7 çentik** (Prolog'daki kömür kapağındaki 47 işareti). Sayaçlar **0, 4, 7** yapılır.
- Kapı açılır. Işık yok: bu an bir kazanç değil, bir ağırlıktır; Lehim bir an göğsünü tutar.

### 5.2 Koku Sensörü (Polen öğretici)
- Kapının hemen ardındaki koridorda bir Toplayıcı nöbet tutar, hortumunu havada gezdirir; tohumu koklar ve Lehim'e döner.
- Tavandaki havalandırma ızgarasından sıcak hava üfler. Tohumu ızgaraya sürükle → tomurcuk polen saçar, **Polen** gücü açılır.
- Polen bulutu rüzgârla yan koridora sürüklenir, Toplayıcı peşinden gider. Yol açılır.

### 5.3 Kömür Bandı (Seçim 5 + zamanlama)
- Uzun bir bant; üstünde kömür, kırık makineler, küçük yeşil kırıntılar ve (varsa) kafeste Pırpır, Fırın ağzına doğru ilerler. Bandın ortasında bir **makas** vardır: kolu çekilince bant iki yola ayrılır, biri Fırın'a, biri **atık kanalına** gider.
- **A: Bandı kökle durdur.** Tohumu dişli motora sürükle: −1 Canlılık, alarm çalar, bant durur, her şey kurtulur ama Körük Salonu'nda iki Toplayıcı bekler.
- **B: Geçip git.** Bant akmaya devam eder; bu sahne kalıcı olarak gri kalır, Işık kaybedilir. (Pırpır kafesteyse kaybedilir.)
- **Üçüncü yol: Makası zamanla.** Bandın üstündeki her canlı şey (yeşil kırıntı, kırık makine, Pırpır'ın kafesi) makasa geldiği anda kolu çek; hepsi atık kanalına kayar. Kömür gelirken çekersen kömür de kanala düşer ve makas birkaç saniye tutukluk yapar (ceza yok, yeniden dene). Pırpır yanındaysa kolu o çeker; oyuncu sadece zamanı söyler (kola dokunur, Pırpır tepeden iner).

### Düdük ve yeşil tren (anlatı)
- Bandın arkasındaki raylarda, boyası solmuş yeşil bir tren durur; vagonlarında boş cam fide kasaları vardır.
- Düdük yanındaysa trene yürür, kasketini çıkarır, buhar düdüğünü bir kez yavaşça öttürür ve lokomotifin yanına oturur. Kalır. Bu sahne yazısız ve kısadır.
- Düdük yoksa tren sessizdir; lokomotifin kabininde Düdük'ün kasketine benzeyen eski bir kasket asılıdır.

### 5.4 Körük Salonu (ritim)
- Dev körükler salonun ortasındaki geçide sırayla sıcak hava üfler. Geçmek için, körüklerin arasındaki basınç kolunu doğru ritimde çalıştırmak gerekir: **kısa, kısa, uzun, kısa**, 1. Bölüm'deki Düdük'ün ritmi.
- Düdük yanındaysa ritmi çalar. Değilse oyuncu hatırlamalıdır; yanlış ritimde körük Lehim'i başa üfler (ceza yok).
- Seçim 5'te A seçildiyse (alarm) salonda iki Toplayıcı vardır; polenle yan kapıya çekilmeleri gerekir.

### 5.5 Ocakbaşı'nı İkna (sıralama + hafıza)
- Salonun ortasında Fırın'ın dev projeksiyon camı durur; önünde **altı çerçeve**. Ocakbaşı, Fırın'ın gücüyle çalışan bir gölge makinesini de kontrol eder.
- Oyuncunun topladığı her **hafıza çizimi** bir cam levhadır (1. Bölüm'den bu yana en fazla 7). Levhalar çerçevelere hikâyenin sırasıyla dizilir: seranın açılışı → bahçıvanlar ve son tohum treni → liman günleri → lunapark → ormanların kesilip taşınması → ateşçiler.
- Eksik çerçeveler için Ocakbaşı'nın masasındaki **boş levhalar** kullanılır; boş levhaya tohumla dokununca, önceki ve sonraki çizime bakılarak mantıkla tamamlanan bir eskiz belirir. Ne kadar çok çizim varsa o kadar az boş levha gerekir.
- Nota kurulduysa, levhalar dizilirken seranın açılış şarkısını çalar ve Ocakbaşı ilk levhada durur.
- Doğru sırada dizilince projeksiyon oynar; Ocakbaşı yıllardır yaktığı şeyin bahçeler olduğunu görür ve çöker. Işık +2. Ocakbaşı "ikna edildi" sayılır.

### 5.6 Isı Hattı (büyük mekanizma, Seçim 6'nın üçüncü yolu)
- Ocakbaşı ikna edildiyse, salonun duvarındaki eski boru panosunu açar: Fırın'ın ısısını şehirden kesip seraya yönlendirecek bir boru ızgarası.
- 5x5 boru ızgarası: parçalar dokunuldukça döner; Fırın'dan çıkan sıcak hattı seraya bağlanmalıdır. Yol üzerinde bir **ağır vana** vardır; Kepçe yanındaysa onu çevirir, değilse vana etrafından dolanılan daha uzun bir yol gerekir.

### Seçim 6 — Fırın'ın kaderi
- **A: Söndür.** Ocakbaşı'nın büyük koluna tohumla kök sal ve indir. Fırın söner; şehir kararır, makineler yavaşlar (finalin ışık kaynağı zayıflar).
- **B: Açık bırak.** Hiçbir şeye dokunmadan çatı merdiveninden çık. Seraya yalnızca tohumla girilir; final her zaman "az dost" tarafına düşer.
- **Üçüncü yol: Isıyı seraya yönlendir.** 5.5 ve 5.6 çözüldüyse Ocakbaşı kolu kendisi çevirir; Fırın'ın ısısı seraya gider. Finalde ısı buradan gelir.

## İsteğe bağlı
- **Paşa Kedi:** Kömür bandının sıcak motor kapağında uyur.
- **Posta Güvercini:** Körük Salonu'nda, bir körüğün ipine dolanmıştır; polenle ya da kökle kurtarılır, hafıza çizimi verir (genç Ocakbaşı'nın, enerji tükenirken şehri kurtarmak için Fırın'ı ilk yaktığı gece; onun korkusunu anlatır).
- **Çarklar (3):** Paşa Kedi, ateşçi kapısının yanındaki kömür yığını, Ocakbaşı'nın masasının çekmecesi.

## Tamir Defteri ipucu sırası
5.1 göğüs kapağı ve kilit → Polen (havalandırma) → 5.2 Toplayıcı → 5.3 bant → 5.4 körükler → 5.5 projeksiyon → 5.6 ısı hattı → Seçim 6.
