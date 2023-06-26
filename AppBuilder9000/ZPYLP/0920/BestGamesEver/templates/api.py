from django.shortcuts import render
import request





    conn = http.client.HTTPSConnection("rawg-video-games-database.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com",
        'x-rapidapi-key': "175c9ae68bmsh71be1c3c47d33c3p185fbejsne41564902858"
    }

    conn.request("GET", "/games/%7Bgame_pk%7D", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))7rnk73s8w0iwscj2w3mps9xptbaoj&client_secret=vc0tey9xrcrl2io8z8jx64etu3l1to&grant_type=client_credentials')