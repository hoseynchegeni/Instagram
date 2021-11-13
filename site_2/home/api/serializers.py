from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from home.models import Post

class postserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','text','user')

class postdetailserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class postdeleteserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class postupdateserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class postcreateserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'