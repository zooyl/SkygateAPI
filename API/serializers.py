from .models import Exam
from rest_framework import serializers


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
