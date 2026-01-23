from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# -------------------------
# Core Library Models
# -------------------------

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    # Custom permissions for RBAC
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name


# -------------------------
# User Profile & Roles
# -------------------------

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# -------------------------
# Signals
# -------------------------

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Default every new user to Member
        UserProfile.objects.create(user=instance, role="Member")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# # Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     # Fix this line: Change 'on_relationship_app_delete' to 'on_delete'
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

#     def __str__(self):
#         return self.title

# class Library(models.Model):
#     name = models.CharField(max_length=200)
#     books = models.ManyToManyField(Book, related_name='libraries')

#     def __str__(self):
#         return self.name

# class Librarian(models.Model):
#     name = models.CharField(max_length=200)
#     # Fix this line too: Change 'on_relationship_app_delete' to 'on_delete'
#     library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

#     def __str__(self):
#         return self.name



# # 1. Define the Badge (Profile)

# # UserProfile model with role-based access
# class UserProfile(models.Model):
#     ROLE_CHOICES = [
#         ('Admin', 'Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member'),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
#     # role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"
# # class UserProfile(models.Model):
# #     ROLE_CHOICES = [
# #         ('Admin', 'Admin'),
# #         ('Librarian', 'Librarian'),
# #         ('Member', 'Member'),
# #     ]
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

# #     def __str__(self):
# #         return f"{self.user.username} - {self.role}"

# # 2. The Robot (Signals) to create a profile automatically
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()