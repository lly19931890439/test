GC.Spread.Common.CultureManager.culture('zh-cn');
window.parent.GC = GC;
var rightspread = new GC.Spread.Sheets.Workbook(document.getElementById('rightsheet'));
window.parent.spread = rightspread;
var rightsheet = rightspread.getActiveSheet();
