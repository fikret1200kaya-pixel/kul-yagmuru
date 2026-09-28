"""4. Bölüm görsellerini assets/raw'dan game/img'ye hazırlar.
Çalıştırma: python3 tools_bolum4.py  (Pillow, numpy, opencv gerekir)
"""
from tools_bolum1 import bg, square
from tools_bolum3 import sprites_at

def clean_strings():
    """The Puppeteer's strings trap little islands of paper between them; clear near-paper pixels."""
    import numpy as np
    from PIL import Image
    for i in (1, 2, 3):
        p = f'game/img/kuklaci_{i}.png'
        a = np.array(Image.open(p)).astype(np.int16)
        d = np.abs(a[:, :, :3] - np.array([252, 240, 219])).sum(2)
        a[:, :, 3] = np.where(d < 55, 0, a[:, :, 3])
        Image.fromarray(a.astype(np.uint8)).save(p)


if __name__ == '__main__':
    bg('A14_lunapark_girisi', 'bg_4a')
    bg('A15_donme_dolap', 'bg_4b')
    bg('A16_carpisan_arabalar', 'bg_4c')
    bg('A17_golge_tiyatrosu', 'bg_4d')
    square('B17_kapi_kilidi', 'cu_kilit')
    square('B18_yirtik_afisler', 'cu_afisler')
    square('B19_gogus_kapagi_tomurcuk', 'cin_tomurcuk', 640)
    square('D10_hafiza_parlamasi', 'cu_parilti')
    square('D11_hafiza_cizimi_6', 'cu_hafiza6')
    sprites_at('C13_nota', [0, .26, .5, .745, 1], 'nota', 170, thr=60)
    sprites_at('C14_kuklaci', [0, .26, .7, 1], 'kuklaci', 260, thr=60)
    clean_strings()
    # the fourth puppet is drawn from Lehim's own sprite in the game, so only the first three are cut
    sprites_at('C15_kuklalar', [0, .2, .53, .77], 'kukla', 200, thr=60)
