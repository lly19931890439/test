function ctr_dispaly(obj){	
	$("#parameter").css('display', 'block');
	$("#rightsheet").css('display', 'none');
	$("#img_diaplay").css('display', 'none');

	var method_myselect=document.getElementById("control_method");
	var method_index=method_myselect.selectedIndex; 
	var method_val=method_myselect.options[method_index].value;
	var display_val=$(obj).val();
	
	if(display_val=="radial plot" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'block');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'block');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="radial plot" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'block');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'block');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="radial plot" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'block');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="KDE" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'block');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="KDE" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'block');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="KDE" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="get ζ" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'block');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="get ζ" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'block');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="get ζ" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'block');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="ages" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'block');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="ages" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'block');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="ages" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else{
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
}

function ctr_method(obj){
	$("#parameter").css('display', 'block');
	$("#rightsheet").css('display', 'none');
	$("#img_diaplay").css('display', 'none');
	
	var display_myselect=document.getElementById("control_display");
	var display_index=display_myselect.selectedIndex; 
	var display_val=display_myselect.options[display_index].value;
	var method_val=$(obj).val();
	
	if(display_val=="radial plot" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'block');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'block');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="radial plot" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'block');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'block');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="radial plot" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'block');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="KDE" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'block');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="KDE" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'block');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="KDE" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="get ζ" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'block');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="get ζ" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'block');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="get ζ" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'block');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="ages" && method_val=="EDM"){
		$("#zetaDiv").css('display', 'block');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'block');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="ages" && method_val=="ICP (ζ)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'block');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
	else if(display_val=="ages" && method_val=="ICP (absolute)"){
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'block');
		$("#mineral").css('display', 'block');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'block');
		$("#rightsheet").css('display', 'none');
	}
	else{
		$("#zetaDiv").css('display', 'none');
		$("#standAgeDiv").css('display', 'none');
		$("#rhoDdiv").css('display', 'none');
		$("#M_zetaDiv").css('display', 'none');
		$("#spot_size").css('display', 'none');
		$("#mineral").css('display', 'none');
		$("#transformation").css('display', 'none');
		$("#moredata").css('display', 'none');
		$("#rightsheet").css('display', 'none');
	}
}