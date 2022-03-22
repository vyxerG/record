from django.contrib import admin
from . models import ToDoApp



# Register your models here.


class TodoTask(admin.ModelAdmin):
    list_display = ('owner', 'title', 'completed', 'created', 'done')

admin.site.register(ToDoApp, TodoTask)