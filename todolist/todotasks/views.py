from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import Response
from . import serializers
from .models import Task
from .exceptions import BadRequestException
from ipware import get_client_ip


class TaskListView(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        client_ip, _ = get_client_ip(self.request)
        if client_ip is None:
            raise BadRequestException("Cannot extract ip address")
        serializer.save(author_ip = client_ip)

class TaskDetailView(generics.RetrieveDestroyAPIView):
     serializer_class = serializers.TaskSerializer
     queryset = Task.objects.all()
