"""5. Bölüm görsellerini assets/raw'dan game/img'ye hazırlar.
Çalıştırma: python3 tools_bolum5.py  (Pillow, numpy, opencv gerekir)
"""
from tools_bolum1 import bg, square
from tools_bolum3 import sprites_at

def clear_feet(prefix, n, paper=(250, 240, 222)):
    """The sheets paint a soft paper shadow under the feet; clear near-paper pixels in the bottom fifth."""
    import numpy as np
    from PIL import Image
    for i in range(1, n + 1):
        p = f'game/img/{prefix}_{i}.png'
        a = np.array(Image.open(p)).astype(np.int16)
        h = a.shape[0]
        d = np.abs(a[:, :, :3] - np.array(paper)).sum(2)
        m = (d < 70); m[:int(h * .8)] = False
        a[:, :, 3] = np.where(m, 0, a[:, :, 3])
        Image.fromarray(a.astype(np.uint8)).save(p)


if __name__ == '__main__':
    bg('A18_atesci_kapisi', 'bg_5a')
    bg('A19_komur_bandi', 'bg_5b')
    bg('A20_koruk_salonu', 'bg_5c')
    bg('A21_ocakbasi_salonu', 'bg_5d')
    square('B20_atesci_kilidi', 'cu_atkilit')
    square('B21_gogus_kapagi_ic', 'cu_gogus')
    square('D13_hafiza_cizimi_7', 'cu_hafiza7')
    # pose 2 reaches its claw over pose 3's column: widen its cut and paper over pose 3's body
    sprites_at('C16_ocakbasi', [(0, .225), (.225, .56), (.505, .74), (.74, 1)], 'ocakbasi', 300, thr=60, blank={2: [(.515, .27, .56, 1)], 3: [(.5, 0, .56, .25)]})
    sprites_at('C17_atesci_robotlar', [0, .4, .69, 1], 'atesci', 150, thr=60)
    clear_feet('ocakbasi', 4); clear_feet('atesci', 3)
    # the green train is painted into the coal-belt scene; the pollen is drawn by the game
