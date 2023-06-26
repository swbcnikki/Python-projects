from django.contrib import admin

# Register your models here.
from .models import PersonalizedNutrition, Account, NutritionixInfoReceived
from .forms import AccountForm, NutritionalQuery

admin.site.register(Account) #this is all that is needed to tell our admin software how to manage our product module
admin.site.register(PersonalizedNutrition) #this is all that is needed to tell our admin software how to manage our product module