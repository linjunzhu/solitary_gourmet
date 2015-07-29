import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    content = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    avatar = models.FileField(blank=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)

