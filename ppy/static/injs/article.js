/**
 * Created by hucx on 16/4/10.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    var postid = $("#postiddiv").text();

    if (tagaction == "") {
        articleRequest(0);
    }else {
         if(postid != ""){
            selectPostInfo(postid);
         }else{
             CKEDITOR.replace('editorarticle')
         }
    }

});

$("#option1").on("click", MicroPopularScienceArticle);
$("#option2").on("click", warmstoryArticle);

function MicroPopularScienceArticle() {
    articleRequest(0)
}
function warmstoryArticle() {
    articleRequest(1)
}


function articleRequest(articleType) {
    $.getJSON($SCRIPT_ROOT + '/articlelist/'+articleType, {

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


//根据id查询分类
function  selectPostInfo(postid) {
     $.getJSON($SCRIPT_ROOT + '/articleedit/' + postid , {}, function (d) {
          console.log(d)
           $("#pId").val(d.data["postId"])
           $("#articleName").val(d.data["title"])
           $("#articleAuthor").val(d.data["author"])
           $("#articleDes").val(d.data["simpleContent"])
           $("#editorarticle").val(d.data["content"])
            CKEDITOR.replace('editorarticle')
     });
}

//edit Main Category
function editPostInfo(postId) {
    window.location.href = "/find/article_page" + "/"+ "editarticle" +"/" + postId;
}


//删除帖子
function deletePostInfo(postid) {
     $.getJSON($SCRIPT_ROOT + '/articledelete/' + postid , {}, function (data) {
             deleteCategoryCallBack(data.code)
     });
}

function deleteCategoryCallBack(code) {
    //alert(data.code);
    if(code == "000000"){
        window.location.href = "/find/article_page"
        // $('#successModel').modal({
        //     keyboard: true
        // });
    }else{
        $('#failureModel').modal({
            keyboard: true
        });
    }
}
 

// js new article
function js_newarticle() {
    console.log("js_newarticle")
    window.location.href="/find/article_page/newarticle"
}
 function js_submitForm() {
    var tag = $("#tagdiv").text();
    document.all.bannerForm.action="/articlesubmit";
    document.all.bannerForm.submit();

}
