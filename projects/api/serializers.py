from rest_framework import serializers

from users.api.serializers import UserSerializer
from ..models import Project


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['title', 'description', 'status', 'start_date', 'end_date', 'url', 'users']

        extra_kwargs = {
            'url': {'view_name': 'api:project-detail', 'lookup_field': 'id'}
        }
