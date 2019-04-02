from rest_framework import viewsets
from .serializers import TaskSerializer, ExamSerializer
from .models import Exam, Task
from rest_framework.response import Response
from rest_framework import status


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-points', 'exam__name', 'task')
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        """ Additional function to delete instance """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
