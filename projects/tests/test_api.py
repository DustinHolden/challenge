from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory

from projects.api.serializers import ProjectSerializer
from projects.models import Project
from projects.tests.factories import ProjectFactory

User = get_user_model()


class ProjectTest(APITestCase):
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
            ProjectFactory()

    def test_create_project(self):
        url = reverse('api:project-list')
        data = {
            'title': 'test_project',
            'description': 'test_description',
            'status': 'ACTIVE',
            'start_date': '2020-01-01',
            'end_date': '2020-12-31',
            # 'users':
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.get(title='test_project').title, 'test_project')

    def test_get_project(self):
        project = Project.objects.first()
        response = self.client.get('/api/projects/{}/'.format(project.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ProjectSerializer(project, context={'request': self.factory.get('/')}).data)

    def test_list_projects(self):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, context={'request': self.factory.get('/')}, many=True)
        response = self.client.get(reverse('api:project-list'))
        self.assertEqual(response.data, serializer.data)
