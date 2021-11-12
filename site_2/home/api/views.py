from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.serializers import Serializer
from home.models import Post
from  . serializers import *

class post_list_api_view(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = postserializer

class post_detail_api_view(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = postdetailserializer
    lookup_field = 'id'


class post_delete_api_view(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = postdeleteserializer
    lookup_field = 'id'