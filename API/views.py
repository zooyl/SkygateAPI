# API imports
import API.serializers
import API.models
import API.permissions
import API.filters

# Rest imports
import rest_framework.permissions
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (API.permissions.TaskPermission,
                          rest_framework.permissions.IsAdminUser)
    serializer_class = API.serializers.TaskSerializer
    filterset_class = API.filters.TaskFilter

    def get_queryset(self):
        user = self.request.user
        return API.models.Task.objects.filter(exam__user_id=user.id)


class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = (API.permissions.ExamPermission,
                          rest_framework.permissions.IsAdminUser)
    serializer_class = API.serializers.ExamSerializer
    filterset_class = API.filters.ExamFilter

    def get_queryset(self):
        user = self.request.user
        return API.models.Exam.objects.filter(user_id=user.id)


class AnswersViewSet(viewsets.ModelViewSet):
    serializer_class = API.serializers.AnswersSerializer
    queryset = API.models.Answers.objects.all()
    filterset_class = API.filters.AnswersFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return API.models.Answers.objects.filter(test__user_id=user.id)
        return API.models.Answers.objects.filter(student_id=user.id)
