/**
 * Created by hucx on 16/4/12.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "") {
        maincate();
    }

});


function maincate() {
    $.getJSON($SCRIPT_ROOT + '/maincatelist', {
    }, function (data) {
        renderEngine(data)
    });
}

function renderEngine(json) {
    var source = $("#maincate-show-template").html();
    var template = Handlebars.compile(source);
    
    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    $('.tbodycontent').html(html)
}


// js new article
function js_newmaincate() {
    console.log("js_newarticle")
    window.location.href="/find/maincate/newmaincate"
}