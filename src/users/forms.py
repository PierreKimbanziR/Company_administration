from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email' , 'password1', 'password2']