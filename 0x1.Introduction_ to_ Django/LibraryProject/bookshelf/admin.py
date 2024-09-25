from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # This will customize the list display in the admin interface
    list_display = ('title', 'author', 'publication_year')

    # Add search fields for easy lookup by title and author
    search_fields = ('title', 'author')

    # Add filters by publication year for more granular browsing
    list_filter = ('publication_year',)

