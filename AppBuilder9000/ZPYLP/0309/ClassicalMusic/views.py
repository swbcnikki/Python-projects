from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import formset_factory, modelformset_factory
from django.db.models import Prefetch, ProtectedError
from django.contrib import messages
from django import forms
from django.db.models.functions import Lower

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from urllib.request import urlopen
import datetime
import math
import requests

from .forms import NewMusicianForm, NewRoleForm, NewCompositionForm, NewMovementForm, NewReleaseForm, NewTrackForm, EditCompositionForm,EditReleaseForm, APINEWMusicianForm
from .models import Composition, Movement, Release, Musician, Track, Role
from . import functions, functions_bs as BS, functions_api as API
from .serializers import MusicianSerializer, CompositionSerializer, MusicianOptionsSerializer




# Create your views here.

def ClassicalMusic_home(request):
    musicians_query = Musician.objects.exclude(image_url="")
    musicians = []
    for i in range(len(musicians_query)):
        musician = {'index': i, 'name': musicians_query[i].name, 'image_url': musicians_query[i].image_url}
        print(musician)
        musicians.append(musician)

    return render(request, 'ClassicalMusic/ClassicalMusic_home.html', {'musicians': musicians})


#ADD FUNCTIONS

def ClassicalMusic_add_role(request):
    if request.method == 'POST':
        form = NewRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_show_roles')
    else:
        form = NewRoleForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_role.html', {'form': form})

def ClassicalMusic_add_musician(request):
    if request.method == 'POST':
        form = NewMusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_show_musicians')
    else:
        form = NewMusicianForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_musician.html', {'form': form})

def ClassicalMusic_add_composition(request):
    if request.method == 'POST':
        form = NewCompositionForm(request.POST)
        if form.is_valid():
            composition = form.save()
            number_movements = form.cleaned_data.get('number_movements'),
            request.session['number_movements'] = number_movements
            request.session['composition'] = composition.pk
            if number_movements[0] == 0: # number_movements is a tuple
                # if there are no movements, it will save one movement with the same title as the composition
                movement = Movement.objects.create(
                    title= composition,
                    composition=composition,
                    order_number=0,
                )
                return redirect('ClassicalMusic_show_compositions')
            return redirect('ClassicalMusic_add_multiple_movements')
    else:
        form = NewCompositionForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_composition.html', {'form': form})

def ClassicalMusic_add_multiple_movements(request):
    number_movements = request.session.get('number_movements')[0] # this is a list
    composition_pk = request.session.get('composition')
    composition = get_object_or_404(Composition, pk=composition_pk)
    NewMovementFormSet = formset_factory(NewMovementForm, extra=number_movements)
    if request.method == 'POST':
        formset = NewMovementFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
            return redirect('ClassicalMusic_show_compositions')
    else:
        formset = NewMovementFormSet()
        # set composition
        # hide composition field
    return render(request, 'ClassicalMusic/ClassicalMusic_add_multiple_movements.html', {'formset': formset, 'composition': composition})

def ClassicalMusic_add_additional_movement(request, pk):
    composition = get_object_or_404(Composition, pk=pk)
    if request.method == 'POST':
        form = NewMovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_details_composition', pk)
    else:
        form = NewMovementForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_additional_movement.html', {'form': form, 'composition': composition})

def ClassicalMusic_add_release(request):
    if request.method == 'POST':
        form = NewReleaseForm(request.POST)
        if form.is_valid():
            release = form.save()
            number_tracks = form.cleaned_data.get('number_tracks'),
            request.session['number_tracks'] = number_tracks
            request.session['release'] = release.pk
            return redirect('ClassicalMusic_add_tracks')
    else:
        form = NewReleaseForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_release.html', {'form': form})

def ClassicalMusic_add_track(request):
    if request.method == 'POST':
        form = NewTrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_show_releases')
    else:
        form = NewTrackForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_track.html', {'form': form})

