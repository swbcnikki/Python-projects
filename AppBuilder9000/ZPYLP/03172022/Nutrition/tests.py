from django.test import TestCase

# Create your tests here.

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Account, PersonalizedNutrition
from .forms import AccountForm, NutritionalQuery
import requests
import json
from bs4 import BeautifulSoup
import pprint
# Create your views here.

api_version = 'v2'
api_base_url = f'https://trackapi.nutritionix.com/{api_version}'
endpoint_path = f'/natural/nutrients'
endpoint = f'{api_base_url}{endpoint_path}'
query = request.GET['user_query']
# requests.post accepts 'headers' as an argument.
# we provide api credentials, as specified in the API documentation, in 'headers'
headers = {
    'x-app-id': '212b5e6c',
    'x-app-key': 'bcfd3f08c16996662783976a3b37793a',
    # remote-user-id is used for billing purposes, but this isn't relevant so
    # api told us to use '0' as a value to disregard.
    'x-remote-user-id': '0'
}

# the API specified that we need to provide 'query' and 'timezone' key/value pairs.
# this is stored as a dictionary in variable 'data', an argument that requests.post
# can accept (requests.post can only accept certain arguments per its documentation)
data = {
    "query": query,

}

# api stated this endpoint requires a POST request.
# the 'endpoint' argument stores the precise URL endpoint
# the 'headers' argument stores API credentials (keys)
# the 'data' argument is what stores the actual query itself
a_request = requests.post(endpoint, headers=headers, data=data)

# prints a status code to verify our request was successful
print(a_request.status_code)

# calls our pprint function, imported from pprint, printing JSON neatly in terminal for legibility
# the purpose is to show ALL the data the API sends us, in contrast to what we end up with through filtering


# the below function filters JSON response data to include only nutritional info
# all nutritional info in JSON response starts with 'nf_', hence we targeted only KVPs with 'nf_'' in the key
if a_request.status_code in range(200, 299):
    data = a_request.json()
    results = data['foods']
    search_key = 'nf_'
    out = {}
    for i in results:
        if not isinstance(i, dict):
            continue
        for k, v in i.items():

            if search_key in k:
                out[k] = v
            nutrients_dict = out

