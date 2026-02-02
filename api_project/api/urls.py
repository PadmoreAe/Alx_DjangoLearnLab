from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


# Initialize the router
router = DefaultRouter()
# Register the ViewSet
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)), # This includes all routes registered with the router
    path('api-token-auth/', obtain_auth_token),

    path('api-auth/', include('rest_framework.urls')), # Adds a "Login" button to the API pages
]