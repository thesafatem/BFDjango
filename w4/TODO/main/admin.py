from django.contrib import admin
from main.models import List, Task
# Register your models here.


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'due_on', 'owner', 'mark']
    ordering = ['name']
    search_fields = ['name', 'owner', 'due_on']