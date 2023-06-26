from django.db import models


# Create your models here:
PasswordTypes = [('Personal', 'Personal'), ('Work', 'Work'), ('Combo', 'Combo'), ('Other', 'Other')] # 1st = db; 2nd = form


class NewPassword(models.Model):
    type = models.CharField(max_length=8, choices=PasswordTypes)
    creation_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)
    website = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    username = models.CharField(max_length=60)
    password = models.CharField(unique=True, max_length=60)
    favorite = models.BooleanField(default=False)

    NewPasswords = models.Manager() # django's 'Object Manager'





