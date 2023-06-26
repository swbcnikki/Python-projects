from django.db import models


class BudgetInfo(models.Model):

    expense_name = models.CharField(max_length=30, default='Expense Name')

    cost = models.FloatField()

    date_added = models.DateField()

    username = models.CharField(max_length=20, default='Your Name!')

    details = models.TextField(max_length=300, default='Details...')

    def __str__(self):
        return self.expense_name

    objects = models.Manager()

