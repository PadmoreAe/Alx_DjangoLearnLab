from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints (CRUD, Filtering, Searching, Permissions).
    """

    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")
        # Create a book
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )
        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def test_get_all_books(self):
        """Test retrieving the list of books (Public Access)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """Test creating a book while logged in."""
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test creating a book fails if not logged in (Permissions check)."""
        data = {"title": "Forbidden Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book's title."""
        self.client.login(username='testuser', password='password123')
        data = {"title": "Updated Title", "publication_year": 1958, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_by_year(self):
        """Test filtering books by publication year."""
        response = self.client.get(self.list_url, {'publication_year': 1958})
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.list_url, {'publication_year': 2000})
        self.assertEqual(len(response.data), 0)

    def test_search_by_title(self):
        """Test searching for books by title."""
        response = self.client.get(self.list_url, {'search': 'Things'})
        self.assertEqual(len(response.data), 1)