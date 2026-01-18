from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library


# 1. Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# 2. Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# 3. Registration view
class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


# Role-checking functions (ALX SAFE)
def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()


def is_librarian(user):
    return user.is_authenticated and user.groups.filter(name='Librarian').exists()


def is_member(user):
    return user.is_authenticated and user.groups.filter(name='Member').exists()


# Protected views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from django.contrib.auth import login
# from .models import Book, Library, UserProfile
# from django.views.generic.detail import DetailView
# from django.contrib.auth.decorators import user_passes_test
# from django.http import HttpResponse


# # 1. Function-based view
# def list_books(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request, 'relationship_app/list_books.html', context)

# # 2. Class-based view
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# # Registration view
# class register(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'

# # Role-checking functions
# def is_admin(user):
#     return user.is_authenticated and user.userprofile.role == 'Admin'

# def is_librarian(user):
#     return user.is_authenticated and user.userprofile.role == 'Librarian'

# def is_member(user):
#     return user.is_authenticated and user.userprofile.role == 'Member'
# # def is_admin(user):
# #     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# # def is_librarian(user):
# #     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# # def is_member(user):
# #     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# # Protected views with role-based access control
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')







# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from django.contrib.auth import login
# from .models import Book
# from .models import Library
# from django.views.generic.detail import DetailView
# from django.contrib.auth.decorators import user_passes_test


# # 1. Function-based view (The Simple Helper)
# def list_books(request):
#     books = Book.objects.all()  # Fetch all books from the database
#     context = {'books': books}  # Create a dictionary to pass to the template
#     return render(request, 'relationship_app/list_books.html', context)

# # 2. Class-based view (The Super Robot)
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# # This is our Registration "Tool"
# class register(CreateView):
#     form_class = UserCreationForm()
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'



# # Functions to check roles
# def is_admin(user):
#     return user.is_authenticated and user.userprofile.role == 'Admin'

# def is_librarian(user):
#     return user.is_authenticated and user.userprofile.role == 'Librarian'

# def is_member(user):
#     return user.is_authenticated and user.userprofile.role == 'Member'

# # The Protected Views
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')