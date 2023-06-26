from django.forms import ModelForm
from .models import Tent

class TentForm(ModelForm):
    class Meta:
        model = Tent
        fields = "__all__"

