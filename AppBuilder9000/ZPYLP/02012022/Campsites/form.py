from django.forms import ModelForm
from .models import CampSites


class CampsitesForm(ModelForm):
    class Meta:
        model = CampSites
        fields = '__all__'
