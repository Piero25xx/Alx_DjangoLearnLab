from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

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

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

# Custom User Manager
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    username = None  # remove username field
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

