from django.contrib import admin
from .models import Book

# This class tells Django how the Book list should look
class BookAdmin(admin.ModelAdmin):
    # 1. Show these columns in the list
    list_display = ('title', 'author', 'publication_year')

    # 2. Add a search bar to find books by Title or Author
    search_fields = ('title', 'author')

    # 3. Add a filter box on the right side
    list_filter = ('publication_year', 'author')

# Register the model with the custom settings
admin.site.register(Book, BookAdmin)