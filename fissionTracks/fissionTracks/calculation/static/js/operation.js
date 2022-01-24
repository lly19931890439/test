$(document).ready(function() {
	//重新设置按钮-default
	$("#reset").click(function () {
		$("#zetaVal").val("350");
		$("#zetaErr").val("10");
		$("#standAgeVal").val("100");
		$("#standAgeErr").val("1");
		$("#rhoDval").val("2500000");
		$("#rhoDerr").val("10000");
	});
	//清空数据按钮-clear
	$('#clear').click(function () {
		sheet.clear(0, 0, sheet.getRowCount(), sheet.getColumnCount(), GC.Spread.Sheets.SheetArea.viewport, GC.Spread.Sheets.StorageType.data);
	});
	
	//控制按钮run（要保证把getzeta.js和getages.js放在operation.js的前面引用）
	$("#run").click(function(){
		var myselect=document.getElementById("control_display")
		var index=myselect.selectedIndex; 
		var val=myselect.options[index].value;
		if(val=="get ζ"){
			calzeta();
		}
		else if(val=="ages"){
			calages();
		}
	})
	
});


