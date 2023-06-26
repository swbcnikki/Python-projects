from django import forms

from .models import Youtuber


class YoutuberForm(forms.ModelForm):
    class Meta:
        model = Youtuber
        fields = "__all__"
