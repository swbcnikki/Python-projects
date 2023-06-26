from . import lichessAPI

startFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'


def parse_response(fen):
    model_format = {}
    lst = lichessAPI.request_lichess(fen)
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
    print(parse_response(startFen))
