from django.db import models


class Account(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.FirstName + ' ' + self.LastName



class Product(models.Model):
    name = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    info = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    objects = models.Manager()
