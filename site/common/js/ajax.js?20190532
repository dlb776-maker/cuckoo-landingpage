//=================================================================================================
// 프로젝트 :
// 처리내용 : Ajax를 jQuery와 연동
// 작 성 자 : 2013-04-23 이영남
//=================================================================================================

if (typeof(AJAX_JS) == 'undefined')
{
  var AJAX_JS = true;

  //-------------------------------------------------------------------------------------
  // 함수명 : $.dialog
  // 기  능 : 다이알로그창
  // 작성일 : 2013-04-23 이영남
  // 참  조 : pFile:실행파일명, pData:파라메타, pW:폭, pH:높이
  // ------------------------------------------------------------------------------------
  $.dialog = function(pFile, pData, pW, pH)
  {
    var scrollTop = $(window).scrollTop();
    var winLeft   = parseInt($(window).width() - pW) / 2;
    var winTop    = parseInt($(window).height() - pH) / 2 + scrollTop; // 상단31,하단4 를 높이에 포함
    var html      = '<img src="/images/loding/AjaxLoader_64.gif" style="margin-top:'+parseInt((pH/2)-8)+'px" />';

    pSkin = "Txt";

    $.dialogRemove();
    $('<div id="idAjaxHeader"></div>').css({'height':$(document).height()+"px"}).appendTo('body');
    $('<div id="idAjaxBody">'+
      '  <div id="idAjaxDisplay"></div>'+
      '  <div class="ssClear"></div>')
      .css({
        'position'     : 'absolute',
          'top'        : winTop+'px',
          'left'       : winLeft+'px',
          'border'     : '0',
          'width'      : parseInt(pW) +'px',
          'height'     : parseInt(pH) +'px',
          'text-align' : 'center',
          'background' : '#4b4f52',
          'z-index'    : '998'
      }).appendTo('body');

    $('#idAjaxDisplay').css({'width' : pW+'px',  'height' : pH+'px', 'text-align' : 'center', 'overflow' : 'hidden'}).html(html);
    $.ajaxPost('#idAjaxDisplay', pFile, pData);

    //$("#idAjaxBody ").draggable();
    //   클래스가 draggable인 요소에 드래그 기본 함수를 적용한다.
    $("#idAjaxBody").draggable({
      cursor      : "move",         // cursor옵션은 드래그 하는 동안 마우스 포인터의 모양을 변화시킴
      stack       : "#idAjaxBody",  // stack옵션은 드래그 대상이 되는 요소들을 자동으로 깊이 설정을 해줌. 드래그 되는 요소가 가장 위에 올라옴
      opacity     : 0.7,            // 드래그 하는 동안 불투명도는 0.7
      containment : 'window',
      scroll      : false,
      handle      : '.xmClose'       //드래그 잡을 수 있는 영역
    });

    $("#idAjaxBody").bind("dragstart",function(event, ui){
      if ( typeof(Fld_Obj) !== "undefined" && Fld_Obj != null )
      {
        Calendar_Reset();
      }
    });
  };

  //-------------------------------------------------------------------------------------
  // 함수명 : $.ajaxPost
  // 기  능 : ajax 전송
  // 작성일 : 2013-04-23 이영남
  // 참  조 : pDivName:DIV명, pFile:실행파일명, pData:파라메타
  // ------------------------------------------------------------------------------------
  $.ajaxPost = function(pDivName, pFile, pData)
  {
    $.post(pFile,pData,
      function(result)
      {
        $(pDivName).html(result);
        scrollAddFlag = true;
      }
    );

  };

  //-------------------------------------------------------------------------------------
  // 함수명 : $.dialogRemove
  // 기  능 : 다이알로그창 없애기
  // 작성일 : 2013-04-23 이영남
  // 참  조 :
  // ------------------------------------------------------------------------------------
  $.dialogRemove = function()
  {
    $("#idAjaxBody").remove();
    $("#idAjaxClose").remove();
    $("#idAjaxHeader").remove();
    if ( typeof(Fld_Obj) !== "undefined" && Fld_Obj != null )
    {
      Calendar_Reset();
    }
    return true;
  };

  //-------------------------------------------------------------------------------------
  // 함수명 : $.insert
  // 기  능 : 페이지 insert
  // 작성일 : 2013-04-23 이영남
  // 참  조 : pDiv:DIV명, pFile:실행파일명, pData:파라메타, pHeight:높이
  // ------------------------------------------------------------------------------------
  $.insert = function(pDiv, pFile, pData, pHeight)
  {
    var h = (pHeight-16)/2;
    var html = '<div style="height:'+pHeight+'px;"><div style="padding-top:'+h+'px;text-align:center;"><img src="/images/ajax_small.gif" width="16" height="16" /></div></div>';
    $(pDiv).html(html);
    $.ajaxPost(pDiv, pFile, pData);
  };

  //-------------------------------------------------------------------------------------
  // 함수명 : $.dialog
  // 기  능 : 다이알로그창
  // 작성일 : 2013-04-23 이영남
  // 참  조 : pFile:실행파일명, pData:파라메타, pW:폭, pH:높이
  // ------------------------------------------------------------------------------------
  $.dialog_div = function(pDiv, pW, pH)
  {
    var scrollTop = $(window).scrollTop();
    var winLeft   = parseInt($(window).width() - pW) / 2;
    var winTop    = parseInt($(window).height() - pH) / 2 + scrollTop; // 상단31,하단4 를 높이에 포함
    var html      = '<img src="/images/ajax_small.gif" width="16" height="16" style="width:16px;height:16px;margin-top:'+parseInt((pH/2)-8)+'px" />';

    pSkin = "Txt";

    $.dialogRemove_div(pDiv);
    $('<div id="idAjaxHeader" style="width:100%; top:0; left:0; overflow:hidden; position:absolute; background:#000; filter:Alpha(opacity=70); opacity:0.7; -moz-opacity:0.7; z-index:9997;"></div>').css({'height':$('body').height()+"px"}).appendTo('body');
    $('<div id="idAjaxBody">'+
      '  <div id="idAjaxDisplay"></div>'+
      '  <div class="ssClear"></div>')
      .css({
        'position'     : 'absolute',
          'top'        : winTop+'px',
          'border'     : '0',
          'width'      : parseInt(pW) +'px',
          'height'     : parseInt(pH) +'px',
          'text-align' : 'center',
          'z-index'    : '9998'
      }).appendTo('body');

     //'left'       : winLeft+'px',

    $('#idAjaxDisplay').css({'width' : pW+'px',  'height' : pH+'px', 'text-align' : 'center', 'overflow' : 'hidden'}).html(html);

    $('#idAjaxDisplay').html('');
    $('#'+pDiv).show();
    $('#'+pDiv).appendTo('#idAjaxDisplay');

    //$("#idAjaxBody ").draggable();
    //   클래스가 draggable인 요소에 드래그 기본 함수를 적용한다.
    $("#idAjaxBody").draggable({
      cursor      : "move",         // cursor옵션은 드래그 하는 동안 마우스 포인터의 모양을 변화시킴
      stack       : "#idAjaxBody",  // stack옵션은 드래그 대상이 되는 요소들을 자동으로 깊이 설정을 해줌. 드래그 되는 요소가 가장 위에 올라옴
      opacity     : 0.7,            // 드래그 하는 동안 불투명도는 0.7
      containment : 'window',
      scroll      : false,
      handle      : '.xmClose'       //드래그 잡을 수 있는 영역
    });

    $("#idAjaxBody").bind("dragstart",function(event, ui){
      if ( typeof(Fld_Obj) !== "undefined" && Fld_Obj != null )
      {
        Calendar_Reset();
      }
    });
  };

  //-------------------------------------------------------------------------------------
  // 함수명 : $.dialogRemove
  // 기  능 : 다이알로그창 없애기
  // 작성일 : 2013-04-23 이영남
  // 참  조 :
  // ------------------------------------------------------------------------------------
  $.dialogRemove_div = function(pDiv)
  {
    $("#idAjaxBody").remove();
    $("#idAjaxClose").remove();
    $("#idAjaxHeader").remove();
    $("#"+pDiv).hide();

    if ( typeof(Fld_Obj) !== "undefined" && Fld_Obj != null )
    {
      Calendar_Reset();
    }
    return true;
  };



  //-------------------------------------------------------------------------------------
  // 함수명 :
  // 기  능 : 클래스명으로 input box에 숫자만 입력
  // 작성일 : 2014-01-28 강대인
  //-------------------------------------------------------------------------------------

  $(document).ready(function()
  {
    // 숫자콤마 자동입력
    $(".pc_comma_input").on('keyup keydown', function ()
    {
      var t_val = $(this).val();
      $(this).val(InComma(t_val));
    });

    // 전화번호 자동하이픈넣기
    $('.pc_tel_input').on("keyup blur",function()
    {
      var str = $(this).val();
      var string = "";

      string = autoHypenPhone(str)
      $(this).val(string);
    });

    // 날자 입력용 ddatepicker
    $(".pc_date_input").datepicker();

    // 사업자등록번호 자동하이픈넣기
    $('.pc_biz_input').on("keyup blur",function()
    {
      var str = $(this).val();
      var string = "";

      string = autoHypenBizNo(str)
      $(this).val(string);
    });

	// 날자 자동하이픈넣기
    $('.pc_date_input2').on("keyup blur",function()
    {
      var str = $(this).val();
      var string = "";

      string = autoHypenDate(str)
      $(this).val(string);
    });

    //----------------------------------------------------------------------------
    // input 항목에 class 로 ss_num_only 지정한다.(숫자만허용)
    //----------------------------------------------------------------------------
    $('.ss_num_only').css('imeMode','disabled').keypress(function(event)
    {
      if(event.which && (event.which < 48 || event.which > 57) )
      {
        event.preventDefault();
      }
    }).keyup(function()
    {
      if( $(this).val() != null && $(this).val() != '' )
      {
        $(this).val( $(this).val().replace(/[^0-9]/g, '') );
      }
      else
      {
        $(this).val('');
      }
    });

    //----------------------------------------------------------------------------
    // input 항목에 class 로 ss_num_coma 지정한다.(숫자허용 + 숫자 3자리수마다 컴마찍기)
    //----------------------------------------------------------------------------
    $('.ss_num_coma').css('imeMode','disabled').keypress(function(event)
    {
      if(event.which && (event.which < 48 || event.which > 57 ) )
      {
        event.preventDefault();
      }
    }).keyup(function()
    {
      if( $(this).val() != null && $(this).val() != '' )
      {
        var tmps = $(this).val().replace(/[^0-9]/g, '');
        var tmps2 = tmps.replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
        $(this).val(tmps2);
      }
      else
      {
        $(this).val('0');
      }
    });

    //----------------------------------------------------------------------------
    // 숫자만 입력 => IE / 파이어폭스 / 크롬 / 모바일 IE / 모바일 크롬 전부다 만족
    //----------------------------------------------------------------------------
    $(".ss_numeric").keydown(function(e)
    {
      // 키입력에 사용되는 몇몇 키는 허용..delete, backspace, esc 등등
      if (e.keyCode==46 || e.keyCode==8 || e.keyCode==9 || e.keyCode==27 || e.keyCode==13 || (e.keyCode==65 && e.ctrlKey===true) || (e.keyCode>=35 && e.keyCode<=39) )
      {
        return;
      }
      else
      {
        if(e.shiftKey || (e.keyCode<48 || e.keyCode>57) && (e.keyCode<96 || e.keyCode>105))
        {
          //모바일 IE 브라우저의 경우 문자입력시 빈값이 남는다
          if($(this).val().length == 0)
          {
            $(this).val('0');
          }

          //모바일 크롬 브라우저의 경우 특수문자가 다 0으로 넘어오고  e.preventDefault(); 이벤트 실행이 안되는 버그수정
          if(e.keyCode == 0)
          {
            $(this).val('0');
          }
          else
          {
            e.preventDefault();
          }
        }
      }
    });
    //----------------------------------------------------------------------------
  });


  // datepicker 셋팅
  $.datepicker.regional['ko'] = {
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true,
    yearRange: 'c-80:c+80', // Range of years to display in drop-down
    showButtonPanel: true,    /* 버튼 패널 사용 */
    showOtherMonths: true,    /* 이전/다음 달 일수 보이기 */
    selectOtherMonths: true,    /* 이전/다음 달 일 선택하기 */
    showOn: "both",
    buttonText: "달력",
    buttonImage: "/images/cal.gif",
    buttonImageOnly: true,
    prevText: '이전달',
    nextText: '다음달',
    closeText: '닫기',
    currentText: '오늘',
    dayNames : ['일', '월', '화', '수', '목', '금', '토'],
    dayNamesShort: ['일','월','화','수','목','금','토'],
    dayNamesMin: ['일', '월', '화', '수', '목', '금', '토'],
    monthNames : ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    monthNamesShort: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'] ,
    showMonthAfterYear: true /* 년과 달의 위치 바꾸기 */
  };
  $.datepicker.setDefaults($.datepicker.regional['ko']);
  $.datepicker._gotoToday = function(id) { $(id).datepicker('setDate', new Date()).datepicker('hide').blur();} // 오늘 클릭시 오늘날자 입력

  // 년월 달력용
  var datepicker_month = {
      showOn: 'both',
      buttonText: "달력",
      currentText: "이번달",
      changeMonth: true,
      changeYear: true,
      buttonImage: "/images/cal.gif",
      showButtonPanel: true,
      yearRange: 'c-99:c+99',
      showOtherMonths: true,
      selectOtherMonths: true,
      monthNames : ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
      monthNamesShort: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'] ,
      showMonthAfterYear: true /* 년과 달의 위치 바꾸기 */
  }

  datepicker_month.closeText = "선택";
  datepicker_month.dateFormat = "yy-mm";
  datepicker_month.onClose = function (dateText, inst) {
      var month = $("#ui-datepicker-div .ui-datepicker-month :selected").val();
      var year = $("#ui-datepicker-div .ui-datepicker-year :selected").val();
      $(this).datepicker( "option", "defaultDate", new Date(year, month, 1) );
      $(this).datepicker('setDate', new Date(year, month, 1));
  }

  /*
  사용법 2019-04-09 강대인
  datepicker_month.beforeShow = function () {
      var selectDate = $("#month_dt").val().split("-");
      var year = Number(selectDate[0]);
      var month = Number(selectDate[1]) - 1;
      $(this).datepicker( "option", "defaultDate", new Date(year, month, 1) );
  }

  $("#month_dt").datepicker(datepicker_month);

  <style type="text/css">
    table.ui-datepicker-calendar { display:none; }
  </style>
  */

}




