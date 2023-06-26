from django import forms
# importing our model from the models folder
from .models import Dallas


# creating our modelform
class DallasForm(forms.ModelForm):
    class Meta:
        model = Dallas
        fields = "__all__"
