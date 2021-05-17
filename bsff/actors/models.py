from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Actor(TimeStampedModel):
    full_name = models.CharField("Full Name", max_length=255)
    slug = AutoSlugField("Actor URL",
        unique=True, always_update=True, populate_from="full_name")
    short_name = models.CharField("First name, short name, or use-name", max_length=255, blank=True)

    bio = models.TextField("Bio", blank=True)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("actors:detail", kwargs={"slug": self.slug})
    

    class Meta:
        ordering = ['full_name']
