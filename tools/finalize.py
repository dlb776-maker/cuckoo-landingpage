# Turns the wget mirror (src) into the static site (dst): local links, our business info, backend features -> /404.
import os, re, shutil, sys
from urllib.parse import unquote, quote

SRC, DST = sys.argv[1], sys.argv[2]
SITE = 'https://www.cuckoo-rentalmall.co.kr'
PHONE = '070-8652-7471'

# Pages/endpoints that need the original backend
BLOCK = re.compile(r"^/user/(sub3011/|login|logout|join|member|main/edit_request|cs_review|product_search|product_detail/(ajax_mms_send|ajax_rev_date_change|ajax_rev_input_html|ajax_ord_input_html)|prod_sms|.*ajsx|admin)|^/admin|^/user/sub4020/|^/user/sub4015/")

FOOTER = '''<p class="dcAddr02">
              주식회사 파이브스톤 &nbsp; / &nbsp; 06568 &nbsp; 서울 서초구 동광로12가길 3 5층 (방배동, 인재빌딩)<br/>
              사업자번호 :&nbsp;108-86-16983 &nbsp;&nbsp; 통신판매번호 :&nbsp;2022-서울서초-0664<br/>
              대표자 :&nbsp;신성연 &nbsp;&nbsp; 대표번호 :&nbsp;070-8652-7471<br/>
              E-MAIL : shin299fa@naver.com&nbsp;&nbsp; 전화번호 :&nbsp;070-8652-7471
          </p>

          '''

