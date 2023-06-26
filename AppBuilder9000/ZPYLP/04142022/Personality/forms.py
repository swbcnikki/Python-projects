from django.forms import ModelForm
from django import forms
from .models import Person, SelectPerson


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'sex']


class SelectPersonForm(ModelForm):
    class Meta:
        model = SelectPerson
        fields = '__all__'


class JobSearchForm(forms.Form):
    location = forms.CharField(label='Location:', max_length=50)


CHOICES = [(2, 'Strongly Agree'),
           (1, 'Agree'),
           (0, 'Neutral'),
           (-1, 'Disagree'),
           (-2, 'Strongly Disagree')]

INVERSE_CHOICES = [(-2, 'Strongly Agree'),
                   (-1, 'Agree'),
                   (0, 'Neutral'),
                   (1, 'Disagree'),
                   (2, 'Strongly Disagree')]


class TestForm(forms.Form):
    questionO1 = forms.ChoiceField(label='I am full of ideas.', choices=CHOICES, widget=forms.RadioSelect)
    questionC1 = forms.ChoiceField(label='I am always prepared.', choices=CHOICES, widget=forms.RadioSelect)
    questionE1 = forms.ChoiceField(label='I am the life of the party.', choices=CHOICES, widget=forms.RadioSelect)
    questionA1 = forms.ChoiceField(label='I have a soft heart.', choices=CHOICES, widget=forms.RadioSelect)
    questionN1 = forms.ChoiceField(label='I get stressed out easily.', choices=CHOICES, widget=forms.RadioSelect)

    questionO2 = forms.ChoiceField(label='I have a vivid imagination.', choices=CHOICES, widget=forms.RadioSelect)
    questionC2 = forms.ChoiceField(label='I am exacting in my work.', choices=CHOICES, widget=forms.RadioSelect)
    questionE2 = forms.ChoiceField(label='I talk to a lot of different people at parties.', choices=CHOICES, widget=forms.RadioSelect)
    questionA2 = forms.ChoiceField(label='I take time out for others.', choices=CHOICES, widget=forms.RadioSelect)
    questionN2 = forms.ChoiceField(label='I worry about things.', choices=CHOICES, widget=forms.RadioSelect)

    questionO3 = forms.ChoiceField(label='I have difficulty understanding abstract ideas.', choices=INVERSE_CHOICES, widget=forms.RadioSelect)
    questionC3 = forms.ChoiceField(label='I leave my belongings around.', choices=INVERSE_CHOICES, widget=forms.RadioSelect)
    questionE3 = forms.ChoiceField(label='I am quiet around strangers.', choices=INVERSE_CHOICES, widget=forms.RadioSelect)
    questionA3 = forms.ChoiceField(label="I am not interested in other people's problems.", choices=INVERSE_CHOICES, widget=forms.RadioSelect)
    questionN3 = forms.ChoiceField(label='I seldom feel blue.', choices=INVERSE_CHOICES, widget=forms.RadioSelect)

    questionO4 = forms.ChoiceField(label='I spend time reflecting on things.', choices=CHOICES, widget=forms.RadioSelect)
    questionC4 = forms.ChoiceField(label='I follow a schedule.', choices=CHOICES, widget=forms.RadioSelect)
    questionE4 = forms.ChoiceField(label="I don't mind being the center of attention.", choices=CHOICES, widget=forms.RadioSelect)
    questionA4 = forms.ChoiceField(label="I sympathize with others' feelings.", choices=CHOICES, widget=forms.RadioSelect)
    questionN4 = forms.ChoiceField(label='I have frequent mood swings.', choices=CHOICES, widget=forms.RadioSelect)

    questionO5 = forms.ChoiceField(label='I Need a creative outlet.', choices=CHOICES, widget=forms.RadioSelect)
    questionC5 = forms.ChoiceField(label='I carry out my plans.', choices=CHOICES, widget=forms.RadioSelect)
    questionE5 = forms.ChoiceField(label='I Make friends easily.', choices=CHOICES, widget=forms.RadioSelect)
    questionA5 = forms.ChoiceField(label='I respect authority.', choices=CHOICES, widget=forms.RadioSelect)
    questionN5 = forms.ChoiceField(label='I get angry easily.', choices=CHOICES, widget=forms.RadioSelect)

