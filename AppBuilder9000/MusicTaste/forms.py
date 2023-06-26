from django.forms import ModelForm
from django import forms
from .models import User, ChooseUser


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['Name', 'Age', 'Gender']


class ChooseUserForm(ModelForm):
    class Meta:
        model = ChooseUser
        fields = '__all__'


quizAnswers1 = [(1, 'A', '1750'),
                (0, 'B', '1900'),
                (0, 'C', '1650'),
                (0, 'D', '1335')]

quizAnswers2 = [(0, 'A', 'Johann Sebastian Bach'),
                (0, 'B', 'Wolfgang Amadeus Mozart'),
                (1, 'C', 'Hildegard of Bingen'),
                (0, 'D', 'Franz Joseph Haydn')]

quizAnswers3 = [(0, 'A', 'Guitar'),
                (0, 'B', 'Piano'),
                (1, 'C', 'Violin'),
                (0, 'D', 'Cello')]

quizAnswers4 = [(0, 'A', 'Johnny Rebb'),
                (0, 'B', 'Elvis Presely'),
                (0, 'C', 'Mark Fischbach'),
                (1, 'D', 'Johnny Cash')]

quizAnswers5 = [(0, 'A', 'Mountain Music'),
                (0, 'B', 'Travelin\' Tunes'),
                (1, 'C', 'Hillbilly Music'),
                (0, 'D', 'Bluegrass')]

quizAnswers6 = [(0, 'A', 'Dolly Parton'),
                (1, 'B', 'Zac Brown Band'),
                (0, 'C', 'Dion and the Belmonts'),
                (0, 'D', 'Lady Lilly')]

quizAnswers7 = [(0, 'A', 'Pearl Jam'),
                (0, 'B', 'Bill Haley and the Comets'),
                (1, 'C', 'Alvin and the Chipmunks'),
                (0, 'D', 'The Beatles')]

quizAnswers8 = [(0, 'A', 'U2'),
                (0, 'B', 'Nirvana'),
                (0, 'C', 'Crumb'),
                (1, 'D', 'Lil Blue Devils')]

quizAnswers9 = [(0, 'A', 'Yes'),
                (1, 'B', 'No'),
                (0, 'C', 'I\'m not sure'),
                (0, 'D', 'Depends')]

quizAnswers10 = [(0, 'A', 'Snoop Dogg'),
                 (0, 'B', 'Tory Lanez'),
                 (0, 'C', 'Logic'),
                 (1, 'D', 'Will Smith')]

quizAnswers11 = [(0, 'A', 'Seeing Green'),
                 (1, 'B', 'Mood'),
                 (0, 'C', 'Stonefruit'),
                 (0, 'D', 'Wants and Needs')]

quizAnswers12 = [(0, 'A', '2000'),
                 (0, 'B', '1955'),
                 (0, 'C', '1983'),
                 (1, 'D', '1970')]

quizAnswers13 = [(0, 'A', 'George Benson'),
                 (0, 'B', 'The Hot Sardines'),
                 (1, 'C', 'Original Dixieland Jazz Band'),
                 (0, 'D', 'The Big Phat Band')]

quizAnswers14 = [(1, 'A', 'Saxophone'),
                 (0, 'B', 'Clarinet'),
                 (0, 'C', 'Trumpet'),
                 (0, 'D', 'Piano')]

quizAnswers15 = [(0, 'A', 'Louis Armstrong'),
                 (1, 'B', 'Wayne Shorter Quartet'),
                 (0, 'C', 'Ella Fitzgerald'),
                 (0, 'D', 'Art Tatum')]


class QuizForm(forms.Form):
    question1 = forms.ChoiceField(label='When was the Baroque era of classical music originated?', choices=quizAnswers1,
                                  widget=forms.RadioSelect)

    question2 = forms.ChoiceField(label='Who originated classical music', choices=quizAnswers2,
                                  widget=forms.RadioSelect)

    question3 = forms.ChoiceField(label='Most popular classical music instrument', choices=quizAnswers3,
                                  widget=forms.RadioSelect)

    question4 = forms.ChoiceField(label='Who came in first in the 2005 top 100 country singers of all time?',
                                  choices=quizAnswers4, widget=forms.RadioSelect)

    question5 = forms.ChoiceField(label='What was the term for country music before it\'s 1949 rename?',
                                  choices=quizAnswers5, widget=forms.RadioSelect)

    question6 = forms.ChoiceField(label='Who wrote Chicken Fried? (If you don\'t know this one, I will find you)',
                                  choices=quizAnswers6, widget=forms.RadioSelect)

    question8 = forms.ChoiceField(label='Which one of these is NOT a real rock band?', choices=quizAnswers8,
                                  widget=forms.RadioSelect)

    question9 = forms.ChoiceField(label='Are rock and metal the same thing?', choices=quizAnswers9,
                                  widget=forms.RadioSelect)

    question10 = forms.ChoiceField(label='Who was the first rapper to win a grammy?', choices=quizAnswers10,
                                   widget=forms.RadioSelect)

    question11 = forms.ChoiceField(label='What rap was #1 in popularity January 2, 2021?', choices=quizAnswers11,
                                   widget=forms.RadioSelect)

    question12 = forms.ChoiceField(label='When was rap created?', choices=quizAnswers12, widget=forms.RadioSelect)

    question13 = forms.ChoiceField(label='Who released some of the first jazz songs?', choices=quizAnswers13,
                                   widget=forms.RadioSelect)

    question14 = forms.ChoiceField(label='What is the most common jazz instrument?', choices=quizAnswers14,
                                   widget=forms.RadioSelect)

    question15 = forms.ChoiceField(label='What jazz artist(s) won a grammy award in 2019?',
                                   choices=quizAnswers15, widget=forms.RadioSelect)
