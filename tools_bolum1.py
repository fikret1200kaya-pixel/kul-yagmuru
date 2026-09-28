"""1. Bölüm görsellerini assets/raw'dan game/img'ye hazırlar.

Arka planlar 1280x720'ye kırpılır, yakın çekimler kare JPG olur,
karakter sayfalarındaki pozlar tools_cut.cut_cells ile kesilip küçültülür.
Çalıştırma: python3 tools_bolum1.py  (Pillow, numpy, opencv gerekir)
"""
import os, glob
from PIL import Image
from tools_cut import cut_cells

RAW, OUT, PROC = 'assets/raw', 'game/img', 'assets/proc'


def bg(name, out, y0=None):
    im = Image.open(f'{RAW}/{name}.webp').convert('RGB')
    w, h = im.size
    ch = round(w * 9 / 16)
    if ch < h:  # 3:2 kaynak: 16:9'a kırp
        y0 = (h - ch) // 2 if y0 is None else y0
        im = im.crop((0, y0, w, y0 + ch))
    im.resize((1280, 720), Image.LANCZOS).save(f'{OUT}/{out}.jpg', quality=84)


def square(name, out, size=600, box=None):
    im = Image.open(f'{RAW}/{name}.webp').convert('RGB')
    if box: im = im.crop(box)
    im.resize((size, size), Image.LANCZOS).save(f'{OUT}/{out}.jpg', quality=84)


def sprites(name, rows, cols, out, height, **kw):
    for f in glob.glob(f'{PROC}/{out}_*.png'): os.remove(f)
    cut_cells(f'{RAW}/{name}.webp', rows, cols, out, **kw)
    for f in sorted(glob.glob(f'{PROC}/{out}_*.png')):
        im = Image.open(f)
        k = height / im.height
        im.resize((max(1, round(im.width * k)), height), Image.LANCZOS).save(f'{OUT}/{os.path.basename(f)}')


if __name__ == '__main__':
    os.makedirs(PROC, exist_ok=True)
    bg('1A_peron', 'bg_1a')
    bg('A3_bekleme_salonu', 'bg_1b', 70)
    bg('A4_makas_kulubesi', 'bg_1c', 120)
    bg('A5_vagon_ici', 'bg_1d', 90)
    square('B1_saat_kadrani', 'cu_saat')
    square('B2_tarife_afisi', 'cu_tarife')
    square('B3_makas_panosu', 'cu_makas')
    square('B4_bilet', 'cu_bilet', 640)
    square('D1_hafiza_cizimi_1', 'cu_hafiza1')
    square('B7_gogus_kapagi_filiz', 'cin_filiz', 640)
    sprites('C2_duduk', 1, 4, 'duduk', 330, thr=70, bigbg=300, keep_ratio=.0015)
    sprites('C3_giseci', 1, 3, 'giseci', 230)
    sprites('C4_pasa_kedi', 1, 4, 'kedi', 150)
    sprites('C5_posta_guvercini', 1, 3, 'guvercin', 130, thr=70, bigbg=300, keep_ratio=.0015)
