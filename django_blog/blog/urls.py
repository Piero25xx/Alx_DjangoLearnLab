from django.urls import path
from .views import index, (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView
)
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),  # Home page
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-edit'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
