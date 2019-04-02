from django.test import TestCase
from .models import Exam


# Create your tests here.

class ExamCreationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Exam.objects.create(task="Simple task to do:", points=0, grade="A+")
        Exam.objects.create(task="Another task with numbers to complete", points=5, grade="F")
        Exam.objects.create(task="test task", points=30, grade="C-")

    def test_exam(self):
        test_exam = Exam.objects.get(id=1)
        test_exam2 = Exam.objects.get(id=2)
        test_exam3 = Exam.objects.get(id=3)
        self.assertEqual(test_exam.points, 0)
        self.assertEqual(test_exam.grade, "A+")
        self.assertEqual(test_exam2.points, 5)
        self.assertEqual(test_exam2.grade, "F")
        self.assertEqual(test_exam3.points, 30)
        self.assertEqual(test_exam3.grade, "C-")
