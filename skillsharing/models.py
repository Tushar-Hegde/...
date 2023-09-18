from django.db import models

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length = 200)
    about = models.TextField()

