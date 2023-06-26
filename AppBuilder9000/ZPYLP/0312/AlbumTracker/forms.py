from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Album


class DateInput(forms.DateInput):
    input_type = 'date'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'title': _('Album Title'),
            'date_listened': _('Date Listened'),
        }
        widgets = {
            'date_listened': DateInput()
        }
