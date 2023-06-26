from django.forms import ModelForm
from .models import Account, PersonalizedNutrition

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class NutritionalQuery(ModelForm):
    class Meta:
        model = PersonalizedNutrition
        fields = '__all__'