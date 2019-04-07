# API imports
import API.models

# Rest imports
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    points = serializers.IntegerField(default=0, min_value=0, max_value=100)

    class Meta:
        model = API.models.Task
        fields = '__all__'


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    """ It sets user_id to actually logged user """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = API.models.Exam
        fields = '__all__'


class AnswersSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = API.models.Answers
        fields = '__all__'
