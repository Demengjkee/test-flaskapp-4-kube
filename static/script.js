"use strict";

function submit(path) {
    var baseUrl = window.location.href;
    var url = baseUrl + path;
    console.log(url);
    $.ajax({
        url: url,
        method: "POST"
    })
    .always(function(resp) {
        console.log(resp);
    });
}

function msg() {
    console.log("message sent");
    var reqPath = "break";
    submit(reqPath);
}
