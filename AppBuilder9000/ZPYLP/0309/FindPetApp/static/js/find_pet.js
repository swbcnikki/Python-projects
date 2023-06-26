// Handles modal
var modal = document.getElementById("delete_modal");

var btn = document.getElementById("open_modal");

var span = document.getElementById("close");

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}