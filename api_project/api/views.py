from django.shortcuts import render, redirect
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Optional: allow anyone to see the list, but not create/delete
    permission_classes = [permissions.IsAuthenticated]

#This help route the defaualt url to the homepage / set it in the urls as well
def home(request):
    # return redirect('/api/books/')
    return JsonResponse({
        "status": "running",
        "endpoints": ["/api/books/"]
    })

# New ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
