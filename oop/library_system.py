class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author


class EBook(Book):
  def __init__(self, file_size, title, author):
    super().__init__(title)
    super().__init(author)
    self.file_size = file_size

class PrintBook(Book):
  def __init__(self, page_count, title, author):
    super().__init__(title)
    super().__init(author)
    self.page_count = page_count

class Lirary:
  def __init__(self):
    self.books = Book()

  def add_book(self, book):
    self.book = Book()
    self.book = EBook()
    self.book = PrintBook()
    
  def list_books(self,Book,EBook,PrintBook):
    self.Book = Book
    self.EBook = EBook
    sel.PrintBook = PrintBook
    print(f"Book:{self.Book}")
    print(f"EBook:{self.EBook")
    print(f"PrintBook:{self.PrintBook")




