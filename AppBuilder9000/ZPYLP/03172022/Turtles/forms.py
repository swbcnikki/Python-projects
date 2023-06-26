from django.forms import ModelForm
from .models import Turtles


# Creating a form class.
class CreateForm(ModelForm):
    class Meta:
        model = Turtles
        fields = '__all__'
