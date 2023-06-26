from django.forms import ModelForm
from .models import Exercises

# shortcut template
# queries everything from dB all at once, ModelForm does that
class ExercisesForm(ModelForm):
    class Meta:
        model = Exercises
        fields = '__all__'
