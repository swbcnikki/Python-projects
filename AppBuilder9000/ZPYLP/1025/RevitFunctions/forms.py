# 2. after creating the classes for the app, now create the forms associated with the app.
    # prior to this is 1. models.py
    # forms is one of the benefit of Django, aid in rapid development with
        #user authentication, form authentication, localization, CRUD (Create, Read, Update, Delete) operations.
    # if models.py has multiple classes, MUST create multiple forms here (classes) associated with them.
    # forms need to import into 3. views.py
    # forms need to also associate with Create Account & Add Transaction 4. templates

from django.forms import ModelForm
from .models import RvtFunction, User         # include all classes from this page

# story2, step2: Create a model form that will include any inputs the user needs to make
# create RvtFunctions form
class AddUserForm(ModelForm):                 # ModelForm is a subclass.
    class Meta:
        model = User
        fields ='__all__'                     # wild card, including all fields in the form.

class AddRvtFunctionForm(ModelForm):          # ModelForm is a subclass.
    class Meta:
        model = RvtFunction
        fields ='__all__'                     # wild card, including all fields in the form.

