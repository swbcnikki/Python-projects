from django.forms import ModelForm
from .models import AvailablePet, PetApplicant
from django import forms
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class AvailablePetForm(ModelForm):
    class Meta:
        model = AvailablePet
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 35}),
            'birthday': DateInput(),
        }


class PetApplicantForm(ModelForm):
    class Meta:
        model = PetApplicant
        fields = '__all__'


FILTERS = [('All','All'),('dogs','Dogs'),('cats','Cats')]


class FilterForm(forms.Form):
    animal_filter = forms.CharField(label='Animal Type', widget=forms.RadioSelect(choices=FILTERS))
    number_of_results = forms.IntegerField(min_value=1, max_value=50)
