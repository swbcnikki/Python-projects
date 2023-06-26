from django.forms import ModelForm
from .models import Records


# define RecipeForm
class RecordsForm(ModelForm):
    class Meta:
        model = Records
        fields = '__all__'

