class Library:
  def __init__(self):
    self.file = open("books.txt", "a+")

  def list_of_books(self):
    self.file.seek(0)
    book_info = self.file.read().splitlines()
    for book in book_info:
      book_data = book.split(", ")
      title = book_data[0]
      author = book_data[1]
      release_date = book_data[2]
      number_of_pages = book_data[3]
      print(f"Book Title: {title}, Author: {author}, Release Date: {release_date}, Pages: {number_of_pages}")

  def add(self):
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    release_date = input("Enter the release date: ")
    number_of_pages = input("Enter the number of pages: ")

    book_info = f"{title}, {author}, {release_date}, {number_of_pages}\n"
    self.file.write(book_info)

  def remove_book(self):
    title = input("Enter the book title to remove: ")

    
    self.file.seek(0)
    book_info = self.file.read().splitlines()
    books_list = []
    for book in book_info:
      book_data = book.split(", ")
      books_list.append(book_data)

    index = None
    for i, book in enumerate(books_list):
      if book[0] == title:
        index = i
        break
    if index is not None:
      books_list.pop(index)
      print(f"Book '{title}' removed successfully.")
    else:
      print(f"Book '{title}' not found.")

    self.file.seek(0)
    self.file.truncate(0)

    for book in books_list:
      book_info = ", ".join(book) + "\n"
      self.file.write(book_info)

  def __del__(self):
    self.file.close()


lib = Library()

while True:
  print("*** MENU ***")
  print("1) List Books")
  print("2) Add Book")
  print("3) Remove Book")
  print("4) Quit (q)")

  choice = input("Enter your choice (1-4): ")
  if choice == "4" or choice.lower() == "q":
    print("You have exited the program")
    break
  if choice == "1":
    lib.list_of_books()
  elif choice == "2":
    lib.add()
  elif choice == "3":
    lib.remove_book()
  else:
    print("Invalid choice. Please try again.")