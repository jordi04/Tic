
function sinus(cat_op, hip){

	resultat = cat_op/hip;
	console.log(resultat);
	console.log(cat_op, hip);

	if (cat_op >= hip) {
		document.getElementById('resultat').innerHTML = "El catet no pot ser igual o més gran que la hipotenusa";
	}
	else {
		resultat = parseFloat(resultat).toFixed(2);
		resultat = "El sinus és: "+ resultat;
		document.getElementById('resultat').innerHTML = resultat;
	}
}

function cosinus(cat_con, hip){

	resultat = cat_con/hip;
	console.log(resultat);
	console.log(cat_con, hip);

	if (cat_con >= hip) {
		document.getElementById('resultat').innerHTML = "El catet no pot ser igual o més gran que la hipotenusa";
	}
	else {
		resultat = parseFloat(resultat).toFixed(2);
		resultat = "El cosinus és: "+ resultat;
		document.getElementById('resultat').innerHTML = resultat;
	}
}

function tangent(cat_con, cat_op){

	resultat = cat_con/cat_op;
	console.log(resultat);
	console.log(cat_con, cat_op);

	resultat = parseFloat(resultat).toFixed(2);
	resultat = "La tangent és: "+ resultat;
	document.getElementById('resultat').innerHTML = resultat;
}