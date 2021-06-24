from django.db import models

# Create your models here.
import enum

from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, IntegerField, DecimalField, TextField
from django.db.models.fields.files import ImageField


class ForestType(TextChoices):
    CONSERVATION = "Conservation"
    REFORESTATION = "Reforestation"
    __empty__ = "Unknown"


class Forest(models.Model):
    name = CharField(max_length=255)
    type = models.CharField(max_length=255, choices=ForestType.choices)
    image = ImageField()
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
    area_covered = IntegerField()
    country = CharField(max_length=255)
    description = TextField()
    carbon_stored = IntegerField()
    change_in_carbon_stored_in_last_30_days = IntegerField()
