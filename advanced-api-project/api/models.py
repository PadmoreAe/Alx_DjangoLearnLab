from django.db import models

# Create your models here.
class Author(models.Model):
    """Model for an Author."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model for a Book, linked to an Author."""
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # One-to-many: One author can have many books
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title