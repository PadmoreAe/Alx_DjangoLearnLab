from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# To confirm deletion:
Book.objects.all()
# Output: <QuerySet []>