from django import forms
# importing our model from the models folder
from .models import Cartoon


# creating our modelform
class CartoonForm(forms.ModelForm):
    class Meta:
        model = Cartoon
        fields = "__all__"
