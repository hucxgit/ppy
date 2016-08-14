/**
 * Created by hucx on 16/8/14.
 */
$(document).ready(function () {
   console.log("nav style js");
    navStyle();
});

function navStyle() {
    if($("#tagdiv").text()=="ads" || $("#tagdiv").text()=="forumbanner" || $("#tagdiv").text()=="mainbanner"){
        $("#yunying").attr("class","active");
    }else if ($("#tagdiv").text()=="article" || $("#tagdiv").text()=="maincate" || $("#tagdiv").text()=="forumcate" || $("#tagdiv").text()=="anony"){
        $("#find").attr("class","active");
    }else if ($("#tagdiv").text()=="reports"){
        $("#report").attr("class","active");
    }else if ($("#tagdiv").text()=="message"){
        $("#message").attr("class","active");
    }else if($("#tagdiv").text()=="image"){
        $("#image").attr("class","active");
    }
}



