function factorial (given){

given = parseInt(given);

let x = 1;
let y = [];
var quants=0;

for (var i = given; i > 0; i--) {
	quants++;
	x = x*i;
	y.push(i);


if (quants == 5){
	y.push("<br>");
	quants=0;
}
}
if (i == 0){
	y = y.toString();
	y = y.replace(/,/g, "x");
	z = given+"! ";
	print = z+"<br>= "+y+"<br>= "+x;
	document.getElementById("print").innerHTML = print;
}

}