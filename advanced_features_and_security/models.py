from django.db import models

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