def ClassicalMusic_add_tracks(request):
    number_tracks = request.session.get('number_tracks')[0] # this is a list
    release_pk = request.session.get('release')
    release = get_object_or_404(Release, pk=release_pk)
    NewTrackFormSet = formset_factory(NewTrackForm, extra=number_tracks)
    if request.method == 'POST':
        formset = NewTrackFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
            return redirect('ClassicalMusic_show_releases')
    else:
        formset = NewTrackFormSet()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_tracks.html', {'formset': formset, 'release': release})

def ClassicalMusic_add_additional_track(request, pk):
    release = get_object_or_404(Release, pk=pk)
    if request.method == 'POST':
        form = NewTrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_details_release', pk)
    else:
        form = NewTrackForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_add_additional_track.html', {'form': form, 'release': release})

def ClassicalMusic_add_default_data(request):
    role1 = Role.objects.create(role='Composer', type='individual', role_type='author_type')
    role2 = Role.objects.create(role='Lyricist', type='individual', role_type='author_type')
    role3 = Role.objects.create(role='Cello', type='individual', role_type='performer')
    role4 = Role.objects.create(role='Piano', type='individual', role_type='performer')
    role5 = Role.objects.create(role='Viola', type='individual', role_type='performer')
    role6 = Role.objects.create(role='Violin', type='individual', role_type='performer')
    role7 = Role.objects.create(role='Orchestra', type='ensemble', role_type='performer')
    role8 = Role.objects.create(role='Choir', type='ensemble', role_type='performer')
    role9 = Role.objects.create(role='Unused author', type='individual', role_type='author_type')
    role10 = Role.objects.create(role='Unused performer', type='individual', role_type='performer')

    role1_pk = role1.pk
    role2_pk = role2.pk
    role3_pk = role3.pk
    role4_pk = role4.pk
    role5_pk = role5.pk
    role6_pk = role6.pk
    role7_pk = role7.pk
    role8_pk = role8.pk

    musician1 = Musician.objects.create(name='Beethoven', type='individual', role=role1)
    musician2 = Musician.objects.create(name='Boston Symphony', type='ensemble', role=role7)
    musician3 = Musician.objects.create(name='Emmanuel Ax', type='individual', role=role4)
    musician4 = Musician.objects.create(name='Heifetz', type='individual', role=role6)
    musician5 = Musician.objects.create(name='Schiller', type='individual', role=role2)
    musician6 = Musician.objects.create(name='Shostakovich', type='individual', role=role1)
    musician7 = Musician.objects.create(name='Yo Yo Ma', type='individual', role=role3)
    musician8 = Musician.objects.create(name='Boston Choir', type='ensemble', role=role8)
    musician9 = Musician.objects.create(name='Unused Composer', type='individual', role=role1)
    musician10 = Musician.objects.create(name='Unused Cellist', type='individual', role=role3)

    musician1_pk = musician1.pk
    musician2_pk = musician2.pk
    musician3_pk = musician3.pk
    musician4_pk = musician4.pk
    musician5_pk = musician5.pk
    musician6_pk = musician6.pk
    musician7_pk = musician7.pk
    musician8_pk = musician8.pk




    composition1 = Composition.objects.create(title='Cello Concerto No. 1 in E-flat major, Op. 107')
    composition1.authors.add(musician6_pk)
    composition1.instrumentation.add(role3_pk, role7_pk)

    composition2 = Composition.objects.create(title='Sonata No. 1 in F major, Op. 5, No. 1')
    composition2.authors.add(musician1_pk)
    composition2.instrumentation.add(role3_pk, role4_pk)

    composition3 = Composition.objects.create(title='Symphony No. 9 in D minor, Op. 125')
    composition3.authors.add(musician1_pk, musician5_pk)
    composition3.instrumentation.add(role7_pk, role8_pk)

    composition4 = Composition.objects.create(title='Composition not in release')

    composition5 = Composition.objects.create(title='Composition without Movements')

    movement1 = Movement.objects.create(title='I. Allegretto', composition=composition1, order_number=1)
    movement2 = Movement.objects.create(title='II. Moderato', composition=composition1, order_number=2)
    movement3 = Movement.objects.create(title='III. Cadenza – Attacca', composition=composition1, order_number=3)
    movement4 = Movement.objects.create(title='IV. Allegro con moto', composition=composition1, order_number=4)

    movement5 = Movement.objects.create(title='Adagio sostenuto – Allegro', composition=composition2, order_number=1)
    movement6 = Movement.objects.create(title='Rondo. Allegro vivace', composition=composition2, order_number=2)

    movement7 = Movement.objects.create(title='	I. Allegro ma non troppo, un poco maestoso', composition=composition3, order_number=1)
    movement8 = Movement.objects.create(title='II. Molto vivace', composition=composition3, order_number=2)
    movement9 = Movement.objects.create(title='III. Adagio molto e cantabile', composition=composition3, order_number=3)
    movement10 = Movement.objects.create(title='IV. Finale', composition=composition3, order_number=4)

    movement11 = Movement.objects.create(title='Movement 1', composition=composition4, order_number=1)
    movement12 = Movement.objects.create(title='Movement 2', composition=composition4, order_number=2)

    release1 = Release.objects.create(title='Cello CD')
    release2 = Release.objects.create(title='Orchestra CD')

    track = Track.objects.create(movement=movement1, release=release1, disk='1', track_number=1)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement2, release=release1, disk='1', track_number=2)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement3, release=release1, disk='1', track_number=3)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement4, release=release1, disk='1', track_number=4)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement5, release=release1, disk='1', track_number=5)
    track.performers.add(musician7_pk, musician3_pk)

    track = Track.objects.create(movement=movement6, release=release1, disk='1', track_number=6)
    track.performers.add(musician7_pk, musician3_pk)

    track = Track.objects.create(movement=movement1, release=release2, disk='1', track_number=1)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement2, release=release2, disk='1', track_number=2)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement3, release=release2, disk='1', track_number=3)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement4, release=release2, disk='1', track_number=4)
    track.performers.add(musician2_pk, musician7_pk)

    track = Track.objects.create(movement=movement7, release=release2, disk='1', track_number=5)
    track.performers.add(musician2_pk, musician8_pk)

    track = Track.objects.create(movement=movement8, release=release2, disk='2', track_number=1)
    track.performers.add(musician2_pk, musician8_pk)

    track = Track.objects.create(movement=movement9, release=release2, disk='2', track_number=2)
    track.performers.add(musician2_pk, musician8_pk)

    track = Track.objects.create(movement=movement10, release=release2, disk='2', track_number=3)
    track.performers.add(musician2_pk, musician8_pk)

    return redirect('ClassicalMusic_show_releases')


