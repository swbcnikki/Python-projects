# 1. Create your models here.
    # 0 prior to this, set up the settings.py, Masonry_base.html, musicfiles_home.html, some css, urls, views.
    # Models.py is How data is represented, accessed, manipulated. defined/represented by Python classes, automated by Django.
    # the class is called model. it drives the dB data.
    # this should be in the app directory folder, RevitFunctions is an app (there can be more than 1 app)
    # each app should have it's own __init__.py, manage.py, settings.py, urls.py
    # go back to the directory where manage.py resides > type: python manage.py makemigrations >
    # then migrate
    # since created classes for forms, next to create the forms.py
    # models.py: Here you can store the application’s data models.
#This is where you specify the entities and relationships between data.
    #dB schema
#https://docs.djangoproject.com/en/3.2/topics/db/models/
# next 1A. register the application in admin.py
# need to migrate after any changes to dB.

from django.db import models

# Create your models here = Create all Classes here
# Story2, Step1: Create your model and add a migration, make sure to plan out all the categories you want to track for your object. Include an objects manager for accessing the database.


rvt_level_choice = [                                                    # using [] will keep the contents as a List & in order as they're listed here. {} is a set and won't be in order as listed.
    ('0 Novice', '0 Novice'),
    ('1 Beginner', '1 Beginner'),
    ('2 Intermediate', '2 Intermediate'),
    ('3 Advance', '3 Advance'),
]

job_category_choice = [
    ('0 All', '0 All'),
    ('1 Designer', '1 Designer'),
    ('2 Production', '2 Production'),
    ('3 Designer & Production', '3 Designer & Production'),
    ('4 Administration', '4 Administration'),
    ('5 Project Lead', '5 Project Lead'),
]

rvt_category_choice = [                                                # drop menu for types. dictionary object, tuple.
    ('0 Revit Basic', '0 Revit Basic'),
    ('1 Revit Modeling', '1 Revit Modeling'),
    ('2 Revit Documentation', '2 Revit Documentation'),
    ('3 Revit Collaboration', '3 Revit Collaboration'),
    ('4 Revit Plug-ins', '4 Revit Plug-ins'),
    ('5 Revit Maintenance', '5 Revit Maintenance'),
    ('6 BIM360', '6 BIM360'),
    ('7 Revit Troubleshoot', '7 Revit Troubleshoot'),
]


class User(models.Model):
    email = models.CharField(max_length=80, default="",                 # start off as empty input field: default = "", but the form can't be blank blank=True
                                 blank=True, null=False)
    revit_level = models.CharField(max_length=80, choices=rvt_level_choice)
    job_category = models.CharField(max_length=80, choices=job_category_choice)
                                                                        # NOT utilized here: IntField does not have max_length - always check doc for more info

    Users = models.Manager()                                            # use the models that we involked. Must be within the class.


                                                                        # basic schema of Product, must register the app in admin file for it to show on browser.
class RvtFunction(models.Model):                                        # Model is the class
    revit_title = models.CharField(max_length=80, default="",
                                 blank=True, null=False)                # start off as empty: default = "", but the form can't be blank blank=True
    revit_description = models.TextField(max_length=300, default="",
                                       blank=True)                      # TextField allow for many texts
    revit_category = models.CharField(max_length=80,                      # fields, what are the restrictions, primary key auto create id for every entry in dB
                                    choices=rvt_category_choice)        #inheritate the choices above class RvtFunctions
    revit_level = models.CharField(max_length=80, choices=rvt_level_choice)
    job_category = models.CharField(max_length=80, choices=job_category_choice)
                                                                        # NOT utilized here: IntField does not have max_length - always check doc for more info

    # Story6 pt1 API, Step 4: Create a way to get any input information from the user and get the specific response for that input.
        # (e.g. allow user to search specific terms through the api, getting all data for that search)
    google_keywords = models.CharField(max_length=100, default="", blank=True, null=False)
                                                                        # enter predefined google search keywrds for API google search.

####### NEED 2 FOREIGN KEYS TO COMBINE BOTH revit_level & job_Category #######

    RvtFunctions = models.Manager()                                     # use the models that we involked. Must be within the class.

    def __str__(self):                                                  # dunnder __str__: Django will use the result of the function to display objects of that type (in this case it will print self).
     return self.revit_title                                            # this take the object we entered & turn it into a string,
                                                                            # and return the title of the object. Always use the first object.

