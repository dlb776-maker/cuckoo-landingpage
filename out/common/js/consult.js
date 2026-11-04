/* Consultation requests without a backend: every request form on the site posts here, and this forwards it to a
   Google Apps Script web app (tools/consult_apps_script.gs) that writes a sheet row and mails the owner. */
(function () {
  // Paste the web app URL from Apps Script "배포 > 새 배포" here, then rebuild. Empty = requests can't be sent yet.
  var ENDPOINT = 'https://script.google.com/macros/s/AKfycbzg-aAfi_Gva_ycTvqvN2-RgKMABomqmJXmusilPow0wlaBfUJ_Mtw5rGRgYcF8EKSBew/exec';
  var PHONE = '070-8652-7471';

  function product() {
    var no = document.getElementById('product_no');
    var ld = document.querySelector('script[type="application/ld+json"]');
    var name = '';
    try { name = ld ? (JSON.parse(ld.textContent.replace(/,\s*([}\]])/g, '$1')).name || '') : ''; } catch (e) {}
    var t = document.title.split('|')[0].split(']').pop().replace(/^렌탈/, '').trim();  // promo tags nest: "[[단 하루] ..!] 이름"
    return { no: no ? no.value : '', name: t || name };
  }

  function selected(id) {
    var s = document.getElementById(id);
    return s && s.options && s.selectedIndex >= 0 ? s.options[s.selectedIndex].text.trim() : '';
  }

  function text(sel) {
    var e = document.querySelector(sel);
    return e ? e.textContent.trim() : '';
  }

  function send(data, done) {
    if (!ENDPOINT) {
      alert('현재 온라인 접수 준비 중입니다.\n' + PHONE + ' 로 전화 주시면 바로 상담해 드리겠습니다.');
      return;
    }
    data.page = location.href;
    var body = new URLSearchParams();
    Object.keys(data).forEach(function (k) { body.append(k, data[k] == null ? '' : String(data[k])); });
    // Apps Script answers with a redirect the browser can't read cross-origin, so success = the request went out
    fetch(ENDPOINT, { method: 'POST', mode: 'no-cors', body: body }).then(function () {
      alert('상담 신청이 접수되었습니다.\n확인 후 빠르게 연락드리겠습니다.');
      if (done) done();
    }, function () {
      alert('접수 중 문제가 발생했습니다.\n' + PHONE + ' 로 전화 주세요.');
    });
  }

  function validPhone(v) { return /^0\d{8,10}$/.test(String(v).replace(/[^0-9]/g, '')); }

  var css = '#cs-modal{position:fixed;inset:0;z-index:100000;background:rgba(0,0,0,.55);display:flex;align-items:center;justify-content:center;padding:16px}' +
    '#cs-modal .cs-box{background:#fff;width:100%;max-width:460px;max-height:92vh;overflow:auto;border-top:4px solid #e60012;padding:28px 24px;font-family:"Malgun Gothic","Apple SD Gothic Neo",sans-serif;color:#333;box-sizing:border-box}' +
    '#cs-modal h2{margin:0 0 6px;font-size:22px}#cs-modal .cs-sub{margin:0 0 18px;font-size:14px;color:#666}' +
    '#cs-modal label{display:block;margin:12px 0 4px;font-size:14px;font-weight:700}' +
    '#cs-modal input[type=text],#cs-modal input[type=tel],#cs-modal textarea{width:100%;box-sizing:border-box;border:1px solid #ccc;padding:10px;font-size:15px}' +
    '#cs-modal textarea{height:70px;resize:vertical}#cs-modal .cs-prod{background:#f5f5f5;padding:10px;font-size:14px}' +
    '#cs-modal .cs-est{border:1px solid #eee;padding:12px;font-size:14px;line-height:1.8}#cs-modal .cs-est b{color:#e60012;font-size:18px}' +
    '#cs-modal .cs-agree{margin-top:14px;font-size:13px}#cs-modal .cs-agree label{display:inline;font-weight:400;margin:0}' +
    '#cs-modal .cs-policy{display:none;margin-top:8px;padding:10px;background:#f9f9f9;font-size:12px;line-height:1.6}' +
    '#cs-modal .cs-btns{display:flex;gap:8px;margin-top:20px}#cs-modal button{flex:1;padding:14px;font-size:16px;border:0;cursor:pointer}' +
    '#cs-modal .cs-ok{background:#e60012;color:#fff}#cs-modal .cs-no{background:#eee;color:#333}' +
    '#cs-modal .cs-tel{display:block;text-align:center;margin-top:14px;font-size:14px;color:#333}';
  // writing a review needs a member login on the original server
  var hide = document.createElement('style');
  hide.textContent = '.pc_review_btn{display:none!important}';
  document.head.appendChild(hide);

  var POLICY = '■ 수집·이용 목적: 렌탈 상담 신청 접수 및 상담 연락<br>■ 수집 항목: 성명, 연락처, 설치지역, 문의내용<br>' +
    '■ 보유·이용 기간: 상담 완료 후 지체 없이 파기<br>■ 동의를 거부할 수 있으며, 거부 시 온라인 상담 신청이 제한됩니다.<br>주식회사 파이브스톤 · ' + PHONE;

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  // opts: {type, product_no, product_nm, estimate: [[label, value], ...]}
  function open(opts) {
    close();
    if (!document.getElementById('cs-style')) {
      var st = document.createElement('style'); st.id = 'cs-style'; st.textContent = css; document.head.appendChild(st);
    }
    var est = opts.estimate ? '<div class="cs-est">' + opts.estimate.map(function (r) {
      return esc(r[0]) + ' : <b>' + esc(r[1]) + '</b>';
    }).join('<br>') + '</div><p class="cs-sub" style="margin-top:10px">연락처를 남겨주시면 상세 견적을 안내해 드립니다.</p>' : '';
    var m = document.createElement('div');
    m.id = 'cs-modal';
    m.innerHTML = '<div class="cs-box" role="dialog" aria-modal="true" aria-labelledby="cs-title">' +
      '<h2 id="cs-title">' + esc(opts.type) + '</h2><p class="cs-sub">남겨주신 연락처로 상담원이 빠르게 연락드립니다.</p>' +
      (opts.product_nm ? '<div class="cs-prod">상품 : ' + esc(opts.product_nm) + '</div>' : '') + est +
      '<label for="cs-name">성명 *</label><input type="text" id="cs-name" maxlength="20" autocomplete="name">' +
      '<label for="cs-tel">연락처 *</label><input type="tel" id="cs-tel" maxlength="13" placeholder="010-0000-0000" autocomplete="tel">' +
      (opts.estimate ? '' : '<label for="cs-area">설치지역</label><input type="text" id="cs-area" maxlength="40" placeholder="예) 서울 서초구">' +
      '<label for="cs-memo">문의내용</label><textarea id="cs-memo" maxlength="500"></textarea>') +
      '<input type="text" id="cs-hp" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">' +
      '<div class="cs-agree"><input type="checkbox" id="cs-agree" checked> <label for="cs-agree">개인정보 수집 및 이용 동의(필수)</label> ' +
      '<a href="#" class="cs-more">[보기]</a><div class="cs-policy">' + POLICY + '</div></div>' +
      '<div class="cs-btns"><button type="button" class="cs-no">닫기</button><button type="button" class="cs-ok">상담 신청</button></div>' +
      '<a class="cs-tel" href="tel:' + PHONE.replace(/-/g, '') + '">전화 상담 ' + PHONE + '</a></div>';
    document.body.appendChild(m);
    var $ = function (s) { return m.querySelector(s); };
    $('.cs-more').onclick = function (e) { e.preventDefault(); var p = $('.cs-policy'); p.style.display = p.style.display === 'block' ? 'none' : 'block'; };
    $('.cs-no').onclick = close;
    m.addEventListener('click', function (e) { if (e.target === m) close(); });
    document.addEventListener('keydown', onKey);
    $('.cs-ok').onclick = function () {
      var name = $('#cs-name').value.trim(), tel = $('#cs-tel').value.trim();
      if (!name) { alert('성명을 입력해주세요'); $('#cs-name').focus(); return; }
      if (!validPhone(tel)) { alert('사용가능한 연락처를 입력해주세요'); $('#cs-tel').focus(); return; }
      if (!$('#cs-agree').checked) { alert('개인정보 수집 및 이용에 동의해주세요'); return; }
      if ($('#cs-hp').value) { close(); return; }  // bot filled the hidden field
      send({
        type: opts.type, name: name, tel: tel,
        area: $('#cs-area') ? $('#cs-area').value.trim() : '', memo: $('#cs-memo') ? $('#cs-memo').value.trim() : '',
        product_no: opts.product_no || '', product_nm: opts.product_nm || '',
        estimate: opts.estimate ? opts.estimate.map(function (r) { return r[0] + ': ' + r[1]; }).join(' / ') : ''
      }, close);
    };
    $('#cs-name').focus();
  }

  function onKey(e) { if (e.key === 'Escape') close(); }
  function close() {
    var m = document.getElementById('cs-modal');
    if (m) m.parentNode.removeChild(m);
    document.removeEventListener('keydown', onKey);
  }

  function productOpts(type) {
    var p = product();
    return { type: type, product_no: p.no, product_nm: p.no ? p.name : '' };
  }

  window.consult_open = open;

  // free consultation links/buttons (menu, banners, product pages) all call f_free_request
  window.f_free_request = function (no, nm) {
    var o = productOpts('무료상담 신청');
    if (no && no !== o.product_no) { o.product_no = no; o.product_nm = nm || ''; }  // page title beats the bare model code
    open(o);
  };

  // the site's own inline forms (bottom bar, B2B, partner) validate and then call post_goto -> rewritten to this
  window.consult_send = function (url, parm) {
    var type = /edit_btob/.test(url) ? '사업자/단체 견적 문의' : /sub4015/.test(url) ? '파트너점 모집 문의' : '하단 상담 신청';
    var p = product();
    send({
      type: type, name: parm.mb_nm || parm.b_name || parm.ft_mb_nm || '', tel: parm.tel_no || parm.b_tel_no || parm.ft_tel_no || '',
      company: parm.b_company || '', email: parm.b_email || '', memo: parm.memo_tx || '',
      product_no: p.no, product_nm: p.no ? p.name : ''
    }, function () {
      ['ft_mb_nm', 'ft_tel_no', 'b_company', 'b_name', 'b_tel_no', 'b_email', 'memo_tx'].forEach(function (id) {
        var e = document.getElementById(id); if (e) e.value = '';
      });
    });
  };

  // product-page buttons whose original handlers opened server-rendered popups; capture runs before those handlers
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('.pc_rent_save_btn, #prod_sms_btn, .CS_Review_btn');
    if (!t) return;
    e.preventDefault();
    e.stopImmediatePropagation();
    if (t.classList.contains('CS_Review_btn')) {
      location.href = '/user/review.html';  // 가입후기: the popup needed the server; the saved review list is the same content
    } else if (t.id === 'prod_sms_btn') {
      var o = productOpts('3초 견적');
      var est = [];
      if (selected('term_no')) est.push(['약정', selected('term_no')]);
      if (selected('color_tx')) est.push(['색상', selected('color_tx')]);
      var kum = text('.rental_kum'), card = text('.rental_card_kum');
      if (kum && kum !== '0') est.push(['월 렌탈료', '월 ' + kum + '원']);
      if (card && card !== '0' && card !== kum) est.push(['제휴카드 적용 시', '월 ' + card + '원']);
      if (!est.length) est.push(['견적', '상담 시 안내']);
      o.estimate = est;
      open(o);
    } else {
      var label = t.textContent.replace(/\s+/g, ' ').trim() || '렌탈 상담';
      var oo = productOpts(label);
      if (selected('term_no')) oo.product_nm += ' / ' + selected('term_no');
      open(oo);
    }
  }, true);
})();
