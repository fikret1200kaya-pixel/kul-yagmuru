# 1. Bölüm — Durmuş Saatler İstasyonu

Tasarım belgesindeki bulmaca özetlerinin (1.1–1.6, Seçim 1) oyunda nasıl kurulduğu. Vurgu rengi kehribar (lamba ışığı); bölüm sonunda tohum Filiz evresine geçer.

## Sahneler
| Kod | Sahne | Çıkışlar |
|---|---|---|
| 1a | Peron (merkez) | sol → Bekleme Salonu, ray yolu → Makas Kulübesi, vagon kapısı → Vagon İçi |
| 1b | Bekleme Salonu | sol kapı → Peron |
| 1c | Makas Kulübesi | sol → Peron |
| 1d | Vagon İçi | arka kapı → Peron |

## Çözüm yolu
1. **1.1 Sönük Lamba (1b):** Bankın altı karanlıktır. Tohum ışığını (Lehim'den sürükle) banka bırak, ampul görünür. Ampulü asılı lambaya sürükle. Salon aydınlanır; duvarda iki tebeşir çizimi çıkar: teldeki mıknatısla borudan dişli çekmek ve uyuyan kedinin altındaki jeton.
2. **Mıknatıs (1b):** Hoparlöre dokun, içinden mıknatıs düşer.
3. **Tel (1a):** Bavula dokun.
4. **Olta:** Envanterde mıknatısı telin üstüne sürükle.
5. **1.2 Durmuş Saat (1a):** Oltayı kırık boruya ver → dişli. Tarifenin kopan alt yarısı peronun sağında, molozların arasındadır; direkteki afişe tak. Yeşil tohum treninin saati **4:10**'dur. Dişliyi saate ver; yakın çekimde iç daire akrebi, dış halka yelkovanı çevirir. Saat çalınca vagondaki Düdük uyanır ama üşür ve zayıf bir düdük ritmi çalar.
6. **1.3 Bilet Gişesi (1a → 1b):** Bankta uyuyan Paşa Kedi'yi okşa: altından jeton ve bir çark çıkar. Jetonu gişe robotuna ver → üzerinde makas diyagramı olan bilet. Envanterdeki bilete dokununca yakın çekimi açılır.
7. **1.4 Makas Kulübesi (1c):** Kulübedeki panoda 3x3 ray parçası vardır; dokunulan parça 90° döner. Biletteki yol: sol alttan gir, orta sıraya çık, sağ üstten çık. Yol ilerledikçe üstteki 5 lamba yanar.
8. **1.5 Düdük'ün Soğuğu — Seçim 1 (1d):**
   - **A: Tohumla ısıt.** Tohum ışığını Düdük'e sürükle: −1 Canlılık, Düdük katılır.
   - **B: Bırak.** Düdük'e yardım etmeden drezine binersen seçim ekranı çıkar; sağ taraf Düdük'ü uykuda bırakır (5. bölümde tren yardımı yok). Ritim ekranından çıkıp geri dönen oyuncu onu hâlâ ısıtabilir.
   - **Üçüncü yol: Sobayı tamir et.** Kül briketini sobaya koy, tohum ışığıyla közü yak (güç kullanımı, bedava), körüğü (1c'deki duvardan) sobaya ver. Canlılık harcanmaz, +2 Işık.
9. **1.6 Düdük'ün Ritmi (1c):** Drezine dokun. Düdük yanındaysa ritmi çalar (Düdük simgesi tekrar çaldırır). Ritim: **kısa, kısa, uzun, kısa**. Kola kısa bas = kısa, basılı tut = uzun. Doğru ritimde tünel ızgarası kalkar ve drezin yola çıkar. Düdük yoksa ritim hatırlanmalı; Tamir Defteri ritmi gösterir.

## İsteğe bağlı
- **Posta Güvercini (1d):** Bagaj rafına takılmış. Oltayı rafa ver → 1. hafıza çizimi (Bahçıvanlar ve seradaki küçük robotlar).
- **Çarklar:** Paşa Kedi (1a), radyatörün dibi (1b, salon aydınlanınca), kömür çuvalı (1c).

## Test
`game/index.html?bolum=1&debug`, oyun durumunu `window.KY` olarak açar. Bölüm üç Seçim 1 yoluyla da uçtan uca headless Chromium'da oynatıldı; konsolda hata yok.
