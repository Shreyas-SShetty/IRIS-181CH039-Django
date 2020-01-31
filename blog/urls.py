# urls.py receives the requests from the templates and passes to views.py 
from django.urls import path
from . import views

urlpatterns = [
    # Get the homepage
    path('', views.post_list, name='post_list'),
    # Get the details of that particular object
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Add a new object
    path('post/new/', views.post_new, name='post_new'),
    # Edit a post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # Remove a post
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    # Error page for insufficient balance
    path('drafter/', views.post_open, name='post_open'),
    # Subtract amount from Buyer and add it to seller
    path('update/<pk>/', views.post_update, name='post_update'),
    # Add a new  user
    path('register/',views.register, name='register'),
]
