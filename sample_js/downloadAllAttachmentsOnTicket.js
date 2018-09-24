// これをIEのコンソールに貼りつけると、ダウンロードダイアログがどんどん出てくるので保存をクリックしまくる。
// IE限定 ∵ msSaveBlobを使っているため。書き換えればChromeでも動くと思う

// See also:
//   https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-issue-attachments/
//   https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-attachment/

+function() {
    var apiKey = "zU8GRPkgJKXFGxjPxnahDMelh04l9w5jGb98oTJ5MBKIAyKu7l4Qt7dDFknDscqG";
    var baseURL = "https://tss-otc.com/backlog";

	var downloadAttachment = function(ticketId) {
		return function(e){
			console.dir(e);
			var xhr2 = new XMLHttpRequest();
			xhr2.open('GET', baseURL + "/api/v2/issues/" + ticketId + "/attachments/" + e.id + "?apiKey=" + apiKey, false);
			xhr2.responseType = "blob";
			xhr2.onreadystatechange = function() {
				if(this.readyState != xhr2.DONE) return;
				if(this.status != 200 ) { console.dir(this); return; }
				blob = this.response;
				console.dir(blob);
				window.navigator.msSaveBlob(blob, ticketId + "_" + e.id + "_" + e.name); 
			};
			xhr2.send();
		};
	};

    var listAttachment = function(ticketId) {
		var xhr = new XMLHttpRequest();
		xhr.open('GET', baseURL + "/api/v2/issues/" + ticketId + "/attachments" + "?apiKey=" + apiKey);
		// xhr.responseType = "blob";
		xhr.onreadystatechange = function() {
			if(this.readyState != xhr.DONE) return;
			if(this.status != 200 ) { console.dir(this); return; }
			response = eval(this.response);
			if(response.length == 0) {
				console.log(ticketId + " has no attachments. skipped.");
			} else {
				[].forEach.call(response, downloadAttachment(ticketId));
			}
		};
		xhr.send();
    };
	
	for (i=1; i<=658; i++) {
		listAttachment("OTC-" + i);
	}
}();