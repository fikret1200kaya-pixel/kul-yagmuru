# Kül Yağmuru — Son Tohumun Yolculuğu

Machinarium tarzı, diyalogsuz, el çizimi görünümlü point-and-click mobil oyun. Yayıncı: EFKA Games. Tüm yanıtlar Türkçe olmalı.

## Durum
- `game/index.html`: tek dosyalık HTML5 canvas oyunu (kütüphanesiz). Oynanabilir: Prolog (Hurda Çukuru P-A, Hurdalık Kapısı P-B) , 1. Bölüm — Durmuş Saatler İstasyonu (1a Peron, 1b Bekleme Salonu, 1c Makas Kulübesi, 1d Vagon İçi; bulmacalar 1.1–1.6, Seçim 1'in üç yolu, Posta Güvercini yan görevi, 3 gizli çark) ve 2. Bölüm — Borular Mahallesi (aşağıda).
- 1. Bölüm'ün adım adım çözümü ve tasarım kararları: `docs/bolum1.md`.
- `game/img/`: oyunda kullanılan işlenmiş görseller (arka planlar 1280x720 `bg_*`, yakın çekimler `cu_*`, kesilmiş sprite'lar, Lehim'in önden `rig_*` ve yandan `side_*` parça animasyonu).
- `assets/raw/`: ChatGPT/ElevenLabs ile üretilen orijinal görseller (A = arka plan, B = yakın çekim, C = karakter sayfası, D = ek görsel).
- `tools_cut.py`: karakter sayfalarından arka planı silip pozları kesen yardımcı betik. `tools_bolum1.py`: 1. Bölüm görsellerini `assets/raw`'dan `game/img`'ye üretir (Pillow, numpy, opencv).

## Kurallar
- Dünya gri/sepyadır; tek canlı renk tohumun yeşilidir. Sahneler tam renkli çizilir, oyunda kodla griye çevrilir; tamir edilen yerlerde renk halkası geri gelir. Yardım edilen karakterler renkli çizilir.
- Görsellerde yazı yok. Bitki/ağaç/yaprak yok (hepsi yanıp kül olmuş).
- Kahraman: Lehim (düğme gözlü teneke tamirci, gri atkı, sönük fener). Tohum: Filiz. Değerler: Canlılık (0-5, sayı olarak gösterilmez; tohumun parlaklığıyla hissedilir), Işık, Çark.
- Tohum gücünü bulmacada kullanmak bedavadır; bir canlıya hayat vermek 1 Canlılık harcar.

## Sahne hissi (her yeni sahnede uygulanır)
- **Arka plan durağan kalmaz:** Her sahneye ortam hareketi eklenir: baca dumanı ve buhar (`EMIT`), titreşen fenerler (`lamp`), sürüklenen sis (`mist`), ışık huzmesinde toz (`motes`), pencere dışında kar (`windowSnow`), yanıp sönen sinyaller (`signal`). Kod `drawAmbient` / `drawAmbientFront` içinde durur.
- **Lehim fotoğrafın üstünde gezmez:**
  - Öndeki nesneler `FG[sahne]` çokgenleriyle arka plandan kesilip taban çizgilerine (`y`) göre Lehim'in önüne çizilir.
  - Karakterler ve sahne eşyaları `dq(y, çiz)` ile aynı derinlik sırasına girer.
  - Karanlık, derinlik sırasından sonra en üste serilir; tohumun ışığı karanlığın içinden parlar.
  - Lehim sahnenin ışığını alır (`lehimTint`).
- **Nesneyi kapatmaz:** Etkin alanların `stand` noktası nesnenin yanında seçilir, üstünde değil. Lehim nesneye döner ve elini uzatır (`reach`).

## Kod yapısı (index.html)
- Sahneler `HS[sahne]` dizisindeki etkin alanlardır: `r` dokunma dikdörtgeni, `stand` Lehim'in durduğu nokta, `tap`/`use[eşya]`/`light` işleyicileri, `to` sahne çıkışı.
- `GEO` her sahnenin yürünebilir zeminini ve Lehim'in ölçeğini, `DRAW1` 1. Bölüm sahnelerinin kodla çizilen katmanlarını, `drawOverlayB1` yakın çekimleri tutar.
- Tamir Defteri üç seviyelidir (GDD): Bakış ücretsiz ve 5 dakikada bir dolar (hedefi, başka sahnedeyse o sahnenin çıkışını vurgular), Fikir 1 Çark (tek eskiz), Tam çözüm 3 Çark (adım adım satırlar). Hedef sırası `hintB1`, eskizler `DEFTER` tablosundadır; satın alınan seviye o hedef için kalıcıdır.
- İlerleme `localStorage` `ky_bolum` anahtarında tutulur; başlık ekranında "1. Bölüm" seçeneği çıkar. `?bolum=1` bu seçeneği her zaman gösterir, `?debug` durumu `window.KY` olarak açar (otomatik test için).

## 2. Bölüm
- Oynanabilir: 2a Buhar Meydanı, 2b Nine Saat'in Evi, 2c Hurdacı Sokağı, 2d Asansör Kulesi. Tasarım `docs/bolum2.md`, görseller `tools_bolum2.py` ile üretilir.
- Kök gücü: tohum sürüklemesi, hedefin `kok()` işleyicisi varsa kök olur (`growRoot`), yoksa ışık (`light()`). Bez Lehim'e takılıyken ikisi de kapalıdır.
- Asansör Kulesi'ndeki iki dişli arka plandan kesilip `disli_kucuk` / `disli_buyuk` sprite'ı yapıldı; yerleri komşu dokuyla yamandı.
- Test için `?bolum=2` başlıkta 2. Bölüm seçeneğini açar.

## 3. Bölüm
- Oynanabilir: 3a İskele, 3b Deniz Feneri, 3c Batık Vapur, 3d Taş Ocağı. Tasarım `docs/bolum3.md`, görseller `tools_bolum3.py` ile üretilir.
- Nilüfer gücü: hedefin `nil()` işleyicisi varsa tohum orada yaprak açar (`openLily`, birkaç saniye sonra batar). Göl geçişi `crossStep`: fenerin gösterdiği sırayla batık makinelere nilüfer açılır, Lehim üstüne zıplar (`hopTo`); yanlış sıra ya da batan yaprak onu iskeleye geri yüzdürür (`fallIn`).
- Kepçe taş ocağı arka planına çizilidir; korkarken bölgesi titretilir, sakinleşince gözleri yanar.
- Alınan boyalı nesneler için arka plana yama basılır (`stamp`): `patch_varil`, `patch_lambalar`.
- Yardımcılar bölümler arası `S.dost` içinde taşınır (Düdük, Pırpır, kurma anahtarı, Kepçe, su şişesi); Pırpır katıldıysa sonraki bölümlerde de Lehim'i izler.

## 4. Bölüm
- Oynanabilir: 4a Giriş, 4b Dönme Dolap, 4c Çarpışan Arabalar ve Aynalı Labirent, 4d Gölge Tiyatrosu (sahneler sıralı bağlı). Tasarım `docs/bolum4.md`, görseller `tools_bolum4.py`.
- Sarmaşık gücü: hedefin `sar()` işleyicisi varsa tohum orada sarmaşık olur.
- Pist bulmacası `PIST0` (Kepçe ile 6, onsuz 12 hamle; `pistNext` en kısa yolu arar, Pırpır ipucu için). Ayna labirenti `aynaTrace`.
- Gölge oyununun son kuklası Lehim'in kendi görseliyle çizilir (`drawKukla`).

## Sıradaki iş
- Test sürümünde ipuçları sınırsız ve ücretsiz: `IPUCU_SINIRSIZ = true`. Yayından önce `false` yapılacak.
- Test sürümünde devriyede iki kez yakalanınca Toplayıcı uyuklar (geçiş serbest). Oyuncu devriyeyi geçemedi: telefonda zamanlama ve saklanma yerleri gözden geçirilecek.
- 5. Bölüm — Büyük Fırın: önce adım adım tasarım ve görsel tarifleri.
- 1. Bölüm prototipini telefonda test etmek (GDD üretim planı aşama 4).
- Bilinen eksik: körük alındıktan sonra duvardaki körük görseli arka planda kalıyor.

## Çalıştırma
`cd game && python3 -m http.server 8000` ve tarayıcıda http://localhost:8000 (doğrudan 1. Bölüm için http://localhost:8000/?bolum=1)
