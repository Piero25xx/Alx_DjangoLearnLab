from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
]

