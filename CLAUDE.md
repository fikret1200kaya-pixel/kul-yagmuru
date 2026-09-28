# Kül Yağmuru — Son Tohumun Yolculuğu

Machinarium tarzı, diyalogsuz, el çizimi görünümlü point-and-click mobil oyun. Yayıncı: EFKA Games. Tüm yanıtlar Türkçe olmalı.

## Durum
- `game/index.html`: tek dosyalık HTML5 canvas oyunu (kütüphanesiz). Oynanabilir: Prolog (Hurda Çukuru P-A, Hurdalık Kapısı P-B) ve 1. Bölüm — Durmuş Saatler İstasyonu (1a Peron, 1b Bekleme Salonu, 1c Makas Kulübesi, 1d Vagon İçi; bulmacalar 1.1–1.6, Seçim 1'in üç yolu, Posta Güvercini yan görevi, 3 gizli çark).
- 1. Bölüm'ün adım adım çözümü ve tasarım kararları: `docs/bolum1.md`.
- `game/img/`: oyunda kullanılan işlenmiş görseller (arka planlar 1280x720 `bg_*`, yakın çekimler `cu_*`, kesilmiş sprite'lar, Lehim'in önden `rig_*` ve yandan `side_*` parça animasyonu).
- `assets/raw/`: ChatGPT/ElevenLabs ile üretilen orijinal görseller (A = arka plan, B = yakın çekim, C = karakter sayfası, D = ek görsel).
- `tools_cut.py`: karakter sayfalarından arka planı silip pozları kesen yardımcı betik. `tools_bolum1.py`: 1. Bölüm görsellerini `assets/raw`'dan `game/img`'ye üretir (Pillow, numpy, opencv).

## Kurallar
- Dünya gri/sepyadır; tek canlı renk tohumun yeşilidir. Sahneler tam renkli çizilir, oyunda kodla griye çevrilir; tamir edilen yerlerde renk halkası geri gelir. Yardım edilen karakterler renkli çizilir.
- Görsellerde yazı yok. Bitki/ağaç/yaprak yok (hepsi yanıp kül olmuş).
- Kahraman: Lehim (düğme gözlü teneke tamirci, gri atkı, sönük fener). Tohum: Filiz. Değerler: Canlılık (0-5, sayı olarak gösterilmez; tohumun parlaklığıyla hissedilir), Işık, Çark.
- Tohum gücünü bulmacada kullanmak bedavadır; bir canlıya hayat vermek 1 Canlılık harcar.

## Kod yapısı (index.html)
- Sahneler `HS[sahne]` dizisindeki etkin alanlardır: `r` dokunma dikdörtgeni, `stand` Lehim'in durduğu nokta, `tap`/`use[eşya]`/`light` işleyicileri, `to` sahne çıkışı.
- `GEO` her sahnenin yürünebilir zeminini ve Lehim'in ölçeğini, `DRAW1` 1. Bölüm sahnelerinin kodla çizilen katmanlarını, `drawOverlayB1` yakın çekimleri tutar.
- İpuçları (Tamir Defteri) `hintB1` sırasıyla verilir; başka sahnedeki hedef için o sahneye giden çıkış vurgulanır.
- İlerleme `localStorage` `ky_bolum` anahtarında tutulur; başlık ekranında "1. Bölüm" seçeneği çıkar. `?bolum=1` bu seçeneği her zaman gösterir, `?debug` durumu `window.KY` olarak açar (otomatik test için).

## Sıradaki iş
- 1. Bölüm prototipini telefonda test etmek (GDD üretim planı aşama 4), sonra 2. Bölüm — Borular Mahallesi.
- Eksikler: Tamir Defteri'nin Çark karşılığı 2. ve 3. seviye ipuçları; körük alındıktan sonra duvardaki körük görseli arka planda kalıyor.

## Çalıştırma
`cd game && python3 -m http.server 8000` ve tarayıcıda http://localhost:8000 (doğrudan 1. Bölüm için http://localhost:8000/?bolum=1)
