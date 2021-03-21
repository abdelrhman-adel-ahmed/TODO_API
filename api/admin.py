from django.contrib import admin

from .models import Task


@admin.register(Task)
class RegisterTask(admin.ModelAdmin):
    list_display = ["id", "title", "completed"]
    fields = ["title", "completed"]
