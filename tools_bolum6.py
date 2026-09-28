"""6. Bölüm ve Epilog görsellerini assets/raw'dan game/img'ye hazırlar.
Çalıştırma: python3 tools_bolum6.py  (Pillow, numpy, opencv gerekir)
"""
from tools_bolum1 import bg, square
from tools_bolum3 import sprites_at


if __name__ == '__main__':
    bg('A22_kubbe_disi', 'bg_6a')
    bg('A23_seranin_kalbi', 'bg_6b')
    square('B22_melodi_kapisi', 'cu_melodi')
    square('B23_toprak_havuzu', 'cu_toprak')
    square('B24_gogus_kapagi_cicek', 'cin_cicek', 640)
    square('D14_hafiza_cizimi_8', 'cu_hafiza8')
    # the endings are full-screen cinematics, kept at scene size
    for i, n in enumerate(['yesil_sabah', 'yalniz_bahce', 'tek_yaprak', 'son_kivilcim'], 1): bg(f'E{i}_son_{n}', f'son_{i}')
    bg('E5_gizli_son_yagmur', 'son_5')
    sprites_at('D15_cicek', [0, .33, .64, 1], 'cicek', 150, thr=60)
