from django.db import models

# Create your models here.


class PollMan(models.Model):
    name = models.CharField(length=50)
    age = models.IntegerField()
