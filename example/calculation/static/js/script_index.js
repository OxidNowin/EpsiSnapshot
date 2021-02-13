/*стрелкu*/
var count = document.getElementsByClassName('post_index').length;

for (var i = 0; i < count; i++) {
	var meter_needle =  document.querySelectorAll('#csi_index_meter_needle')[i];
	var slider1 = document.querySelectorAll('.csi_index #slider1')[i];
	var percent = slider1.value;
	percent = percent.replace("," , ".");
	
	if (percent>=55) {
		meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';
	}

	var meter_needle =  document.querySelectorAll('#loy_index_meter_needle')[i];
	var slider2 = document.querySelectorAll('.loy_index #slider2')[i];
	var percent = slider2.value;
	percent = percent.replace("," , ".");

	if (percent>=55) {
		meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';
	}
}
