from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, FavPlayer

TEAM_OPTIONS = (
    ('Anaheim Ducks', 'Anaheim Ducks'),
    ('Arizona Coyotes', 'Arizona Coyotes'),
    ('Boston Bruins', 'Boston Bruins'),
    ('Buffalo Sabres', 'Buffalo Sabres'),
    ('Calgary Flames', 'Calgary Flames'),
    ('Carolina Hurricanes', 'Carolina Hurricanes'),
    ('Colorado Avalanche', 'Colorado Avalanche'),
    ('Columbus Blue Jackets', 'Columbus Blue Jackets'),
    ('Dallas Stars', 'Dallas Stars'),
    ('Detroit Red Wings', 'Detroit Red Wings'),
    ('Edmonton Oilers', 'Edmonton Oilers'),
    ('Florida Panthers', 'Florida Panthers'),
    ('Los Angeles Kings', 'Los Angeles Kings'),
    ('Minnesota Wild', 'Minnesota Wild'),
    ('Montreal Canadians', 'Montreal Canadians'),
    ('Nashville Predators', 'Nashville Predators'),
    ('New Jersey Devils', 'New Jersey Devils'),
    ('New York Rangers', 'New York Rangers'),
    ('New York Islanders', 'New York Islanders'),
    ('Ottawa Senators', 'Ottawa Senators'),
    ('Philadelphia Flyers', 'Philadelphia Flyers'),
    ('Pittsburgh Penguins', 'Pittsburgh Penguins'),
    ('San Jose Sharks', 'San Jose Sharks'),
    ('Seattle Kraken', 'Seattle Kraken'),
    ('St. Louis Blues', 'St. Louis Blues'),
    ('Tampa Bay Lightning', 'Tampa Bay Lightning'),
    ('Toronto Maple Leafs', 'Toronto Maple Leafs'),
    ('Vancouver Canucks', 'Vancouver Canucks'),
    ('Vegas Golden Knights', 'Vegas Golden Knights'),
    ('Washington Capitals', 'Washington Capitals'),
    ('Winnipeg Jets', 'Winnipeg Jets'),
)


class TeamForm(forms.Form):
    team_choice = forms.ChoiceField(choices=TEAM_OPTIONS)


class NewUserForm(UserCreationForm):
    TEAM_OPTIONS = (
        ('Anaheim Ducks', 'Anaheim Ducks'),
        ('Arizona Coyotes', 'Arizona Coyotes'),
        ('Boston Bruins', 'Boston Bruins'),
        ('Buffalo Sabres', 'Buffalo Sabres'),
        ('Calgary Flames', 'Calgary Flames'),
        ('Carolina Hurricanes', 'Carolina Hurricanes'),
        ('Colorado Avalanche', 'Colorado Avalanche'),
        ('Columbus Blue Jackets', 'Columbus Blue Jackets'),
        ('Dallas Stars', 'Dallas Stars'),
        ('Detroit Red Wings', 'Detroit Red Wings'),
        ('Edmonton Oilers', 'Edmonton Oilers'),
        ('Florida Panthers', 'Florida Panthers'),
        ('Los Angeles Kings', 'Los Angeles Kings'),
        ('Minnesota Wild', 'Minnesota Wild'),
        ('Montreal Canadians', 'Montreal Canadians'),
        ('Nashville Predators', 'Nashville Predators'),
        ('New Jersey Devils', 'New Jersey Devils'),
        ('New York Rangers', 'New York Rangers'),
        ('New York Islanders', 'New York Islanders'),
        ('Ottawa Senators', 'Ottawa Senators'),
        ('Philadelphia Flyers', 'Philadelphia Flyers'),
        ('Pittsburgh Penguins', 'Pittsburgh Penguins'),
        ('San Jose Sharks', 'San Jose Sharks'),
        ('Seattle Kraken', 'Seattle Kraken'),
        ('St. Louis Blues', 'St. Louis Blues'),
        ('Tampa Bay Lightning', 'Tampa Bay Lightning'),
        ('Toronto Maple Leafs', 'Toronto Maple Leafs'),
        ('Vancouver Canucks', 'Vancouver Canucks'),
        ('Vegas Golden Knights', 'Vegas Golden Knights'),
        ('Washington Capitals', 'Washington Capitals'),
        ('Winnipeg Jets', 'Winnipeg Jets'),
    )

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    favorite_team = forms.ChoiceField(choices=TEAM_OPTIONS)
    favorite_player = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'favorite_player', 'favorite_team', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'favorite_team', 'favorite_player')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'favorite_team': 'Favorite Team',
            'favorite_player': 'Favorite NHL Player',
        }


class PlayerForm(forms.Form):
    player_name = forms.CharField(max_length=50)
    player_number = forms.IntegerField(max_value=99, min_value=1)
    player_position = forms.CharField(max_length=1)
