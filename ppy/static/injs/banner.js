/**
 * Created by hucx on 16/4/10.
 */

$(document).ready(function () {
    var tag = $("#tagdiv").text();
    var tagaction = $("#tagactiondiv").text();
    var bannerId = $("#bannerId").text();
    if (tagaction == "") {
        console.log("ready get first request")
        if (tag == "mainbanner") {
            mainbannerRequest();
        }
        if (tag == "forumbanner") {
            forumbannerRequest();
        }
    }else{
        console.log("ready get first request ===")
        console.log("ready get first request")
        console.log(bannerId)

        if(bannerId != ""){
            selectBanner(bannerId);
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
    window.location.href = "/banner/banners_page/" + tag + "/newbanner"
}

//js edit banner
function selectBanner(bannerId) {
     var tag = $("#tagdiv").text();
     if (tag == "mainbanner") {
         $.getJSON($SCRIPT_ROOT + '/mainbanneredit/' + bannerId , {}, function (d) {
             $("#bId").val(d.data["bannerId"])
             $("#bannerName").val(d.data["bannerName"])
             $("#bannerImageUrl").attr("src",d.data["imageUrl"])
             $("#bannerUrl").val(d.data["bannerUrl"])
             $("#BannerState").val(d.data["bannerIsDelete"]?1:0)
         });
     }

    if (tag == "forumbanner") {
        $.getJSON($SCRIPT_ROOT + '/forumbanneredit/' + bannerId , {}, function (d) {
             $("#bId").val(d.data["bannerId"])
             $("#bannerName").val(d.data["bannerName"])
             $("#bannerImageUrl").attr("src",d.data["imageUrl"])
             $("#bannerUrl").val(d.data["bannerUrl"])
             $("#BannerState").val(d.data["bannerIsDelete"]?1:0)
         });
    }



}


function editBanner(bannerId) {
    //editBanner
    //banner/banners_page/{{ tag }}/editbanner
    var tag = $("#tagdiv").text();
    window.location.href = "/banner/banners_page/" + tag + "/"+ "editbanner" +"/" + bannerId;
}



// js delete banner
function deleteBanner(bannerId) {
     var tag = $("#tagdiv").text();
     if (tag == "mainbanner") {
         $.getJSON($SCRIPT_ROOT + '/mainbannerdelete/' + bannerId , {}, function (data) {
             deleteBanaerCallBack(data.code)
         });
     }
     if (tag == "forumbanner") {
         $.getJSON($SCRIPT_ROOT + '/forumbannerdelete/' + bannerId , {}, function (data) {
             //alert(data.code);
             deleteBanaerCallBack(data.code)
         });
     }
}

function deleteBanaerCallBack(code) {
    //alert(data.code);
    var tag = $("#tagdiv").text();
    if(code == "000000"){
        window.location.href = "/banner/banners_page/" + tag
        // $('#successModel').modal({
        //     keyboard: true
        // });
    }else{
        $('#failureModel').modal({
            keyboard: true
        });
    }
}

//js submit form
//$("#submitBtn").on("click", js_submitForm);
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
 