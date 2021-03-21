from django.urls import path

from .views import *

app_name = "api"
urlpatterns = [
    path("", api, name="main"),
    path("task-list/", taskList, name="taskList"),
    path("task-detail/<str:pk>/", detailTask, name="detail"),
    path("task-create/", createTask, name="createTask"),
    path("task-update/<str:pk>/", updateTask, name="updatTask"),
    path("task-delete/<str:pk>/", deleteTask, name="deleteTask"),
]
