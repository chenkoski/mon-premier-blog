


function myFunction1() {
    	document.getElementById("environnement").style.color = "red";
}


function myFunction() {
    document.getElementById("domaineCompetences").innerHTML = "Hello World";
}

function hideMeById (id){
 var x = document.getElementById(id);
   if (x.style.display === 'none') {
   	x.style.display = 'block';
   	 } else {
        x.style.display = 'none';
     }
}
function hideMeByClass (Klass){
 var x =document.getElementsByClassName(Klass)
  if (x[0].style.display === 'none') {
   	x[0].style.display = 'block';
   	 } else {
        x[0].style.display = 'none';
     }
}
