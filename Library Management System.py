import os
class Library:
  def __init__(self):
    if not os.path.exists("books.txt"):
      open("books.txt", "w").close()  
    self.file = open("books.txt", "a+")
      
      
  def list_books(self):
    try:
      self.file.seek(0)
      book_lines = self.file.read().splitlines()
      if len(book_lines) == 0:
        print("No books found.")
      else:
        for line in book_lines:
          book_info = line.split(",")
          if len(book_info) >= 2:  # Check if book_info has at least 2 elements
            book_name = book_info[0]
            author = book_info[1]
            print(f"Book Name: {book_name}, Author: {author}")
    except Exception as e:
      print(f"An error occurred: {str(e)}")

  def add_book(self):
    book_title = input("Enter the book title: ")
    book_author = input("Enter the book author: ")
    release_year = input("Enter the first release year: ")
    num_pages = input("Enter the number of pages: ")

    book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
    self.file.write(book_info)

  def remove_book(self):
    book_title = input("Enter the book title to remove: ")

    
    self.file.seek(0)
    book_lines = self.file.read().splitlines()
    books_list = []
    for line in book_lines:
      book_info = line.split(",")
      book_name = book_info[0]
      books_list.append(book_name)

    if book_title in books_list:
      book_index = books_list.index(book_title)
      del books_list[book_index]

     
      self.file.seek(0)
      self.file.truncate()

      
      for book in books_list:
        self.file.write(f"{book}\n")

      print(f"Book '{book_title}' has been removed.")
    else:
      print(f"Book '{book_title}' not found.")

def menu():
  lib = Library()
  while True:
      print("*** MENU ***")
      print("1) List Books")
      print("2) Add Book")
      print("3) Remove Book")
      print("4) Quit")

      choice = input("Enter your choice: ")
      if choice == "1":
        lib.list_books()
      elif choice == "2":
        lib.add_book()
      elif choice == "3":
        lib.remove_book()
      elif choice == "4":
        print("Goodbye!")
        break
      else:
        print("Invalid choice")

menu()