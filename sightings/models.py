from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.FloatField(
        blank=False,
        null=False,
    )

    Longitude = models.FloatField(
        blank=False,
        null=False,
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True,
    )

    Shift = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Date = models.DateField(
        blank=True,
        null=True,
    )

    Age = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Primary_Fur_Color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Specific_Location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Running = models.BooleanField(
        blank=True,
        null=True,
    )

    Chasing = models.BooleanField(
        blank=True,
        null=True,
    )

    Climbing = models.BooleanField(
        blank=True,
        null=True,
    )

    Eating = models.BooleanField(
        blank=True,
        null=True,
    )

    Foraging = models.BooleanField(
        blank=True,
        null=True,
    )

    Other_Activities = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Kuks = models.BooleanField(
        blank=True,
        null=True,
    )

    Quaas = models.BooleanField(
        blank=True,
        null=True,
    )

    Moans = models.BooleanField(
        blank=True,
        null=True,
    )

    Tail_Flags = models.BooleanField(
        blank=True,
        null=True,
    )

    Tail_Twitches = models.BooleanField(
        blank=True,
        null=True,
    )

    Approaches = models.BooleanField(
        blank=True,
        null=True,
    )

    Indifferent = models.BooleanField(
        blank=True,
        null=True,
    )

    Runs_From = models.BooleanField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
