from django import forms
from django.forms import ModelForm, PasswordInput
from .models import Register, Goals, Diary

class UserForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

        # this widget allows password to be replaced with ****
        # must set render_value to True
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

class LoginForm(forms.Form):
        username = forms.CharField(max_length=60)
        password = forms.CharField(max_length=60)
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = '__all__'


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('Task_Completed', 'Daily_Hours_Spent', 'Entry',)