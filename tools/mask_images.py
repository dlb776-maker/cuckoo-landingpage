# Paints boxes over third-party text in images. Input lines: "<path> | <text> | x,y,w,h | WxH [| bg hex]" (path relative to project root).
# Originals are kept once under orig_images/ so re-running never stacks edits on an already-masked file.
import os, re, shutil, subprocess, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
boxes = defaultdict(list)
for line in open(sys.argv[1], encoding='utf-8'):
    parts = [p.strip() for p in line.split('|')]
    if len(parts) < 3 or not re.fullmatch(r'\d+,\d+,\d+,\d+', parts[2]):
        continue
    color = parts[4] if len(parts) > 4 and parts[4].startswith('0x') else 'white'
    boxes[parts[0]].append((*map(int, parts[2].split(',')), color))

# the same image is often saved twice (full/ext flat copy and full/daon full path); mask every byte-identical copy
import hashlib
def digest(f):
    return hashlib.md5(open(f, 'rb').read()).hexdigest()
by_name = defaultdict(list)
for d in ('full/ext', 'full/daon', 'full/site_data', 'full/modules'):
    for dp, _, fs in os.walk(os.path.join(ROOT, d)):
        for f in fs:
            by_name[f].append(os.path.relpath(os.path.join(dp, f), ROOT))
for rel in list(boxes):
    src = os.path.join(ROOT, 'orig_images', rel)
    src = src if os.path.exists(src) else os.path.join(ROOT, rel)
    h = digest(src)
    for other in by_name[os.path.basename(rel)]:
        o = os.path.join(ROOT, 'orig_images', other)
        o = o if os.path.exists(o) else os.path.join(ROOT, other)
        if other != rel and other not in boxes and digest(o) == h:
            boxes[other] = boxes[rel]

PAD = int(sys.argv[2]) if len(sys.argv) > 2 else 3  # boxes measured tightly between letters need 0

def bg(img, x, y, w, h, W, H):
    """Most common colour on the 1px ring just outside the box, so the patch blends into coloured backgrounds."""
    rx, ry = max(0, x - 2), max(0, y - 2)
    rw, rh = min(W - rx, w + 4), min(H - ry, h + 4)
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', img, '-vf', f'format=rgb24,crop={rw}:{rh}:{rx}:{ry}', '-frames:v', '1',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    if len(raw) < rw * rh * 3:
        return 'white'
    px = [raw[i:i + 3] for i in range(0, len(raw), 3)]
    ring = [px[r * rw + c] for r in range(rh) for c in range(rw) if r in (0, rh - 1) or c in (0, rw - 1)]
    return '0x' + max(set(ring), key=ring.count).hex() if ring else 'white'

for rel, bs in boxes.items():
    src = os.path.join(ROOT, rel)
    orig = os.path.join(ROOT, 'orig_images', rel)
    if not os.path.exists(orig):
        os.makedirs(os.path.dirname(orig), exist_ok=True)
        shutil.copy2(src, orig)
    W, H = map(int, subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', orig],
                                    capture_output=True, text=True).stdout.split(',')[:2])
    draws = []
    for x, y, w, h, c in bs:
        x, y = max(0, x - PAD), max(0, y - PAD)
        w, h = min(W - x, w + 2 * PAD), min(H - y, h + 2 * PAD)
        draws.append(f'drawbox=x={x}:y={y}:w={w}:h={h}:color={c if c != "white" else bg(orig, x, y, w, h, W, H)}:t=fill')
    vf = 'format=rgb24,' + ','.join(draws)
    ext = os.path.splitext(src)[1]
    tmp = src + '.tmp' + ext
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', orig, '-vf', vf, '-q:v', '2', tmp], check=True)
    os.replace(tmp, src)
    print('masked', len(bs), rel)
