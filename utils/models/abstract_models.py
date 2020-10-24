import uuid

from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating 'created' and 'last_modified'
    """

    last_modified = models.DateTimeField(
        auto_now=True, editable=False, null=False, blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False
    )

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    id = models.CharField(
        max_length=80, default=uuid.uuid4, primary_key=True, editable=False
    )

    class Meta:
        abstract = True
