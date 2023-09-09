from rest_framework import serializers

from main.models import Task


class TaskSerializer(serializers.ModelSerializer):


    class Meta:
        model = Task
        fields = [
            "id",
            "created_at",
            "name",
            "path",
            "description",
            "schedule_param",
            "last_execution",
            "next_execution",
            "executions",
            "active",
        ]