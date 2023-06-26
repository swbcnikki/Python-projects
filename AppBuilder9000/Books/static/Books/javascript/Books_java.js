const text = document.querySelector(".fancy");
const strText = text.textContent;
const splitText = strText.split("");
text.textContent = "";
for(let i = 0; i < splitText.length; i++){
    text.innerHTML += "<span>" + splitText[i] + "</span>";
}

let char = 0;
let timer = setInterval(onTick, 50);

function onTick(){
    const span = text.querySelectorAll('span')[char];
    span.classList.add('fancier');
    char++
    if(char === splitText.length){
        complete()
        return;
    }
}

function complete(){
    clearInterval(timer);
    timer = null;
}

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
}