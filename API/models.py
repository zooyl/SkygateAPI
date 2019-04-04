from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    grade = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    task = models.TextField(max_length=512)
    points = models.PositiveSmallIntegerField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
