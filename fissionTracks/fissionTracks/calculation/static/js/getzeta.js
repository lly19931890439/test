function calzeta() {
    const xhttp = new XMLHttpRequest();
    var myselect=document.getElementById("sel_mineral");
    var index=myselect.selectedIndex; 
    var option_value=myselect.options[index].value;
	console.log("option_value");
	console.log(option_value);
	
    var data={
        'zetaVal': document.getElementById('zetaVal').value,
        'zetaErr': document.getElementById('zetaErr').value,
        'standAgeVal': document.getElementById('standAgeVal').value,
        'standAgeErr': document.getElementById('standAgeErr').value,
        'rhoDval': document.getElementById('rhoDval').value,
        'rhoDerr': document.getElementById('rhoDerr').value,
        'M_zetaVal': document.getElementById('M_zetaVal').value,
        'M_zetaErr': document.getElementById('M_zetaErr').value,
        'spot_size': document.getElementById('myspot_size').value,
        'input_errors': 1,
        'method': document.querySelector('#control_method').selectedIndex,
        //'sig': document.getElementById('sig').value,
		'sig':2,
        'mineral': option_value,
        'U238U235': document.getElementById('myU238U235').value,
        'errU238U235': document.getElementById('errU238U235').value,
        'LambdaU238': document.getElementById('myLambdaU238').value,
        'errLambdaU238': document.getElementById('errLambdaU238').value,        
        'LambdaFission': document.getElementById('myLambdaFission').value,
        'errLambdaFission': document.getElementById('errLambdaFission').value,
        'etchfact': document.getElementById('myetchfact').value,
        'tracklength': document.getElementById('mytracklength').value,
        'mindens': document.getElementById('mymindens').value,
        'mytable': sheet.toJSON().data.dataTable,
    }
    xhttp.onload = function(){
		$("#parameter").css('display', 'none');
		$("#img_diaplay").css('display', 'none');
        $("#rightsheet").css('display', 'block');
        let lst = [] 
		
		console.log(this.responseText);
        const obj = JSON.parse(this.responseText);  
        console.log(obj)
        for (const [key, value] of Object.entries(obj['mydata'])) {
          lst.push(value)
        }
        rightsheet.clear(0, 0, sheet.getRowCount(), sheet.getColumnCount(), GC.Spread.Sheets.SheetArea.viewport, GC.Spread.Sheets.StorageType.data);
        try {
            var table = rightsheet.tables.addFromDataSource(
              "Table1",
              0,
              0,
              lst,
              GC.Spread.Sheets.Tables.TableThemes.medium2
            );
            } catch (e) {
                alert(e.message);
            }      
        console.log('success')
    }
    xhttp.open("POST", "calzeta");
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
}
