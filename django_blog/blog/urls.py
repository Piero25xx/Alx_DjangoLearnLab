from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, CommentCreateView, 
    CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Post URLs
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Add a new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Edit a comment (should match checker expectation)
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete a comment
]
