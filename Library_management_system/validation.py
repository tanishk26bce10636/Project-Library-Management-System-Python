def book_id_exists(books, book_id):

# Go through each book in the list
    for book in books:

 # If the book's ID matches the one we're looking for, it exists
        if book["id"] == book_id:
            return True

# No match was found after checking all books
    return False


def member_id_exists(members, member_id):

# Go through each member in the list
    for member in members:

 # If the member's ID matches the one we're looking for, it exists
        if member["id"] == member_id:
            return True

# No match was found after checking all members
    return False


def check_empty(value):

# strip() removes leading/trailing whitespace, so a string of
    # only spaces becomes "" and is treated as empty
    if value.strip() == "":
        return True

# The value contains at least one real character
    return False
