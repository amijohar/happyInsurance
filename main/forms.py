from django.forms import ModelForm
from django import forms
from . import models



class UserForm(ModelForm):
    class Meta:
        model = models.Users
        exclude = ['user']