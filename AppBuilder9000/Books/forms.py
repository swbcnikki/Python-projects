from django .forms import ModelForm
from .models import AddBook
from django import forms


class AddBookForm(ModelForm):
    class Meta:
        model = AddBook
        fields = '__all__'

