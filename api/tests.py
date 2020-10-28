from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from . import views
from django.contrib.auth.models import User
# Create your tests here.


class TestUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.UserAPIView.as_view(
            {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})
        self.uri = '/users/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.factory.enforce_csrf_checks = False
        request = self.factory.post(
            self.uri, {"username": "harshil", "email": "harshil@xyz.com", "password": "okok"})
        response = self.view(request)
        self.assertEqual(response.status_code, 201)

    def test_update(self):

        self.factory.enforce_csrf_checks = False
        request = self.factory.post(
            self.uri, {"username": "harshil", "email": "harshil@xyz.com", "password": "okok"})
        self.view(request)
        request = self.factory.put(
            self.uri, {"username": "ok", "email": "harshil@xyz.com", "password": "okok"})
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        request = self.factory.post(
            self.uri, {"username": "harshil", "email": "harshil@xyz.com", "password": "okok"})
        self.view(request)
        request = self.factory.delete(self.uri)
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 204)


class TestGroup(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.GroupAPIView.as_view()
        self.uri = '/groups/'

    def test_list(self):
        request = self.factory.get(self.uri)
        request.method = 'get'
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
