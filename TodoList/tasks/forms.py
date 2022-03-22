from django.forms import ModelForm
from django import forms
from . models import *

class ToDoAppForm(forms.ModelForm):
    class Meta:
        model = ToDoApp
        fields = ["title","created","completed"]
        exclude = ['owner','done']  # Helps hide the owner while in the carrier

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'created': forms.DateTimeInput(attrs={'class': 'input'}),
        }
