from django.db import models


SEX_CHOICES = {
    ('male', 'male'),
    ('female', 'female'),
}


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=60, choices=SEX_CHOICES)
    o_average_score = models.FloatField(max_length=5, default=0)
    c_average_score = models.FloatField(max_length=5, default=0)
    e_average_score = models.FloatField(max_length=5, default=0)
    a_average_score = models.FloatField(max_length=5, default=0)
    n_average_score = models.FloatField(max_length=5, default=0)

    Persons = models.Manager()

    def __str__(self):
        return self.name


class ComparedPerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    o_percentile = models.IntegerField(null=True, blank=True)
    c_percentile = models.IntegerField(null=True, blank=True)
    e_percentile = models.IntegerField(null=True, blank=True)
    a_percentile = models.IntegerField(null=True, blank=True)
    n_percentile = models.IntegerField(null=True, blank=True)

    ComparedPersons = models.Manager()

    def __str__(self):
        return self.person.name


class SelectPerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
