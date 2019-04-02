from rest_framework import viewsets
from .serializers import TaskSerializer, ExamSerializer
from .models import Exam, Task
from .permissions import ExamPermission, TaskPermission


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (TaskPermission,)
    queryset = Task.objects.all().order_by('-points', 'exam__name', 'task')
    serializer_class = TaskSerializer


class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = (ExamPermission,)
    queryset = Exam.objects.all().order_by('-grade')
    serializer_class = ExamSerializer
