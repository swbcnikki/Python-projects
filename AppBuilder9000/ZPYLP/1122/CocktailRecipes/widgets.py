from django import forms

unit_choices = [
    ('', '--'),
    ('oz', 'oz'),
    ('dash', 'dash'),
    ('mL', 'mL'),
    ('cL', 'cL'),
    ('drop', 'drop'),
    ('part', 'part'),
    ('wash', 'wash'),
    ('garnish', 'garnish'),
]


class IngredientMultiWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(),
            forms.TextInput(),
            forms.Select(attrs=attrs, choices=unit_choices),
        ]
        super(IngredientMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('\t')[0:3]
        return []
