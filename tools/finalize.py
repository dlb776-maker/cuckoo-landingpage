# Turns the wget mirror (src) into the static site (dst): local links, our business info, backend features -> /404.
import os, re, shutil, sys
from urllib.parse import unquote, quote

SRC, DST = sys.argv[1], sys.argv[2]
SITE = 'https://www.cuckoo-rentalmall.co.kr'
PHONE = '070-8652-7471'

# Pages/endpoints that need the original backend
BLOCK = re.compile(r"^/user/(sub3010|sub3011|login|logout|join|member|main/edit_request|cs_review|product_search|product_detail/(ajax_mms_send|ajax_rev_date_change|ajax_rev_input_html|ajax_ord_input_html)|prod_sms|.*ajsx|admin)|^/admin|^/user/sub4020/|^/user/sub4015/")

FOOTER = '''<p class="dcAddr02">
              주식회사 파이브스톤 &nbsp; / &nbsp; 06568 &nbsp; 서울 서초구 동광로12가길 3 5층 (방배동, 인재빌딩)<br/>
              사업자번호 :&nbsp;108-86-16983 &nbsp;&nbsp; 통신판매번호 :&nbsp;2022-서울서초-0664<br/>
              대표자 :&nbsp;신성연 &nbsp;&nbsp; 대표번호 :&nbsp;070-8652-7471<br/>
              E-MAIL : shin299fa@naver.com&nbsp;&nbsp; 전화번호 :&nbsp;070-8652-7471
          </p>

          '''

TEXT = [
    ('1566-1134', PHONE), ('1566 - 1134', PHONE), ('15661134', PHONE.replace('-', '')),
    ('050-2350-1134', PHONE),
    ('196-38-00677', '108-86-16983'), ('410-87-05732', '108-86-16983'),
    ('제 2019-gwangjugwangsan - 0800 호', '2022-서울서초-0664'),
    ('2015-Gwangsan-gu, Gwangju-0047 호', '2022-서울서초-0664'),
    ('kim jinyong', '신성연'), ('kim ju hyeon', '신성연'),
    ('daonhomesys@naver.com', 'shin299fa@naver.com'),
    ('75, Sudeung-ro 123beon-gil, Gwangsan-gu, Gwangju, Republic of korea', '서울 서초구 동광로12가길 3 5층 (방배동, 인재빌딩)'),
    ('328, Imbangul-daero, Gwangsan-gu, Gwangju, Republic of Korea', '서울 서초구 동광로12가길 3 5층 (방배동, 인재빌딩)'),
]

def local_path(path):
    """Site path -> file path inside DST (wget naming), or None."""
    p = unquote(path.replace('&amp;', '&')).split('#')[0]
    p = p.rstrip('/') or '/user'
    for cand in (p.lstrip('/') + '.html', p.lstrip('/')):
        if os.path.isfile(os.path.join(DST, cand)):
            return cand
    return None

def href_for(path):
    if BLOCK.search(path):
        return '/404'
    lp = local_path(path)
    if lp:
        return '/' + quote(lp, safe='/&=-_.~')
    return None

unresolved = {}

def fix_url(m):
    q, path = m.group(1), m.group(2)
    h = href_for(path)
    if h is None:
        unresolved[path] = unresolved.get(path, 0) + 1
        return m.group(0)
    return q + h

ABS = re.compile(r"""(["'(=])https?://(?:www\.)?cuckoo-rentalmall\.co\.kr(/[^"'\s)<>\\]*)""")
ROOTREL = re.compile(r"""(["'])(/user(?:[/?][^"'\s<>\\]*)?)(?=["'])""")  # root-relative URLs in attributes and JS strings
EXT = re.compile(r"https?://www\.daonhomesys\.com/site_data/[a-z_]+/([^\"'\s)<>]+)")

def transform(s):
    s = re.sub(r"https?://(?:www\.)?cuckoo-rentalmall\.co\.kr(?=[\"'])", '/', s)
    s = ABS.sub(fix_url, s)
    s = ROOTREL.sub(fix_url, s)
    # shortcut: files over Vercel's 100MB limit stay on the original host; re-encode them if they must be local
    s = EXT.sub(lambda m: '/ext/' + m[1] if os.path.isfile(os.path.join(DST, 'ext', m[1])) else m[0], s)
    # popups load per-id pages by string concat; point them at the saved copies
    s = s.replace('"/user/product_detail/ajax_rev_view_html?review_no="+review_no', '"/user/product_detail/ajax_rev_view_html%3Freview_no="+review_no+".html"')
    s = s.replace('"/user/sub5011/detail?gift_no="+gift_no+"&call_type="+call_type', '"/user/sub5011/detail%3Fgift_no="+gift_no+"&call_type="+call_type+".html"')
    s = re.sub(r'(<script[^>]*jquery-1\.10\.2\.js[^>]*></script>)', r'\1<script src="/common/js/mock.js"></script>', s)
    # forms post via post_goto into a hidden iframe; send the visitor to the 404 page instead
    s = s.replace('post_goto(url, parm, target);', "location.href='/404'; return;")
    s = re.sub(r'(<form[^>]*\baction=)(["\'])[^"\']*\2', r'\1"/404"', s)
    i, j = s.find('<p class="dcAddr02">'), s.find('<p class="dcCopyright">')
    if 0 < i < j:
        s = s[:i] + FOOTER + s[j:]
    for a, b in TEXT:
        s = s.replace(a, b)
    return s

if os.path.exists(DST):
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)
for f in os.listdir(os.path.join(DST, 'ext')):
    if os.path.getsize(os.path.join(DST, 'ext', f)) > 95 * 2**20:
        os.remove(os.path.join(DST, 'ext', f))
shutil.copyfile(os.path.join(DST, 'user.html'), os.path.join(DST, 'index.html'))
shutil.copyfile(os.path.join(os.path.dirname(__file__), 'mock.js'), os.path.join(DST, 'common/js/mock.js'))
n = 0
for d, _, fs in os.walk(DST):
    for f in fs:
        if f.endswith(('.html', '.css', '.js', '.json')):
            p = os.path.join(d, f)
            s = open(p, encoding='utf-8', errors='surrogateescape').read()
            t = transform(s)
            if t != s:
                open(p, 'w', encoding='utf-8', errors='surrogateescape').write(t)
                n += 1
print('files changed', n)
for k, v in sorted(unresolved.items(), key=lambda x: -x[1]):
    print('UNRESOLVED', v, k)
