from django.db import models




TRAIL_DIFFICULTY = [
    ("Easy", "1 - Easy"),
    ("Easy/Intermediate", "2 - Easy/Intermediate"),
    ("Intermediate", "3 - Intermediate"),
    ("Intermediate/Difficult", "4 - Intermediate/Difficult"),
    ("Difficult", "5 - Difficult"),
    ("Very Difficult", "6 - Very Difficult"),
]

US_STATES = [
    ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"),
    ("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"),
    ("FL", "Florida"), ("GA", "Georgia"), ("HI", "Hawaii"), ("ID", "Idaho"),
    ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"), ("KS", "Kansas"),
    ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"),
    ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"), ("MS", "Mississippi"),
    ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"), ("NH", "New Hampshire"),
    ("NJ", "New Jersey"), ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"),
    ("ND", "North Dakota"), ("NV", "Nevada"), ("OH", "Ohio"), ("OK", "Oklahoma"),
    ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"), ("SC", "South Carolina"),
    ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"), ("UT", "Utah"),
    ("VA", "Virginia"), ("VT", "Vermont"), ("WA", "Washington"), ("WV", "West Virginia"),
    ("WI", "Wisconsin"), ("WY", "Wyoming"),
]

WATER = [
    ("Yes", "Yes"),
    ("No", "No"),
    ("Only with purifier", "Only with purifier"),
]


class ReviewTrail(models.Model):
    trail_name = models.CharField(max_length=60)
    rider_name = models.CharField(max_length=60, blank=True)
    nearest_city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=60, choices=US_STATES)
    water_available = models.CharField(max_length=20, choices=WATER, blank=True)
    review = models.TextField()
    difficulty = models.CharField(max_length=60, choices=TRAIL_DIFFICULTY)

    objects = models.Manager()

    def __str__(self):
        return self.trail_name