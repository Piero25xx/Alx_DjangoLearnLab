from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)  # Get the token for the newly created user
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data  # The user instance

        # Create or get the token for the authenticated user
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key}, status=status.HTTP_200_OK)
