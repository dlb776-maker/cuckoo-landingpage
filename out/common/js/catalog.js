/* Product-list sorting and the top search box, done in the browser because the static site has no server to ask. */
(function () {
  var CATS = ['23', '30', '35', '10', '12', '77', '11', '14', '15', '20', '16', '26', '18'];  // top-level categories = every product
  var SEARCH = '/user/product_list/run/category_no/search.html';

  function num(s) { return parseInt(String(s || '').replace(/[^0-9]/g, ''), 10) || 0; }
  function keyOf(el) {
    var ul = el.querySelector('[onclick]');
    var m = ul && ul.getAttribute('onclick').match(/product_no=([0-9]{6}-[0-9]+)/);
    return m ? m[1] : '';
  }
  function price(el) { var k = el.querySelector('.prod_kum'); var m = k && k.textContent.match(/월\s*([0-9,]+)/); return m ? num(m[1]) : 0; }
  function sales(el) { var m = el.textContent.match(/누적구매\s*([0-9,]+)/); return m ? num(m[1]) : 0; }

  function items(wrap) { return Array.prototype.slice.call(wrap.querySelectorAll(':scope > .prod_list')); }

  function sortList(name) {
    var wrap = document.querySelector('.ProdListWrap');
    if (!wrap) return;
    var list = items(wrap);
    list.forEach(function (el, i) { if (el.dataset.order == null) el.dataset.order = i; });
    var by = {
      sort_no1: function (a, b) { return a.dataset.order - b.dataset.order; },
      sale_cnt2: function (a, b) { return sales(b) - sales(a); },
      insert_info2: function (a, b) { return keyOf(b) < keyOf(a) ? -1 : keyOf(b) > keyOf(a) ? 1 : 0; },  // product_no starts with YYYYMM
      price_amt1: function (a, b) { return price(a) - price(b); },
      price_amt2: function (a, b) { return price(b) - price(a); }
    }[name];
    if (!by) return;
    list.sort(function (a, b) { return by(a, b) || a.dataset.order - b.dataset.order; }).forEach(function (el) { wrap.appendChild(el); });
    var lis = document.querySelectorAll('.list_sort li');
    Array.prototype.forEach.call(lis, function (li) {
      li.className = (li.getAttribute('onclick') || '').indexOf("'" + name + "'") > 0 ? 'sort_on' : '';
    });
  }
  window.f_set4 = sortList;

  window.f_top_search = function () {
    var box = document.getElementById('pc_top_search_tx');
    var q = box ? box.value.trim() : '';
    if (!q) { alert('검색하고자 하시는 제품명을 입력해주세요'); if (box) box.focus(); return; }
    location.href = SEARCH + '?q=' + encodeURIComponent(q);
  };

  function circles(root) {  // the score rings are animated by inline scripts, which don't run for inserted markup
    Array.prototype.forEach.call(root.querySelectorAll('.Lcircle'), function (c) {
      var p = c.querySelector('.progress'), len = 2 * Math.PI * 26;
      if (!p) return;
      p.style.strokeDasharray = len;
      p.style.strokeDashoffset = len - (c.getAttribute('data-score') / 100) * len;
    });
  }

  function runSearch() {
    var q = (new URLSearchParams(location.search).get('q') || '').trim();
    var wrap = document.querySelector('.ProdListWrap');
    if (!wrap) return;
    document.title = (q ? q + ' 검색결과' : '제품 검색') + ' | 쿠쿠홈시스';
    var box = document.getElementById('pc_top_search_tx');
    if (box) box.value = q;
    var h = document.querySelector('.dcCateTitle h3'), tabs = document.querySelector('.sub_ctr');
    if (h) h.textContent = '제품 검색';  // the page is a copy of the 정수기 category; drop its title and sub-tabs
    if (tabs) tabs.style.display = 'none';
    wrap.innerHTML = '<p style="padding:60px 0;text-align:center;color:#888">검색 중입니다…</p>';
    var words = q.toLowerCase().split(/\s+/).filter(Boolean);
    Promise.all(CATS.map(function (c) {
      return fetch(c + '.html').then(function (r) { return r.ok ? r.text() : ''; }, function () { return ''; });
    })).then(function (pages) {
      var seen = {}, found = [];
      pages.forEach(function (html) {
        var doc = new DOMParser().parseFromString(html, 'text/html');
        Array.prototype.forEach.call(doc.querySelectorAll('.ProdListWrap > .prod_list'), function (el) {
          var k = keyOf(el);
          if (!k || seen[k]) return;
          seen[k] = 1;
          var info = el.querySelector('.prod_info'), img = el.querySelector('img[alt]');
          var hay = ((info ? info.textContent : '') + ' ' + (img ? img.alt : '')).toLowerCase();
          if (words.length && words.every(function (w) { return hay.indexOf(w) >= 0; })) found.push(el);
        });
      });
      wrap.innerHTML = '';
      found.forEach(function (el) {
        Array.prototype.forEach.call(el.querySelectorAll('script'), function (s) { s.parentNode.removeChild(s); });
        wrap.appendChild(document.importNode(el, true));
      });
      if (!found.length) {
        wrap.innerHTML = '<p style="padding:60px 0;text-align:center;color:#888">\'' + q.replace(/[<>&"]/g, '') +
          '\' 에 해당하는 제품이 없습니다.<br>다른 검색어로 찾아보시거나 070-8652-7471 로 문의해 주세요.</p>';
      }
      circles(wrap);
      var cnt = document.querySelector('.list_sort');
      cnt = cnt && cnt.parentNode.querySelector('ul li');
      if (cnt) cnt.innerHTML = '검색결과 <span style="color:#ff9900">' + found.length + ' 건 </span>';
    });
  }

  if (location.pathname === SEARCH) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', runSearch); else runSearch();
  }
})();
