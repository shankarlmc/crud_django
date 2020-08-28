from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyForm(forms.ModelForm):
    # create meta class
    class Meta:
        model = Blog
        # specify the fields which use

        fields = [
            "title",
            "description",
            "author",
            "feature_image",
            "is_active",
        ]


class MyRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


