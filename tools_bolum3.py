"""3. Bölüm görsellerini assets/raw'dan game/img'ye hazırlar.
Çalıştırma: python3 tools_bolum3.py  (Pillow, numpy, opencv gerekir)
"""
import os, glob
from PIL import Image
from tools_bolum1 import bg, square, sprites, RAW, OUT, PROC
from tools_cut import cut_cells


def sprites_at(name, cuts, out, height, **kw):
    """Like sprites(), but with hand-picked column borders (fractions of the width) for sheets whose poses overlap equal cells."""
    import numpy as np
    im = Image.open(f'{RAW}/{name}.webp').convert('RGB')
    w, h = im.size
    a0 = np.array(im)
    paper = tuple(int(v) for v in np.median(np.concatenate([a0[:8].reshape(-1, 3), a0[-8:].reshape(-1, 3)]), axis=0))
    for f in glob.glob(f'{PROC}/{out}_*.png'): os.remove(f)
    for i, (a, b) in enumerate(zip(cuts, cuts[1:]), 1):
        # the pose on a clean sheet of paper, so the background touches every edge
        tmp = f'{PROC}/_cell.png'
        x0, x1 = int(a * w), int(b * w)
        sheet = Image.new('RGB', (x1 - x0 + 40, h + 40), paper)
        sheet.paste(im.crop((x0, 0, x1, h)), (20, 20))
        sheet.save(tmp)
        cut_cells(tmp, 1, 1, f'_{out}', **kw)
        os.replace(f'{PROC}/_{out}_1.png', f'{PROC}/{out}_{i}.png')
        os.remove(tmp)
        s = Image.open(f'{PROC}/{out}_{i}.png')
        s.resize((max(1, round(s.width * height / s.height)), height), Image.LANCZOS).save(f'{OUT}/{out}_{i}.png')


def patches():
    """Patches stamped over the background when a painted object is taken:
    patch_varil (the barrel pulled off the ash, cloned from the pier further right, keeping the post between)
    patch_lambalar (the spare lanterns taken from the lighthouse shelf, window bays repeated and feathered)."""
    import cv2, numpy as np
    a = cv2.imread(f'{OUT}/bg_3a.jpg')
    y0, y1 = 588, 672
    # the pier's underside repeats every few metres: copy the stretch 320 px to the right
    cv2.imwrite(f'{OUT}/patch_varil.png', a[y0:y1, 506:684])
    # the lantern shelf stands before tall windows, like the ones right of the lens
    b = cv2.imread(f'{OUT}/bg_3b.jpg')
    strip = b[168:258, 804:848]  # one clean window bay, repeated across the shelf top
    p = np.hstack([strip, cv2.flip(strip, 1), strip, cv2.flip(strip, 1), strip])[:, :180]
    h, w = p.shape[:2]
    # feather the edges so the patch melts into the painting
    alpha = np.ones((h, w), np.float32)
    for i in range(14): k = i / 14; alpha[i, :] *= k; alpha[:, i] *= k; alpha[:, w - 1 - i] *= k
    rgba = np.dstack([p, (alpha * 255).astype(np.uint8)])
    cv2.imwrite(f'{OUT}/patch_lambalar.png', rgba)


if __name__ == '__main__':
    bg('A10_iskele', 'bg_3a')
    bg('A11_deniz_feneri', 'bg_3b')
    bg('A12_batik_vapur', 'bg_3c')
    bg('A13_tas_ocagi', 'bg_3d')
    square('B13_isaret_tablosu', 'cu_isaret')
    square('B14_fener_lensi', 'cu_lens')
    square('B15_cay_ocagi', 'cu_cay')
    square('B16_gogus_kapagi_sarmasik', 'cin_sarmasik', 640)
    square('D8_hafiza_cizimi_4', 'cu_hafiza4')
    square('D9_hafiza_cizimi_5', 'cu_hafiza5')
    sprites_at('C11_capa', [0, .285, .525, .795, 1], 'capa', 230, thr=60)
    sprites_at('C12_kepce', [0, .24, .47, .70, 1], 'kepce', 300, thr=60)
    sprites_at('D7_nilufer', [0, .28, .61, 1], 'nilufer', 110, thr=60, keep_ratio=.2)
    patches()
