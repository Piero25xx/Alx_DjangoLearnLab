from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book  # Adjust this to match your model's location

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and authenticate client
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')
        
        # Example books for testing
        self.book1 = Book.objects.create(title="Book One", author="Author One", price=9.99)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", price=19.99)
        
        # URLs for endpoints
        self.list_url = reverse('book-list')  # Adjust name to your URLs
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])

def test_create_book(self):
    data = {"title": "New Book", "author": "New Author", "price": 12.99}
    response = self.client.post(self.list_url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)  # Two from setup, one new
    self.assertEqual(response.data['title'], "New Book")


def test_get_books(self):
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)


def test_get_single_book(self):
    response = self.client.get(self.detail_url(self.book1.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], "Book One")


def test_update_book(self):
    data = {"title": "Updated Title", "author": "Author One", "price": 10.99}
    response = self.client.put(self.detail_url(self.book1.id), data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book1.refresh_from_db()
    self.assertEqual(self.book1.title, "Updated Title")


def test_delete_book(self):
    response = self.client.delete(self.detail_url(self.book2.id))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 1)  # One book remaining


def test_filter_books_by_price(self):
    response = self.client.get(self.list_url, {'price': 9.99})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], "Book One")


def test_search_books(self):
    response = self.client.get(self.list_url, {'search': 'Two'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], "Book Two")


def test_order_books_by_price(self):
    response = self.client.get(self.list_url, {'ordering': 'price'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['title'], "Book One")


def test_access_without_authentication(self):
    self.client.logout()  # Ensure user is logged out
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



