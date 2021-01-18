from django.urls import path

from django.contrib.auth import views as auth_views

from . import views 

urlpatterns=[
    path('',views.profile,name="profile"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('liked',views.liked,name="liked"),
    path('saved',views.saved,name="saved"),
    path('published',views.published,name="published"),
    
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), 
        name='password_change'),

]

