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
        blank=False,
        unique=True,
    )

    Shift = models.CharField(
        max_length=100,
        blank=False,
    )

    Date = models.DateField(
        blank=False,
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
        default=False,
    )

    Climbing = models.BooleanField(
        blank=True,
        default=False,
    )

    Eating = models.BooleanField(
        blank=True,
        default=False,
    )

    Foraging = models.BooleanField(
        blank=True,
        default=False,
    )

    Other_Activities = models.CharField(
        max_length=100,
        blank=True,
    )

    Kuks = models.BooleanField(
        blank=True,
        default=False,
    )

    Quaas = models.BooleanField(
        blank=True,
        default=False,
    )

    Moans = models.BooleanField(
        blank=True,
        default=False,
    )

    Tail_Flags = models.BooleanField(
        blank=True,
        default=False,
    )

    Tail_Twitches = models.BooleanField(
        blank=True,
        default=False,
    )

    Approaches = models.BooleanField(
        blank=True,
        default=False,
    )

    Indifferent = models.BooleanField(
        blank=True,
        default=False,
    )

    Runs_From = models.BooleanField(
        blank=True,
        default=False,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
