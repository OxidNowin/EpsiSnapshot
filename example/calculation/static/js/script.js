/*стрелка*/
var meter_needle =  document.querySelector('img#csi_meter_needle');
var slider1 = document.querySelector('.csi #slider1').value;
slider1 = slider1.replace("," , ".");
meter_needle.style.transform = 'rotate(' + (-150 + (Number(slider1)*3)) + 'deg)';

var meter_needle =  document.querySelector('#loy_meter_needle');
var slider2 = document.querySelector('.loy #slider2').value;
slider2 = slider2.replace("," , ".");
meter_needle.style.transform = 'rotate(' + (-150 + (Number(slider2)*3)) + 'deg)';

/* возрастание */
function reg_calc() {
	var loy_up = document.getElementById('loy_up');
	var csi_up = document.querySelector('.regress #csi_up').value;
	var coefa = document.querySelector('.regress #coefa').value;
	coefa = coefa.replace("," , ".");
	csi_up = csi_up.replace("," , ".");
	var res =  0;
	if (Number(csi_up) <= (100-Number(slider1)) && csi_up > 0) {
		res = Number(csi_up)*Number(coefa);
		loy_up.innerHTML='индекс лояльности изменится на '+res.toFixed(2)+' баллов';
	}
	else {
		alert("Введите значение в промежутке от 1 до " + (100-slider1).toFixed(1));
	}
}

