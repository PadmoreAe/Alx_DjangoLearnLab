from django.contrib import admin
from .models import Book, UserProfile, Author

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Author)