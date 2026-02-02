from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#This help route the defaualt url to the homepage / set it in the urls as well
def home(request):
    # return redirect('/api/books/')
    return JsonResponse({
        "status": "running",
        "endpoints": ["/api/books/"]
    })

# New ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer