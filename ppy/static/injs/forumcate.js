/**
 * Created by hucx on 16/4/12.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "") {
        forumcateRequest(0);
    }


});


function forumcateRequest(parentid) {
    $.getJSON($SCRIPT_ROOT + '/forumcatelist', {
        parentid:parentid
    }, function (data) {
        renderEngine(data)
    });
}

function renderEngine(json) {
    var source = $("#forumcate-show-template").html();
    var template = Handlebars.compile(source);

    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    $('.tbodycontent').html(html)
}


// js new article
function js_newforumcate() {
    console.log("js_newforumcate")
    window.location.href="/find/forumcate_page/newforumcate"
}

function js_subForumCate() {
    console.log("js_subForumCate")
    forumcateRequest(1)
}