# Admin Customization for Book Model

## Register the Book Model

In the `bookshelf/admin.py` file, register the `Book` model to make it available in the admin interface.

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