# SHOW FUNCTIONS

def ClassicalMusic_show_musicians(request):
    all_musicians = Musician.objects.all().order_by(Lower('sort_name'))
    return render(request, 'ClassicalMusic/ClassicalMusic_show_musicians.html', {'musicians': all_musicians})

def ClassicalMusic_show_compositions(request):
    all_compositions = Composition.objects.all().prefetch_related(Prefetch('authors__role')).order_by('title')

    return render(request, 'ClassicalMusic/ClassicalMusic_show_compositions.html', {'compositions': all_compositions})

def ClassicalMusic_show_releases(request):
    # order_by is set in the query in composition()
    all_releases = Release.objects.compositions()

    return render(request, 'ClassicalMusic/ClassicalMusic_show_releases.html', {'releases': all_releases})

def ClassicalMusic_show_roles(request):
    all_roles = Role.objects.all().order_by('role_type', 'role')
    return render(request, 'ClassicalMusic/ClassicalMusic_show_roles.html', {'roles': all_roles})


# DETAILS FUNCTIONS

def ClassicalMusic_details_musician(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    all_fields = Musician._meta.fields
    all_fields2 =Musician._meta.get_fields()

    return render(request, 'ClassicalMusic/ClassicalMusic_details_musician.html', {'musician': musician})

def ClassicalMusic_details_composition(request, pk):
    composition = get_object_or_404(Composition, pk=pk)
    all_fields2 = Composition._meta.get_fields()

    return render(request, 'ClassicalMusic/ClassicalMusic_details_composition.html', {'composition': composition})

def ClassicalMusic_details_release(request, pk):
    release = get_object_or_404(Release, pk=pk)
    all_fields2 = release._meta.get_fields()
    print(all_fields2)
    track = release.track_set

    return render(request, 'ClassicalMusic/ClassicalMusic_details_release.html', {'release': release})


# EDIT FUNCTIONS

def ClassicalMusic_edit_musician(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        form = NewMusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_details_musician', pk)
    else:
        form = NewMusicianForm(instance=musician)
    return render(request, 'ClassicalMusic/ClassicalMusic_edit_musician.html', {'form': form, 'pk': pk})

def ClassicalMusic_edit_movement(request, c_pk, m_pk):
    composition = get_object_or_404(Composition, pk=c_pk)
    movement = get_object_or_404(Movement, pk=m_pk)
    if request.method == "POST":
        form = NewMovementForm(request.POST, instance=movement)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_details_composition', c_pk)
    else:
        form = NewMovementForm(instance=movement)
    return render(request, 'ClassicalMusic/ClassicalMusic_edit_movement.html', {'form': form, 'composition': composition})

def ClassicalMusic_edit_release(request, pk):
    release = get_object_or_404(Release, pk=pk)
    if request.method == "POST":
        form = EditReleaseForm(request.POST, instance=release)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_details_release', pk)
    else:
        form = EditReleaseForm(instance=release)
    return render(request, 'ClassicalMusic/ClassicalMusic_edit_release.html', {'form': form, 'release': release})

def ClassicalMusic_edit_tracks(request, pk):
    release = get_object_or_404(Release, pk=pk)
    NewTrackFormSet = modelformset_factory(Track, exclude=(), extra=0, widgets={
            'movement': forms.Select(attrs={'class': 'form-control'}),
            # release widget no longer selection, so only for prefilled fields
            'release': forms.TextInput(attrs={'class': 'form-control release-prefill', 'type': 'hidden'}),
            'performers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'disk': forms.TextInput(attrs={'class': 'form-control'}),
            'track_number': forms.NumberInput(attrs={'class': 'form-control'}),
        })
    if request.method == 'POST':
        formset = NewTrackFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
            return redirect('ClassicalMusic_details_release', pk)
    else:
        formset = NewTrackFormSet(queryset=Track.objects.filter(release=pk))
    return render(request, 'ClassicalMusic/ClassicalMusic_edit_tracks.html', {'formset': formset, 'release': release})

    # def ClassicalMusic_add_tracks(request):
    #     number_tracks = request.session.get('number_tracks')[0]  # this is a list
    #     release_pk = request.session.get('release')
    #     release = get_object_or_404(Release, pk=release_pk)
    #     NewTrackFormSet = formset_factory(NewTrackForm, extra=number_tracks)
    #     if request.method == 'POST':
    #         formset = NewTrackFormSet(request.POST)
    #         if formset.is_valid():
    #             print(formset)
    #             for form in formset:
    #                 if form.is_valid():
    #                     print(form)
    #                     form.save()
    #             return redirect('ClassicalMusic_show_releases')
    #     else:
    #         formset = NewTrackFormSet()
    #     return render(request, 'ClassicalMusic/ClassicalMusic_add_tracks.html',
    #                   {'formset': formset, 'release': release})

def ClassicalMusic_edit_composition(request, pk):
    composition = get_object_or_404(Composition, pk=pk)
    if request.method == "POST":
        form = EditCompositionForm(request.POST, instance=composition)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_details_composition', pk)
    else:
        form = EditCompositionForm(instance=composition)
    return render(request, 'ClassicalMusic/ClassicalMusic_edit_composition.html', {'form': form, 'pk': pk})

def ClassicalMusic_edit_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == "POST":
        form = NewRoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('ClassicalMusic_show_roles')
    else:
        form = NewRoleForm(instance=role)
    return render(request, 'ClassicalMusic/ClassicalMusic_edit_role.html', {'form': form})


# DELETE FUNCTIONS

def ClassicalMusic_delete_musician(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        try:
            musician.delete()
            return redirect('ClassicalMusic_show_musicians')

        except ProtectedError as e:
            messages.add_message(request, messages.ERROR, "The Musician is in use in other records.")
            return redirect('ClassicalMusic_details_musician', pk)

        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something went wrong.")
            return redirect('ClassicalMusic_details_musician', pk)
    else:
        return redirect('ClassicalMusic_details_musician', pk)

# deletes dependant movements too
def ClassicalMusic_delete_composition(request, pk):
    composition = get_object_or_404(Composition, pk=pk)
    if request.method == 'POST':
        try:
            composition.delete()
            return redirect('ClassicalMusic_show_compositions')

        except ProtectedError as e:
            messages.add_message(request, messages.ERROR, "This composition or it's movements are in use in other records.")
            return redirect('ClassicalMusic_details_composition', pk)

        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something went wrong.")
            return redirect('ClassicalMusic_details_composition', pk)
    else:
        return redirect('ClassicalMusic_details_composition', pk)

# always routes back to the release details page the user came from.
def ClassicalMusic_delete_track(request, r_pk, t_pk):
    track = get_object_or_404(Track, pk=t_pk)
    if request.method == 'POST':
        try:
            track.delete()
            return redirect('ClassicalMusic_details_release', r_pk)

        except ProtectedError as e:
            messages.add_message(request, messages.ERROR, "The this is in use in other records.")
            return redirect('ClassicalMusic_details_release', r_pk)

        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something went wrong.")
            return redirect('ClassicalMusic_details_release', r_pk)
    else:
        return redirect('ClassicalMusic_details_release', r_pk)

# always routes back to the composition details page the user came from.
def ClassicalMusic_delete_movement(request, c_pk, m_pk):
    movement = get_object_or_404(Movement, pk=m_pk)
    if request.method == 'POST':
        try:
            movement.delete()
            return redirect('ClassicalMusic_details_composition', c_pk)

        except ProtectedError as e:
            messages.add_message(request, messages.ERROR, "This movement is in use in other records.")
            return redirect('ClassicalMusic_details_composition', c_pk)

        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something went wrong.")
            return redirect('ClassicalMusic_details_composition', c_pk)
    else:
        return redirect('ClassicalMusic_details_composition', c_pk)

# deletes dependant tracks too
def ClassicalMusic_delete_release(request, pk):
    release = get_object_or_404(Release, pk=pk)
    if request.method == 'POST':
        try:
            release.delete()
            return redirect('ClassicalMusic_show_releases')

        except ProtectedError as e:
            messages.add_message(request, messages.ERROR, "This composition or it's movements are in use in other records.")
            return redirect('ClassicalMusic_details_release', pk)

        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something went wrong.")
            return redirect('ClassicalMusic_details_release', pk)
    else:
        return redirect('ClassicalMusic_details_release', pk)

def ClassicalMusic_delete_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        try:
            role.delete()
            return redirect('ClassicalMusic_show_roles')

        except ProtectedError as e:
            messages.add_message(request, messages.ERROR, "The Role is in use in other records.")
            return redirect('ClassicalMusic_show_roles')

        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something went wrong.")
            return redirect('ClassicalMusic_show_roles')
    else:
        return redirect('ClassicalMusic_show_roles')


# API MUSICBRAINZ

# https://musicbrainz.org/doc/Developer_Resources
# Work with either the Accept header or the fmt parameter. If both, the fmt takes precedence
# A meaningful user-agent string, with contact information is required

def ClassicalMusic_search_musician(request):
    if request.method == 'POST':
        name = request.POST.get("search")
        # this is called a search in MusicBrainz documentation
        limit = 25
        page = 1
        try:
            page = int(request.POST.get("page"))
        except:
            pass
        offset = (page - 1) * limit
        headers = {
            # 'Accept': 'application/json',
            'User-Agent': 'ClassicalMusic ( catharinavanveen.com )'
        }
        parameters = {
            'query': name,
            'limit': limit,
            'offset': offset,
            'fmt': 'json'
        }
        try:
            response = requests.get("https://musicbrainz.org/ws/2/artist?", headers=headers, params=parameters)
        except:
            messages.add_message(request, messages.ERROR, "This service is not available at the time.TRY FAILED")
            return redirect('ClassicalMusic_show_musicians')

        if response.status_code == 200:
            artists = response.json()['artists']
            number_artists = response.json()['count']
            pages = math. ceil(number_artists/limit)
            musicians = []
            for artist in artists:
                # if these top fields don't exist in the data then skip artist.
                try:
                    musician = {
                        'MBID': artist['id'],
                        'name': artist['name']
                    }
                    # if any of the fields below aren't present in the data, then skip field
                    try:
                        musician['type'] = artist['type']
                    except:
                        pass
                    try:
                        musician['type_MBID'] = artist['type-id']
                    except:
                        pass
                    try:
                        musician['sort_name'] = artist['sort-name']
                    except:
                        pass
                    try:
                        musician['gender'] = artist['gender']
                    except:
                        pass
                    try:
                        musician['disambiguation'] = artist['disambiguation']
                    except:
                        pass
                    try:
                        if artist['life-span']:
                            try:
                                musician['life_begin'] = artist['life-span']['begin']
                            except:
                                pass
                            try:
                                musician['life_end'] = artist['life-span']['end']
                            except:
                                pass
                            try:
                                musician['life_ended'] = artist['life-span']['ended']
                            except:
                                pass
                    except:
                        pass
                    musicians.append(musician)
                except:
                    pass
            request.session['search_musician'] = musicians
            return render(request, 'ClassicalMusic/ClassicalMusic_search_result_musician.html', {'musicians': musicians, 'search_name': name, 'pages': pages, 'page': page})
        else: # status code is not 200
            messages.add_message(request, messages.ERROR, "This service is not available at the time.")
    else:
        # the mothod is not post. In case the user gets redirected from 'ClassicalMusic_search_details_musician' check if there is a session first
        try:
            musicians = request.session['search_musician']
            return render(request, 'ClassicalMusic/ClassicalMusic_search_result_musician.html',
                          {'musicians': musicians})
        except:
            return redirect('ClassicalMusic_show_musicians')


def ClassicalMusic_search_composition(request):

    return render(request, 'ClassicalMusic/ClassicalMusic_search_result_composition.html')

def ClassicalMusic_search_release(request):

    return render(request, 'ClassicalMusic/ClassicalMusic_search_result_release.html')

def ClassicalMusic_search_role(request):

    return render(request, 'ClassicalMusic/ClassicalMusic_search_result_release.html')


def ClassicalMusic_search_details_musician(request, MBID):
    # get recordings details from API function
    recordings, pages, page = API.ClassicalMusic_api_get_details_musician(request, MBID)

    # retrieve musicians info from session, find musician with right MBID, get details
    musicians = request.session['search_musician']
    musician = {}
    for mus in musicians:
        if mus['MBID'] == MBID:
            musician = mus
            break

    # get compositions details and image urls from Beautifull Soup function
    catalogues, image_urls = BS.ClassicalMusic_soup_get_compositions(request, MBID)

    # Include form for when user wants to add to templates

    try:
        name = musician['name']
    except:
        name = ""

    try:
        sort_name = musician['sort_name']
    except:
        sort_name = ""
    try:
        if musician['type'] == "Person":
            type = "individual"
        else:
            type = "ensemble"
    except:
        type = ""

    try:
        gender =  musician['gender']
    except:
        gender = ""

    try:
        life_begin =  musician['life_begin'],
    except:
        life_begin = ""

    try:
        life_end =  musician['life_end']
    except:
        life_end = ""
    try:
        image_url = image_urls[0]
    except:
        image_url = ""

    try:
        if musician['life_ended']:
            life_ended = 'true'
        elif musician['life_end']:
            life_ended = 'true'
        elif musician['life_ended'] == 'unknown':
            life_ended = 'unknown'
        else:
            life_ended = 'false'
    except:
        life_ended = 'unknown'

    form = NewMusicianForm(initial={
        'name': name,
        'sort_name': sort_name,
        'type': type,
        'gender': gender,
        'Life_begin': life_begin,
        'Life_end': life_end,
        'life_ended': life_ended,
        'image_url': image_url,
        'MBID': musician['MBID']
    })

    context = {'recordings': recordings, 'musician': musician, 'pages': pages, 'page': page, 'catalogues': catalogues, 'image_urls': image_urls, 'form': form, }
    return render(request, 'ClassicalMusic/ClassicalMusic_search_details_musician.html', context)



# BUILD API

@api_view(['GET', 'POST'])
def ClassicalMusic_api_musician_collection(request):
    if request.method == 'GET':
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {'name': request.data.get('name'),'sort_name': request.data.get('sort_name'),'type': request.data.get('type'),'gender': request.data.get('gender'),'role': request.data.get('role'),'Life_begin': request.data.get('Life_begin'),'Life_end': request.data.get('Life_end'), 'life_ended': request.data.get('life_ended'), 'image_url': request.data.get('image_url'), 'MBID': request.data.get('MBID')}
        serializer = MusicianSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'POST'])
def ClassicalMusic_api_musician_single(request, pk):
    try:
        musician = Musician.objects.get(pk=pk)
    except Musician.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # add the empty string in case the user has no exclude defined.
        exclude = request.GET.get('exclude', '')
        tuple_exclude = tuple(exclude.split(','))
        serializer = MusicianOptionsSerializer(musician, fields=tuple_exclude)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        data = {'name': request.data.get('name'),'sort_name': request.data.get('sort_name'),'type': request.data.get('type'),'gender': request.data.get('gender'),'role': request.data.get('role'),'Life_begin': request.data.get('Life_begin'),'Life_end': request.data.get('Life_end'), 'life_ended': request.data.get('life_ended'), 'image_url': request.data.get('image_url'), 'MBID': request.data.get('MBID')}
        serializer = MusicianSerializer(musician, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def ClassicalMusic_api_composition_single(request, pk):
    try:
        composition = Composition.objects.get(pk=pk)
    except Composition.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CompositionSerializer(composition)
        return Response(serializer.data)



# TEST API. The fucntions below have HARDCODED pk for edit and delete.

def ClassicalMusic_TEST_api_musician_collection(request):
    headers = {
        'Accept': 'application/json',
    }
    parameters = {
        'format': 'json'
    }
    response = requests.get("http://127.0.0.1:8000/ClassicalMusic/api/v1/musicians/", headers=headers, params=parameters)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:  # No status code of 200
        messages.add_message(request, messages.ERROR, "FAILED.")

    return redirect('ClassicalMusic_show_musicians')

def ClassicalMusic_TEST_api_musician_single(request):
    headers = {
        'Accept': 'application/json',
    }
    # the exclude parameters have to be entered without spaces
    parameters = {
        'format': 'json',
        'exclude': 'composition_set,track_set'

    }
    response = requests.get("http://127.0.0.1:8000/ClassicalMusic/api/v1/musicians/1/", headers=headers, params=parameters)
    print(response.url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:  # No status code of 200
        messages.add_message(request, messages.ERROR, "FAILED.")

    return redirect('ClassicalMusic_show_musicians')


def ClassicalMusic_TEST_api_musician_collection_POST(request):
    form = APINEWMusicianForm()
    return render(request, 'ClassicalMusic/ClassicalMusic_TEST_api_add_musician.html', {'form': form})

def ClassicalMusic_TEST_api_musician_single_DELETE(request):
    headers = {
        'Accept': 'application/json',

    }
    parameters = {
        'format': 'json'
    }
    response = requests.delete("http://127.0.0.1:8000/ClassicalMusic/api/v1/musicians/9", headers=headers, params=parameters)
    print(response)
    return redirect('ClassicalMusic_show_musicians')

def ClassicalMusic_TEST_api_musician_single_POST(request):
    try:
        musician = Musician.objects.get(pk=2)
    except Musician.DoesNotExist:
        return HttpResponse(status=404)
    form = APINEWMusicianForm(instance=musician)
    return render(request, 'ClassicalMusic/ClassicalMusic_TEST_api_edit_musician.html', {'form': form})


def ClassicalMusic_TEST_api_composition_single(request):
    headers = {
        'Accept': 'application/json',
    }
    parameters = {
        'format': 'json'
    }
    response = requests.get("http://127.0.0.1:8000/ClassicalMusic/api/v1/compositions/1/", headers=headers, params=parameters)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:  # No status code of 200
        messages.add_message(request, messages.ERROR, "FAILED.")

    return redirect('ClassicalMusic_show_compositions')
