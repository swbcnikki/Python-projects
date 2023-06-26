//Alright! This function will grab whatever the user enters into the box and try to grab the appropriate Steam Game with it!
//I'm adding some error validation, as STEAM only allows for numeric characters. I'm using the Number() function to grab
//any answers that don't contain just numbers. With Number(), though, I have to add validation for blank entries.
function SteamGameIDCall() {
    //First we grab the user's entry
    SGID = document.getElementById("SteamGameID").value
    //Then we ensure that the user didn't leave the box blank
    if (SGID == "") {
        alert("Please enter a number into the box below to find a Steam game's info.")
    }
    else {
        number_SGID = Number(SGID)
        //This validates whether or not the user entry is actually a number!
        if (Number.isNaN(number_SGID)) {
            //alert("that's not a number!")
        }
        else
        {
            //alert("That is a number!")

            /*
            Ok the original idea was to use JS to send out an XMLHttpRequest to the Steam server. If it pinged a 200, it would call
            the appropriate URL. Unfortunately, as we are in a private/test server and not actually online, I'm encountering the:

            Access to XMLHttpRequest at 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=xml'
            from origin 'http://127.0.0.1:8000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin'
            header is present on the requested resource.

            From my research, this CORS policy is stopping the local server. As a result, I'll keep this code below in case if
            another solution pops up, but I think I'll just modify my views call instead.


            var request = new XMLHttpRequest()
            request.open('GET', "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=xml")
            request.send()
            alert(request.status)
            */

            //Here we should call the api. If we get a 200, we'll load the page. Otherwise, we'll have the user try again.
            window.location.href = "../" + SGID + "/SteamAPITest/";

        }
    }


}