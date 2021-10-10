from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class register_form(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class meta:
        model = User
        fields = ('username','email,','password','first_name','last_name')

    def save(self,commit=True):
        user = super(register_form,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class userlogin(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Email or Username'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class userupdateform(forms.ModelForm):
    class Meta:
        model= User
        fields = ['email','first_name','last_name']
    
class profileupdateform(forms.ModelForm):
    class Meta:
        model = profile
        fields =['phone','addres','birth','bio','img']


    