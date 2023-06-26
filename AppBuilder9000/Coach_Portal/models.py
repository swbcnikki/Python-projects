from django.db import models

# Create your models here.
TYPE_GRADE = {
    ('K-1st','K-1st'),
    ('2nd-3rd','2nd-3rd'),
    ('4th-5th','4th-5th'),
    ('6th-7th','6th-7th'),
}

#This is for coaches to create an account
class Coach(models.Model):
    Coach_Name = models.CharField(max_length=60)
    Coach_Email = models.CharField(max_length=30)
    Coach_Grade = models.CharField(max_length=10, choices=TYPE_GRADE)



    Coaches = models.Manager()

    def __str__(self):
        return self.Coach_Name

#This is to add children into the database
class Child(models.Model):
    First_Name = models.CharField(max_length=60)
    Last_Name = models.CharField(max_length=60)
    Child_Grade = models.CharField(max_length=10, choices=TYPE_GRADE)
    Jersey_Number = models.IntegerField( default='0')
    Parent_Name = models.CharField(max_length=60)
    Parent_Phone = models.CharField(max_length=60)
    Parent_Email = models.CharField(max_length=60)
    Notes_or_Allergies = models.TextField(max_length=300)


    Children = models.Manager()

    def __str__(self):
        return self.Child_Name