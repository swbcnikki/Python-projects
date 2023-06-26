// HOW TO ADD ACTIVE STYLING TO NAV BUTTONS WHEN CLICKED

// get the navbar container

var navContainer = document.getElementById("nav_id");

// get all nav links with class="navbar_item" inside the container

var items = navContainer.getElementsByClassName("navbar_item");

// loop through the buttons and find the active class to the current/clicked button

for (var i = 0; i < items.length; i++) {
    items[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

