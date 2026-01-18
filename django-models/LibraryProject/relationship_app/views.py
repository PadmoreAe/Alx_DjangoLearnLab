from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login 
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# 1. Function-based view (The Simple Helper)
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    context = {'books': books}  # Create a dictionary to pass to the template
    return render(request, 'relationship_app/list_books.html', context)

# 2. Class-based view (The Super Robot)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# This is our Registration "Tool"
class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'