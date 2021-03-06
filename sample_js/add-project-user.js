﻿// https://tss-otc.com/backlog/dashboard を開いて、F12をタイプし、コンソールに以下を貼り付けて「実行」することで
// ユーザを指定したプロジェクトに追加します。
// 結果は確認せずにバルク投入していますので、画面から確認してください。

// See Also: https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-project-user/

// require "jquery.js"

+function() {
    var apiKey = "RE1nBrY9d34HeBiUx1U8I4KhOUTmjzmBvssXIFJ3XM09dZxd15lfcrR2Oz3pELWC";  // as user role
    var baseURL = "https://tss-otc.com/backlog";
    var projectIdOrKey = "ALL";
    var UserIDToAdd = [
        "1","22","29","31","73","74",
        "116","139","156","166","169","170","171","183","184","189","190","191","195","196","197",
        "202","204","213","217","219","231","234","242","245","246","250","254","256","258","260",
        "261","262","265","266","267","270","272","277","278","283","287","297","298","299","300",
        "301","303","305","308","311","313","314","315","317","326","327","330","331","337","339",
        "342","343","344","345","346","347","350","356","357","361","362","363","366","367","368",
        "369","370","371","372","373","374","375","376","377","378","379","380","381","382","384",
        "385","386","387","388","389","390","391","394","395","396","397","398","400","408","410",
        "415","426","430","433","436","437","438","439","440","444","446","447","451","452","455",
        "456","457","460","461","463","464","465","467","469","470","471","472","474","479","482",
        "486","487","489","492","493","494","495","496","497","498","499","501","505","507","508",
        "509","511","519","520","522","523","524","525","526","527","528","540","541","555","557",
        "558","559","560","563","568","569","573","574","575","578","583","614","619","620","621",
        "622","623","624","626","632","633","634","635","636","637","638","639","640"
    ];

    UserIDToAdd.forEach(function(userid) {
        console.log(userid);
        $.post(baseURL + "/api/v2/projects/"+projectIdOrKey+"/users" + "?apiKey=" + apiKey, {"userId": userid})
        .done(function(response) {
            console.log(response);
        });
    });
}();

