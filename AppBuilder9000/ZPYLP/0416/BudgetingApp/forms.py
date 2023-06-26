from django import forms
from django.forms import ModelForm
from .models import BudgetInfo


# Commenting out code that is not operational at this time.
#class RegisterForm(ModelForm):
    #username = forms.CharField(label='username', max_length=100)
    #password = forms.CharField(label='password', widget=forms.PasswordInput)

    #class Meta:
        #model = AccountInfo
        #fields = ["username", "password"]


class BudgetForm(ModelForm):
    class Meta:
        model = BudgetInfo
        fields = ['expense_name', 'cost', 'date_added', 'username', 'details']
        widgets = {
            'expense_name': forms.TextInput(attrs={'class': 'expense_name', 'placeholder': 'Name of expense'}),
            'cost': forms.NumberInput(attrs={'class': 'cost', 'placeholder': 'Cost'}),
            'date_added': forms.DateInput(attrs={'class': 'date_added', 'placeholder': 'Date Added', 'type': 'date'}),
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Your Name!'}),
            'details': forms.TextInput(attrs={'class': 'details', 'placeholder': 'Enter Details Here..'}),
                   }


        def clean_budget_info(self):
            data = self.cleaned_data['expense_name', 'cost', 'date_added', 'username', 'details']

            return data



