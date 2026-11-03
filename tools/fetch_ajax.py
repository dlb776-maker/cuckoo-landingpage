# Saves the read-only ajax responses product pages need (prices, term options, reviews) as static files under mock/.
import glob, json, os, re, sys, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = sys.argv[1]
BASE = 'https://www.cuckoo-rentalmall.co.kr/user/product_detail/'
UA = {'User-Agent': 'Mozilla/5.0'}

def key(params):
    # must match mock-key in tools/mock.js: sorted k=v joined by &, then encodeURIComponent
    k = '&'.join(f'{a}={params[a]}' for a in sorted(params))
    return urllib.parse.quote(k, safe="-_.!~*'()")

def post(ep, params):
    req = urllib.request.Request(BASE + ep, urllib.parse.urlencode(params).encode(), UA)
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8')

def save(ep, params, body):
    d = os.path.join(ROOT, 'mock', ep)
    os.makedirs(d, exist_ok=True)
    # file name is the encoded key itself; the page requests it double-encoded so the server decodes once
    open(os.path.join(d, key(params) + '.json'), 'w', encoding='utf-8').write(body)

def product(no, html):
    terms = set(re.findall(r"option value='([0-9]+-[0-9]+)'", html))
    for kbn in sorted(set(re.findall(r"term_change\('(\d*)'\)", html))):
        p = {'kbn': kbn, 'product_no': no}
        body = post('term_select_box', p); save('term_select_box', p, body)
        terms |= set(re.findall(r"value='([0-9]+-[0-9]+)'", json.loads(body).get('data') or ''))
    for t in sorted(terms):
        p = {'product_no': no, 'term_no': t}
        save('ajax_prod_term_info_hwi', p, post('ajax_prod_term_info_hwi', p))
    m = re.search(r'function term_adm_change\(kbn\)\{.*?product_nm = "(.*?)";.*?sale_card = "(.*?)";.*?giwon = "(.*?)";', html, re.S)
    if m:
        for kbn in sorted(set(re.findall(r"term_adm_change\('(\d*)'\)", html))):
            p = {'kbn': kbn, 'product_no': no, 'product_nm': m[1], 'sale_card': m[2], 'giwon': m[3]}
            save('term_list_table_adm', p, post('term_list_table_adm', p))
    prev = None
    for page in range(1, 200):
        p = {'product_no': no, 'page': str(page)}
        body = post('ajax_rev_list_html', p)
        save('ajax_rev_list_html', p, body)
        if body == prev or '<li' not in body:
            break
        prev = body
    return no, len(terms)

pages = {}
for f in glob.glob(os.path.join(ROOT, 'user', 'product_detail?product_no=*.html')):
    no = re.search(r'product_no=([0-9-]+)', f)[1]
    pages.setdefault(no, open(f, encoding='utf-8').read())
with ThreadPoolExecutor(6) as ex:
    for no, n in ex.map(lambda kv: product(*kv), pages.items()):
        pass
print('products', len(pages))
