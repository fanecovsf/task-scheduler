from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):


    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    path = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000, blank=True, null=True)
    schedule_param = models.CharField(max_length=50, blank=True, null=True)
    last_execution = models.DateTimeField(null=True, blank=True)
    next_execution = models.DateTimeField(null=True, blank=True)
    executions = models.IntegerField()
    active = models.BooleanField(blank=False, null=False)


class TaskExecutions(models.Model):


    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    execution_date = models.DateTimeField(null=False, blank=False)
