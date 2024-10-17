# accounts/urls.py

from django.urls import path
from .views import RegisterView, LoginView,follow_user, unfollow_user, CustomUserListView, CustomUserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

# follow and unfollow 
path('follow/<int:user_id>/', follow_user, name='follow_user'),
path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),

#users 
path('users/', CustomUserListView.as_view(), name='user-list'),  # Endpoint to list users
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),  # Endpoint for user details
]