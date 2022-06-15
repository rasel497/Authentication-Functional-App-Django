# from dataclasses import field
# from pyexpat import model
import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username','password1', 'password2')
