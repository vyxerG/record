from django.contrib import admin
from . models import Profile

# Register your models here.
# admin.site.register(Profile)


class ToDoProfile(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'username', 'created')


admin.site.register(Profile, ToDoProfile)
