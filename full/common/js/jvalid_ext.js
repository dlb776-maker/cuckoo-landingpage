if (typeof(VALID_EXT_JS) == 'undefined')
{
  var VALID_EXT_JS = true;

	function validHangul(fld) {
		var pattern = /([^가-힣\x20])/i;
		if (!pattern.test(fld)) {
			return true;
		}
		return false;
	}

  // 휴대폰번호를 입력시 올바른 휴대폰 번호인지 체크  2013-11-26 강대인
  // 010 국번만 허용하며 중간자리는 4자리로 고정 - 2025-03-21 강대인
  // 하이픈 필수
  function hp_no_chk(pVal)
  {
    pVal = pVal.trim();  // 앞뒤 공백 제거

    // 정규식: 010으로 시작, 하이픈 필수, 중간 4자리, 끝 4자리
    var mobileRegex = /^010-\d{4}-\d{4}$/;

    return mobileRegex.test(pVal);
  }

  // 전화번호를 입력시 올바른 번호인지 체크  2025-03-21 강대인
  // 하이픈 필수
  function tel_no_chk(pVal)
  {
    pVal = pVal.trim();  // 앞뒤 공백 제거

    // 1. 국내 일반전화 (지역번호 + 국번 + 4자리 번호)
    var landlineRegex = /^(02|0[3-6][1-5]|0[7-9][1-9])-\d{3,4}-\d{4}$/;

    // 2. 전국대표번호 (15XX, 16XX, 18XX + 하이픈 + 4자리)
    var nationwideRegex = /^(15|16|18)\d{2}-\d{4}$/;

    // 3. 인터넷전화번호 (070-XXXX-XXXX)
    var internetPhoneRegex = /^070-\d{4}-\d{4}$/;

    // 4. 인터넷팩스번호 (050X-XXX-XXXX 또는 050X-XXXX-XXXX)
    var internetFaxRegex = /^050[1-9]-\d{3,4}-\d{4}$/;

    // 5. 0303 팩스번호 (0303-XXX-XXXX 또는 0303-XXXX-XXXX) - 하이픈 필수
    var fax303Regex = /^0303-\d{3,4}-\d{4}$/;

    // 6. 휴대폰 번호 (010-XXXX-XXXX)
    var mobileRegex = /^010-\d{4}-\d{4}$/;

    return (
        landlineRegex.test(pVal) ||
        nationwideRegex.test(pVal) ||
        internetPhoneRegex.test(pVal) ||
        internetFaxRegex.test(pVal) ||
        fax303Regex.test(pVal) ||
        mobileRegex.test(pVal)
    );
  }

  // 팩스번호를 입력시 올바른 번호인지 체크  2025-03-21 강대인
  // 하이픈 필수
  function fax_no_chk(pVal)
  {
    pVal = pVal.trim();  // 앞뒤 공백 제거

    // 1. 국내 일반전화 (지역번호 + 국번 + 4자리 번호)
    var landlineRegex = /^(02|0[3-6][1-5]|0[7-9][1-9])-\d{3,4}-\d{4}$/;

    // 3. 인터넷전화번호 (070-XXXX-XXXX)
    var internetPhoneRegex = /^070-\d{4}-\d{4}$/;

    // 4. 인터넷팩스번호 (050X-XXX-XXXX 또는 050X-XXXX-XXXX)
    var internetFaxRegex = /^050[1-9]-\d{3,4}-\d{4}$/;

    // 5. 0303 팩스번호 (0303-XXX-XXXX 또는 0303-XXXX-XXXX) - 하이픈 필수
    var fax303Regex = /^0303-\d{3,4}-\d{4}$/;

    return (
        landlineRegex.test(pVal) ||
        internetPhoneRegex.test(pVal) ||
        internetFaxRegex.test(pVal) ||
        fax303Regex.test(pVal)
    );
  }

  // 사업자번호를 입력시 올바른 번호인지 체크  2018-11-24 강대인
  function biz_no_chk(pVal)
  {
    pVal = pVal.trim();  // 앞뒤 공백 제거

    var rtn_cd = true;
    pVal       = pVal.replace(/-/gi,"");

    if ( 10 != WorkNum.length )
    {
      rtn_cd = false;
    }
    else
    {
      sumMod  = 0;
      sumMod += parseInt(pVal.substring(0,1));
      sumMod += parseInt(pVal.substring(1,2)) * 3 % 10;
      sumMod += parseInt(pVal.substring(2,3)) * 7 % 10;
      sumMod += parseInt(pVal.substring(3,4)) * 1 % 10;
      sumMod += parseInt(pVal.substring(4,5)) * 3 % 10;
      sumMod += parseInt(pVal.substring(5,6)) * 7 % 10;
      sumMod += parseInt(pVal.substring(6,7)) * 1 % 10;
      sumMod += parseInt(pVal.substring(7,8)) * 3 % 10;
      sumMod += Math.floor(parseInt(pVal.substring(8,9)) * 5 / 10);
      sumMod += parseInt(pVal.substring(8,9)) * 5 % 10;
      sumMod += parseInt(pVal.substring(9,10));

      if ( 0 != sumMod % 10 )
      {
         rtn_cd = false;
      }
    }
    return rtn_cd;
  }

	$(document).ready(function()
  {
		$.validator.addMethod('hangul', function(value, element) {
			return this.optional(element) || validHangul(value);
		}, '한글이 아닙니다. (자음, 모음만 있는 한글은 처리하지 않습니다.)');

		$.validator.addMethod('alphanumunder', function(value, element) {
			return this.optional(element) || /(^[a-zA-Z0-9\_]+$)/.test(value);
		}, '영문, 숫자, _ 가 아닙니다.');

		$.validator.addMethod('hp', function(value, element) {
			return this.optional(element) || hp_no_chk(value);
		}, '잘못된 휴대폰번호 입니다.');

		$.validator.addMethod('tel', function(value, element) {
			return this.optional(element) || tel_no_chk(value);
		}, '잘못된 전화번호 입니다.');

		$.validator.addMethod('fax', function(value, element) {
			return this.optional(element) || fax_no_chk(value);
		}, '잘못된 팩스번호 입니다.');

		$.validator.addMethod('biz', function(value, element) {
			return this.optional(element) || biz_no_chk(value);
		}, '잘못된 사업자 등록번호 입니다.');

	});
}