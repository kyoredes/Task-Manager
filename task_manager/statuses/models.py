from django.db import models
from django.db import models
# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=200)
    