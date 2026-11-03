# Collects links to the original site that have no local copy yet and writes them to a wget input list.
import os, re, sys
from urllib.parse import unquote

ROOT = sys.argv[1]
ORIGIN = re.compile(r"(?:https?://(?:www\.)?cuckoo-rentalmall\.co\.kr|(?<=[\"']))(/user[/?][^\"' )<>\\]*)")
PAGE = re.compile(r"^/user/(review|review/view|product_detail|product_list|board/(view|lists)|best_product|sale_product|sub(4015|4020|5011|5014|5015|6010|6011|6012|6020)|clause_)")
SKIP = re.compile(r"(sub3010|sub3011|ajsx|product_detail/|=$|login|logout|join|member|edit_request|cs_review|ajax|search|admin)")

def local_file(path):
    p = unquote(path).split('#')[0].rstrip('/') or '/user'
    return os.path.join(ROOT, p.lstrip('/') + '.html')

missing = set()
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith('.html'):
            continue
        for path in ORIGIN.findall(open(os.path.join(d, f), encoding='utf-8', errors='ignore').read()):
            path = path.replace('&amp;', '&')
            if PAGE.match(path) and not SKIP.search(path) and not os.path.exists(local_file(path)):
                missing.add('https://www.cuckoo-rentalmall.co.kr' + path)
print('\n'.join(sorted(missing)))
