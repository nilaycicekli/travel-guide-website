from django.urls import path
from . import views 

urlpatterns=[
    path('',views.home,name="index"),
    path('home',views.home,name="home"),
    path('home2',views.home2,name="home2"),
    path('profile',views.profile,name="profile"),
    path('profile/edit_profile',views.edit_profile,name="edit_profile"),
    path('search_result',views.search_result,name="search_result"),
    path('content',views.content,name="content"),
    path('profile/liked',views.liked,name="liked"),
    path('profile/saved',views.saved,name="saved"),
    path('add_content',views.add_content,name="add_content"),
    
]

