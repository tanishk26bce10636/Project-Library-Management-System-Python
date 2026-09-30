# Import functions to load and save books
from database import load_books, save_books


# Function to issue a book
def issue_book():

    print("\n--- Issue Book ---")

  # Load all books from the database
    books = load_books()

# Ask the user to enter the Book ID
    book_id = input("Enter Book ID: ")

# Search for the book in the list
    for book in books:

# Check if the Book ID matches
        if book["id"] == book_id:

# Check if the book is currently available
            if book["status"] == "Available":

# Change the status of the book to Issued
                book["status"] = "Issued"
              # Save the updated book information
                save_books(books)

 # Display success message
                print("Book issued successfully.")

            else:
              # Display message if the book is already issued
                print("Book is already issued.")

# Stop the function after finding the book
            return

# Display message if the Book ID was not found
    print("Book not found.")


# Function to return a book
def return_book():

    print("\n--- Return Book ---")

# Load all books from the database
    books = load_books()

# Ask the user to enter the Book ID
    book_id = input("Enter Book ID: ")

# Search for the book in the list

    for book in books:
# Check if the Book ID matches
        if book["id"] == book_id:

 # Check if the book is currently issued
            if book["status"] == "Issued":

# Change the status of the book to Available
                book["status"] = "Available"
             # Save the updated book information
                save_books(books)

               # Display success message
                print("Book returned successfully.")

            else:
               # Display message if the book is already available
                print("Book is already available.")

# Stop the function after finding the book
            return
# Display message if the Book ID was not found
    print("Book not found.")
