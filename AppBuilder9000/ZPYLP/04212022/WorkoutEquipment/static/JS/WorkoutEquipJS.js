//THIS FUNCTION DISPLAYS THE 1ST IMG IN THE SLIDESHOW WHEN PAGE LOADS*/
var slideIndex = 1;
showSlides(slideIndex);

function plus_slides(n) {
    showSlides(slideIndex +=n);
}

//THIS FUNCTION CHANGES THE SLIDE WHEN THE DOTS ARE CLICKED
function current_slide(n) {
    showSlides(slideIndex = n);
}
//THIS FUNCTION CREATES SLIDESHOW BY USING CONDITIONAL STATEMENTS AND FOR LOOPS
function showSlides(n) {
    var slides = document.getElementsByClassName("mySlides"); // THIS TAKES ALL ELEMMTS WITH THE CLASS NAME "mySlides" STORES IN VARIABLE ARRAY "slides"
    var dots = document.getElementsByClassName("dot"); // STORES IN VARIABLE ARRAY "dots"
    if(n > slides.length) {slideIndex = 1}; // If n (the number passed into a function) is greater than the length of the array "slides" , the slideIndex is set to 1
  // this (above) also resets the img to the first image in array on users screen when you've clicked nxt through every img/slide.
    if(n < 1) {slideIndex = slides.length}; // if n (the number passed into a function) is less than 1, the slideIndex is set to the length of the array "slides"
    for(i = 0; i < slides.length; i++) {
        slides[i].style.display = "none" // This for loop takes each item in the array "slides" and sets the display to none
    }
    for(i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active",""); //THIS FOR LOOP TAKES EACH ITEM IN THE ARRAY "dots" AND REMOVES "active" WHICH REMOVES THE ACTIVE STYLING
    }
    slides[slideIndex - 1].style.display = "block"; // THIS DISPLAYS THE IMG IN SLIDESHOW
    dots[slideIndex -1 ].className += " active"; // THIS ADDS THE ACTIVE STYLING TO THE DOT ASSOCIATED WITH THE IMG
}