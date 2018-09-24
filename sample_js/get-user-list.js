// https://tss-otc.com/backlog/dashboard を開いて、F12をタイプし、コンソールに以下を貼り付けて「実行」することで
// 画面内にcsvを生成するので、コピペで取り出してください。

// See Also: https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-user-list/

// require "jquery.js"

+function() {
    var apiKey = "cSOrCzMHqO6Kbs2xoXJTs0kTmI9Qvlb1QiqDr4PzcJOke9SEFmzdCuJk6SrcyBjL";  // as user role
    var baseURL = "https://tss-otc.com/backlog";

    (baseURL + "/api/v2/users" + "?apiKey=" + apiKey)
    $.get(baseURL + "/api/v2/users" + "?apiKey=" + apiKey)
    .done(function(response) {\
        response = response.map(funct\\ion(e){return '"'+e.id+'","'+e.mailAddress+'","'+e.name+'"';});
        $('#contents').prepend("<pre>"+response.join("<br>")+"</pre>");
        console.log(response);
    });
}();
