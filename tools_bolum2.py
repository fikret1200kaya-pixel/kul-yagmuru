"""2. Bölüm görsellerini assets/raw'dan game/img'ye hazırlar.
Çalıştırma: python3 tools_bolum2.py  (Pillow, numpy, opencv gerekir)
"""
import numpy as np
from PIL import Image
from tools_bolum1 import bg, square, sprites


def fix_nine1():
    """The crying pose touches its cell edge, so paper is left to its right; clear it below the clock face."""
    p = 'game/img/nine_1.png'
    im = np.array(Image.open(p)).astype(np.int16)
    h, w, _ = im.shape
    d = np.abs(im[:, :, :3] - np.array([250, 233, 208])).sum(2)
    yy, xx = np.mgrid[0:h, 0:w]
    face = (xx > w * .55) & (yy < h * .47)
    mask = ((d < 60) & (xx > w * .62) & ~face) | ((d < 60) & (xx > w * .94))
    im[:, :, 3] = np.where(mask, 0, im[:, :, 3])
    Image.fromarray(im.astype(np.uint8)).save(p)

def tower_without_gears():
    """The tower's hanging small gear and floor gear are moved by the game: cut them out as sprites
    (disli_kucuk, disli_buyuk) and fill their places in the background. The filled spot under the big
    gear is only seen after it is lifted, and the game covers it with settling dust and rubble."""
    import cv2
    im = cv2.imread('game/img/bg_2d.jpg')
    # keep the painted gears as sprites (round cut-outs) so the game can move them
    for name, (cx, cy, r) in {'disli_kucuk': (937, 100, 42), 'disli_buyuk': (838, 500, 114)}.items():
        crop = cv2.cvtColor(im[cy - r:cy + r, cx - r:cx + r], cv2.COLOR_BGR2RGB)
        a = np.zeros((2 * r, 2 * r), np.uint8); cv2.circle(a, (r, r), r - 1, 255, -1); a = cv2.GaussianBlur(a, (5, 5), 0)
        Image.fromarray(np.dstack([crop, a])).save(f'game/img/{name}.png')
    out = im.copy()

    def clone(dst, src, mask_circle):
        """copy the rectangle src (x0, y0, x1, y1) onto dst's top-left corner, feathered inside a circle"""
        (dx, dy), (sx0, sy0, sx1, sy1) = dst, src
        patch = im[sy0:sy1, sx0:sx1].astype(np.float32)
        h, w = patch.shape[:2]
        m = np.zeros(im.shape[:2], np.float32); cx, cy, r = mask_circle
        cv2.circle(m, (cx, cy), r, 1, -1); m = cv2.GaussianBlur(m, (21, 21), 0)[dy:dy + h, dx:dx + w, None]
        out[dy:dy + h, dx:dx + w] = (out[dy:dy + h, dx:dx + w] * (1 - m) + patch * m).astype(np.uint8)

    # small hanging gear: the arches just to its right continue behind it
    clone((890, 52), (985, 52, 1080, 150), (937, 100, 48))
    # big floor gear: tower column on its left half, railing and far arches on its right half
    clone((696, 376), (574, 376, 720, 620), (838, 500, 132))
    clone((838, 380), (962, 380, 1080, 620), (900, 500, 90))
    cv2.imwrite('game/img/bg_2d.jpg', out, [cv2.IMWRITE_JPEG_QUALITY, 84])


if __name__ == '__main__':
    bg('A6_buhar_meydani', 'bg_2a')
    bg('A7_nine_saat_evi', 'bg_2b')
    bg('A8_hurdaci_sokagi', 'bg_2c')
    bg('A9_asansor_kulesi', 'bg_2d')
    tower_without_gears()
    square('B8_vana_paneli', 'cu_vana')
    square('B9_montaj_cizimi', 'cu_montaj')
    square('B10_disli_duvari', 'cu_disliduvar')
    square('B12_gogus_kapagi_iki_yaprak', 'cin_ikiyaprak', 640)
    square('D4_hafiza_cizimi_2', 'cu_hafiza2')
    square('D5_hafiza_cizimi_3', 'cu_hafiza3')
    square('D6_kivilcim', 'cu_kivilcim')
    sprites('C7_nine_saat', 1, 4, 'nine', 260, thr=60)
    fix_nine1()
    sprites('C8_torun', 1, 2, 'torun', 200, thr=60)
    sprites('C9_vida_somun', 1, 3, 'ikiz', 280, thr=60, bigbg=300, keep_ratio=.0015)
    sprites('C10_pirpir', 1, 4, 'pirpir', 160, thr=60, bigbg=300, keep_ratio=.0015)
    sprites('C6_kul_toplayici', 1, 2, 'toplayici', 300, thr=60, bigbg=300, keep_ratio=.0015)
