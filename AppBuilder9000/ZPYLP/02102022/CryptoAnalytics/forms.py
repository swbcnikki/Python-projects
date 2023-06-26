from django.forms import ModelForm
from django import forms
from .models import Post


class UserRegisterForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)
