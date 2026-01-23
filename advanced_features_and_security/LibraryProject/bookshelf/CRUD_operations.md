# CRUD Operations

## Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## Retrieve
book = Book.objects.get(title="1984")

## Update
book.title = "Nineteen Eighty-Four"
book.save()

## Delete
book.delete()