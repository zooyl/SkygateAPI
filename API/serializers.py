from .models import Exam
from rest_framework import serializers


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

    def validate(self, attrs):
        """ Validation for exam points (Limit is set to 100) """
        if attrs['points'] > 100:
            raise serializers.ValidationError('Maximum value of points is 100')
        return attrs
