from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='post_img')
    like = models.ManyToManyField(User,blank=True,null=True,related_name='post_like')
    like_counter = models.PositiveBigIntegerField(default=0)

    
    def like_counter(self):
        return self.like.count()
