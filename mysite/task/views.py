from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import TaskSerializers
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_filds = ['completed']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
