from django import forms
from django.forms import ModelForm
from .models import Story, Resource


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'article': forms.Textarea(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'tags': forms.Select(attrs={'class': 'form-control'}),
        }

class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'objective': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'URL': forms.URLInput(attrs={'class': 'form-control'}),
        }

