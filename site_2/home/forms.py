from django import forms
from django.contrib.auth.models import User
from .models import *
class post_form(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['img','text']