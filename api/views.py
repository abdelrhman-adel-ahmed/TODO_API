from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import TaskSerializer


@api_view(["GET"])
def api(request):
    api_url = {
        "list": "/task-list/",
        "detail": "/task-detail/<str:pk>/",
        "create": "/task-create/",
        "update": "/task-update/<str:pk>/",
        "delete": "/task-delete/<str:pk>/",
    }
    return Response(api_url)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all().order_by("-id")
    # the serializer will take care of serialize the data into json formate
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def detailTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted")
