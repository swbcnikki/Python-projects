from django.db import models

class RockLoc(models.Model):
    created_at = models.DateField()
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    address = models.CharField(max_length=60, default="", blank=True)
    location_description = models.TextField(max_length=300, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

# class EditRockLoc(models.Model):
#     updated_at = models.DateField()
#     name = models.CharField(max_length=60, default="", blank=True, null=False)
#     address = models.CharField(max_length=60, default="", blank=True)
#     location_description = models.TextField(max_length=300, default="", blank=True)
#
#     objects = models.Manager()
#
#     def __unicode__(self):
#         return u"%s" % self.name



# class RockLoc(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     location_description = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
