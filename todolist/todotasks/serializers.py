from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    author_ip = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ["id", "title", "done", "author_ip", "created_date", "done_date"]
