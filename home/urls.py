from django.urls import path
from . import views 

urlpatterns=[
    path('',views.home,name="index"),
    path('home',views.home,name="home"),
    path('home2',views.home2,name="home2"),
    path('search_result',views.search_result,name="search_result"),
    path('content',views.content,name="content"),
    path('add_content',views.add_content,name="add_content"),
    
]

