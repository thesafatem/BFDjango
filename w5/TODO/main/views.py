from django.shortcuts import render
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from main.models import List, Task
from main.serializers import ListSerializer, ListRetrieveSerializer, TaskSerializer


# Create your views here.


class ListViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return List.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ListRetrieveSerializer
        return ListSerializer

    permission_classes = (AllowAny,)

    @action(methods=['GET'], detail=True, url_path='completed')
    def completed(self, request, *args, **kwargs):
        self.queryset = List.objects.all().prefetch_related(
            Prefetch('tasks', queryset=Task.objects.filter(mark=True)))

        instance = self.get_object()
        serializer = ListRetrieveSerializer(instance)
        return Response(serializer.data)
