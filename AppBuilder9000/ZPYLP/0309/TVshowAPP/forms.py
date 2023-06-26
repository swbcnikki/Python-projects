from django.forms import ModelForm
from .models import TVshows

class TVshowsForm(ModelForm):
    class Meta:
        model = TVshows
        fields = '__all__'