from django.urls import path
from . import views 

urlpatterns=[
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('home2',views.home2,name="home2"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('profile',views.profile,name="profile"),
    path('profile/edit_profile',views.edit_profile,name="edit_profile"),
    path('search_result',views.search_result,name="search_result"),
]

