# Kül Yağmuru — Son Tohumun Yolculuğu

Machinarium tarzı, diyalogsuz, el çizimi görünümlü point-and-click mobil oyun. Yayıncı: EFKA Games. Tüm yanıtlar Türkçe olmalı.

## Durum
- `game/index.html`: tek dosyalık HTML5 canvas oyunu (kütüphanesiz). Prolog oynanabilir: Hurda Çukuru (P-A) ve Hurdalık Kapısı (P-B).
- `game/img/`: oyunda kullanılan işlenmiş görseller (arka planlar 1280x720, kesilmiş sprite'lar, Lehim'in önden `rig_*` ve yandan `side_*` parça animasyonu).
- `assets/raw/`: ChatGPT/ElevenLabs ile üretilen orijinal görseller (A = arka plan, B = yakın çekim, C = karakter sayfası, D = ek görsel).
- `tools_cut.py`: karakter sayfalarından arka planı silip pozları kesen yardımcı betik.

## Kurallar
- Dünya gri/sepyadır; tek canlı renk tohumun yeşilidir. Sahneler tam renkli çizilir, oyunda kodla griye çevrilir; tamir edilen yerlerde renk halkası geri gelir.
- Görsellerde yazı yok. Bitki/ağaç/yaprak yok (hepsi yanıp kül olmuş).
- Kahraman: Lehim (düğme gözlü teneke tamirci, gri atkı, sönük fener). Tohum: Filiz. Değerler: Canlılık (0-5), Işık, Çark.

## Sıradaki iş
1. Bölüm — Durmuş Saatler İstasyonu: sahneler 1-A Peron (`assets/raw/1A_peron.webp`), 1-B Bekleme Salonu (A3_bekleme_salonu.webp), 1-C Makas Kulübesi (A4), 1-D Vagon İçi (A5); bulmacalar 1.1–1.6 ve Seçim 1 (Düdük). Ayrıntılı senaryo tasarım belgesindeki "Prolog ve 1. Bölüm Senaryosu" sekmesindedir.

## Çalıştırma
`cd game && python3 -m http.server 8000` ve tarayıcıda http://localhost:8000
