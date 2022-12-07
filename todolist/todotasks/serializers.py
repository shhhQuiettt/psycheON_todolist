from rest_framework import serializers
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    author_ip = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ["id", "title", "done", "author_ip", "created_date", "done_date"]

    def validate(self, attrs):
        if attrs.get("done") is False and attrs.get("done_date") is not None:
            raise serializers.ValidationError(
                "If task is not done, it cannot have done_date"
            )
        return attrs

    def save(self, *args, **kwargs):
        if self.validated_data["done"] and self.validated_data.get("done_date") is None:
            self.validated_data["done_date"] = timezone.now().date()

        super().save(*args, **kwargs)
