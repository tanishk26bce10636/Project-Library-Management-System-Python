# Import book-related functions from the book file
from book import add_book, view_books, update_book, delete_book
# Import member-related functions from the member file
from member import add_member, view_members
# Import issue and return functions
from issue_return import issue_book, return_book
# Import search function
from search import search_book

# Main function of the Library Management System
def main():

 # Keep showing the menu until the user chooses Exit
    while True:

# Display the main heading
        print("\n======================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("======================================")

 # Display all available options
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Add Member")
        print("7. View Members")
        print("8. Issue Book")
        print("9. Return Book")
        print("10. Exit")

 # Ask the user to select an option
        choice = input("\nEnter your choice: ")
# If the user chooses 1, add a book
        if choice == "1":
            add_book()

# If the user chooses 2, display all books
        elif choice == "2":
            view_books()

 # If the user chooses 3, update a book
        elif choice == "3":
            update_book()

# If the user chooses 4, delete a book
        elif choice == "4":
            delete_book()

 # If the user chooses 5, search for a book
        elif choice == "5":
            search_book()

# If the user chooses 6, add a new member
        elif choice == "6":
            add_member()

 # If the user chooses 7, display all members
        elif choice == "7":
            view_members()

# If the user chooses 8, issue a book
        elif choice == "8":
            issue_book()

 # If the user chooses 9, return a book
        elif choice == "9":
            return_book()

# If the user chooses 10, exit the program
        elif choice == "10":
            print("Thank you for using Library Management System")
         # Stop the while loop
            break

 # If the user enters anything other than 1-10
        else:
            print("Wrong choice. Please try again.")


# This line would normally check whether this file is
# being run directly as the main program.
# It is commented here in the original code.
# if __name__ == "__main__":

# Start the Library Management System
main()
