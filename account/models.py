from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    # AutoMAtically generate time for each creation
    created = models.DateTimeField(default=timezone.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)  # Override uuid

    
    def __str__(self):
        return str(self.username)
