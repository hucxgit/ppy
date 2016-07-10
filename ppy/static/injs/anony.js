/**
 * Created by hucx on 16/4/12.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    var categoryId = $("#categoryId").text();

    if (tagaction == "") {
        anonyRequest(0);
    }else {
         if(categoryId != ""){
            selectCategory(categoryId);
         }
    }


});


function anonyRequest(parentid) {
    $.getJSON($SCRIPT_ROOT + '/anonylist/'+parentid, {
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

//根据id查询分类
function  selectCategory(categoryId) {
     $.getJSON($SCRIPT_ROOT + '/annoyedit/' + categoryId , {}, function (d) {
          console.log(d)
          $("#cId").val(d.data["categoryId"])
          $("#maincateName").val(d.data["name"])
          $("#categoryImageUrl").attr("src",d.data["imageUrl"])
     });
}





//edit Main Category
function editCategory(categoryId) {
    window.location.href = "/find/anony_page" + "/"+ "editanony" +"/" + categoryId;
}




//delete category
function deleteCategory(categoryId) {
     $.getJSON($SCRIPT_ROOT + '/maincatedelete/' + categoryId , {}, function (data) {
             deleteCategoryCallBack(data.code)
     });
}

function deleteCategoryCallBack(code) {
    if(code == "000000"){
        window.location.href = "/find/anony_page"
        // $('#successModel').modal({
        //     keyboard: true
        // });
    }else{
        $('#failureModel').modal({
            keyboard: true
        });
    }
}



function js_subAnony() {
    var tag = $("#tagdiv").text();
    document.all.bannerForm.action="/anonysubmit";
    document.all.bannerForm.submit();
}
function js_newanony() {
    console.log("js_newanony");
    window.location.href = "/find/anony_page/newanony"

}