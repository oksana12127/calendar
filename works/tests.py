# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Event

from django.contrib.auth.models import User






# initialize the APIClient app
client = Client()
# Create your tests here.

class AuthorTest(TestCase):

    def setUp(self):
        # Создание двух пользователей
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()


        Event.objects.create(
            summary='123', date='2021-04-04')




    def test_author_name(self):
        author_tokio= Event.objects.get(summary='123')
        # author_minsk = Event.objects.objectsget(summary='123', date='2021-04-04')
        self.assertEqual(
            author_tokio.get_author(), "123")
        # self.assertEqual(
        #     author_minsk.get_author(), "123 2021-04-04")


