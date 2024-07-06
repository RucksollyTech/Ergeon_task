from ..models import Book,Author
from django.db.models import Count

''' 
Question 6.1 : 
Using Django ORM, write a function that will print the book title and the author name (who wrote it) for
all the books we have in the database 
'''

def print_books_and_authors():
    books = Book.objects.select_related('author').all()
    for book in books:
        print(f'"{book.title}". {book.author.name}')

# Example usage
# print_books_and_authors()



''' 
Question 6.2 : 
Write another function that will print the author’s name and all the books he wrote. For all the authors we
have in the database.
'''

def print_authors_and_books():
    authors = Author.objects.prefetch_related('book_set').all()
    for author in authors:
        books = author.book_set.all()
        book_titles = ', '.join([f'"{book.title}"' for book in books])
        print(f'{author.name}: {book_titles}')

# Example usage
# print_authors_and_books()


''' 
Question 6.3 : 
Implement the third function, it should print the author’s name and the number of books he wrote. Order
by the number of books written, descending.
'''

def print_authors_and_book_counts():
    authors = Author.objects.annotate(book_count=Count('book')).order_by('-book_count')
    for author in authors:
        print(f'{author.name}: {author.book_count}')

# Example usage
# print_authors_and_book_counts()
