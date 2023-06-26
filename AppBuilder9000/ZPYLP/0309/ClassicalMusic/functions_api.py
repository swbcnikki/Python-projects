from django.contrib import messages

import requests
import math

from . import functions


def ClassicalMusic_api_get_details_musician(request, MBID):
    # this is called a browse in MusicBrainz documentation.
    # I used a browse becuase a lookup limits the number of works to 100 max.
    # A browse does not inlcude artist information so I get that from the session.
    recordings = []  # initialize here in case API fails
    pages = 1  # initialize here in case API fails
    limit = 25
    page = 1
    if request.method == 'POST':
        page = int(request.POST.get("page"))
    offset = (page - 1) * limit
    headers = {
        # 'Accept': 'application/json',
        'User-Agent': 'ClassicalMusic ( catharinavanveen.com )'
    }
    parameters = {
        'artist': MBID,
        'limit': limit,
        'offset': offset,
        'fmt': 'json'
    }
    try:
        # for testing of redirect to previous, create typo in the url below
        response = requests.get("https://musicbrainz.org/ws/2/recording?", headers=headers, params=parameters)
        if response.status_code == 200:
            data = response.json()
            try:
                number_recordings = data['recording-count']
                pages = math.ceil(number_recordings / limit)
                recs = data['recordings']
                for rec in recs:
                    try:
                        recording = {'MBID': rec['id'], }
                        try:
                            recording['title'] = rec['title']
                        except:
                            pass
                        try:
                            recording['disambiguation'] = rec['disambiguation']
                        except:
                            pass
                        try:
                            recording['length'] = functions.timeformat(rec['length'])
                        except:
                            pass
                        recordings.append(recording)
                    except:  # there is no essential info on the recording
                        pass
            except:
                pass
        else:  # No status code of 200
            messages.add_message(request, messages.ERROR, "No recordings were found in MusicBrainz templates.")
    except:
        messages.add_message(request, messages.ERROR, "The MusicBrainz templates is not available for searching recordings.")

    return recordings, pages, page

