from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from home.models import Post

class postserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'