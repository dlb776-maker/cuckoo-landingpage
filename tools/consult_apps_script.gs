// Receives consultation requests from the site (tools/consult.js), adds a row to this sheet and mails the owner.
// Setup: see tools/상담접수_설정방법.md
var NOTIFY = 'shin299fa@naver.com';
var COLS = ['접수일시', '구분', '성명', '연락처', '상품', '상품번호', '설치지역', '문의내용', '견적', '회사명', '이메일', '페이지'];

function doPost(e) {
  var p = e.parameter || {};
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sh = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sh.getLastRow() === 0) sh.appendRow(COLS);
    var clip = function (v) { return String(v || '').slice(0, 500).replace(/^[=+\-@]/, "'$&"); };  // no formula injection
    var row = [new Date(), p.type, p.name, p.tel, p.product_nm, p.product_no, p.area, p.memo, p.estimate, p.company, p.email, p.page].map(clip);
    row[0] = new Date();
    sh.appendRow(row);
    MailApp.sendEmail(NOTIFY, '[홈페이지 상담신청] ' + clip(p.type) + ' - ' + clip(p.name),
      COLS.map(function (c, i) { return c + ' : ' + row[i]; }).join('\n'));
  } finally {
    lock.releaseLock();
  }
  return ContentService.createTextOutput('OK');
}
