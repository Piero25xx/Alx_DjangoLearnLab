from django.contrib import admin
from django.urls import path, include 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('api/', include('api.urls')),  # Include the URLs from your api app
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
