from django.urls import path
from . import views 
from .views import  SearchResultsView

urlpatterns=[
    path('',views.home,name="index"),
    path('home',views.home,name="home"),
    path('search/', SearchResultsView.as_view(), name='search_result'),
    #path('search_result',views.search_result,name="search_result"),
    path('content/<int:id>',views.content,name="content"), # to view content details
    path('content/new',views.add_content,name="add_content"), # to create and publish new content
    path('content/<int:id>/delete',views.delete_content,name="delete_content"), # to delete the content
    path('content/<int:id>/like',views.like,name="like"), # to like/unlike the content
    path('content/<int:id>/save',views.save,name="save"), # to save/discard the content
    path('comment/<int:id>',views.add_comment,name="add_comment"),#to add comment
    path('comment/<int:id>/remove',views.remove_comment,name="remove_comment"),#to remove the comment
    path('district/<int:id>',views.district,name="district"),#to remove the comment
    
]

