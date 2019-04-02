from django.db import models


# Create your models here.

class Exam(models.Model):
    task = models.TextField(max_length=512)
    points = models.PositiveSmallIntegerField(default=0)
    grade = models.CharField(max_length=2)
