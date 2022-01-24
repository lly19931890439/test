GC.Spread.Common.CultureManager.culture('zh-cn');
window.parent.GC = GC;
var spread = new GC.Spread.Sheets.Workbook(document.getElementById('ss'));
window.parent.spread = spread;
var sheet = spread.getActiveSheet();
function csvChange(){
	var file = document.getElementById('fileDemo').files[0]
	var reader = new FileReader()
	reader.readAsText(file,"UTF-8")
	reader.onload = function(e){
		var fileStr = e.target.result
		sheet.setCsv(0,0,fileStr,"\r\n",",")
	}
	reader.onerror = function(){
		console.log('error')
	}
	document.getElementById("fileDemo").value = "";
}
document.addEventListener('change',csvChange)

// 给Date添加format属性，设置日期格式
Date.prototype.format = function(fmt) {
     var o = {
        "M+" : this.getMonth()+1,                 //月份
        "d+" : this.getDate(),                    //日
        "h+" : this.getHours(),                   //小时
        "m+" : this.getMinutes(),                 //分
        "s+" : this.getSeconds(),                 //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt)) {
            fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    }
     for(var k in o) {
        if(new RegExp("("+ k +")").test(fmt)){
             fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
         }
     }
    return fmt;
}

// 下载csv文件保存
document.getElementById("saveExcel").onclick = function(){
var csv = sheet.getCsv(0, 0, sheet.getRowCount(), sheet.getColumnCount(), undefined, ",");
	console.log(csv)
	var file_name=new Date().format("yyyyMMddhhmmss") + '.csv';
	download(file_name, csv);
	// download();
}
// 试图使用node实现
// function download(){
// 	var fs = require("fs");
// 	let buffer='data:text/plain;charset=utf-8,' + encodeURIComponent(csv);
// 	fs.writeFile(`./文件名.csv`, buffer, function (err) {
// 		if (err)
// 			throw err;
// 		console.log('写入到文件结束.');
// 	});
// }

// download下载函数
function download(filename, text) {
	var pom = document.createElement('a');
	pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
	pom.setAttribute('download', filename);
	if (document.createEvent) {
		var event = document.createEvent('MouseEvents');
		event.initEvent('click', true, true);
		pom.dispatchEvent(event);
	} else {
		pom.click();
	}
}