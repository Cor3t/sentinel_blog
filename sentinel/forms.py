from django import forms
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'post']