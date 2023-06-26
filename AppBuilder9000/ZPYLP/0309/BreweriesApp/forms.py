from django.forms import ModelForm
from django import forms
from .models import Brewery, AllBreweries
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, ButtonHolder, Row, Column, HTML, Button

# add brewery form
class BreweryForm(ModelForm):
    class Meta:
        model = Brewery
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['name'].label = "Brewery Name:"
        self.fields['address1'].label = "Address Line 1:"
        self.fields['address2'].label = "Address Line 2:"
        self.fields['beerstyles1'].label = "Best Style:"
        self.fields['beerstyles2'].label = "Second Best:"
        self.fields['notes'].label = "Field Notes:"
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group form-control-md makeinline col-md-6 mb-1'),
                Column('beerstyles1', css_class='form-group makeinline col-md-3 mb-1'),
                Column('beerstyles2', css_class='form-group makeinline col-md-3 mb-1'),
                css_class='form-row'
            ),
            Row(
                Column('address1', css_class='form-group makeinline col-md-6 mb-1'),
                Column('address2', css_class='form-group makeinline col-md-6 mb-1'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group makeinline col-md-6 mb-1'),
                Column('state', css_class='form-group makeinline col-md-3 mb-1'),
                Column('zip', css_class='form-group makeinline col-md-3 mb-1'),
                css_class='form-row'
            ),
            Row(
                Column('notes', css_class='form-group col-md-12 mb-1'),
            ),
            Row(
                Submit('submit', 'Save', css_class='btn btn-primary col-md-2 ml-auto mb-3'),
                HTML('<a class="btn btn-danger col-md-2 ml-1 mr-3 mb-3" href="">Back</a>')
            ),
        )



