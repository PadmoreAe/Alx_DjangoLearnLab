from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # The 'Follow' relationship: A user follows many users, and is followed by many users.
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

# Provide an alias expected elsewhere in the codebase/tests
# so imports like `from .models import CustomUser` work.
CustomUser = User