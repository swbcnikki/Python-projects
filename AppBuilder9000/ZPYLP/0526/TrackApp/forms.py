from django import forms
from .models import Location
from .models import User



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"






