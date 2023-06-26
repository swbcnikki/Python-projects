from django import forms
from .widgets import IngredientMultiWidget


unit_choices = [
    ('', '---'),
    ('oz', 'oz'),
    ('dash', 'dash'),
    ('mL', 'mL'),
    ('cL', 'cL'),
    ('drop', 'drop'),
    ('part', 'part'),
    ('wash', 'wash'),
    ('garnish', 'garnish'),
]


class IngredientMultiField(forms.MultiValueField):
    widget = IngredientMultiWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField(),
            forms.ChoiceField(choices=unit_choices),
        )
        super(IngredientMultiField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return '\t'.join(data_list)
        return ''
