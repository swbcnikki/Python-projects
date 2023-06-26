/* toggle for responsive navigation */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
  }
}

function myFunction_show() {
    var x = document.getElementById("hide");
    if (x.style.display === "none") {
        x.style.display = "block";
    }else {
        x.style.display = "none";
    }
  }
