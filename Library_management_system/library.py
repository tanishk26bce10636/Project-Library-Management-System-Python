# Import functions to load books and members
from database import load_books, load_members


# Function to find a book using its Book ID
def find_book(book_id):
    """
    Find a book using Book ID.
    Returns the book if found, otherwise returns None.
    """

   # Load all books from the database
    books = load_books()

# Search through each book
    for book in books:

# Check if the Book ID matches
        if book["id"] == book_id:
        # Return the book if it is found
            return book

# Return None if the book is not found
    return None


# Function to find a member using Member ID
def find_member(member_id):
    """
    Find a member using Member ID.
    Returns the member if found, otherwise returns None.
    """

 # Load all members from the database
    members = load_members()

# Search through each member
    for member in members:

# Check if the Member ID matches
        if member["id"] == member_id:
            return member

# Return None if the member is not found
    return None


# Function to check whether a book is available
def check_book_available(book_id):
    """
    Check whether a book is available for issue.
    """

 # Find the book using its ID
    book = find_book(book_id)

# If the book does not exist
    if book is None:
      # Return False because the book cannot be issued
        return False

# Check whether the book is available
    if book["status"] == "Available":
       # Return True if the book is available
       return True

# Return False if the book is already issued
    return False


# Function to get basic library statistics
def get_library_summary():
    """
    Return basic library statistics.
    """
# Load all books
    books = load_books()
    # Load all members
    members = load_members()

 # Count the total number of books
    total_books = len(books)
    # Initially set available books to zero
    available_books = 0
     # Initially set issued books to zero
    issued_books = 0
    # Count the total number of members
    total_members = len(members)
 # Go through each book
    for book in books:
  # Check if the book is available
        if book["status"] == "Available":
           # Increase available book count by 1
            available_books += 1
# Check if the book is issued
        elif book["status"] == "Issued":
          # Increase issued book count by 1
            issued_books += 1

# Create a dictionary containing library statistics
    summary = {
        "total_books": total_books,
        "available_books": available_books,
        "issued_books": issued_books,
        "total_members": total_members
    }
# Return the library summary
    return summary