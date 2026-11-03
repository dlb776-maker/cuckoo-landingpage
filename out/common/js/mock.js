/* Static stand-in for the original server's ajax: read-only calls load saved JSON from /mock, anything else goes to 404. */
(function ($) {
  var READ = ['term_select_box', 'term_list_table_adm', 'ajax_prod_term_info_hwi', 'ajax_rev_list_html'];
  $.post = function (url, data, cb, type) {
    var ep = String(url).split('?')[0].split('/').pop();
    var d = $.Deferred();
    if (READ.indexOf(ep) < 0) { location.href = '/404'; return d.promise(); }
    data = data || {};
    var k = Object.keys(data).sort().map(function (a) { return a + '=' + data[a]; }).join('&');
    var url2 = '/mock/' + ep + '/' + encodeURIComponent(encodeURIComponent(k)) + '.json';
    // a missing mock stays pending instead of failing, so pages never alert raw error HTML
    $.ajax({ url: url2, type: 'GET', dataType: type || 'text' }).done(function (r) { if (cb) cb(r); d.resolve(r); });
    return d.promise();
  };
})(jQuery);
