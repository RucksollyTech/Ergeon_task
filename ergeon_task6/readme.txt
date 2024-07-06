The functions for question 6 can be found in 
models_fetch -> fetch_functions_container -> fetch_functions_container.py

This can be ran from the shell like so:
>>> cd into ergeon_task6 directory

Open Django shell
>>> python manage.py shell

>>> from models_fetch.fetch_functions_container.fetch_functions import print_books_and_authors

Call the functions
>>> print_books_and_authors()
>>> print_authors_and_books()
>>> print_authors_and_book_counts()



