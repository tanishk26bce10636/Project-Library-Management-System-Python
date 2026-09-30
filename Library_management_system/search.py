# Import the function used to load books
from database import load_books

# Function to search for a book
def search_book():

    print("\n--- Search Book ---")

# Load all books from the database
    books = load_books()

 # Ask the user to enter a search keyword
    # lower() converts the keyword to lowercase
    keyword = input("Enter title, author or category: ").lower()

# Initially assume that no book has been found
    found = False

# Go through each book in the list
    for book in books:

 # Check if the keyword is present in:
        # 1. Book title
        # 2. Author name
        # 3. Book category
        if (keyword in book["title"].lower()
                or keyword in book["author"].lower()
                or keyword in book["category"].lower()):
# Display a message when a matching book is found

            print("\nBook Found")
            print("Book ID  :", book["id"])
            print("Title    :", book["title"])
            print("Author   :", book["author"])
            print("Category :", book["category"])
            print("Status   :", book["status"])

            found = True

 # After checking all books,
    # display this message if no matching book was found
    if not found:
        print("No matching book found.")
