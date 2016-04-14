$(document).ready(function () {
    reportListRequest(2);
});

$("#option1").on("click", healthShareClick);
$("#option2").on("click", anonymousQuestionClick);
$("#option3").on("click", allReportsClick);
//click event
function healthShareClick(e) {
    reportListRequest(0);
    return e.preventDefault();
}
function anonymousQuestionClick(e) {
     reportListRequest(1);
    return e.preventDefault();
}
function allReportsClick(e) {
    reportListRequest(2);
    return e.preventDefault();
}

//request
function reportListRequest(reportType) {
    $.getJSON($SCRIPT_ROOT + '/reportlist', {
        reportType: reportType,
    }, function (data) {
        renderEngine(data)
    });
}

function renderEngine(json) {
    var source = $("#report-show-template").html();
    var template = Handlebars.compile(source);

    //注册一个Handlebars Helper,用来将索引+1，因为默认是从0开始的
    Handlebars.registerHelper("addOne", function (index, options) {
        return parseInt(index) + 1;
    });
    var html = template(json);
    console.log("2 context");
    console.log(html);

    $('.tbodycontent').html(html)
}
