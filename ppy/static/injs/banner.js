/**
 * Created by hucx on 16/4/10.
 */

$(document).ready(function () {
    var tag = $("#tagdiv").text();
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "") {
        console.log("ready get first request")
        if (tag == "mainbanner") {
            mainbannerRequest();
        }
        if (tag == "forumbanner") {
            forumbannerRequest();
        }
    }

});

function mainbannerRequest() {
    $.getJSON($SCRIPT_ROOT + '/mainbannerlist', {}, function (data) {
        renderEngine(data)
    });

}

function forumbannerRequest() {
    $.getJSON($SCRIPT_ROOT + '/forumbannerlist', {}, function (data) {
        renderEngine(data)
    });
}

function renderEngine(json) {
    var source = $("#mainbanner-show-template").html();
    var template = Handlebars.compile(source);

    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    $('.tbodycontent').html(html)
}

// js new ad
function js_newBanner() {
    console.log("js_newBanner")
    var tag = $("#tagdiv").text();
    window.location.href = "/banner/banners/" + tag + "/newbanner"
}

//js submit form
$("#submitBtn").on("click", js_submitForm);
function js_submitForm() {
    var tag = $("#tagdiv").text();
    console.log(tag)


    if (tag == "forumbanner") {
        document.all.bannerForm.action="/forumbannersubmit";
        document.all.bannerForm.submit();
    } else {
        document.all.bannerForm.action="/mainbannersubmit";
        document.all.bannerForm.submit();
    }
}