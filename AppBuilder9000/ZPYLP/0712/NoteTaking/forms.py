from django.forms import ModelForm
from .models import Note, Categorie

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'