from django.urls import path
from . import views 

urlpatterns=[
    path('',views.profile,name="profile"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('liked',views.liked,name="liked"),
    path('saved',views.saved,name="saved"),
    path('published',views.published,name="published"),
    
]

