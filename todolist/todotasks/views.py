from rest_framework import generics
from . import serializers
from .models import Task
from .exceptions import BadRequestException
from ipware import get_client_ip
from django.utils import timezone
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.exceptions import ValidationError


@extend_schema_view(
    get=extend_schema(
        summary="Return a list of all the existing tasks",
    ),
    post=extend_schema(
        summary="Retrieve all tasks",
        description="Note, that if `done` is set to `false`, `done_date` cannot be set",
    ),
)
class TaskListView(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        client_ip, _ = get_client_ip(self.request)
        if client_ip is None:
            raise BadRequestException("Cannot extract ip address")

        serializer.save(author_ip=client_ip)


@extend_schema_view(
    get=extend_schema(summary="Retrieve task with the given id"),
    delete=extend_schema(summary="Delete task with the given id"),
)
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()
