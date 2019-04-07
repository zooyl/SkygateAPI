# API imports
import API.serializers
import API.models
import API.permissions

# Rest imports
import rest_framework.permissions
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (API.permissions.TaskPermission, rest_framework.permissions.IsAuthenticated,
                          rest_framework.permissions.IsAdminUser)
    # queryset = API.models.Task.objects.all().order_by('-points', 'exam__name', 'task')
    serializer_class = API.serializers.TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return API.models.Task.objects.filter(exam__user_id=user.id)


class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = (API.permissions.ExamPermission, rest_framework.permissions.IsAuthenticated,
                          rest_framework.permissions.IsAdminUser)
    # queryset = API.models.Exam.objects.all().order_by('user', '-grade')
    serializer_class = API.serializers.ExamSerializer

    def get_queryset(self):
        user = self.request.user
        return API.models.Exam.objects.filter(user_id=user.id)

class AnswersViewSet(viewsets.ModelViewSet):

    serializer_class = API.serializers.AnswersSerializer
    queryset = API.models.Answers.objects.all()