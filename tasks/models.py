from django.db import models
from account.models import Profile
import uuid
from django.utils import timezone
from datetime import datetime, date

# Create your models here.

class ToDoApp(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)#owner
    title = models.TextField(max_length=2000)
    completed = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(default=timezone.now, auto_now_add=False, auto_now=False, blank=True)
    # difference btw auto_now and auto_now_add is that auto_now updates the date and time as you update the record while auto_now_add does not update the date and time NOTE: when set to True
    done = models.DateTimeField(auto_now=True,  null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)#Override uuid 

    # @property
    # def tasks(self):  # By doing values_list() this gets the values of the owner then by specifying the 'owner__id' gets the particular user id
    #     # This helps us get the id of a particular owner
    #     queryset = self.review_set.all().values_list('owner__id', flat=True)
    #     # when we say (flat=True) is gonna convert it into a true list.So it won't even be an object.
    #     return queryset
    class Meta:
        ordering = ("-created","-done")

    def __str__(self):
        return self.title

class Task(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)#owner
    todo = models.ForeignKey(ToDoApp, on_delete=models.CASCADE, blank=True, null=True)#owner
    # created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)#Override uuid 

    # class Meta:
    #     unique_together = [['owner', 'todo']]

    def __str__(self):
        return self.owner