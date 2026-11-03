# Writes our company name into the gaps left where the old seller name ("다이렉트") was masked in banners.
# Run after mask_images.py; needs Pillow. Text colour/weight are sampled from the original pixels in each box.
import os, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
BOLD, REGULAR = 6, 0  # face indexes in AppleSDGothicNeo.ttc

# path, box (x, y, w, h), replacement text[, font face]
JOBS = [
    ('full/modules/user/img/skin01/sub/B2B_Title.jpg', (60, 126, 184, 55), '파이브스톤'),
    ('full/modules/user/img/skin01/shop/event_title_banner.jpg', (378, 49, 110, 34), '파이브스톤'),
    ('full/site_data/banner_mst/1622161551_5t04UrKS_topbanner0.jpg', (19, 38, 58, 20), '파이브스톤', REGULAR),
    ('full/site_data/banner_mst/1622161551_5t04UrKS_topbanner0.jpg', (19, 74, 92, 28), '파이브스톤'),
    ('full/site_data/banner_mst/1659081972_L6KNSslv_topbanner1.jpg', (189, 164, 64, 18), '파이브스톤', REGULAR),
    ('full/site_data/banner_mst/1662432639_B3raMWHb_middleeven.jpg', (167, 76, 127, 41), '파이브스톤'),
    ('full/site_data/banner_mst/1662531938_WEUozvuA_main01.jpg', (70, 108, 131, 42), '파이브스톤'),
    ('full/site_data/banner_mst/1662531938_zywxneoi_main03.jpg', (70, 108, 163, 40), '파이브스톤으로'),
]

def text_colour(orig, box):
    """Colour of the old lettering: the most common pixel colour in the box that differs clearly from its edge colour."""
    x, y, w, h = box
    px = list(orig.crop((x, y, x + w, y + h)).getdata())
    edge = max(set(px[:w]), key=px[:w].count)
    far = [p for p in px if sum(abs(a - b) for a, b in zip(p, edge)) > 150]
    return max(set(far), key=far.count) if far else (255, 255, 255)

for rel, box, text, *face in JOBS:
    path = os.path.join(ROOT, rel)
    orig = Image.open(os.path.join(ROOT, 'orig_images', rel)).convert('RGB')
    img = Image.open(path).convert('RGB')
    x, y, w, h = box
    colour = text_colour(orig, box)
    size = int(h * 0.95)
    while size > 6:
        font = ImageFont.truetype(FONT, size, index=face[0] if face else BOLD)
        l, t, r, b = font.getbbox(text)
        if r - l <= w and b - t <= h:
            break
        size -= 1
    d = ImageDraw.Draw(img)
    d.text((x - l, y + (h - (b - t)) // 2 - t), text, font=font, fill=colour)
    img.save(path, quality=95)
    print('text', size, colour, rel)
