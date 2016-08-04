function Greeting(){
	alert("Welcome to my portfolio! Enjoy.")
}

function bigImg(x){
	x.style.height = "768px";
	x.style.width = "1366px";
}

function normalImg(x) {
    x.style.height = "370px";
    x.style.width = "500px";
}

function moreInfo(){
	alert("I will be graduating high school in the spring of 2017. Most of the time I require caffeine (tea OR coffee, I don't discriminate) to function. I have one little sister. The TV show Sherlock owns my life.")
}

var slideIndex = 1;
function showDivs(n) {
	var i;
	var x = document.getElementsByClassName("slides");
	if (n > x.length) {slideIndex = 1}
	if (n < 1) {slideIndex = x.length}
	for (i = 0; i < x.length; i++) {
		x[i].style.display = "none";
	}
x[slideIndex-1].style.display = "block";
}

showDivs(slideIndex);

function plusdivs(n){
	showDivs(slideIndex += 1);
}
