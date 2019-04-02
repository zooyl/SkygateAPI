from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExamSerializer
from .models import Exam


# Create your views here.

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
