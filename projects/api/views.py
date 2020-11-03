from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectSerializer
from ..models import Project


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'id'

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [
        'title', 'description', 'status', 'start_date', 'end_date',
        'users__username', 'users__email', 'users__name',
    ]
    search_fields = [
        'title', 'description', 'status', 'start_date', 'end_date',
        'users__username', 'users__email', 'users__name',
    ]
