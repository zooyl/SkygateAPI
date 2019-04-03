from django.test import TestCase
from .models import Exam, Task
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

# API Client

client = APIClient()


class ModelTest(TestCase):
    """ Model Tests """
    fixtures = ['task-exam.json']

    def test_user(self):
        test_user = User.objects.get(id=1)
        self.assertIsInstance(test_user, User)
        self.assertEqual(test_user.username, 'super-user')

    def test_task(self):
        test_task = Task.objects.get(id=1)
        test_task2 = Task.objects.get(id=2)
        test_task3 = Task.objects.get(id=3)
        self.assertEqual(test_task.task, 'SuperUserTask1')
        self.assertIsInstance(test_task, Task)
        self.assertEqual(test_task2.points, 40)
        self.assertIsInstance(test_task2, Task)
        self.assertEqual(test_task3.exam_id, 2)
        self.assertIsInstance(test_task3, Task)

    def test_exam(self):
        test_exam = Exam.objects.get(id=1)
        test_exam2 = Exam.objects.get(id=2)
        self.assertIsInstance(test_exam, Exam)
        self.assertIsInstance(test_exam2, Exam)
        self.assertEqual(test_exam.name, 'SuperUserExam1')
        self.assertEqual(test_exam2.name, 'SuperUserExam2')


class ForbiddenTest(APITestCase):
    """ Authentication required tests """

    def test_api_forbidden(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_exam_forbidden(self):
        response = self.client.get("http://127.0.0.1:8000/exam/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_task_forbidden(self):
        response = self.client.get("http://127.0.0.1:8000/task/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_exam_example_forbidden(self):
        response = self.client.get("http://127.0.0.1:8000/exam/1", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_task_example_forbidden(self):
        response = self.client.get("http://127.0.0.1:8000/task/1", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ConnectionTest(APITestCase):
    """ Tests to check if user is logged in """
    fixtures = ['task-exam.json']

    def setUp(self):
        self.client.login(username='super-user', password='mkonjibhu')

    def tearDown(self):
        self.client.logout()

    def test_api_ok(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_exam_ok(self):
        response = self.client.get("http://127.0.0.1:8000/exam/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_ok(self):
        response = self.client.get("http://127.0.0.1:8000/task/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_exam_example_ok(self):
        response = self.client.get("http://127.0.0.1:8000/exam/1", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_example_ok(self):
        response = self.client.get("http://127.0.0.1:8000/task/1", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
