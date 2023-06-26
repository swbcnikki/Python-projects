from django import forms
from django.forms import ModelForm, Select, CheckboxInput, RadioSelect
from .models import Result

##FORM FOR ADDING RESULTS
class ResultForm(ModelForm):
    ##GETTING RID OF LABELS (THEY'LL BE SHOWN INSIDE OF DROPDOWNS)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Driver_Name'].label = ''
        self.fields['Current_Team'].label = ''
        self.fields['Race'].label = ''
        self.fields['Race_Type'].label = ''
        self.fields['Fastest_Lap'].label = 'Fastest Lap?'


    class Meta:
        model = Result
        fields = ['Driver_Name', 'Current_Team', 'Race', 'Race_Type', 'Finishing_Position', 'Fastest_Lap']
        ##ADDING CSS CLASSES FOR STYLING
        widgets = {
            'Driver_Name': Select(attrs={
                'class': 'form-dropdown'
            }),
            'Current_Team': Select(attrs={
                'class': 'form-dropdown'
            }),
            'Race': Select(attrs={
                'class': 'form-dropdown'
            }),
            'Race_Type': RadioSelect(attrs={
                'class': 'form-radio'
            }),
            'Finishing_Position': Select(attrs={
                'class': 'small-form-dropdown'
            }),
            'Fastest_Lap': CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }