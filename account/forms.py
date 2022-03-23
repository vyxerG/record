
from .models import Profile

from django.forms import forms, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            # 'first_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'first_name':'Name',
            # 'first_name':'Full Name',
        }
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'Enter name...'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Enter emailaddress example@gmail.com...'}),
        #     'username': forms.TextInput(attrs={'placeholder': 'Enter username...'}),
        # }
        # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        #     'class': 'input-text with-border', 'placeholder': 'Password'}))


        # password2 = forms.CharField(widget=forms.PasswordInput(attrs={      
        #     'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input'
            })



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'username',
        ]
