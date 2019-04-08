# API imports
import API.serializers
import API.models

# Rest imports
from rest_framework import filters
import rest_framework.permissions
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (rest_framework.permissions.IsAdminUser,)
    serializer_class = API.serializers.TaskSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('title', 'task', 'points')
    ordering_fields = ('title', 'task', 'points')

    def get_queryset(self):
        user = self.request.user
        return API.models.Task.objects.filter(exam__user_id=user.id)


class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = (rest_framework.permissions.IsAdminUser,)
    serializer_class = API.serializers.ExamSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('name', 'grade', 'comments')
    ordering_fields = ('name', 'grade', 'comments')

    def get_queryset(self):
        user = self.request.user
        return API.models.Exam.objects.filter(user_id=user.id)


class AnswersViewSet(viewsets.ModelViewSet):
    serializer_class = API.serializers.AnswersSerializer
    queryset = API.models.Answers.objects.all()
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return API.models.Answers.objects.filter(test__user_id=user.id)
        return API.models.Answers.objects.filter(student_id=user.id)
