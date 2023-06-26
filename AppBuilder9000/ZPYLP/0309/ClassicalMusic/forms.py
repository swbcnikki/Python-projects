from django import forms
from django.db import models

from .models import Musician, Role, Composition, Movement, Release, Track


class NewMusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['name','sort_name','type','gender','role','Life_begin','Life_end', 'life_ended', 'image_url', 'MBID']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sort_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'Life_begin': forms.TextInput(attrs={'class': 'form-control'}),
            'Life_end': forms.TextInput(attrs={'class': 'form-control'}),
            'life_ended': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
            'MBID': forms.TextInput(attrs={'class': 'form-control'}),

        }

class NewRoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role', 'type', 'role_type']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'role_type': forms.Select(attrs={'class': 'form-control'}),

        }

class NewCompositionForm(forms.ModelForm):
    number_movements = forms.IntegerField(min_value=0, max_value=25, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Composition
        fields = ['title', 'authors', 'instrumentation']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'instrumentation': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }

class EditCompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = ['title', 'authors', 'instrumentation']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'instrumentation': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }

class NewMovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['order_number', 'title', 'composition']
        widgets = {
            'order_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            # composistion widget widget no longer selection, so only for prefilled fields
            'composition': forms.TextInput(attrs={'class': 'form-control composition-prefill', 'type': 'hidden'}),
        }

class NewReleaseForm(forms.ModelForm):
    number_tracks = forms.IntegerField(min_value=1, max_value=150, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Release
        fields = ['title', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = ['title', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NewTrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['movement', 'release', 'performers', 'disk', 'track_number']
        widgets = {
            'movement': forms.Select(attrs={'class': 'form-control'}),
            # release widget no longer selection, so only for prefilled fields
            'release': forms.TextInput(attrs={'class': 'form-control release-prefill', 'type': 'hidden'}),
            'performers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'disk': forms.TextInput(attrs={'class': 'form-control'}),
            'track_number': forms.NumberInput(attrs={'class': 'form-control'}),

        }


#API TEST
class APINEWMusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['name','sort_name','type','gender','role','Life_begin','Life_end', 'life_ended', 'image_url', 'MBID']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sort_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'Life_begin': forms.TextInput(attrs={'class': 'form-control'}),
            'Life_end': forms.TextInput(attrs={'class': 'form-control'}),
            'life_ended': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
            'MBID': forms.TextInput(attrs={'class': 'form-control'}),

        }
