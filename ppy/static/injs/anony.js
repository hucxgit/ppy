/**
 * Created by hucx on 16/4/12.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "") {
        anonyRequest(0);
    }


});


function anonyRequest(parentid) {
    $.getJSON($SCRIPT_ROOT + '/anonylist', {
        parentid: parentid
    }, function (data) {
        renderEngine(data)
    });
}

function renderEngine(json) {
    var source = $("#anony-show-template").html();
    var template = Handlebars.compile(source);

    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    $('.tbodycontent').html(html)
}


function js_subAnony() {
    console.log("js_subAnony");
    anonyRequest(1)
}
function js_newanony() {
    console.log("js_newanony");
    window.location.href = "/find/anony_page/newanony"

}


