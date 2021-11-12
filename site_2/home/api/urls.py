from django.urls import path
from . import views

name = 'api'
urlpatterns = [
    path('',views.post_list_api_view.as_view(),name='api_list'),
    path('detail/<int:id>/',views.post_detail_api_view.as_view(),name='api_detail'),
    path('<int:id>/delete/',views.post_delete_api_view.as_view(),name='api_delete')
]