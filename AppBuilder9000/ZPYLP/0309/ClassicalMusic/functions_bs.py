from django.contrib import messages

import requests

from bs4 import BeautifulSoup


# BEAUTIFUL SOUP

# this function prints the catalogues (title and url). It also returns the links to the pictures
def ClassicalMusic_soup_get_catalogues(request, MBID):
    catalogue_urls = []  # initialize here in case BS fails
    image_urls = []  # initialize here in case BS fails
    try:
        relationships_url = "https://musicbrainz.org/artist/{}/relationships".format(MBID)
        page = requests.get(relationships_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all_tr = soup.find_all('tr')
        catalogue_succes = False
        picture_success = False
        for tr in all_tr:
            try:
                if tr.th.text == "has catalogue:":
                    print("HAS CATALOGUE")
                    for a in (tr.td.find_all('a')):
                        catalogue_url = {
                            'title': a.text,
                        }
                        str = a.get('href')
                        if str.startswith('/'):
                            catalogue_url['link'] = "https://musicbrainz.org" + str
                        else:
                            pass
                        catalogue_urls.append(catalogue_url)
                    catalogue_succes = True
            except:
                pass
            try:
                if tr.th.text == "picture:":
                    for a in (tr.td.find_all('a')):
                        image_url = a.get('href')
                        if image_url.startswith('//commons.wikimedia.org/wiki'):
                            image_url_corrected = ClassicalMusic_soup_get_image_url(image_url)
                            image_urls.append(image_url_corrected)
                        else:
                            pass
                    picture_success = True
            except:
                pass
            if picture_success and  catalogue_succes:
                break
    except:
        messages.add_message(request, messages.ERROR, "The MusicBrainz is not available for searching details.")
    return catalogue_urls, image_urls

# this function returns the only the catalog names and the image urls
def ClassicalMusic_soup_get_compositions(request, MBID):
    # if request.method == 'POST', then the user is updating the recordings page, so BS should use the session data
    if request.method == 'POST':
        catalogues = request.session['catalogues']
        image_urls = request.session['image_urls']
    else:
        catalogue_urls,  image_urls = ClassicalMusic_soup_get_catalogues(request, MBID)
        catalogues = []
        for url in catalogue_urls:
            catalogue = {
                'title': url['title'],
            }
            catalogues.append(catalogue)

        request.session['catalogues'] = catalogues
        request.session['image_urls'] = image_urls
    return catalogues, image_urls

# # this function returns the catalogs (title and list of compositions). It also passes on the image urls
# def ClassicalMusic_soup_get_compositions(request, MBID):
#     # if request.method == 'POST', then the user is updating the recordings page, so BS should use the session data
#     if request.method == 'POST':
#         catalogues = request.session['catalogues']
#         image_urls = request.session['image_urls']
#     else:
#         catalogue_urls,  image_urls = ClassicalMusic_soup_get_catalogues(request, MBID)
#         catalogues = []
#         for url in catalogue_urls:
#             try:
#                 page = requests.get(url['link'])
#                 soup = BeautifulSoup(page.content, 'html.parser')
#                 all_tr = soup.find_all('tr')
#                 compositions = []
#                 for tr in all_tr:
#                     try:
#                         all_td = tr.find_all('td')
#                         composition = {'title': all_td[1].bdi.text}
#                         composition['opus'] = all_td[0].text
#                         composition['link'] = "https://musicbrainz.org" + all_td[1].a.get('href')
#                         compositions.append(composition)
#                     except:
#                         pass
#                 catalogue = {
#                     'title': url['title'],
#                     'compositions': compositions
#                 }
#                 catalogues.append(catalogue)
#             except:
#                 pass
#         request.session['catalogues'] = catalogues
#         request.session['image_urls'] = image_urls
#     return catalogues, image_urls
#
def ClassicalMusic_soup_get_image_url(image_url):
    page = requests.get("https:" + image_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    image_url_corrected = soup.select_one('div:is(.fullImageLink)').a.get('href')

    return image_url_corrected