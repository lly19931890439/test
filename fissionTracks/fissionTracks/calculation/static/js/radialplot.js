function addElementImg(obj, src) {
    $("#rightsheet").css('display', 'none');
    // {#获取div元素#}
    var div = document.getElementById(obj);
    // {#创建img元素#}
    var img = document.createElement("img");
    // {#为img元素设置属性#}
    img.setAttribute("id", "radialImg");
	img.setAttribute("style", "padding-left:50px;");
    img.src = src ;
    // {#将新建的img元素加到div当中#}
    div.appendChild(img);
}

function dispimage(){
    const xhttp = new XMLHttpRequest();

    var myselect=document.getElementById("sel_mineral");
    var index=myselect.selectedIndex; 
    var option_value=myselect.options[index].value;

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
    xhttp.responseType = 'blob' ;
    xhttp.onload = function(){
		$("#parameter").css('display', 'none');
		$("#rightsheet").css('display', 'none');
		$("#img_diaplay").css('display', 'block');
        var blob = this.response;
        src = window.URL.createObjectURL(blob) ;
        addElementImg('img_diaplay', src) ;
    }
    xhttp.open("POST", "image");
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
}

document.getElementById('plot').onclick = dispimage;