from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.serializers import Serializer
from home.models import Post
from  . serializers import *

class post_list_api_view(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = postserializer