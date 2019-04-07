# API imports
from django.test import TestCase
import API.models
from django.contrib.auth.models import User

# Rest imports
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

# API Client

client = APIClient()


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


class GetTest(APITestCase):
    """ Tests for GET method """
    fixtures = ['task-exam.json']

    def setUp(self):
        self.client.login(username='super-user', password='mkonjibhu')

    def tearDown(self):
        self.client.logout()

    def test_task_get(self):
        response = self.client.get("http://127.0.0.1:8000/task/1", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['task'], "SuperUserTask1")

    def test_exam_get(self):
        response = self.client.get("http://127.0.0.1:8000/exam/1", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "SuperUserExam1")

    def test_all_task_get(self):
        response = self.client.get("http://127.0.0.1:8000/task/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 14)

    def test_all_exam_get(self):
        response = self.client.get("http://127.0.0.1:8000/exam/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 7)
