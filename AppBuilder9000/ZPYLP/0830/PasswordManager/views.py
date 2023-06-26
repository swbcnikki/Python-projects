from django.shortcuts import render, redirect, get_object_or_404
from .models import NewPassword
from .forms import NewPasswordForm
from django.core.paginator import Paginator


# Displays the 'HOME PAGE':
def home(request):
    return render(request, 'PasswordManager/PwdMgr_home.html')


# Displays the SELECTED PASSWORD's DETAILS:
def passwordDetails(request, id):
    chosenPwd = get_object_or_404(NewPassword, id=id) # 'NewPassword' from models.py; red 'id' == dictionary object, 2nd 'id == from line 14
    content = {'chosenPwd': chosenPwd}
    return render(request, 'PasswordManager/PwdMgr_details.html', content)


# Displays the "SAVE A NEW PASSWORD" form:
def passwordInput(request):
    form = NewPasswordForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST': # if the method is POST...
        if form.is_valid(): # ... and all fields are valid...
            form.save() # ...save the form's contents to the templates
            return redirect('PwdMgr_home') # return User to this app's Home page
    content = {'form': form}
    return render(request, 'PasswordManager/PwdMgr_pwdInput.html', content) # render form's data within the 'pwdInput.html' page


# Displays ALL SAVED PASSWORDS (as a list; no details):
def passwordsList(request):
    allPasswords = NewPassword.NewPasswords.filter(id__gt=0) # returns a filtered dictionary of passwords
    paginator = Paginator(allPasswords, 10) # displays 10 passwords per page; overflow == a new 'Next' page
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return render(request, 'PasswordManager/PwdMgr_pwdsList.html', {'content': content})