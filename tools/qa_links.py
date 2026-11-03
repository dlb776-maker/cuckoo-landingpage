# QA: every local href/src in the built site must resolve to a file; lists external hosts still referenced.
import os, re, sys
from collections import Counter
from urllib.parse import unquote, urlsplit

ROOT = sys.argv[1]
ATTR = re.compile(r"""(?:href|src|action)\s*=\s*["']([^"'<>]*)["']|url\(\s*["']?([^"')]+)["']?\s*\)""", re.I)
missing, external = Counter(), Counter()
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(('.html', '.css')):
            continue
        page = os.path.join(d, f)
        for a, b in ATTR.findall(open(page, encoding='utf-8', errors='ignore').read()):
            u = (a or b).strip().replace('&amp;', '&')
            if not u or u.startswith(('#', 'javascript:', 'mailto:', 'tel:', 'data:', 'about:')) or u in ('/404',):
                continue
            if u.startswith(('http://', 'https://', '//')):
                external[urlsplit(u if not u.startswith('//') else 'https:' + u).netloc] += 1
                continue
            path = unquote(u.split('#')[0].split('?')[0])
            target = os.path.join(ROOT, path.lstrip('/')) if path.startswith('/') else os.path.join(d, path)
            if path in ('/', '') or os.path.isfile(target) or os.path.isfile(os.path.join(target, 'index.html')):
                continue
            missing[path] += 1
print('MISSING', len(missing))
for k, v in missing.most_common(60):
    print(' ', v, k)
print('EXTERNAL HOSTS')
for k, v in external.most_common():
    print(' ', v, k)
