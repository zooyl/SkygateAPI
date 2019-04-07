# API imports
from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    grade = models.CharField(max_length=2, blank=True)
    comments = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=64)
    task = models.TextField(max_length=512)
    points = models.PositiveSmallIntegerField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)


class Answers(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    answers = models.TextField(max_length=1024)
    test = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
