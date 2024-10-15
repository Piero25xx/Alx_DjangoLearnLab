# Deleting the book instance

retrieved_book.delete()

# Checking if the book is deleted

books_remaining = Book.objects.all()
print(books_remaining)

# <QuerySet []>

