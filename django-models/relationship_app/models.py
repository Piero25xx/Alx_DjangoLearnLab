from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Author model with a simple CharField
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model with a ForeignKey to Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_view_book', 'Can view book'),  # Custom permission
            ('can_edit_book', 'Can edit book'),
        ]

    def __str__(self):
        return self.title

# Library model with a ManyToMany relationship to Book
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
            ('can_view_book', 'Can view book'),
        ]

    def __str__(self):
        return self.name

# Librarian model with a OneToOne relationship to Library
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('can_view_library', 'Can view library'),  # Custom permission
            ('can_edit_library', 'Can edit library'),
        ]

    def __str__(self):
        return self.name


 Choices for user roles
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to create or update the UserProfile whenever a User is created or updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
