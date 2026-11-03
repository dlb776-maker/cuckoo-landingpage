//=================================================================================================
// 프로젝트 : 에이시스템 ERP
// 파 일 명 : /common/js/common.js
// 처리내용 : 공통자바스크립트
// 작 성 자 : 2010-03-20 김현옥
//=================================================================================================

if (typeof(COMMON_1_JS) == 'undefined')
{
  var COMMON_1_JS = true;

  var getOp7Up,getOp6Dn,getIE4Up,getIE4,getIE5,getIE6,getNN4,getUA=navigator.userAgent.toLowerCase();
  if(window.opera)
  {
    var i=getUA.indexOf('opera');
    if( i!=-1 )
    {
      var v=parseInt(getUA.charAt(i+6));
      getOp7Up=v>=7;
      getOp6Dn=v<7;
    }
  }

  // sns 연동

  /*

<title>태안서 5.1규모 지진…국내 지진 중 두번째 규모</title>
<meta name="description" content=" 충남 태안지역에서 규모 5.1의 지진이 발생해 서울과 인천 등 수도권 지역에까지 진동이 전해졌다. 이는 국내 지진 중 두 번째 ..." />

<meta name="author" content="헤럴드경제" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<LINK rel="alternate" TYPE="application/rss+xml" TITLE="헤럴드경제" HREF="/rss_xml.php" />
<link rel="image_src" href="http://res.heraldm.com/content/image/2014/04/01/20140401000020_0.jpg" />


<meta property="me2:post_tag"		content="헤럴드경제"/>
<meta property="me2:category1"		content="헤럴드경제"/>
<meta property="me2:category2"		content="속보"/>
<meta property="me2:image"			content="http://res.heraldm.com/content/image/2014/04/01/20140401000020_0.jpg"/>

<meta property="og:title"			content="태안서 5.1규모 지진…국내 지진 중 두번째 규모"/>
<meta property="og:type"			content="article"/>
<meta property="og:url"				content="http://biz.heraldcorp.com/view.php?ud=20140401000028"/>
<meta property="og:image"			content="http://res.heraldm.com/content/image/2014/04/01/20140401000020_0.jpg"/>
<meta property="og:description"		content=" 충남 태안지역에서 규모 5.1의 지진이 발생해 서울과 인천 등 수도권 지역에까지 진동이 전해졌다. 이는 국내 지진 중 두 번째 ..."/>
<meta property="og:article:author"	content="헤럴드경제 | 코리아헤럴드"/>

<meta name="twitter:card"			content="summary_large_image">
<meta name="twitter:title"			content="태안서 5.1규모 지진…국내 지진 중 두번째 규모">
<meta name="twitter:site"			content="헤럴드경제">
<meta name="twitter:creator"		content="헤럴드">
<meta name="twitter:image"			content="http://res.heraldm.com/content/image/2014/04/01/20140401000020_0.jpg">
<meta name="twitter:description"	content=" 충남 태안지역에서 규모 5.1의 지진이 발생해 서울과 인천 등 수도권 지역에까지 진동이 전해졌다. 이는 국내 지진 중 두 번째 ...">

function fbs_click()
{
  u='http://biz.heraldcorp.com/view.php?ud=20140401000028&pp=001';
  var fbWin = window.open('http://www.facebook.com/sharer.php?u='+encodeURIComponent(u),'facebooksharer','toolbar=0,status=0,width=626,height=436');
  return;
}

<a target="blank" href="http://twitter.com/?status=%ED%83%9C%EC%95%88%EC%84%9C 5.1%EA%B7%9C%EB%AA%A8 %EC%A7%80%EC%A7%84%E2%80%A6%EA%B5%AD%EB%82%B4 %EC%A7%80%EC%A7%84 %EC%A4%91 %EB%91%90%EB%B2%88%EC%A7%B8 %EA%B7%9C%EB%AA%A8 http://biz.heraldcorp.com/view.php?ud=20140401000028"><img alt="" src="http://res.heraldm.com/new_201209/images/icon/ico_sns_t.gif"></a>
<a target="blank" href="http://me2day.net/posts/new?new_post[body]=%ED%83%9C%EC%95%88%EC%84%9C+5.1%EA%B7%9C%EB%AA%A8+%EC%A7%80%EC%A7%84%E2%80%A6%EA%B5%AD%EB%82%B4+%EC%A7%80%EC%A7%84+%EC%A4%91+%EB%91%90%EB%B2%88%EC%A7%B8+%EA%B7%9C%EB%AA%A8:http://biz.heraldcorp.com/view.php?ud=20140401000028"><img alt="" src="http://res.heraldm.com/new_201209/images/icon/ico_sns_m.gif"></a>
<a href="javascript:var clogWin=window.open('http://csp.cyworld.com/bi/bi_recommend_pop.php?url=http%3A%2F%2Fbiz.heraldcorp.com%2Fview.php%3Fud%3D20140401000028', 'recom_icon_pop', 'width=400,height=364,scrollbars=no,resizable=no');"><img alt="" src="http://res.heraldm.com/new_201209/images/icon/icn_sns04.gif"></a>
<a href="javascript:var daumWin=window.open( 'http://yozm.daum.net/api/popup/prePost?link=http://biz.heraldcorp.com/view.php?ud=20140401000028&prefix=%ED%83%9C%EC%95%88%EC%84%9C+5.1%EA%B7%9C%EB%AA%A8+%EC%A7%80%EC%A7%84%E2%80%A6%EA%B5%AD%EB%82%B4+%EC%A7%80%EC%A7%84+%EC%A4%91+%EB%91%90%EB%B2%88%EC%A7%B8+%EA%B7%9C%EB%AA%A8', 'yozmSend', 'width=466, height=356' );"><img alt="" src="http://res.heraldm.com/new_201209/images/icon/icn_sns05.gif"></a>
  */



  var SNS = {
    facebook: function (DocTitle, DocSummary,ShareUrl,DocImage )
    {
      //link = encodeURIComponent(link);
      //description = encodeURIComponent(description);
      //var url = 'http://www.facebook.com/sharer.php?u=' + link + '&t=' + description;

      ShareUrl = encodeURIComponent(ShareUrl);
      DocTitle = encodeURIComponent(DocTitle);
      DocSummary = encodeURIComponent(DocSummary);
      DocImage = encodeURIComponent(DocImage);

      var url = 'http://www.facebook.com/sharer.php?s=100&p[url]='+(ShareUrl)+'&p[title]='+(DocTitle)+"&p[summary]="+(DocSummary)+"&p[images][0]="+(DocImage);
      var a = window.open(url, 'facebook', 'width=466, height=356');
      if (a)
      {
        a.focus();
      }
    },
    /*
    facebook_feed:function (title, desc, url, img)
    {
      FB.init({appId:"259680654171010", cookie:true, status:true, xfbml:true});
      FB.ui({
        method:"feed",
        name:title,
        caption:url,
        description:desc,
        message:desc,
        picture:img,
        link:url,
      });
    },
    */
    twitter:function(link, title, description)
    {
      link = encodeURIComponent(link);
      title = encodeURIComponent(title);
      description = encodeURIComponent(description);

      //var url = 'http://twitter.com/share?text=' + description + '& url=' + link;
      var url = 'http://twitter.com/share?original_referer='+ link +'&url=' + link + '&text=' + title + '::' + description;
      var a = window.open(url, 'twitter', 'width=466, height=356');
      if (a)
      {
        a.focus();
      }
    },
    me2day : function (link, description)
    {
      link=encodeURIComponent(link);
      description = encodeURIComponent(description);

      var url = 'http://www.me2day.net/posts/new?new_post[body]="'+description+'":'+link;
      var a = window.open(url,'me2day','');
      if (a)
      {
        a.focus();
      }
    },
    yozm: function (link, description)
    {
      link=encodeURIComponent(link);
      description = encodeURIComponent(description);

      var url = 'http://yozm.daum.net/api/popup/prePost?sourceid=&link='+link+'&prefix='+description;
      var a = window.open(url,'yozm','');
      if (a)
      {
        a.focus();
      }
     }
  };

 function share_sns(sns)
 {
   var long_url = "<?=$board_skin_path?>/sns_share.php?bo_table=<?=$bo_table?>&wr_id=<?=$wr_id?>";
   if(sns == "fb") snsurl = long_url + "&sns=fb";
   if(sns == "tw") snsurl = long_url + "&sns=tw";
   if(sns == "cs") snsurl = long_url + "&sns=cs";
   var newwin = window.open(snsurl, "sns", "width=600, height=400, toolbar=0");
  }

  // IE 버젼확인
  var strAppVersion = navigator.appVersion;
  var ieVersion = strAppVersion.substr(strAppVersion.indexOf('MSIE')+5,1)

  var scrollAddFlag      = true; // 스크롤형 목록에서 추가되는 데이타가 중복되지 않도록 처리
  var findSelectOverFlag = false;
  var calendarOverFlag   = false; // 달력이미지오버상태

  var topMenuClick = false; // 탑메뉴클릭(토글)
  var topMenuOver  = false; // 탑메뉴오버상태

  var menuFlag     = false; // top메뉴보기처리
  var menuSubFlag  = false; // top메뉴보기처리
  var menuSubFlagA = false; // top메뉴보기처리
  var topFlag1 = false;
  var topFlag2 = false;
  var topFlag3 = false;
  //---------------------------------------------------------------------------------------
  // 함수명 : findSelectOver
  // 기  능 : DIV선택목록 mouse over 상태 저장
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function findSelectOver(pKbn)
  {
    if ("1" == pKbn) { findSelectOverFlag = true;  }
    else             { findSelectOverFlag = false; }
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : getNum
  // 기  능 : 숫자형체크
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function getNum(arguments)
  {
    for ( var loopC=0; loopC<arguments.length; ++loopC )
    {
      if (isNaN(arguments[loopC]) || typeof(arguments[loopC])!='number')
      {
        return false;
      }
    }
    return true;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getStr
  // 기  능 : 문자형체크
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function getStr(arguments)
  {
    for ( var loopC=0; loopC<arguments.length; ++loopC )
    {
      if ( typeof(arguments[loopC])!='string' )
      {
        return false;
      }
    }
    return true;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getDef
  // 기  능 : 객체생성체크
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function getDef(arguments)
  {
    for( var loopC=0; loopC<arguments.length; ++loopC )
    {
      if( typeof(arguments[loopC])=='undefined' )
      {
        return false;
      }
    }
    return true;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : toGetElementById
  // 기  능 :
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function toGetElementById( pE )
  {
    if( typeof(pE) != 'string' ) { return pE; }

    if      (document.getElementById) { pE = document.getElementById(pE); }
    else if (document.all)            { pE = document.all[pE]; }
    else                              { pE = null; }
    return pE;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getClientWidth
  // 기  능 : 화면폭취득
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function getClientWidth()
  {
    /*
    var width = 0;
    if ( getOp6Dn )
    {
      width = window.innerWidth;
    }
    else if ( document.compatMode == 'CSS1Compat' && !window.opera && document.documentElement && document.documentElement.clientWidth )
    {
      width = document.documentElement.clientWidth;
    }
    else if ( document.body && document.body.clientWidth )
    {
      width = document.body.clientWidth;
    }
    else if ( getDef(window.innerWidth,window.innerHeight,document.height) )
    {
      width = window.innerWidth;
      if ( document.height>window.innerHeight ) { width -= 16; }
    }
    return width;
    */

    return $(window).width();

  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getClientHeight
  // 기  능 : 화면높이취득
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function getClientHeight()
  {
    var height = 0;
    /*
    if ( getOp6Dn )
    {
      height = window.innerHeight;
    }
    else if ( document.compatMode == 'CSS1Compat' && !window.opera && document.documentElement && document.documentElement.clientHeight )
    {
      height = document.documentElement.clientHeight;
    }
    else if ( document.body && document.body.clientHeight )
    {
      height = document.body.clientHeight;
    }
    else if ( getDef(window.innerWidth,window.innerHeight,document.width) )
    {
      height = window.innerHeight;
      if ( document.width>window.innerWidth ) { height -= 16; }
    }
    */

    height = $(window).height();
    return height;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getBodyHeight
  // 기  능 : 바디높이
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function getBodyHeight()
  {
    /*
    var cw = getClientHeight();
    //var sw = window.document.body.scrollHeight;
    var sw = $(window).scrollTop() + $(window).height();
    return cw>sw ? cw : sw;
    */
    return $(document).height();
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getScrollTop
  // 기  능 : top stroll
  // 작성일 : 2009-07-07 김현옥
  // --------------------------------------------------------------------------------------
  function getScrollTop(pE, pWin)
  {
    var offset = 0;
    /*
    if ( !getDef(pE) || pWin || pE == document || pE.tagName.toLowerCase() == 'html' || pE.tagName.toLowerCase() == 'body' )
    {
      var w = window;
      if (pWin && pE) { w = pE; }
      if      (w.document.documentElement && w.document.documentElement.scrollTop) { offset = w.document.documentElement.scrollTop; }
      else if (w.document.body && getDef(w.document.body.scrollTop)              ) { offset = w.document.body.scrollTop; }
    }
    else
    {
      pE = toGetElementById(pE);
      if (pE && getNum(pE.scrollTop)) { offset = pE.scrollTop; }
    }
    */
    offset = $(window).scrollTop();
    return offset;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getTop
  // 기  능 : top이동
  // 작성일 : 2009-07-07 김현옥
  // --------------------------------------------------------------------------------------
  function getTop( pE, pY )
  {
    if ( !(pE=toGetElementById(pE)) ) { return 0; }
    var css = getDef(pE.style);

    if ( css && getStr(pE.style.top) )
    {
      if ( getNum(pY) )
      {
        pE.style.top = pY + 'px';
      }
      else
      {
        pY = parseInt(pE.style.top);
        if( isNaN(pY) ) { pY = 0; }
      }
    }
    else if (css && getDef(pE.style.pixelTop))
    {
      if(getNum(pY)) { pE.style.pixelTop = pY; }
      else           { pY = pE.style.pixelTop; }
    }
    return pY;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : flashWrite
  // 기  능 : flash 출력
  // 작성일 : 2010-03-20 김현옥
  // 참  조 :
  // --------------------------------------------------------------------------------------
  function flashWrite( pUrl, pW, pH, pId, pVars )
  {
    // 플래시 코드 정의
    var flashStr="<object classid='clsid:d27cdb6e-ae6d-11cf-96b8-444553540000' codebase='http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,0,0' width='"+pW+"' height='"+pH+"' id='"+pId+"' align='middle'>"+
                 "<param name='movie' value='"+pUrl+"' />"+
                 "<param name='wmode' value='transparent' />"+
                 "<param name='menu' value='false' />"+
                 "<param name='quality' value='high' />"+
                 "<param name='flashVars' value='"+pVars+"' />"+
                 "<embed src='"+pUrl+"' wmode='transparent' menu='false' flashVars='"+pVars+"' quality='high' width='"+pW+"' height='"+pH+"' name='"+pId+"' align='middle' type='application/x-shockwave-flash' pluginspage='http://www.macromedia.com/go/getflashplayer' />"+
                 "</object>";

    // 플래시 코드 출력
    document.write(flashStr);
  }

  //---------------------------------------------------------------------------------------#
  // 함수명 : goUrl
  // 기  능 : URL이동
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------#
  function goUrl(pUrl, pTarget)
  {
    if (pTarget == "_blank") { newwin = window.open(pUrl,'newwin',''); }
    else                     { location.href = pUrl;                   }
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : byteCheck
  // 기  능 : Textarea의 바이트수 (글자수 제한)
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function byteCheck(pObj, pTarget, pBytesLimit)
  {
    var msgVal      = pObj.value;
    var bytesLen    = 0;
    var curMsgLen   = '';
    var curBytesLen = 0;
    var realVal     = '';
    var realLen     = 0;
    for(var loopC = 0; loopC < msgVal.length; loopC++)
    {
      var oneChar = msgVal.charAt(loopC);
      if ( escape(oneChar).length > 4              ) { bytesLen += 2; }
      else if ( oneChar != '\r' || oneChar != '\n' ) { bytesLen++;    }

      if ( bytesLen <= pBytesLimit )
      {
        curMsgLen = loopC + 1;
        curBytesLen = bytesLen;
      }
    }

    if ( bytesLen > pBytesLimit )
    {
      alert("더이상 입력하실 수 없습니다. 초과된 글은 삭제합니다.");
      pObj.value = msgVal.substr(0, curMsgLen);    // 초과 입력시 초과된 만큼 잘라줌
      realLen = curBytesLen;
    }
    else
    {
      realLen = bytesLen;
    }

    if(pTarget)
    {
      toGetElementById(pTarget).innerHTML = realLen;
    }
    else
    {
      return realLen;
    }
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : contentReSize
  // 기  능 :
  // 작성일 : 2010-03-20 김현옥
  // 참  조 :
  // --------------------------------------------------------------------------------------
  function contentReSize(pType)
  {
    frm = document.getElementById('reply');
    switch(pType)
    {
      case "+" : frm.style.pixelHeight += 50;                                      break;
      case "-" : if( frm.style.pixelHeight > 82 ) { frm.style.pixelHeight -= 50; } break;
    }
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getCookie
  // 기  능 : 쿠키값취득
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function getCookie(pName)
  {
    var flag = document.cookie.indexOf(pName+'=');
    if (flag != -1)
    {
      flag += pName.length + 1
      end = document.cookie.indexOf(';', flag)

      if (end == -1) { end = document.cookie.length; }
      return unescape(document.cookie.substring(flag, end))
    }
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : setCookie
  // 기  능 : 쿠키값저장
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function setCookie(pName, pValue, pExpire)
  {
    var today     = new Date();
    var expireday = new Date(today.getTime() + pExpire);
    document.cookie = pName + "=" + escape(pValue)+ "; path=/; expires=" + expireday.toGMTString() + ";";
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : new_window
  // 기  능 : 가운데창 - POST용 파라메타 사용
  // 작성일 : 2014-04-01 강대인
  // 참  조 :
  // --------------------------------------------------------------------------------------
  function new_window( pPage, arrVal, pName, pW, pH, pTool, pScroll,pFull,pNameHold,pWindowType)
  {
    if ( "yes" != pNameHold   ) { pName       = gf_getTime(); }
    if ( "yes" != pFull       ) { pFull       = "no"; }
    if ( "yes" != pWindowType ) { pWindowType = "no"; }
    var winl = (screen.width-pW)/2;
    var wint = (screen.height-pH)/2;
    var settings  = 'height='+pH+',';
        settings += 'width='+pW+',';
        settings += 'top='+wint+',';
        settings += 'left='+winl+',';
        settings += 'toolbar='+pTool+',';
        settings += 'scrollbars='+pScroll+',';
        settings += 'fullscreen='+pFull+',';
        settings += 'location='+pWindowType+',directories='+pWindowType+',menubar='+pWindowType+',resizable='+pWindowType;
    win = window.open("about:blank",pName,settings);

    $('#idPost').remove();
    var act     = pPage;
    var html = "<form name='postForm' method='post' action='"+act+"' target='"+pName+"'>";

    for(var key in arrVal)
    {
      html += "<input type='hidden' name='"+key+"' value='"+arrVal[key]+"' />";
    }

    html += "</form>";
    $('<div id="idPost" class="ssHide"></div>').appendTo('body');
    $('#idPost').html(html);

    document.postForm.submit();
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : newWindow
  // 기  능 : 가운데창
  // 작성일 : 2010-03-20 김현옥
  // 참  조 :
  // --------------------------------------------------------------------------------------
  function newWindow( pPage, pName, pW, pH, pTool, pScroll,pFull,pNameHold,pWindowType)
  {
    if ( "yes" != pNameHold   ) { pName       = gf_getTime(); }
    if ( "yes" != pFull       ) { pFull       = "no"; }
    if ( "yes" != pWindowType ) { pWindowType = "no"; }
    var winl = (screen.width-pW)/2;
    var wint = (screen.height-pH)/2;
    var settings  = 'height='+pH+',';
        settings += 'width='+pW+',';
        settings += 'top='+wint+',';
        settings += 'left='+winl+',';
        settings += 'toolbar='+pTool+',';
        settings += 'scrollbars='+pScroll+',';
        settings += 'fullscreen='+pFull+',';
        settings += 'location='+pWindowType+',directories='+pWindowType+',menubar='+pWindowType+',resizable='+pWindowType;
    win = window.open("about:blank",pName,settings);

    $('#idPost').remove();
    var tmpPage  = pPage.split("?");
    var act     = tmpPage[0];
    var html = "<form name='postForm' method='post' action='"+act+"' target='"+pName+"'>";

    if ( 1 < tmpPage.length )
    {
      var tmpParm = tmpPage[1].split("&");
      for( loopC=0; loopC<tmpParm.length; loopC++ )
      {
        var parm = tmpParm[loopC].split("=");
        if ( "" != parm )
        {
          html += "<input type='hidden' name='"+parm[0]+"' value='"+parm[1]+"' />";
        }
      }
    }
    html += "</form>";
    $('<div id="idPost" class="ssHide"></div>').appendTo('body');
    $('#idPost').html(html);

    document.postForm.submit();
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : newWindow2
  // 기  능 : 구석창
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function newWindow2( pPage, pName, pW, pH, pL, pTool, pScroll,pFull )
  {
    pName = gf_getTime();
    if ( "yes" != pFull ) { pFull = "no"; }
    var settings  = 'height='+pH+',';
        settings += 'width='+pW+',';
        settings += 'top=0,';
        settings += 'left='+pL+',';
        settings += 'toolbar='+pTool+',';
        settings += 'scrollbars='+pScroll+',';
        settings += 'fullscreen='+pFull+',';
        settings += 'location=no,directories=no,menubar=no,resizable=no';
    win = window.open("about:blank",pName,settings);

    $('#idPost').remove();
    var tmpPage  = pPage.split("?");
    var act     = tmpPage[0];
    var html = "<form name='postForm' method='post' action='"+act+"' target='"+pName+"'>";
    var tmpParm = tmpPage[1].split("&");

    if ( 1 < tmpPage.length )
    {
      var tmpParm = tmpPage[1].split("&");
      for( loopC=0; loopC<tmpParm.length; loopC++ )
      {
        var parm = tmpParm[loopC].split("=");
        if ( "" != parm )
        {
          html += "<input type='hidden' name='"+parm[0]+"' value='"+parm[1]+"' />";
        }
      }
    }
    html += "</form>";
    $('<div id="idPost" class="ssHide"></div>').appendTo('body');
    $('#idPost').html(html);

    document.postForm.submit();

  }
  //---------------------------------------------------------------------------------------
  // 함수명 : newWindow3
  // 기  능 : 위치지정창
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function newWindow3( pPage, pName, pWidth, pHeight, pTop, pLeft, pTool, pScroll,pFull )
  {
    pName = gf_getTime();
    if ( "yes" != pFull ) { pFull = "no"; }
    var settings  = 'height='+pHeight+',';
        settings += 'width='+pWidth+',';
        settings += 'top='+pTop+',';
        settings += 'left='+pLeft+',';
        settings += 'toolbar='+pTool+',';
        settings += 'scrollbars='+pScroll+',';
        settings += 'fullscreen='+pFull+',';
        settings += 'location=no,directories=no,menubar=no,resizable=no';
    win = window.open("about:blank",pName,settings);

    $('#idPost').remove();
    var tmpPage  = pPage.split("?");
    var act     = tmpPage[0];
    var html = "<form name='postForm' method='post' action='"+act+"' target='"+pName+"'>";

    if ( 1 < tmpPage.length )
    {
      var tmpParm = tmpPage[1].split("&");
      for( loopC=0; loopC<tmpParm.length; loopC++ )
      {
        var parm = tmpParm[loopC].split("=");
        if ( "" != parm )
        {
          html += "<input type='hidden' name='"+parm[0]+"' value='"+parm[1]+"' />";
        }
      }
    }
    html += "</form>";
    $('<div id="idPost" class="ssHide"></div>').appendTo('body');
    $('#idPost').html(html);

    document.postForm.submit();

  }
  //---------------------------------------------------------------------------------------
  // 함수명 : newWindow3
  // 기  능 : 위치지정창
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function newWindow32( pPage, pName, pWidth, pHeight, pTop, pLeft, pTool, pScroll,pFull )
  {
    //pName = gf_getTime();
    if ( "yes" != pFull ) { pFull = "no"; }
    var settings  = 'height='+pHeight+',';
        settings += 'width='+pWidth+',';
        settings += 'top='+pTop+',';
        settings += 'left='+pLeft+',';
        settings += 'toolbar='+pTool+',';
        settings += 'scrollbars='+pScroll+',';
        settings += 'fullscreen='+pFull+',';
        settings += 'location=no,directories=no,menubar=no,resizable=no';
    win = window.open("about:blank",pName,settings);

    $('#idPost').remove();
    var tmpPage  = pPage.split("?");
    var act     = tmpPage[0];
    var html = "<form name='postForm' method='post' action='"+act+"' target='"+pName+"'>";
    var tmpParm = tmpPage[1].split("&");

    if ( 1 < tmpPage.length )
    {
      var tmpParm = tmpPage[1].split("&");
      for( loopC=0; loopC<tmpParm.length; loopC++ )
      {
        var parm = tmpParm[loopC].split("=");
        if ( "" != parm )
        {
          html += "<input type='hidden' name='"+parm[0]+"' value='"+parm[1]+"' />";
        }
      }
    }
    html += "</form>";
    $('<div id="idPost" class="ssHide"></div>').appendTo('body');
    $('#idPost').html(html);

    document.postForm.submit();

  }
  // --------------------------------------------------------------------------------------
  // 모달창 오픈
  // --------------------------------------------------------------------------------------
  function modalWindow( pUrl, pParam, pW, pH, pScroll )
  {
    var settings  ='dialogWidth='+pW+'px;';
    settings +='dialogHeight='+pH+'px;';
    settings +='center=yes;';
    settings +='screenTop=yes;';
    settings +='scroll='+pScroll+';';
    settings +='status=no;';
    settings +='help=no;';
    showModalDialog( pUrl, pParam, settings );
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : disableKeys
  // 기  능 :
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function disableKeys()
  {
    //var event = e || window.event; //

    if( (event.ctrlKey == true && (event.keyCode == 78 || event.keyCode == 82)) ||
        (event.keyCode >= 112 && event.keyCode <= 123) )
    {
      event.keyCode = 0;
      event.cancelBubble = true;
      event.returnValue  = false;
    }
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : gf_checkNums
  // 기  능 : 숫자만 입력
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function gf_checkNums(e)
  {
    var keyCode = "";

    if(window.event)
    {
      keyCode = window.event.keyCode;
    }
    else
    {
      keyCode = e.which;
    }

    //alert(keyCode);
    if((keyCode >= 48 && keyCode <=57) || (keyCode >= 96 && keyCode <=105) ||  keyCode == 8 || keyCode == 9 || keyCode == 13 || keyCode == 46 || keyCode == 37 || keyCode == 39 )
    {
      return true;
    }
    else
    {
      if(navigator.appName == "Opera")
      {
        alert("숫자만 입력할 수 있습니다.");
        e.preventDefault();
        return false;
      }

      if(window.event)
        window.event.returnValue = false;
      else
      {
        e.preventDefault();
      }
    }

  }

  //---------------------------------------------------------------------------------------
  // 함수명 : gf_checkNumsPoint
  // 기  능 : 숫자만 입력(소수점 가능)
  // 작성일 : 2013-05-08 이영남
  // --------------------------------------------------------------------------------------
  function gf_checkNumsPoint(e)
  {
    var keyCode = "";

    if(window.event)
    {
      keyCode = window.event.keyCode;
    }
    else
    {
      keyCode = e.which;
    }

    if((keyCode >= 48 && keyCode <=57) || (keyCode >= 96 && keyCode <=105) || keyCode == 8 || keyCode == 9 || keyCode == 13 || keyCode == 46 || keyCode == 110 || keyCode == 190 || keyCode == 37 || keyCode == 39 )
    {
      return true;
    }
    else
    {

      if(navigator.appName == "Opera")
      {
        alert("숫자만 입력할 수 있습니다.");
        e.preventDefault();
        return false;
      }

      if(window.event)
      {
        window.event.returnValue = false;
      }
      else
      {
        e.preventDefault();
      }
    }

  }

  //---------------------------------------------------------------------------------------
  // 함수명 : isNumber
  // 기  능 : 숫자인지 체크
  // 작성일 : 2013-05-29 이영남
  // --------------------------------------------------------------------------------------
  function isNumber(s)
  {
    s += ''; // 문자열로 변환
    s = s.replace(/^\s*|\s*$/g, ''); // 좌우 공백 제거
    if (s == '' || isNaN(s)) return false;
    return true;
  }


  //---------------------------------------------------------------------------------------
  // 함수명 : OutHyphen
  // 기  능 : 숫자하이픈빼기
  // 작성일 : 2013-05-19 이영남
  // 참  조 : pStr : 문자열
  // --------------------------------------------------------------------------------------
  function OutHyphen(pStr)
  {
    hyphenStr   = String(pStr);
    unHyphenStr = '';

    for( loopC=0; loopC<hyphenStr.length; loopC++ )
    {
        substr = hyphenStr.substring(loopC,loopC+1);
        if( substr != '-' ) { unHyphenStr += substr; }
    }

    return unHyphenStr;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : filterChk
  // 기  능 : 특수문자체크
  // 작성일 : 2013-06-19 이영남
  // 참  조 : pStr : 문자열
  // --------------------------------------------------------------------------------------
  function filterChk(pStr)
  {
    var chktext = /[ \{\}\[\]\/?.,;:|\)*~`!^\-_+┼<>@\#$%&\'\"\\\(\=]/gi;
    if ( chktext.test(pStr) ) { alert('특수문자는 입력하실 수 없습니다.'); return ''; }
    return pStr;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : getByteLen
  // 기  능 : 바이트구하기
  // 작성일 : 2013-06-24 이영남
  // 참  조 : str : 문자열
  // --------------------------------------------------------------------------------------
  function getByteLen(str)
  {
    len = (function(s,b,i,c) { for(b=i=0;c=s.charCodeAt(i++);b+=c>>11?2:c>>7?2:1); return b })(str);
    return len;
  }

  // 자동하이픈(주민번호) ----------------------------------------------------------------------------
  function gf_autoHyphen(pObj)
  {
    var phone = pObj.value;
    phone = phone.replace(/-/gi,"");
    if ( 6 <= phone.length )
    {
      pObj.value = phone.substring(0,6)+"-"+phone.substring(6,phone.length);
    }
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : gf_checkComma
  // 기  능 : 실시간 입력창에 콤마 찍기
  // 작성일 : 2010-03-20 김현옥
  // 참  조 :
  // --------------------------------------------------------------------------------------
  function gf_checkComma(pObj)
  {
    var num = pObj.value;
    if (pObj.value.length >= 3)
    {
      re  = /^$|,/g;
      num = num.replace(re, "");
      fl  = "";
      if ( isNaN(num) ) { alert("문자는 사용할 수 없습니다."); return 0; }  // 숫자형이 아닌경우
      if ( num == 0 ) { return num; }                                       // 0인경우
      if ( num < 0  ) { num = num * (-1); fl = "-"; } // 음수확인
      else            { num = num * 1;              }

      num = new String(num);
      var arrNum = num.split(".");
      num = new String(arrNum[0]);

      var temp    = "";
      var co      = 3;
      var num_len = num.length;
      while ( num_len > 0 )
      {
        num_len = num_len - co;
        if ( num_len < 0 ) { co = num_len + co; num_len=0; }
        temp = "," + num.substr(num_len,co) + temp;
      }
      if ( arrNum[1] ) { pObj.value = fl + temp.substr(1) + "." + arrNum[1];    }
      else             { pObj.value = fl + temp.substr(1);    }
    }
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : OutComma
  // 기  능 : 숫자컴마빼기
  // 참  조 : pStr : 문자열
  // --------------------------------------------------------------------------------------
    function OutComma(pStr)
    {
      str = String(pStr);
      //console.log(pStr);
      return str.replace(/[^-\.\d]/g, '');
    }

  //---------------------------------------------------------------------------------------
  // 함수명 : InComma
  // 기  능 : 숫자컴마넣기
  // 참  조 : pStr : 문자열
  // --------------------------------------------------------------------------------------
  function InComma(pStr)
  {
    var str = OutComma(pStr);
    //console.log(str);
	  var regExp = /^([-+]?\d+)(\d{3})(\.\d+)?/;  // 필요한 정규식.

	  while ( regExp.test( str ) )
    {
      str = str.replace( regExp, "$1" + "," + "$2" + "$3" );  // 쉼표 삽입.
    }

    return str;
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : chkBox
  // 기  능 : 체크박스 체크
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function chkBox( pObj )
  {
    var tmp = pObj.id;
    var objName = tmp.split("__");
    var chk = document.getElementById(objName[0]);
    if ( "6" == ieVersion ) { chk.click(); } // IE6인경우 클릭처리

    if ( chk.checked ) { $("#"+pObj.id).css({'background':'#afe02e'}); } // 체크액션이 일어나기전이라 반대로 세팅
    else               { $("#"+pObj.id).css({'background':''});        }
  }

  //---------------------------------------------------------------------------------------
  // 함수명 : chkRadio
  // 기  능 : 라디오버튼 체크
  // 작성일 : 2010-03-20 김현옥
  // 참  조 : pObj : 라벨Obj
  //          라벨의 명칭은 __ 로 구분(예:이름__번호)
  // --------------------------------------------------------------------------------------
  function chkRadio( pObj,pColor)
  {
    var label_id = pObj.id;

    var tmp = label_id.split("__");
    $("label[id^="+tmp[0]+"__]").css({'background':''}); // 그룹라벨 배경을 지움

    if ( "nocolor" != pColor )
    {
      $("#"+label_id).css({'background':'#afe02e'}); // 해당라벨의 배경색변경
    }

    //$("#"+label_id+" > input[type:radio]").click();
  }


  //-----------------------------------------------------------------------------
  // 처리내용 : 사업자등록번호 정합성 체크
  // 인수     : 사업자등록번호(XXX-XX-XXXXX) 생략불가
  // 변경이력 : xxxx.xx.xx    xxxxxxxxxxxxxxxxxxxxxxxxxx
  // 이벤트   : onBlur
  // 사용예   : onBlur='f_chk_SaupNo(this.value)'
  //-----------------------------------------------------------------------------
  function gf_ChkSaupNo(WorkNum)
  {
     var rtn_cd = true;
     WorkNum    = WorkNum.replace(/-/gi,"");

     if ( 10 != WorkNum.length )
     {
        alert("잘못된 사업자등록번호 입니다.");
        rtn_cd = false;
     }

     if ( rtn_cd )
     {
        sumMod  = 0;
        sumMod += parseInt(WorkNum.substring(0,1));
        sumMod += parseInt(WorkNum.substring(1,2)) * 3 % 10;
        sumMod += parseInt(WorkNum.substring(2,3)) * 7 % 10;
        sumMod += parseInt(WorkNum.substring(3,4)) * 1 % 10;
        sumMod += parseInt(WorkNum.substring(4,5)) * 3 % 10;
        sumMod += parseInt(WorkNum.substring(5,6)) * 7 % 10;
        sumMod += parseInt(WorkNum.substring(6,7)) * 1 % 10;
        sumMod += parseInt(WorkNum.substring(7,8)) * 3 % 10;
        sumMod += Math.floor(parseInt(WorkNum.substring(8,9)) * 5 / 10);
        sumMod += parseInt(WorkNum.substring(8,9)) * 5 % 10;
        sumMod += parseInt(WorkNum.substring(9,10));

        if ( 0 != sumMod % 10 )
        {
           alert("잘못된 사업자등록번호 입니다.");
           rtn_cd = false;
        }
     }
     return rtn_cd;
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : gf_checkDate
  // 기  능 : 날짜자동생성 및 정합성체크
  // 작성일 : 2010-03-20 김현옥
  // 참  고 : onChange 이벤트 또는 외부셋팅이후 체크
  // --------------------------------------------------------------------------------------
  function gf_checkDate(pObj)
  {
    if ("" == pObj.value) { return false; }

    var rtnCode = true;
    var pattern = /^[12][0-9]{3}\-[01]?[0-9]\-[0-3]?[0-9]$/;
    var repDate = pObj.value.match(/[0-9]+$/);
    var d = new Date();
    var year  = d.getFullYear();
    var month = d.getMonth()+1;
    var days  = new Array(31,28,31,30,31,30,31,31,30,31,30,31);
    var chkDate = pObj.value;

    switch(repDate.length)
    {
      case 8 : chkDate = repDate.substring(0,4)+"-"+repDate.substring(4,6)+"-"+repDate.substring(6,8);      break;
      case 6 : chkDate = "20"+repDate.substring(0,2)+"-"+repDate.substring(2,4)+"-"+repDate.substring(4,6); break;
      case 4 : chkDate = year+"-"+repDate.substring(0,2)+"-"+repDate.substring(2,4); break;
      case 2 : chkDate = year+"-"+month+"-"+repDate.substring(0,2); break;
    }

    var arrDate = chkDate.split("-");

    if( 3 == arrDate.length && "" != arrDate[0] )
    {
      var aYear  = arrDate[0];
      var aMonth = arrDate[1];
      var aDay   = arrDate[2];

      //윤년계산(윤년의2월은29일로지정)
      if( aYear%4==0 && (aYear%100!=0 || aYear%400==0)) { days[1]=29; }

      //월체크
      if( '01' > aMonth || '12' < aMonth ) { rtnCode = true; }
      //일체크
      if( rtnCode && ( '01' > aDay || days[aMonth-1] < aDay ) ) { rtnCode = true; }

      if(rtnCode)
      {
         //월 포맷변경
         if( 1 == aMonth.length ){ aMonth = '0' + aMonth; }
         //일 포맷변경
         if( 1 == aDay.length )  { aDay = '0' + aDay; }
         chkDate = aYear+"-"+aMonth+"-"+aDay;
      }
    }
    else
    {
      rtnCode = false;
    }
    if ( rtnCode ) { pObj.value = chkDate; }
    else           { alert("입력된 날짜가 형식에 맞지 않습니다.["+chkDate+"]"); pObj.value = ""; }
    return rtnCode;
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : gf_fileTypecheck
  // 기  능 : 업로드파일의 파일타입확인
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function gf_fileTypecheck(pObj,pType)
  {
    if ( "excel" == pType )
    {
      var fileName = pObj.value;
      if (fileName != "")
      {
        var dotIndex = fileName.lastIndexOf(".");
        var ext = fileName.substring(dotIndex+1).toLowerCase();
        if(ext != "xlsx")
        {
          return false;
        }
      }
    }
    return true;
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : gf_autoSize
  // 기  능 : 입력폼의 길이를 글자수에 맞게 자동조정
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function gf_autoSize(pObj)
  {
    var msgVal      = pObj.value;
    var bytesLen    = 0;
    for(var loopC = 0; loopC < msgVal.length; loopC++)
    {
      var oneChar = msgVal.charAt(loopC);
      if ( escape(oneChar).length > 4              ) { bytesLen += 2; }
      else if ( oneChar != '\r' || oneChar != '\n' ) { bytesLen++;    }
    }
    if ( bytesLen )
    {
      pObj.size = bytesLen+1;
    }
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : gf_leftShow
  // 기  능 : 좌측메뉴숨기기(토글)
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function gf_leftShow(pKbn)
  {
    if ( "hide" == pKbn ) { $('#idLeftMenu').hide(); $("#idContainer").css({"padding-left":"0px"});   }
    else                  { $('#idLeftMenu').show(); $("#idContainer").css({"padding-left":"195px"}); }
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : overClass
  // 기  능 :
  // 작성일 : 2009-07-07 김현옥
  // --------------------------------------------------------------------------------------
  function overClass(pEl)
  {
    var pattern = /(On)$/;
    var code    = pEl.className;
    var tag     = "On";

    if( pattern.test(code) == true )
    {
      code = code.replace(tag, "");
      pEl.className = code;
    }
    else
    {
      pEl.className = code+"On";
    }
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : gf_ucFirst
  // 기  능 : 문자열의 첫글자를 대문자로 변환
  // 작성일 : 2010-03-20 김현옥
  // --------------------------------------------------------------------------------------
  function gf_ucFirst(pStr)
  {
    return pStr.substring(0,1).toUpperCase()+pStr.substring(1,pStr.length);
  }
  //---------------------------------------------------------------------------------------
  // 선택레이어토글표시
  // --------------------------------------------------------------------------------------
  function gf_viewSelectBox(pId1,pId2,pLocation)
  {
    if ( "none" == $("#"+pId2).css("display") )
    {
      $('[id^=shHide]').hide();
      if ( "top" == pLocation )
      {
        $("#"+pId2).css({"top":(parseInt($("#"+pId1).offset().top)+7)+"px"});
        $("#"+pId2).css({"left":"0"});
      }
      else
      {
        $("#"+pId2).css({"top":(parseInt($("#"+pId1).offset().top)+parseInt($("#"+pId1).height())+2)+"px"});
        $("#"+pId2).css({"left":(parseInt($("#"+pId1).offset().left))+"px"});
      }
      $("#"+pId2).show();
      $("#"+pId2).focus();
    }
    else
    {
      $("#"+pId2).hide();
      $("#"+pId1).blur();
    }
  }
  //---------------------------------------------------------------------------------------
  // 선택레이어토글표시
  // --------------------------------------------------------------------------------------
  function gf_allCheckBox(pId)
  {
    if ($("#shAll"+pId+":checked").length > 0)
    {
      $("input[id^=sh"+pId+"]:not(checked)").attr("checked", true);
      $("label[id^=sh"+pId+"]").css("background", "#afe02e");
    }
    else
    {
      $("input[id^=sh"+pId+"]:checked").attr("checked", false);
      $("label[id^=sh"+pId+"]").css("background", "");
    }
  }
  //---------------------------------------------------------------------------------------
  // 함수명 : gf_bookMark
  // 기  능 : 실시간 입력창에 콤마 찍기
  // 작성일 : 2012-03-19 강대운
  // 참  조 : pTitle = 북마크 제목
  // --------------------------------------------------------------------------------------
  function gf_bookMark(pTitle)
  {
    pUrl = location.href;
    if (window.sidebar) // firefox
    window.sidebar.addPanel(pTitle, pUrl, "");

    else if(window.opera && window.print)
    { // opera
     var elem = document.createElement('a');
     elem.setAttribute('href',url);
     elem.setAttribute('title',pTitle);
     elem.setAttribute('rel','sidebar');
     elem.click();
    }
    else if(document.all) // ie
    window.external.AddFavorite(pUrl,pTitle);
  }
  //---------------------------------------------------------------------------------------
  // 날짜값취득(팝업창의 명칭에사용:동일명칭안생기게하기위한방법)
  // --------------------------------------------------------------------------------------
  function gf_getTime()
  {
    var now = new Date();
    var nowStr = now.toString().replace(/ /gi,"").replace(/[+:]/gi,"");
    return nowStr;
  }

  // 스피트메뉴추가 ----------------------------------------------------------------------------------
  function addSpeedMenu(pType,pCate,pName,pPos)
  {
    if ( "" != pCate )
    {
      if ( confirm("["+pName+"]을(를) 메뉴에 추가 하시겠습니까?") )
      {
        $.post("/_admin/index.php", {shProgram:15,shType:pType,addCate:pCate}, function(data)
        {
          if ( "DUP" == data )
          {
            alert("이미 등록하신 메뉴 입니다.");
          }
          else
          {
            var aData = data.split("||");
            if ( "POPUP" == pPos ) { opener.refreshSpeedMenu(aData[1]); }
            else                   { refreshSpeedMenu(aData[1]); }

          }
        });
      }
    }
  }

  //---------------------------------------------------------------------------------------
  // 카피할때 출처 삽입하기
  // --------------------------------------------------------------------------------------
  function insertOrigin(pTitle, pForm, pUrl)
  {
    if (window.event)
    {
      window.event.returnValue = true;
      __insert_origin_title__  = pTitle;
      __insert_origin_url__    = pUrl;
      __insert_origin_from__   = pForm;
      window.setTimeout("_procInsertOrigin()", 25);
    }
  }

  //---------------------------------------------------------------------------------------
  // _procInsertOrigin
  // --------------------------------------------------------------------------------------
  function _procInsertOrigin()
  {
    if (window.clipboardData)
    {
      var obj       = document.frames["hdFrame"].document.body;
      var rng       = obj.createTextRange();
      var printFrom = '';
      if ( __insert_origin_from__ != "" )
      {
        printFrom = " from " + __insert_origin_from__;
      }
      var footerHTML = "<p style='margin:15px 0 0 0;'>";
      footerHTML    += "<a href='"+ __insert_origin_url__ +"' target='_new' title='제목 부분을 클릭하면\n원 게시물을 볼 수 있습니다.'>[출처] "+ __insert_origin_title__ + printFrom;
      footerHTML    += "</a></p>";
      rng.execCommand("Paste");
      obj.insertAdjacentHTML("BeforeEnd",  footerHTML);
      rng = obj.createTextRange();
      rng.execCommand("SelectAll");
      rng.execCommand("Cut");
    }
  }

  // 라인선택시 색상변경 -----------------------------------------------------------------------------
  function gf_lineSelect(pPos,pObj,pChoice)
  {
    //if ( "white" == $("#tr_"+pPos).css('backgroundColor') ) { $("#tr_"+pPos).css({'backgroundColor' : '#f2f2f2'}); $("#choice_"+pChoice).attr("checked","checked"); }

    if ( !$("#choice_"+pChoice).is(":checked") ) { $("#tr_"+pPos).css({'backgroundColor' : '#f2f2f2'}); $("#choice_"+pChoice).attr("checked",true);}
    else                                         { $("#tr_"+pPos).css({'backgroundColor' : 'white'});    $("#choice_"+pChoice).attr("checked",false);}
  }

  // 전체선택시 색상변경 -----------------------------------------------------------------------------
  function gf_allLineSelect(pObj)
  {
    if ( pObj.checked ) { $("#srListList [id^=tr_]").css({'background' : '#f2f2f2'});   }
    else                { $("#srListList [id^=tr_]").css({'background' : 'white'}); }
  }

  // 화면 상단 메뉴관련함수 --------------------------------------------------------------------------
  function tmOver(pPos) { $("#idHeader #menu"+pPos).attr("class","ssTblOn"); mf_topMenuMouseOver(pPos); }
  function tmOut(pPos)  { $("#idHeader #menu"+pPos).attr("class","ssTbl");   }
  function tssOver()    { $("#idHeader #topSpeedSys").attr("class","ssBtnSysOn"); }
  function tssOut()     { $("#idHeader #topSpeedSys").attr("class","ssBtnSys");   }
  function tshOver()    { $("#idHeader #topSpeedHome").attr("class","ssBtnHomeOn"); }
  function tshOut()     { $("#idHeader #topSpeedHome").attr("class","ssBtnHome");   }
  function tsmOver()    { $("#idHeader #topSpeedMenu").attr("class","ssBtnMenuOn"); }
  function tsmOut()     { $("#idHeader #topSpeedMenu").attr("class","ssBtnMenu");   }
  function tspOver()    { $("#idHeader #topSpeedPlus").attr("class","ssBtnPlusOn"); }
  function tspOut()     { $("#idHeader #topSpeedPlus").attr("class","ssBtnPlus");   }
  function tslOver()    { $("#idHeader #topSpeedMoveLeft").attr("class","ssBtnLeftOn"); }
  function tslOut()     { $("#idHeader #topSpeedMoveLeft").attr("class","ssBtnLeft");   }
  function tsrOver()    { $("#idHeader #topSpeedMoveRight").attr("class","ssBtnRightOn"); }
  function tsrOut()     { $("#idHeader #topSpeedMoveRight").attr("class","ssBtnRight");   }
  function tsiOver(pObj) { pObj.className="ssSMenuOn"; }
  function tsiOut(pObj)  { pObj.className="ssSMenu"; }

  //-----------------------------------------------------------------------------
  // 이미지 롤오버 관련함수(드림위버)
  //-----------------------------------------------------------------------------
  function MM_swapImgRestore() { //v3.0
    var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
  }
  function MM_preloadImages() { //v3.0
    var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
      var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
      if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
  }
  function MM_findObj(n, d) { //v4.01
    var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
      d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
    if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
    for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
    if(!x && d.getElementById) x=d.getElementById(n); return x;
  }
  function MM_swapImage() { //v3.0
    var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
     if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
  }
  function MM_scanStyles(obj, prop) { //v8.0
    var inlineStyle = null; var ccProp = prop; var dash = ccProp.indexOf("-");
    while (dash != -1){ccProp = ccProp.substring(0, dash) + ccProp.substring(dash+1,dash+2).toUpperCase() + ccProp.substring(dash+2); dash = ccProp.indexOf("-");}
    inlineStyle = eval("obj.style." + ccProp);
    if(inlineStyle) return inlineStyle;
    var ss = document.styleSheets;
    for (var x = 0; x < ss.length; x++) { var rules = ss[x].cssRules;
    for (var y = 0; y < rules.length; y++) { var z = rules[y].style;
      if(z[prop] && (rules[y].selectorText == '*[ID"' + obj.id + '"]')) {
          return z[prop];
    }  }  }  return "";
  }

  function MM_getProp(obj, prop) { //v8.0
    if (!obj) return ("");
    if (prop == "L") return obj.offsetLeft;
    else if (prop == "T") return obj.offsetTop;
    else if (prop == "W") return obj.offsetWidth;
    else if (prop == "H") return obj.offsetHeight;
    else {
      if (typeof(window.getComputedStyle) == "undefined") {
        if (typeof(obj.currentStyle) == "undefined"){
          if (prop == "P") return MM_scanStyles(obj,"position");
          else if (prop == "Z") return MM_scanStyles(obj,"z-index");
          else if (prop == "V") return MM_scanStyles(obj,"visibility");
        } else {
          if (prop == "P") return obj.currentStyle.position;
          else if (prop == "Z") return obj.currentStyle.zIndex;
          else if (prop == "V") return obj.currentStyle.visibility;
        }
      } else {
        if (prop == "P") return window.getComputedStyle(obj,null).getPropertyValue("position");
        else if (prop == "Z") return window.getComputedStyle(obj,null).getPropertyValue("z-index");
        else if (prop == "V") return window.getComputedStyle(obj,null).getPropertyValue("visibility");
      }
    }
  }

  function MM_dragLayer(objName,x,hL,hT,hW,hH,toFront,dropBack,cU,cD,cL,cR,targL,targT,tol,dropJS,et,dragJS) { //v8.0
    //Copyright 2005 Macromedia, Inc. All rights reserved.
    var i,j,aLayer,retVal,curDrag=null,curLeft,curTop,IE=document.all,NS4=document.layers;
    var NS6=(!IE&&document.getElementById), NS=(NS4||NS6); if (!IE && !NS) return false;
    retVal = true; if(IE && event) event.returnValue = true;
    if (MM_dragLayer.arguments.length > 1) {
      curDrag = MM_findObj(objName); if (!curDrag) return false;
      if (!document.allLayers) { document.allLayers = new Array();
        with (document) if (NS4) { for (i=0; i<layers.length; i++) allLayers[i]=layers[i];
          for (i=0; i<allLayers.length; i++) if (allLayers[i].document && allLayers[i].document.layers)
            with (allLayers[i].document) for (j=0; j<layers.length; j++) allLayers[allLayers.length]=layers[j];
        } else {
          if (NS6) { var spns = getElementsByTagName("span"); var all = getElementsByTagName("div");
            for (i=0;i<spns.length;i++) if (MM_getProp(spns[i],'P')) allLayers[allLayers.length]=spns[i];}
          for (i=0;i<all.length;i++) {
      if (NS4){if (all[i].style&&all[i].style.position) allLayers[allLayers.length]=all[i];}
            else if (MM_getProp(all[i],'P')) allLayers[allLayers.length]=all[i];
          }
      } }
      curDrag.MM_dragOk=true; curDrag.MM_targL=targL; curDrag.MM_targT=targT;
      curDrag.MM_tol=Math.pow(tol,2); curDrag.MM_hLeft=hL; curDrag.MM_hTop=hT;
      curDrag.MM_hWidth=hW; curDrag.MM_hHeight=hH; curDrag.MM_toFront=toFront;
      curDrag.MM_dropBack=dropBack; curDrag.MM_dropJS=dropJS;
      curDrag.MM_everyTime=et; curDrag.MM_dragJS=dragJS;

      curDrag.MM_oldZ = (NS4)?curDrag.zIndex:MM_getProp(curDrag,'Z');
      curLeft= (NS4)?curDrag.left:MM_getProp(curDrag,'L');
      if (String(curLeft)=="NaN") curLeft=0; curDrag.MM_startL = curLeft;
      curTop = (NS4)?curDrag.top:MM_getProp(curDrag,'T');
      if (String(curTop)=="NaN") curTop=0; curDrag.MM_startT = curTop;
      curDrag.MM_bL=(cL<0)?null:curLeft-cL; curDrag.MM_bT=(cU<0)?null:curTop-cU;
      curDrag.MM_bR=(cR<0)?null:curLeft+cR; curDrag.MM_bB=(cD<0)?null:curTop+cD;
      curDrag.MM_LEFTRIGHT=0; curDrag.MM_UPDOWN=0; curDrag.MM_SNAPPED=false; //use in your JS!
      document.onmousedown = MM_dragLayer; document.onmouseup = MM_dragLayer;
      if (NS) document.captureEvents(Event.MOUSEDOWN|Event.MOUSEUP);
    } else {
      var theEvent = ((NS)?objName.type:event.type);
      if (theEvent == 'mousedown') {
        var mouseX = (NS)?objName.pageX : event.clientX + document.body.scrollLeft;
        var mouseY = (NS)?objName.pageY : event.clientY + document.body.scrollTop;
        var maxDragZ=null; document.MM_maxZ = 0;
        for (i=0; i<document.allLayers.length; i++) { aLayer = document.allLayers[i];
          var aLayerZ = (NS4)?aLayer.zIndex:MM_getProp(aLayer,'Z');
          if (aLayerZ > document.MM_maxZ) document.MM_maxZ = aLayerZ;
          var isVisible = ((NS4)?aLayer.visibility:MM_getProp(aLayer,'V')).indexOf('hid') == -1;
          if (aLayer.MM_dragOk != null && isVisible) with (aLayer) {
            var parentL=0; var parentT=0;
            if (NS6) { parentLayer = aLayer.parentNode;
              while (parentLayer != null && parentLayer != document && MM_getProp(parentLayer,'P')) {
                parentL += parseInt(MM_getProp(parentLayer,'L')); parentT += parseInt(MM_getProp(parentLayer,'T'));
                parentLayer = parentLayer.parentNode;
                if (parentLayer==document) parentLayer = null;
            } } else if (IE) { parentLayer = aLayer.parentElement;
              while (parentLayer != null && MM_getProp(parentLayer,'P')) {
                parentL += MM_getProp(parentLayer,'L'); parentT += MM_getProp(parentLayer,'T');
                parentLayer = parentLayer.parentElement; } }
            var tmpX=mouseX-((NS4)?pageX:(MM_getProp(aLayer,'L'))+parentL+MM_hLeft);
            var tmpY=mouseY-((NS4)?pageY:(MM_getProp(aLayer,'T'))+parentT+MM_hTop);
            if (String(tmpX)=="NaN") tmpX=0; if (String(tmpY)=="NaN") tmpY=0;
            var tmpW = MM_hWidth;  if (tmpW <= 0) tmpW += (NS4)?clip.width:MM_getProp(aLayer,'W');
            var tmpH = MM_hHeight; if (tmpH <= 0) tmpH += (NS4)?clip.height:MM_getProp(aLayer,'H');
            if ((0 <= tmpX && tmpX < tmpW && 0 <= tmpY && tmpY < tmpH) && (maxDragZ == null
                || maxDragZ <= aLayerZ)) { curDrag = aLayer; maxDragZ = aLayerZ; } } }
        if (curDrag) {
          document.onmousemove = MM_dragLayer; if (NS4) document.captureEvents(Event.MOUSEMOVE);
          curLeft = (NS4)?curDrag.left:MM_getProp(curDrag,'L');
          curTop = (NS4)?curDrag.top:MM_getProp(curDrag,'T');
          if (String(curLeft)=="NaN") curLeft=0; if (String(curTop)=="NaN") curTop=0;
          MM_oldX = mouseX - curLeft; MM_oldY = mouseY - curTop;
          document.MM_curDrag = curDrag;  curDrag.MM_SNAPPED=false;
          if(curDrag.MM_toFront) {
            var newZ = parseInt(document.MM_maxZ)+1;
            eval('curDrag.'+((NS4)?'':'style.')+'zIndex=newZ');
            if (!curDrag.MM_dropBack) document.MM_maxZ++; }
          retVal = false; if(!NS4&&!NS6) event.returnValue = false;
      } } else if (theEvent == 'mousemove') {
        if (document.MM_curDrag) with (document.MM_curDrag) {
          var mouseX = (NS)?objName.pageX : event.clientX + document.body.scrollLeft;
          var mouseY = (NS)?objName.pageY : event.clientY + document.body.scrollTop;
          var newLeft = mouseX-MM_oldX; var newTop  = mouseY-MM_oldY;
          if (MM_bL!=null) newLeft = Math.max(newLeft,MM_bL);
          if (MM_bR!=null) newLeft = Math.min(newLeft,MM_bR);
          if (MM_bT!=null) newTop  = Math.max(newTop ,MM_bT);
          if (MM_bB!=null) newTop  = Math.min(newTop ,MM_bB);
          MM_LEFTRIGHT = newLeft-MM_startL; MM_UPDOWN = newTop-MM_startT;
          if (NS4) {left = newLeft; top = newTop;}
          else if (NS6){style.left = newLeft + "px"; style.top = newTop + "px";}
          else {style.pixelLeft = newLeft; style.pixelTop = newTop;}
          if (MM_dragJS) eval(MM_dragJS);
          retVal = false; if(!NS) event.returnValue = false;
      } } else if (theEvent == 'mouseup') {
        document.onmousemove = null;
        if (NS) document.releaseEvents(Event.MOUSEMOVE);
        if (NS) document.captureEvents(Event.MOUSEDOWN); //for mac NS
        if (document.MM_curDrag) with (document.MM_curDrag) {
          if (typeof MM_targL =='number' && typeof MM_targT == 'number' &&
              (Math.pow(MM_targL-((NS4)?left:MM_getProp(document.MM_curDrag,'L')),2)+
               Math.pow(MM_targT-((NS4)?top:MM_getProp(document.MM_curDrag,'T')),2))<=MM_tol) {
            if (NS4) {left = MM_targL; top = MM_targT;}
            else if (NS6) {style.left = MM_targL + "px"; style.top = MM_targT + "px";}
            else {style.pixelLeft = MM_targL; style.pixelTop = MM_targT;}
            MM_SNAPPED = true; MM_LEFTRIGHT = MM_startL-MM_targL; MM_UPDOWN = MM_startT-MM_targT; }
          if (MM_everyTime || MM_SNAPPED) eval(MM_dropJS);
          if(MM_dropBack) {if (NS4) zIndex = MM_oldZ; else style.zIndex = MM_oldZ;}
          retVal = false; if(!NS) event.returnValue = false; }
        document.MM_curDrag = null;
      }
      if (NS) document.routeEvent(objName);
    } return retVal;
  }

  //이메일 형식체크
  function gf_emailChk(parm)
  {
    var bol = false;
    if(!parm) return false;
    var exptext = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
    if (exptext.test(parm) == true) { bol = true; }
    return bol;     // bol 값을 반환 . 이메일 형식이 아니면 false
  }

  // 날짜형식('Y-m-d') 리턴
  // 작성자 : 이영남
  // sDate  : Date() 값
  function f_formatDate(sDate)
  {
    var year      = sDate.getFullYear();
    var month     = (sDate.getMonth()+1)<10? "0" + (sDate.getMonth()+1) : (sDate.getMonth()+1) ;
    var day			  = sDate.getDate()<10 ? "0" + sDate.getDate() : sDate.getDate();
    var rtn_date  = year + "-" + month+ "-" + day;

    return rtn_date;
  }

  // 날짜 덧셈/뺄셈
  // 작성자 : 이영남
  // sDate  : Y-m-d 형식 날짜
  // op     : 연산자
  // dc     : 일수(count day)
  function f_calcDate(sDate, op, dc)
  {
    var	date	= sDate.split('-');
    var dt3   = "";

    if ( op == "plus" )
    {
      dt3				= new Date(date[0], Number(date[1])-1, Number(date[2])+Number(dc));
    }
    else if ( op == 'minus' )
    {
      dt3				= new Date(date[0], Number(date[1])-1, Number(date[2])-Number(dc));
    }

    var rtn_date  = f_formatDate(dt3);

    return rtn_date;
  }

  // 날짜계산
  // 작성자 : 이영남
  // sDate  : Y-m-d 형식 날짜
  // op     : 연산자
  // type   : 년,월,일 별 계산 (y:년,m:월,d:일)
  // cnt    : 계산 수
  function f_calcDate2(sDate, op, type, cnt)
  {
    var	date	= sDate.split('-');
    var dt3   = "";

    if ( op == "plus" )
    {
      if      ( type == "y" ) { dt3	= new Date(Number(date[0])+Number(cnt), Number(date[1])-1, Number(date[2])); }
      else if ( type == "m" ) { dt3	= new Date(Number(date[0]), Number(date[1])-1+Number(cnt), Number(date[2])); }
      else if ( type == "d" ) { dt3	= new Date(Number(date[0]), Number(date[1])-1, Number(date[2])+Number(cnt)); }
    }
    else if ( op == 'minus' )
    {
      if      ( type == "y" ) { dt3	= new Date(Number(date[0])-Number(cnt), Number(date[1])-1, Number(date[2])); }
      else if ( type == "m" ) { dt3	= new Date(Number(date[0]), Number(date[1])-1-Number(cnt), Number(date[2])); }
      else if ( type == "d" ) { dt3	= new Date(Number(date[0]), Number(date[1])-1, Number(date[2])-Number(cnt)); }
    }

    var rtn_date  = f_formatDate(dt3);

    return rtn_date;
  }

  // 날짜형식체크
  // 작성자 : 이영남
  // confirmText : YYYY-mm_dd 형식값
  function onlyDate(confirmText)
  {
    var txtYear, txtMonth, txtDay, txtLastDay;
    if( confirmText.length != 10 ) { return false; }
    try
    {
      var sDate = confirmText.split("-");
      var cDate = new Date(sDate[0], Number(sDate[1])-1, sDate[2]);
      if( cDate == "NaN" ) { return false; }
      if( confirmText != f_formatDate(cDate) ) { return false; }
      return true;
    }
    catch(e)
    {
      return false;
    }
  }

  // 문자열을 byte 단위로 자르기 - 한글깨지지않게
  // 2016-05-11 강대인
  function cutByte(str,len)
  {
    var count = 0;

    for(var i = 0; i < str.length; i++) {
      if(escape(str.charAt(i)).length >= 4)
        count += 2;
      else
        if(escape(str.charAt(i)) != "%0D")
          count++;


      if(count >  len) {
        if(escape(str.charAt(i)) == "%0A")
          i--;
        break;
      }
    }
    return str.substring(0, i);
  }

}