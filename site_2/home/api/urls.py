from django.urls import path
from . import views

name = 'api'
urlpatterns = [
    path('',views.post_list_api_view.as_view(),name='api_list')
]