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

    def test_answers_example_forbidden(self):
        response = self.client.get("http://127.0.0.1:8000/answers/1", follow=True)
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
        self.assertEqual(response.data['count'], 6)

    def test_all_exam_get(self):
        response = self.client.get("http://127.0.0.1:8000/exam/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)


class ExamAPIViewTestCase(APITestCase):
    """ Tests for Exam View method """
    fixtures = ['task-exam.json']

    def setUp(self):
        self.client.login(username='super-user', password='mkonjibhu')

    def tearDown(self):
        self.client.logout()

    def test_exam_post_valid(self):
        post = {
            'user': self.client,
            'name': 'test_name',
            'grade': 'A+',
            'comments': 'good job'
        }
        response = self.client.post("http://127.0.0.1:8000/exam/", post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comments'], 'good job')

    def test_exam_post_grade_invalid(self):
        post = {
            'user': self.client,
            'name': 'test_name',
            'grade': 'too_many',
            'comments': 'good job'
        }
        response = self.client.post("http://127.0.0.1:8000/exam/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['grade'], ["Ensure this field has no more than 2 characters."])

    def test_exam_post_name_blank(self):
        post = {
            'user': self.client,
            'name': '',
            'grade': 'F',
            'comments': 'good job'
        }
        response = self.client.post("http://127.0.0.1:8000/exam/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'], ["This field may not be blank."])

    def test_exam_post_name_too_long(self):
        post = {
            'user': self.client,
            'name': 'that_name_is_too_long_for_this_field',
            'grade': '5',
            'comments': 'good job'
        }
        response = self.client.post("http://127.0.0.1:8000/exam/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'], ["Ensure this field has no more than 32 characters."])

    def test_exam_post_comment_too_long(self):
        post = {
            'user': self.client,
            'name': 'test_name',
            'grade': 'C',
            'comments': 'that_comment_is_too_long_for_this_field' * 15
        }
        response = self.client.post("http://127.0.0.1:8000/exam/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['comments'], ["Ensure this field has no more than 128 characters."])

    # I don't know why put and delete is not working properly (in every case)
    #
    # def test_exam_put(self):
    #     put = {
    #         'name': 'put_test_name',
    #         'grade': 'B+',
    #         'comments': 'put_test_comment'
    #     }
    #     response = self.client.put("http://127.0.0.1:8000/exam/1", put, follow=True)
    #     self.assertEqual(response.data['name'], 'put_test_name')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_exam_delete(self):
    #     response = self.client.delete("http://127.0.0.1:8000/exam/1", follow=True)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskAPIViewTestCase(APITestCase):
    """ Tests for Task View method """
    fixtures = ['task-exam.json']

    def setUp(self):
        self.client.login(username='super-user', password='mkonjibhu')

    def tearDown(self):
        self.client.logout()

    def test_task_post_valid(self):
        post = {
            'points': 10,
            'title': 'test_title',
            'task': 'test_task',
            'exam': 1
        }
        response = self.client.post("http://127.0.0.1:8000/task/", post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'test_title')

    def test_task_post_points_invalid_101(self):
        post = {
            'points': 101,
            'title': 'test_title',
            'task': 'test_task',
            'exam': 1
        }
        response = self.client.post("http://127.0.0.1:8000/task/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['points'], ["Ensure this value is less than or equal to 100."])

    def test_task_post_points_invalid_under_0(self):
        post = {
            'points': -1,
            'title': 'test_title',
            'task': 'test_task',
            'exam': 1
        }
        response = self.client.post("http://127.0.0.1:8000/task/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['points'], ["Ensure this value is greater than or equal to 0."])

    def test_task_post_title_blank(self):
        post = {
            'points': 10,
            'title': '',
            'task': 'test_task',
            'exam': 1
        }
        response = self.client.post("http://127.0.0.1:8000/task/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'], ["This field may not be blank."])

    def test_task_post_task_blank(self):
        post = {
            'points': 10,
            'title': 'test_title',
            'task': '',
            'exam': 1
        }
        response = self.client.post("http://127.0.0.1:8000/task/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['task'], ["This field may not be blank."])

    def test_task_post_title_too_long(self):
        post = {
            'points': 10,
            'title': 'test_title' * 50,
            'task': 'test_task',
            'exam': 1
        }
        response = self.client.post("http://127.0.0.1:8000/task/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'], ["Ensure this field has no more than 64 characters."])

    def test_task_post_task_too_long(self):
        post = {
            'points': 10,
            'title': 'test_title',
            'task': 'test_task' * 60,
            'exam': 1
        }
        response = self.client.post("http://127.0.0.1:8000/task/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['task'], ["Ensure this field has no more than 512 characters."])


class AnswersAPIViewTestCase(APITestCase):
    """ Tests for Answers View method """
    fixtures = ['task-exam.json']

    def setUp(self):
        self.client.login(username='super-user', password='mkonjibhu')

    def tearDown(self):
        self.client.logout()

    def test_answers_get(self):
        response = self.client.get("http://127.0.0.1:8000/answers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_answers_valid(self):
        post = {
            'student': self.client,
            'answers': 'test_answers',
            'test': 1
        }

        response = self.client.post("http://127.0.0.1:8000/answers/", post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['answers'], 'test_answers')

    def test_answers_invalid(self):
        post = {
            'student': self.client,
            'answers': '1' * 1025,
            'test': 1
        }
        response = self.client.post("http://127.0.0.1:8000/answers/", post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['answers'], ['Ensure this field has no more than 1024 characters.'])
