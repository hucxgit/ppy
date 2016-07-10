/**
 * Created by hucx on 16/4/12.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    var categoryId = $("#categoryId").text();

    if (tagaction == "") {
        forumcateRequest(0);
    }else {
         if(categoryId != ""){
            selectCategory(categoryId);
         }
    }


});


function forumcateRequest(parentid) {
    $.getJSON($SCRIPT_ROOT + '/forumcatelist/'+parentid, {
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


//根据id查询分类
function  selectCategory(categoryId) {
     $.getJSON($SCRIPT_ROOT + '/forumcateedit/' + categoryId , {}, function (d) {
          console.log(d)
          $("#cId").val(d.data["categoryId"])
          $("#maincateName").val(d.data["name"])
          $("#categoryImageUrl").attr("src",d.data["imageUrl"])
     });
}



//edit Main Category
function editForumCategory(categoryId) {
    window.location.href = "/find/forumcate_page" + "/"+ "editmaincate" +"/" + categoryId;
}



//delete category
function deleteCategory(categoryId) {
     $.getJSON($SCRIPT_ROOT + '/forumcatedelete/' + categoryId , {}, function (data) {
             deleteCategoryCallBack(data.code)
     });
}

function deleteCategoryCallBack(code) {
    //alert(data.code);
    if(code == "000000"){
        window.location.href = "/find/forumcate_page"
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
function js_newforumcate() {
    console.log("js_newforumcate")
    window.location.href="/find/forumcate_page/newforumcate"
}

 function js_submitForm() {
    var tag = $("#tagdiv").text();
    document.all.bannerForm.action="/forumcatesubmit";
    document.all.bannerForm.submit();

}