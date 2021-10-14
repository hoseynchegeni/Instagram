
from django.urls import path
from . import views

app_name = 'register'
urlpatterns =[
     path ('',views.index,name='register'),
     path('step2/',views.index_2,name='next_step'),
     path('login/',views.login,name='login'),
     path('profile/<int:id>/',views.userprofile,name='profile'),
     path('update/',views.ProfileUpdate,name='update'),
     path('change/',views.changepassword,name='change'),
     path('logout/',views.logoutuser,name='logout'),
     path('follow/<int:id>/',views.follow_user,name='follow')

]

