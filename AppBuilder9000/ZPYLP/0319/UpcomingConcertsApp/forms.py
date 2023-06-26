from django.forms import ModelForm
from .models import Concert, Piece, Orchestra, Conductor


class ConcertForm(ModelForm):
    class Meta:
        model = Concert
        fields = '__all__'


class OrchestraForm(ModelForm):
    class Meta:
        model = Orchestra
        fields = '__all__'


class PieceForm(ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'


class ConductorForm(ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__'
