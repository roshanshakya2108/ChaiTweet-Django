from django.urls import path
from . import views

urlpatterns = [
    # List all tweets
    path('', views.tweet_list, name='tweet_list'),

    # Create a new tweet
    path('tweet/create/', views.tweet_create, name='tweet_create'),

    # Edit an existing tweet
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),

    # Delete a tweet
    path('/<int:tweet_id>/delete/',
         views.tweet_delete, name='tweet_delete'),

    # Register
    path('register/',
         views.register, name='register'),
]
