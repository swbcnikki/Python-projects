from django.forms import ModelForm
from.models import NewPassword


class NewPasswordForm(ModelForm):
    class Meta:
        model = NewPassword
        fields = '__all__'