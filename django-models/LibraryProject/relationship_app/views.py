from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library, UserProfile

# --- Book Views ---
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        # Simplified for brevity; usually use a ModelForm
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        Book.objects.create(title=title, author_id=author_id)
        return redirect("list_books")
    return render(request, "relationship_app/add_book.html")

# --- Library Detail View (Class Based) ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# --- Authentication Views ---
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# --- Role-Based Views ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, DetailView
# from django.contrib.auth.decorators import user_passes_test, permission_required
# from .models import Book, Library


# # 1. Function-based view
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})


# # 2. Class-based view
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'


# # 3. Registration view
# class register(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'


# # -------- ALX REQUIRED ROLE CHECKS --------

# def is_admin(user):
#     return user.is_authenticated and user.userprofile.role == "Admin"


# def is_librarian(user):
#     return user.is_authenticated and user.userprofile.role == "Librarian"


# def is_member(user):
#     return user.is_authenticated and user.userprofile.role == "Member"


# # -------- PROTECTED VIEWS --------

# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')


# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')


# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')


# # -------- PERMISSION-BASED BOOK VIEWS --------

# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     if request.method == "POST":
#         pass
#     return render(request, 'relationship_app/add_book.html')


# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         pass
#     return render(request, 'relationship_app/edit_book.html', {'book': book})


# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         book.delete()
#         return redirect('list_books')
#     return render(request, 'relationship_app/delete_book.html', {'book': book})




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