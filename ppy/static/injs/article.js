/**
 * Created by hucx on 16/4/10.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "") {
        articleRequest(2);
    }

});

$("#option1").on("click", MicroPopularScienceArticle);
$("#option2").on("click", warmstoryArticle);
$("#option3").on("click", allArticle);

function MicroPopularScienceArticle() {
    articleRequest(0)
}
function warmstoryArticle() {
    articleRequest(1)
}
function allArticle() {
    articleRequest(2)
}

function articleRequest(articleType) {
    $.getJSON($SCRIPT_ROOT + '/articlelist', {
        articleType : articleType
    }, function (data) {
        renderEngine(data)
    });
}


function renderEngine(json) {
    var source = $("#article-show-template").html();
    var template = Handlebars.compile(source);

    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    $('.tbodycontent').html(html)
}

 

// js new article
function js_newarticle() {
    console.log("js_newarticle")
    window.location.href="/find/article_page/newarticle"
}
