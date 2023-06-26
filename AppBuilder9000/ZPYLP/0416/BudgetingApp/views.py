from django.shortcuts import render, get_object_or_404
from .forms import BudgetForm, BudgetInfo
import requests

def home(request):
    return render(request, 'BudgetingApp/BudgetingApp_home.html')


def login(request):
    return render(request, 'BudgetingApp/BudgetingApp_login.html')


def create_budget(request):
    form = BudgetForm()
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = BudgetForm(request.POST)
        form.save()  # will validate form and save

    context = {
        'form': form
    }

    return render(request, 'BudgetingApp/BudgetingApp_budget.html', context)


def account(request):
    items = BudgetInfo.objects.all()

    context = {
        'items': items
    }

    return render(request, 'BudgetingApp/BudgetingApp_account.html', context)


def details(request, pk):
    item = get_object_or_404(BudgetInfo, pk=pk)
    context = {'item': item}
    return render(request, 'BudgetingApp/BudgetingApp_details.html', context)










