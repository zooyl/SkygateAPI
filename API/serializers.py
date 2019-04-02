from .models import Exam, Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, attrs):
        """ Validation for task points (Limit is set to 100) and if field is blank """
        try:
            if attrs['points'] > 100:
                raise serializers.ValidationError('Maximum value of points is 100')
        except KeyError:
            raise serializers.ValidationError('Points row can not be blank')
        return attrs


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
