var filledHeart = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
</svg>`

var emptyHeart = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
    <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
</svg>`

$(window).on('load', function() {
	$("body").removeClass('fade-out')
});

$("#delete-game-button").on('click', function(){
    return confirm('Are you sure you want to delete this game?')
})

$("#pull-from-bgg").on('click', function() {
    // I really wanted to use python for this, and the code was _relatively_ easier, but I decided it was
    // very important in terms of flow to have this functionality client-side.
    // gameid is the unique value used by Board Game Geek to identify a board game.
    var gameid = prompt("Enter the gameid for the game you would like to pull.\nThis is an integer between one and six digits.\nOnce you find the game on https://www.boardgamegeek.com,\nthe page for the game is in the following format:\nhttps://boardgamegeek.com/boardgame/<gameid>/<name>", "")

    //Ensuring the given value for gameid is a positive integer with equal to or less than six digits.
    if (parseInt(gameid) && parseInt(gameid) > 0 && gameid.length <= 6) {
        // Instructions for the API are here: https://boardgamegeek.com/wiki/page/BGG_XML_API2
        var url = "https://api.geekdo.com/xmlapi2/thing?thing=boardgame&id=" + gameid
        // $.ajax is a jQuery function used for pulling JSON or XML data from an API.
        $.ajax({
            url: url,
            dataType: 'xml',
            success: function(xml) {
                // Determining these values was a several hours long process of trial and error and frustration.
                // And searching Google (and primarily Stack Overflow) for help was mostly fruitless.
                $("#id_Description").val($(xml).find('description').eq(0).text())
                $("#id_Image").val($(xml).find('image').eq(0).text())
                $("#id_Thumbnail").val($(xml).find('thumbnail').eq(0).text())

                // When I finally determined what to do for image, thumbnail, and description, I tried .attr().  No luck.
                // Searching through the object I found the attributes node had the data I needed.
                // By sheer luck, adding .value got the data I needed.
                $("#id_Name").val($(xml).find('name').eq(0)[0].attributes['value'].value)
                $("#id_Year").val($(xml).find('yearpublished').eq(0)[0].attributes['value'].value)

                // There was a Stack Overflow entry for working with Python that helped me with searching by attribute.
                //     It was really helpful for finding the publisher.  In JavaScript I needed to remove the @ sign.
                $("#id_Publisher").val($(xml).find('link[type="boardgamepublisher"]').eq(0)[0].attributes['value'].value)
            }
        })
    }
})

//I copied the general layout of this function from the one above.
//To get access to the url I added it as a data attribute.
//
$(".toggleFavorite").on("click", function (e) {
    var id = $(this).data('id')
    $.ajax({
        type: 'POST',
        url: $(this).data('href'),
        data: {
            'id': id,
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
        success: function(data) {
            $(`#${id} .toggleFavorite`).html(data.value ? filledHeart : emptyHeart)
            var container = $('#container')
            if (container) { //Don't sort if there's no container (it's the details page)
                var cards = container.children().detach()  //detach so this event doesn't get lost
                cards.sort(function(a, b) {  //Sort the cards by favorite then by name then by id
                    //Value of xFavorite is true if it has the bi-heart-fill class, false if not
                    var aFavorite = $(a).find(".favorite svg").hasClass('bi-heart-fill')
                    var bFavorite = $(b).find(".favorite svg").hasClass('bi-heart-fill')
                    var aId = $(a).attr('id')
                    var bId = $(b).attr('id')
                    var aName = $(a).find(".card-title").text()
                    var bName = $(b).find(".card-title").text()
                    //The way sort works, -1 means a comes before, 0 means they're equal, and 1 means it goes after.
                    //Because I use the id, it should never return 0, but the ternary operator requires an else.
                    return ((aFavorite === true && bFavorite === false) ||                   //a comes first if it's favorited and b isn't,
                            (aFavorite === bFavorite && aName.localeCompare(bName) == -1) || //favorite is equal but it's name comes first,
                            (aFavorite === bFavorite && aName === bName && aId < bId)) ? -1  //or their names are equal and it's id comes first
                         : ((aFavorite === false && bFavorite === true) ||                   //b comes first if it's favorited and a isn't,
                            (aFavorite === bFavorite && aName.localeCompare(bName) == 1) ||  //favorite is equal but it's name comes first,
                            (aFavorite === bFavorite && aName === bName && aId > bId)) ? 1   //or their names are equal and it's id comes first
                         : 0
                })
                //Append all the detached and sorted items to the container.
                $.each(cards, function(idx, itm) { container.append(itm) })
            }
        },
        error: function (error) {
            console.log(error)
        }
    })
})

//This was copied from https://www.erickmccollum.com/2020/12/19/use-django-csrf-ajax.html.  It's on several pages.
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}