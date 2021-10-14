from django.urls import path
from . import views

app_name = 'home'

urlpatterns =[
    path('',views.home,name='home'),
    path('profile/',views.all_profile,name='profile'),
    path('test/',views.profile_link_homepage),
    path('create_post/',views.post,name='post'),
    path('like_post/<int:id>/',views.like_post,name='like'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('comment/<int:id>/',views.post_comment,name='comment'),
      path('replay/<int:id>/<int:comment_id>/',views.replay,name='replay'),
]