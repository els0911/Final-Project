from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.FloatField(
        blank=False,
    )

    Longitude = models.FloatField(
        blank=False,
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
    )

    Shift = models.CharField(
        max_length=100,
        blank=True,
    )

    Date = models.DateField(
        blank=True,
    )

    Age = models.CharField(
        max_length=100,
        blank=True,
    )

    Primary_Fur_Color = models.CharField(
        max_length=100,
        blank=True,
    )

    Location = models.CharField(
        max_length=100,
        blank=True,
    )

    Specific_Location = models.CharField(
        max_length=100,
        blank=True,
    )

    Running = models.BooleanField(
        blank=True,
        default=False,
    )

    Chasing = models.BooleanField(
        blank=True,
    )

    Climbing = models.BooleanField(
        blank=True,
    )

    Eating = models.BooleanField(
        blank=True,
        default=True,
    )

    Foraging = models.BooleanField(
        blank=True,
    )

    Other_Activities = models.CharField(
        max_length=100,
        blank=True,
    )

    Kuks = models.BooleanField(
        blank=True,
    )

    Quaas = models.BooleanField(
        blank=True,
    )

    Moans = models.BooleanField(
        blank=True,
    )

    Tail_Flags = models.BooleanField(
        blank=True,
    )

    Tail_Twitches = models.BooleanField(
        blank=True,
    )

    Approaches = models.BooleanField(
        blank=True,
    )

    Indifferent = models.BooleanField(
        blank=True,
    )

    Runs_From = models.BooleanField(
        blank=True,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
