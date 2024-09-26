from django.urls import path
from .views import list_books
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),  # Add your home view here
    path('books/', views.list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
]

