from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

from utils.models.abstract_models import TimeStampedModel
from utils.models.abstract_models import UUIDModel


class Organization(TimeStampedModel, UUIDModel):
    name = models.CharField(max_length=25, null=False, blank=False)
    abbr = models.CharField(max_length=10, null=False, blank=False, unique=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    registered_country = CountryField(
        blank_label="Select Country", null=False, blank=False
    )
    countries_of_operation = CountryField(blank_label="Select Countries", multiple=True)

    def __str__(self):
        return self.name


class User(AbstractUser, TimeStampedModel, UUIDModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="users"
    )
