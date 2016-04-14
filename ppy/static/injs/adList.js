/**
 * Created by hucx on 16/4/9.
 */
$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "") {
        console.log("ready get first request")
        adsRequest(1);
    }

   //
});

$("#option1").on("click", globalAds);
$("#option2").on("click", allAds);


function globalAds(e) {
    console.log("globalAds");
    adsRequest(0)
    return e.preventDefault();
}
function allAds(e) {
    console.log("allAds");
    adsRequest(1)
    return e.preventDefault();
}





function adsRequest(adPlace) {
    $.getJSON($SCRIPT_ROOT + '/adlist', {
        adPlace: adPlace,
    }, function (data) {
        renderEngine(data)
    });
}


function renderEngine(json) {
    var source = $("#ad-show-template").html();
    var template = Handlebars.compile(source);

    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    console.log("ad context");
    console.log(html);

    $('.tbodycontent').html(html)
}


// js new ad
function js_newadd() {
    console.log("js_newadd")
    window.location.href="/ad/ads/newad"
}