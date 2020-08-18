from django.db import models

# Create your models here.
class CowsayModel(models.Model):
    text = models.CharField(max_length=200)