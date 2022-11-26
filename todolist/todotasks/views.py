from django.core.files.storage import get_random_string
from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import Response
from . import serializers
from .models import Task
from .exceptions import BadRequestException
from ipware import get_client_ip
from django.utils import timezone


class TaskListView(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        client_ip, _ = get_client_ip(self.request)
        if client_ip is None:
            raise BadRequestException("Cannot extract ip address")
        
        done_date = serializer.validated_data.get("done_date")
        if serializer.validated_data.get("done") is True and done_date is None:
            done_date = timezone.now().date()

        serializer.save(author_ip = client_ip, done_date=done_date)

class TaskDetailView(generics.RetrieveDestroyAPIView):
     serializer_class = serializers.TaskSerializer
     queryset = Task.objects.all()
