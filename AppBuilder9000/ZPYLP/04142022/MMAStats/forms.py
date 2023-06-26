from django import forms
# importing our model from the models folder
from .models import Champions

# creating our modelform
class ChampForm(forms.ModelForm):
    class Meta:
        model = Champions
        fields = "__all__"