TEXT = [
    ("$('.dcReviewListWrap').offset().top", "($('.dcReviewListWrap').offset()||{top:1e9}).top"),  # pages without reviews threw on every scroll
    ('다이렉트 상담신청', '빠른 상담신청'), ('다이렉트 빠른설치', '빠른설치 신청'),
    ('"url": "www.cuckoo-rentalmall.co.kr"', '"url": "/"'),
    ("domain:'.cuckoo-rentalmall.co.kr', ", ''), ("goto_url('/muser')", "goto_url('/')"), ('href="/muser"', 'href="/"'),
    ('회사 : 다이렉트렌탈', '회사 : 주식회사 파이브스톤'), ('다이렉트렌탈', '파이브스톤'),
    ('다이렉트접수처', '파이브스톤 접수처'), ('다이렉트 접수처', '파이브스톤 접수처'),
    ('쿠쿠전자 다이렉트 렌탈몰', '파이브스톤 렌탈몰'), ('쿠쿠전자 다이렉트<br />렌탈몰', '파이브스톤<br />렌탈몰'),
    ('쿠쿠전자<br />다이렉트몰', '파이브스톤<br />렌탈몰'), ('쿠쿠전자 다이렉트몰', '파이브스톤 렌탈몰'), ('다이렉트몰', '파이브스톤 렌탈몰'),
    ("<p class='brand_nm'>쿠쿠전자 다이렉트</p>", "<p class='brand_nm'>파이브스톤</p>"),
    ('다온 이벤트', '이벤트'), ('(다온은', '(당사는'),
    # other companies' numbers: removed, per owner's call
    ('1588-8899(AS), ', ''), ('1588-8900(AS), ', ''), ('1588-8899(AS)', ''), ('1588-8900(AS)', ''),
    ('A/S 고객센터: 1588-8899', 'A/S 고객센터'), ('1588-8899', ''), ('1588-8900', ''),
    ('1588-9260', ''), ('1577-8045', ''), ('02-1800-6611', ''),
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

# Cuckoo certification review fixes
FIXES = [
    # banners that pointed at the wrong place
    (re.compile(r'href="[^"]*"(?=[^>]*>\s*<img src="[^"]*1586232128_TkcRGBHg_05\.jpg")'), 'href="/user/sub4015.html"'),  # 영업점 모집
    (re.compile(r'href="[^"]*"(?=[^>]*>\s*<img src="[^"]*1694051088_Mz6lxsE4_1main\.jpg")'), 'href="/user/product_detail%3Fproduct_no=202209-1126.html"'),  # STEAM 100
    (re.compile(r'href="[^"]*"(?=[^>]*>\s*<img src="[^"]*1694152758_CE1QylzL_5main\.jpg")'), 'href="/user/product_list/run/category_no/1410.html"'),  # 인덕션
    (re.compile(r'href="[^"]*"(?=[^>]*>\s*<img src="[^"]*1586144459_fBxO0UnJ_topbanner0\.jpg")'), 'href="/user/product_list/run/category_no/23.html"'),  # 쿠쿠 패키지
    (re.compile(r'href="[^"]*"(?=[^>]*>\s*<img src="[^"]*1586224098_OKiyfTdS_eventbanne\.jpg")'), 'href="/user/product_list/run/category_no/23.html"'),  # 1+1 패키지
    (re.compile(r'href="[^"]*"(?=[^>]*>\s*<img src="[^"]*1586141009_ltb4qhWM_bottombann\.jpg")'), 'href="/user/sub4020.html"'),  # 단체 할인
    (re.compile(r'href="[^"]*"(?=[^>]*>\s*<img src="[^"]*1659081972_L6KNSslv_topbanner1\.jpg")'), 'href="javascript:f_free_request();"'),  # 상담바로신청
    (re.compile(r'href="javascript:f_free_request\(\);"(?=[^>]*>\s*무료상담 신청현황)'), 'href="/user/sub3011.html"'),
    (re.compile(r'<li class="dcFixBottom04"><a href="/404"[^>]*>관리자 로그인</a></li>'), ''),
    # Falomo partnership ended: banner slide and its pager tab
    (re.compile(r'<li><a [^>]*>\s*<img src="[^"]*1662531938_SdNIYOpc_main05\.jpg"[^>]*/></a></li>'), ''),
    (re.compile(r"<li><a data-slide-index='4' [^>]*>팔로모고급침대</a></li>"), ''),
    # KB card may only be shown by Cuckoo HQ: its card block and its tab
    (re.compile(r'<ul class="card_Wrap">(?:(?!</ul>).)*?렌탈II 국민카드(?:(?!</ul>).)*?</ul>', re.S), ''),
    (re.compile(r'<ul [^>]*class="card_view">(?:(?!</ul>).)*?렌탈II 국민카드(?:(?!</ul>).)*?</ul>', re.S), ''),
    # 접수현황 page: only page 1 is saved, and searching it needs the server
    (re.compile(r'<div class="dcPager"><a id="pg_first"[^\n]*?</div>'), ''),
    (re.compile(r'<form id="bform" name="bform"[^>]*>\s*<div class="dcTopRight clearfix">.*?</form>', re.S), ''),
    # FAQ and review boards were members-only on the original (alert + redirect); point at the public equivalents
    (re.compile(r'''(?<=["'])(?:[^"']*/)?faqs\.html(?=["'])'''), '/user/board/lists/board_cd/notice.html'),
    (re.compile(r'''(?<=["'])[^"']*lists/board_cd/reviews\.html(?=["'])'''), '/user/review.html'),
    (re.compile(r"<form name='fsearch'.*?</form>", re.S), ''),  # board search needs the server
    # shortcut: the original's separate mobile site isn't cloned; phones get the 1200px PC layout scaled to fit
    (re.compile(r'<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">'), '<meta name="viewport" content="width=1240">'),
    (re.compile(r'무료상담이나 카톡상담을 이용해 주세요'), '무료상담을 이용해 주세요'),
    (re.compile(r'쿠쿠홈시스은\(는\)'), '주식회사 파이브스톤은(는)'),
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
    if re.match(r'/user/sub3010(?:[/?]|$)', path):
        return 'javascript:f_free_request();'  # the consultation form (tools/consult.js) replaces the server page
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
DAON = re.compile(r"https?://(?:www\.)?daonhomesys\.com/([^\"'\s)<>]+)")

def daon_url(m):
    # images that lived on the original seller's server; served from /daon (full path) or /ext (older flat copies)
    p = m[1]
    if os.path.isfile(os.path.join(DST, 'daon', unquote(p))):
        return '/daon/' + p
    if os.path.isfile(os.path.join(DST, 'ext', p.rsplit('/', 1)[-1])):
        return '/ext/' + p.rsplit('/', 1)[-1]
    if p.lower().endswith(('.mp4', '.webm', '.mov')):
        return m[0]  # shortcut: videos over Vercel's 100MB limit stay remote; re-encode them if they must be local
    return 'data:image/gif;base64,R0lGODlhAQABAAAAACw='  # image gone upstream too: blank pixel, no link to the old host

TRACKERS = [
    re.compile(r'<meta name="(?:google|naver)-site-verification"[^>]*>\s*'),
    re.compile(r'<script[^>]*src="(?:https?:)?//(?:www\.googletagmanager\.com|t1\.daumcdn\.net/kas|cdn\.onetag\.co\.kr|wcs\.naver\.net)[^"]*"[^>]*></script>\s*'),
    re.compile(r"<script>\s*window\.dataLayer[^<]*</script>\s*"),
]
# the original operator's analytics are stripped; these stubs keep leftover calls (kakaoPixel(...).x(), wcs_do()) from throwing
STUBS = ('<script>window.kakaoPixel=function(){return new Proxy({},{get:function(){return function(){};}});};'
         'window.wcs=new Proxy({},{get:function(){return function(){};}});window.wcs_add={};window.wcs_do=function(){};'
         'window.gtag=function(){};</script>')

def transform(s):
    for t in TRACKERS:
        s = t.sub('', s)
    s = re.sub(r'(<head[^>]*>)', lambda m: m[1] + STUBS, s, count=1)
    s = re.sub(r"https?://(?:www\.)?cuckoo-rentalmall\.co\.kr(?=[\"'])", '/', s)
    s = ABS.sub(fix_url, s)
    s = ROOTREL.sub(fix_url, s)
    # shortcut: files over Vercel's 100MB limit stay on the original host; re-encode them if they must be local
    s = DAON.sub(daon_url, s)
    # review videos are not deployed (too large for the repo); drop the player and its centring wrapper
    s = re.sub(r'<div[^>]*>\s*<video\b.*?</video>\s*</div>|<video\b.*?</video>', '', s, flags=re.S)
    s = re.sub(r"""(<img[^>]*?src=)(["'])[^"']*\.(?:mp4|mov|webm)\2""", r'\1\2data:image/gif;base64,R0lGODlhAQABAAAAACw=\2', s, flags=re.I)
    # nothing may point back at the original site; leftovers become same-path local URLs
    s = re.sub(r'https?://(?:www\.)?cuckoo-rentalmall\.co\.kr(?=/)', '', s)
    # popups load per-id pages by string concat; point them at the saved copies
    s = s.replace('"/user/product_detail/ajax_rev_view_html?review_no="+review_no', '"/user/product_detail/ajax_rev_view_html%3Freview_no="+review_no+".html"')
    s = s.replace('"/user/sub5011/detail?gift_no="+gift_no+"&call_type="+call_type', '"/user/sub5011/detail%3Fgift_no="+gift_no+"&call_type="+call_type+".html"')
    s = re.sub(r'(<script[^>]*jquery-1\.10\.2\.js[^>]*></script>)', r'\1<script src="/common/js/mock.js"></script>', s)
    # forms post via post_goto into a hidden iframe; tools/consult.js forwards them to the owner's sheet instead
    s = s.replace('post_goto(url, parm, target);', 'consult_send(url, parm); return;')
    s = re.sub(r'(<form[^>]*\baction=)(["\'])[^"\']*\2', r'\1"/404"', s)
    i, j = s.find('<p class="dcAddr02">'), s.find('<p class="dcCopyright">')
    if 0 < i < j:
        s = s[:i] + FOOTER + s[j:]
    for a, b in TEXT:
        s = s.replace(a, b)
    for a, b in FIXES:
        s = a.sub(b, s)
    s = s.replace('</body>', '<script src="/common/js/consult.js"></script><script src="/common/js/catalog.js"></script>\n</body>', 1)
    return s

if os.path.exists(DST):
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)
# wget saved query-string assets as 'x.css?v.css'; pages that request 'x.css?v' get served 'x.css'
for d, _, fs in os.walk(DST):
    for f in fs:
        if '?' in f and not f.startswith(('review', 'product_', 'ajax_', 'detail', 'sub3011')):
            plain = os.path.join(d, f.split('?')[0])
            if not os.path.exists(plain):
                shutil.copyfile(os.path.join(d, f), plain)
for f in os.listdir(os.path.join(DST, 'ext')):
    if os.path.getsize(os.path.join(DST, 'ext', f)) > 95 * 2**20:
        os.remove(os.path.join(DST, 'ext', f))
shutil.copyfile(os.path.join(DST, 'user.html'), os.path.join(DST, 'index.html'))
shutil.copyfile(os.path.join(DST, 'favicon.ico'), os.path.join(DST, 'favicon.png'))
os.remove(os.path.join(DST, 'user/review/view'))
os.remove(os.path.join(DST, 'user/sub4020/edit_btob.html'))  # empty wget artifact
shutil.copyfile(os.path.join(os.path.dirname(__file__), '404.html'), os.path.join(DST, '404.html'))  # stray wget copy without .html, never linked
shutil.copyfile(os.path.join(os.path.dirname(__file__), 'mock.js'), os.path.join(DST, 'common/js/mock.js'))
for js in ('consult.js', 'catalog.js'):
    shutil.copyfile(os.path.join(os.path.dirname(__file__), js), os.path.join(DST, 'common/js', js))
# product search results page: a category page whose list catalog.js refills (same folder, so relative paths hold)
cat = os.path.join(DST, 'user/product_list/run/category_no')
shutil.copyfile(os.path.join(cat, '10.html'), os.path.join(cat, 'search.html'))
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
