from django.forms import ModelForm
from .models import Entry

# create a ModelForm
class EntryForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Entry
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'what\'s on your mind?'})
        self.fields['name'].widget.attrs.update({'class': 'input'})
        self.fields['Mood'].widget.attrs.update({'class': 'input'})
