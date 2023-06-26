from django.contrib import admin

from .models import Person
from .models import ComparedPerson
from .models import SelectPerson

admin.site.register(Person)
admin.site.register(ComparedPerson)
admin.site.register(SelectPerson)

