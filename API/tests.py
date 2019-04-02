from django.test import TestCase
from .models import Exam, Task
from django.contrib.auth.models import User


class TaskCreationTest(TestCase):
    """ Model Tests """

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test_user')
        Exam.objects.create(user_id=1, name='test_name')
        Task.objects.create(task="Simple task to do:", points=0, exam_id=1)
        Task.objects.create(task="Another task with numbers to complete", points=5, exam_id=1)
        Task.objects.create(task="test_task", points=30, exam_id=1)

    def test_user_creation(self):
        test_user = User.objects.get(id=1)
        self.assertIsInstance(test_user, User)
        self.assertEqual(test_user.username, 'test_user')

    def test_task_creation(self):
        test_task = Task.objects.get(id=1)
        test_task2 = Task.objects.get(id=2)
        test_task3 = Task.objects.get(id=3)
        self.assertEqual(test_task.task, 'Simple task to do:')
        self.assertIsInstance(test_task, Task)
        self.assertEqual(test_task2.points, 5)
        self.assertIsInstance(test_task2, Task)
        self.assertEqual(test_task3.exam_id, 1)
        self.assertIsInstance(test_task3, Task)

    def test_exam_creation(self):
        test_exam = Exam.objects.get(id=1)
        self.assertIsInstance(test_exam, Exam)
        self.assertEqual(test_exam.name, 'test_name')
