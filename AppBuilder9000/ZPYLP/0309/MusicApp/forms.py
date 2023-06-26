from django.forms import ModelForm
from django import forms
from .models import MusicalArtists, SongNames, AlbumNames
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column





class MusicalArtistsForm(forms.ModelForm):
    class Meta:
        model = MusicalArtists
        fields = '__all__'

        widgets = {
            'active': forms.NullBooleanSelect(attrs={'class': 'form-styling'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('artist_name', css_class='form-group col-md-7 mb-0'),
                Column('year_formed', css_class='form-group col-md-5 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('genre', css_class='form-group col-md-7 mb-0'),
                Column('group_or_solo', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image_url', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('active', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save Artist')
        )



class SongNamesForm(forms.ModelForm):
    class Meta:
        model = SongNames
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('song_name', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('artist_name', css_class='form-group col-md-6 mb-0'),
                Column('album_name', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('song_release_year', css_class='form-group col-md-6 mb-0'),
                Column('song_length', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save Song')
        )



class AlbumNamesForms(forms.ModelForm):
    class Meta:
        model = AlbumNames
        fields = '__all__'
        widgets = {
            'date_album_released': forms.DateInput(attrs={'class': 'form-styling'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('album_name', css_class='form-group col-md-9 mb-0'),
                Column('number_of_tracks', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('artist_name', css_class='form-group col-md-8 mb-0'),
                Column('date_album_released', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('img_url', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save Album')
        )

