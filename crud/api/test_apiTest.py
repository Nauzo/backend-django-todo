from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api import views
from api.models import Tarea
from api.serializers import TareaSerializer


class DataTestList(APITestCase):
   
   
    def setUp(self):
        self.client = APIClient()
        self.todo = Tarea.objects.create(id=1,body='test01')
        self.todoSerialized = TareaSerializer(self.todo).data
    
    def test_get_api(self):
        url = reverse(views.getTarea)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_api(self):
        url = reverse(views.postTarea)
        data = self.todoSerialized
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_api(self):
        data = {"body": "Test update api"}
        response = self.client.put('/api/put/1/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_api(self):
        response = self.client.delete('/api/delete/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
