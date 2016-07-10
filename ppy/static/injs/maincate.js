/**
 * Created by hucx on 16/4/12.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    var categoryId = $("#categoryId").text();
    if (tagaction == "") {
        maincate();
    }else{
        if(categoryId != ""){
            selectCategory(categoryId);
        }
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


//根据id查询分类
function  selectCategory(categoryId) {
     $.getJSON($SCRIPT_ROOT + '/maincateedit/' + categoryId , {}, function (d) {
          console.log(d)
          $("#cId").val(d.data["categoryId"])
          $("#maincateName").val(d.data["name"])
          $("#categoryImageUrl").attr("src",d.data["imageUrl"])
     });
}





//edit Main Category
function editMainCategory(categoryId) {
    window.location.href = "/find/maincate_page" + "/"+ "editmaincate" +"/" + categoryId;
}





//delete category
function deleteCategory(categoryId) {
     $.getJSON($SCRIPT_ROOT + '/maincatedelete/' + categoryId , {}, function (data) {
             deleteMainCategoryCallBack(data.code)
     });
}

function deleteMainCategoryCallBack(code) {
    //alert(data.code);
    if(code == "000000"){
        window.location.href = "/find/maincate_page"
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
function js_newmaincate() {
    console.log("js_newarticle")
    window.location.href="/find/maincate_page/newmaincate"
}
//$("#submitBtn").on("click", js_submitForm);
function js_submitForm() {
    var tag = $("#tagdiv").text();
    console.log(tag)
    document.all.bannerForm.action="/maincatesubmit";
    document.all.bannerForm.submit();

}