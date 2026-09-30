# Import functions to load and save books from the database
from database import load_books, save_books
# Import function to check whether a Book ID already exists
from validation import book_id_exists

# Function to add a new book
def add_book():

    print("\n--- Add Book ---")

# Load all existing books
    books = load_books()

# Ask the user to enter a Book ID
    book_id = input("Enter Book ID: ")

# Check if the entered Book ID already exists
    if book_id_exists(books, book_id):
        print("Book ID already exists")
        return

# Get details of the new book from the user
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category: ")

# Create a dictionary containing the book details
    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "status": "Available"
    }

# Add the new book to the list
    books.append(book)
   
    # Save the updated list of books
    save_books(books)

   # Display success message
    print("Book added successfully")

# Function to display all books
def view_books():

    print("\n--- All Books ---")

# Load all books from the database
    books = load_books()

# Check if there are no books
    if len(books) == 0:
        print("No books available.")
        return

# Go through each book in the list
    for book in books:

        print("----------------------------")
       # Display the Book ID
        print("Book ID  :", book["id"])
        # Display the book title
        print("Title    :", book["title"])
         # Display the author's name
        print("Author   :", book["author"])
        # Display the book category
        print("Category :", book["category"])
         # Display whether the book is available or issued
        print("Status   :", book["status"])


# Function to update an existing book
def update_book():

    print("\n--- Update Book ---")

    # Load all books from the database
    books = load_books()

# Ask the user for the Book ID to update
    book_id = input("Enter Book ID: ")

# Search for the book in the list
    for book in books:

 # Check whether the current book has the entered ID
        if book["id"] == book_id:

# Ask for new book details
            book["title"] = input("Enter new title: ")
            book["author"] = input("Enter new author: ")
            book["category"] = input("Enter new category: ")

# Save the updated book list
            save_books(books)

 # Display success message
            print("Book updated successfully")
       # Stop the function after updating the book
            return

  # This message is displayed if no matching Book ID is found
    print("Book not found.")

# Function to delete a book
def delete_book():

    print("\n--- Delete Book ---")

# Load all books from the database
    books = load_books()

# Ask the user for the Book ID to delete
    book_id = input("Enter Book ID: ")

 # Search for the book in the list
    for book in books:

# Check whether the current book has the entered ID
        if book["id"] == book_id:

# Remove the book from the list
            books.remove(book)
         # Save the updated list
            save_books(books)

         # Display success message
            print("Book deleted successfully")
          # Stop the function after deleting the book
            return

# This message is displayed if no matching Book ID is found
    print("Book not found.")
