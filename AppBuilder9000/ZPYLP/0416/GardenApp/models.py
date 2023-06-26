from django.db import models

zone_type = [('1a', '1a'), ('1b', '1b'), ('2a', '2a'), ('2b', '2b'), ('3a', '3a'), ('3b', '3b'), ('4a', '4a'),
             ('4b', '4b'), ('5a', '5a'), ('5b', '5b'), ('6a', '6a'), ('6b', '6b'), ('7a', '7a'), ('7b', '7b'),
             ('8a', '8b'),
             ('9a', '9b'), ('9a', '9b'), ('10a', '10a'), ('10b', '10b'), ('11a', '11a'), ('11b', '11b'),
             ('12a', '12a'), ('12b', '12b'), ('13a', '13a'), ('13b', '13b'),
             ]


class Planner(models.Model):
    Vegetable_Name = models.CharField(max_length=30)
    Growing_Year = models.CharField(max_length=30, blank=True)
    Growing_Zone = models.CharField(max_length=30, blank=True)
    Sowing_Time_Frame = models.CharField(max_length=30, default='', blank=True, null=False)
    Harvest_Tips = models.TextField(max_length=300, default='', blank=True, null=True)
    General_Care_Tips = models.TextField(max_length=500, default='', blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "Garden_Planner"

    def __str__(self):
        return self.Vegetable_Name


class Tracker(models.Model):
    Vegetable_Name = models.ForeignKey(Planner, on_delete=models.CASCADE)
    Growing_Season_Observations = models.TextField(max_length=500, default='', blank=True)
    Harvest_Weight = models.CharField(max_length=30, blank=True)
    Harvest_Observations = models.TextField(max_length=500, default='', blank=True)

    objects = models.Manager()

    class Meta:
        db_table = "Garden_Tracker"

    def __str__(self):
        return self.Vegetable_Name

