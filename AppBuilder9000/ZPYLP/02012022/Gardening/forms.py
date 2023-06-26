from django.forms import ModelForm
from .models import Plants
from crispy_forms.helper import FormHelper


# This model form is based on the Plants model class
class PlantsForm(ModelForm):
    helper = FormHelper()
    helper.label_class = 'col-lg-8'


    class Meta:
        model = Plants
        fields = '__all__'




