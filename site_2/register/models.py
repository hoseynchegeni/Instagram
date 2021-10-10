from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class profile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField(null=True,blank=True)
    addres= models.CharField(max_length=200,null=True,blank=True)
    bio = models.CharField(max_length=100,null=True,blank=True)
    birth = models.DateField(null=True,blank=True)
    img=models.ImageField(upload_to='profile_img',null=True,blank=True)
def saveorifuleuser(sender ,**kwargs):
    if kwargs.get('created'):
        profileuser=profile(user=kwargs.get('instance'))
        profileuser.save()


post_save.connect(saveorifuleuser,sender=User)