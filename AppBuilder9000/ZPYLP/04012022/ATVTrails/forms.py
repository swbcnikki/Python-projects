from django.forms import ModelForm

from .models import AtvTrails


class Trails_Form(ModelForm):
    class Meta:
        model = AtvTrails
        fields = "__all__"
