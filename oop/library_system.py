class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return  f"Book: {self.title} by {self.author}"

class EBook(Book):
  def __init__(self, file_size, title, author):
    super().__init__(title,author)
    self.file_size = file_size
    
  def __str__(self):
    return f"EBook: {self.title} by {self.author}, file size: {self.file_size}"
    
class PrintBook(Book):
  def __init__(self, page_count, title, author):
    super().__init__(title,author)
    self.page_count = page_count

  def __str__(self):
    return f"PrintBook: {self.title} by {self.author}, page count: {self.page_count}"
    
class Lirary:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)
    
  def list_books(self,Book,EBook,PrintBook):
    for book in self.books:
      print(f"{book}"



