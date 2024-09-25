# Delete a Book

```python
from bookshelf.models import Book

# Retrieve the book instance (assuming it exists)
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book_to_delete.delete()

# Confirm the deletion by checking if any books remain
books_remaining = Book.objects.all()
print(books_remaining)

# <QuerySet []>

