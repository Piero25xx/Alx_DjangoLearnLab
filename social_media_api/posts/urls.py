from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView
from .views import FeedView


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),

#feed view
    path('feed/', FeedView.as_view(), name='user_feed'),  # Add the feed route

# likes and unlikes
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
#test
path('test/<int:pk>/', TestView.as_view(), name='test_post'),

]
