from rest_framework import viewsets
from .serializers import ExamSerializer
from .models import Exam
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def destroy(self, request, *args, **kwargs):
        """ Additional function to delete instance """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
