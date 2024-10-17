from django.shortcuts import render

from rest_framework import viewsets, permissions, generics

from rest_framework.response import Response

from .models import Post, Comment

from .serializers import PostSerializer, CommentSerializer

from django_filters.rest_framework import DjangoFilterBackend

from notifications.models import Notification

from django.contrib.contenttypes.models import ContentType


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']  # Allow filtering by title and content


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)  # Only allow users to see their posts

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)  # Only allow users to see their comments


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Get all users that the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Retrieve posts from followed users
    
   class LikePostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )
            return Response({"message": "Post liked successfully."})
        else:
            return Response({"message": "You already liked this post."})

    def get_object(self, pk):
        return Post.objects.get(pk=pk)

class UnlikePostView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({"message": "Post unliked successfully."})

    def get_object(self, pk):
        return Post.objects.get(pk=pk) 