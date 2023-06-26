from django.db import models

# Create your models here.
Gender_options = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}


class User(models.Model):
    Name = models.CharField(max_length=40)
    Age = models.IntegerField(default='')
    Gender = models.CharField(default="gender", max_length=40, choices=Gender_options)
    score = models.FloatField(default=0, max_length=4)

    Users = models.Manager()

    def __str__(self):
        return self.Name


class ChooseUser(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)

