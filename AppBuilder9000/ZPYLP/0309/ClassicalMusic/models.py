

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE_CHOICES = [
    ('individual', 'individual'),
    ('ensemble', 'ensemble'),
]

ROLE_TYPE_CHOICES = [
    ('author_type', 'Composer, lyricist, etc'),
    ('performer', 'performer'),
]

# on_delete=models.SET_NULL, null=True

# Roles are aall the roles musicians can have. The author type roles like composer and the performer type roles like conductor or violin or orchestra
class Role(models.Model):
    role = models.CharField(max_length=120, verbose_name="Role", default="", blank=False, null=False)
    type = models.CharField(max_length=20,verbose_name="Type", choices=TYPE_CHOICES, blank=False, null=False)
    role_type = models.CharField(max_length=20,verbose_name="Type of contributor", choices=ROLE_TYPE_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.role

#Musician can be an individual or an ensemble, it can be a composer, performer, conductor etc. This is the actual person or group
# For now a musician can have only one role.
class Musician(models.Model):
    name = models.CharField(max_length=120, verbose_name="Musician name", default="", blank=False, null=False)
    sort_name = models.CharField(max_length=120, verbose_name="Musician sort name", default="", blank=False, null=False)
    type = models.CharField(max_length=20,verbose_name="Type", choices=TYPE_CHOICES, blank=False, null=False)
    gender = models.CharField(max_length=120, verbose_name="Musician gender", default="", blank=True, null=False)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=False)
    Life_begin = models.CharField(max_length=20, verbose_name="Life begin", default="", blank=True, null=False)
    Life_end = models.CharField(max_length=20, verbose_name="Life end", default="", blank=True, null=False)
    life_ended = models.BooleanField(verbose_name="Deceased/Dissolved", blank=True, null=True)
    image_url = models.CharField(max_length=260, verbose_name="Image URL", default="", blank=True, null=False)
    MBID = models.CharField(max_length=80, verbose_name="Musician MBID", default="", blank=True, null=False)

    def __str__(self):
        return self.name

# a composition can have many authors (composer and lyricist) and can have many roles (instrumentation)
class Composition(models.Model):
    title = models.CharField(max_length=180, verbose_name="Title", default="", blank=False, null=False)
    authors = models.ManyToManyField(Musician)
    instrumentation = models.ManyToManyField(Role)

    def __str__(self):
        return self.title


# If a composition has no movements the defualt is one movement
class Movement(models.Model):
    title = models.CharField(max_length=180, verbose_name="Movement Title", default="", blank=False, null=False)
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    order_number = models.IntegerField(verbose_name="#")

    def __str__(self):
        string = "{}: {}".format(self.composition, self.title)
        return string

class ReleaseManager(models.Manager):
    def compositions(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT release.id, release.title, composition.id, composition.title, GROUP_CONCAT(DISTINCT author.name) AS author_names, GROUP_CONCAT(DISTINCT performer.name) AS performer_names, release.image_url

                FROM ClassicalMusic_release AS release
                LEFT OUTER JOIN ClassicalMusic_track as track ON release.id=track.release_id
                LEFT OUTER JOIN ClassicalMusic_movement as movement ON movement.id=track.movement_id
                LEFT OUTER JOIN ClassicalMusic_composition as composition ON composition.id=movement.composition_id
                LEFT OUTER JOIN ClassicalMusic_composition_authors AS comp_auth ON comp_auth.composition_id=composition.id
                LEFT OUTER JOIN ClassicalMusic_musician AS author ON comp_auth.musician_id=author.id
                
                LEFT OUTER JOIN ClassicalMusic_track_performers as track_perf ON track_perf.track_id=track.id
                LEFT OUTER JOIN ClassicalMusic_musician as performer ON track_perf.musician_id=performer.id
                
                GROUP BY release.id, composition.id
                ORDER BY release.title, release.id, composition.title
                """)
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], title=row[1])
                p.composition_id = row[2]
                p.composition_title = row[3]
                p.author_names = row[4]
                p.performer_names = row[5]
                p.image_url = row[6]
                result_list.append(p)
        return result_list

class Release(models.Model):
    title = models.CharField(max_length=180, verbose_name="Title", default="", blank=False, null=False)
    image_url = models.CharField(max_length=260, verbose_name="Cover art URL", default="", blank=True, null=False)
    objects = ReleaseManager()

    def __str__(self):
        return self.title



# recording are handled at the movement level, because sometimes only individual movements are recorded in stead of the entire composition
class Track(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.PROTECT)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    performers = models.ManyToManyField(Musician)
    disk = models.CharField(max_length=180, verbose_name="Disk", default="", blank=False, null=False)
    track_number = models.IntegerField()

    def __str__(self):
        return "{}".format(self.movement)


