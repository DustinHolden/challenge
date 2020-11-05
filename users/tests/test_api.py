from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory

from users.api.serializers import UserSerializer
from users.tests.factories import UserFactory

User = get_user_model()


class UserTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='setup_user', email='setup_user@example.com', password='password')
        self.user.is_superuser = True
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        for i in range(10):
            UserFactory()

    def test_get_auth_token(self):
        url = reverse('get-auth-token')
        user = User.objects.first()
        user.set_password(raw_password='change_me_1234')
        user.save()
        data = {
            'username': user.username,
            'password': 'change_me_1234'
        }
        response = self.client.post(url, data, format='json')
        token = response.data.get('token')
        self.assertEqual(token, Token.objects.get(user=user).key)

    def test_create_user(self):
        url = reverse('api:user-list')
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'change_me_test1234',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get(username='test_user').email, 'test@example.com')

    def test_get_user(self):
        response = self.client.get('/api/users/setup_user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'username': 'setup_user', 'email': 'setup_user@example.com', 'name': '',
                          'url': 'http://testserver/api/users/setup_user/'})

    def test_list_users(self):
        users = User.objects.all()
        request = self.factory.get('/')
        serializer = UserSerializer(users, context={'request': request}, many=True)
        response = self.client.get(reverse('api:user-list'))
        self.assertEqual(response.data, serializer.data)
