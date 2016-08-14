/**
 * Created by hucx on 15/1/1.
 */

$(document).ready(function () {
    console.log("message ready go");
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "oneday") {
        statictisOneDay();
    }
    if (tagaction == "allday"){
        statictisAllDay();
    }

    /**
     * 绑定表单 提交事件
     */
    $('#sendMessageForm').bind('submit',sendMessage);


});


function sendMessage() {
    if(!checkParameter()){
        $('#parameterModel').modal({
        keyboard: true
        });
        return false;
    }
    ajaxSubmit(this, function(data){
        var obj = JSON.parse(data); //由JSON字符串转换为JSON对象
        alert(obj.respDesc);
    });
    return false;
}
function checkParameter() {
    exp=$("#messageTitle").val();
    if(!exp){
        return false;
    }
    exp = $("#messageContent").val();
    if(!exp){
        return false;
    }
    exp = $("#messageUrl").val();
    if(!exp){
        return false;
    }
    exp = $("#messageImageUrl").val();
    if(!exp){
        return false;
    }
    return true;
}

function statictisOneDay() {
    $.getJSON($SCRIPT_ROOT + '/oneday', {
    }, function (data) {
        renderEngine(data)
    });
}
function statictisAllDay() {
    $.getJSON($SCRIPT_ROOT + '/allday', {
    }, function (data) {
        renderEngine(data)
    });
}



function renderEngine(json) {
    var source = $("#message-show-template").html();
    var template = Handlebars.compile(source);

    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    $('.tbodycontent').html(html)
}
