from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
class post_form(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['img','text']
class commentform(ModelForm):
    class Meta:
        model = Comment
        fields=['comment'] 