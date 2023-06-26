import requests
import json
from itertools import chain
import os
import webbrowser

# Get Personal API Token from https://lichess.org/account/oauth/token
# you only need the puzzle option enabled; see https://en.wikipedia.org/wiki/Principle_of_least_privilege
# Store in Environment Variable for safe keeping (do NOT commit this to source control or others will be able to use it)
startFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'


def request_lichess(fen):
    api_key = 'lip_q9Y0nx9iRSGx2K6iUAnd'

    # Make GET request to Lichess API
    resp = requests.get(
        'https://explorer.lichess.ovh/masters',
        params={
            'fen': fen,
            'topGames': 5,

        },
        headers={
            'Authorization': f'Bearer {api_key}'  # Need this or you will get a 401: Not Authorized response
        }
    )

    # Parse application/x-ndjson into list of JSON objects

    resp_json = []
    ndjson = resp.content.decode().split('\n')
    print(resp.headers["content-type"])
    for json_obj in ndjson:
        if json_obj:
            resp_json.append(json.loads(json_obj))

    # Get first (most recently completed) puzzle in resp
    games_obj = resp_json[0]
    top_games = games_obj['topGames']
    # Open puzzle in web browser
    games_list = []

    for obj in top_games:
        game_resp = requests.get(
            'https://lichess.org/game/export/{}'.format(obj['id']),
            params={

                'clocks': False,
                'evals': False,

            },
            headers={"accept": "application/json"} # Need this or you will get a 401: Not Authorized response

        )

        # game_string = game_resp.content
        # game_info = json.loads(game_resp.text)
        # games_list.append(game_info)
        # print(game_resp.text)
        #print(game_resp.headers["content-type"])
        resp_json = []
        ndjson = game_resp.content.decode().split('\n')
        #print(resp.headers["content-type"])
        for json_obj in ndjson:
            if json_obj:
                resp_json.append(json.loads(json_obj))
        games_list.append(resp_json)


    return games_list



def parse_response(fen):
    model_format = {}
    lst = request_lichess(fen)
    count = 0
    for item in lst:
        model_format[count] = {"playerWhite": item[0]['players']['white']['name'],
                               "playerBlack": item[0]['players']['black']['name'],

                               "opening": item[0]['opening']['name'],
                               "PGN": item[0]['moves']}
        if item[0]['status'] == 'draw':
            model_format[count]['winner'] = 'draw'
        else:
            model_format[count]['winner'] = item[0]['winner']
        count += 1

    return model_format




if __name__ == "__main__":
    print(request_lichess(startFen))
