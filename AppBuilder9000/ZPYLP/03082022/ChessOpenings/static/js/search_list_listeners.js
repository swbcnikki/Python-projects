
document.querySelectorAll('#searchTable tr')
.forEach(e => e.addEventListener("click", function() {
    // Here, `this` refers to the element the event was hooked on
    console.log("clicked")
}));