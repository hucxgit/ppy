/**
 * Created by hucx on 15/1/1.
 */

$(document).ready(function () {
    var tagaction = $("#tagactiondiv").text();
    if (tagaction == "oneday") {
        statictisOneDay();
    }
    if (tagaction == "allday"){
        statictisAllDay();
    }


});

function sendMessage() {
    $('#sendMessageForm').submitForm({
            url: $SCRIPT_ROOT + "/sendMessages",
            dataType: "text",
            callback: function (data) {
                alert("success success");
            },
            before: function () {

            }
    }).submit();
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
