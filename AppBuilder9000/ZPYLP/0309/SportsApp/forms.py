from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, HTML
from django.forms import ModelForm
from .models import SavedNbaGame
from django import forms
from .models import FavPlayer
from django.contrib.admin.widgets import AdminTimeWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'
    format('%H:%M',)


class NbaGameForm(ModelForm):
    class Meta:
        model = SavedNbaGame
        fields = '__all__'

        widgets = {
            'date_game': DateInput(),
            'time_start': forms.TimeInput(attrs={'type': 'time'}),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['home_team'].label = "Home Team: "
        self.fields['away_team'].label = "Away Team: "
        self.fields['date_game'].label = "Date of Game: "
        self.fields['time_start'].label = "Start Time: "
        self.fields['email'].label = "Contact Email: "
        self.helper.layout = Layout(
            Row(
                Column('home_team', css_class='form-group makeinline col-md-4 mb-1'),
                Column('away_team', css_class='form-group makeinline col-md-4- mb-1'),
                css_class='form-row'
            ),
            Row(
                Column('date_game', css_class='form-group makeinline col-md-4 mb-1'),
                Column('time_start', css_class='form-group makeinline col-md-4 mb-1'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6- mb-1'),
                css_class='form-row'
            ),
            Submit('submit', 'Save'),
            HTML('<a class="btn btn-danger" onclick="history.back()">Back</a>')
        )


class FavPlayerForm(ModelForm):
    class Meta:
        model = FavPlayer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['email'].label = "Contact Email: "
        self.fields['fav_player'].label = "Favorite Player: "
        self.fields['corresponding_team'].label = "Plays On: "
        self.helper.layout = Layout(
            Row(
                Column('fav_player', css_class='form-group makeinline col-md-4 mb-1'),
                Column('corresponding_team', css_class='form-group makeinline col-md-4 mb-1'),
            ),
            Row(
                Column('email', css_class='form-group makeinline col-md-6 mb-1'),
            ),
            Submit('submit', 'Save'),
            HTML('<a class="btn btn-danger" onclick="history.back()">Back</a>')

        )



