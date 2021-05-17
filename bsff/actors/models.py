from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# Create your models here.

class Actor(TimeStampedModel):
    full_name = models.CharField("Full Name", max_length=255)
    slug = AutoSlugField("Actor URL",
        unique=True, always_update=True, populate_from="full_name")
    short_name = models.CharField("First name, short name, or use-name", max_length=255)

    bio = models.TextField("Bio", )

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
