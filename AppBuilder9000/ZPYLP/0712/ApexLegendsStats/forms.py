import crispy_forms
from django.forms import ModelForm
from .models import Entry, LEGEND_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = "__all__"