import pdb
from models.author import Author 
from models.book import Book 

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author('Patrick Ness')
author_repository.save(author1)

author2 = Author("Nina Lacor")
author_repository.save(author2)


book1 = Book("Monsters of Men", author1, "Fantasy")
book_repository.save(book1)

book2 = Book("We are OK", author2, "LGBT")
book_repository.save(book2)

pdb.set_trace()