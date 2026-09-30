import json
import os

# Location of the JSON file used to store books
BOOK_FILE = "data/books.json"
# Location of the JSON file used to store members
MEMBER_FILE = "data/members.json"

# Function to load data from a JSON file
def load_data(file_name):

    # Create file if it does not exist
    if not os.path.exists(file_name):

 # Create the data folder if it does not exist
        os.makedirs("data", exist_ok=True)

# Create a new empty JSON file
        with open(file_name, "w") as file:
            json.dump([], file, indent=4)

# Return an empty list
        return []

    # Check if file is empty
    if os.path.getsize(file_name) == 0:
        return []

    try:

 # Open the file in read mode
        with open(file_name, "r") as file:
            # Read the JSON data and return it
            return json.load(file)

 # Handle the error if the JSON file contains invalid data
    except json.JSONDecodeError:

# Display a warning message
        print("Warning: Data file contains invalid JSON.")
        print("Starting with empty data.")

# Return an empty list
        return []


# Function to save data into a JSON file
def save_data(file_name, data):

  # Make sure the data folder exists
    os.makedirs("data", exist_ok=True)

# Open the file in write mode
    with open(file_name, "w") as file:
     # Convert the Python data into JSON and save it
     json.dump(data, file, indent=4)

# Function to load book data
def load_books():
  # Load and return the data from the books file
  return load_data(BOOK_FILE)

# Function to save book data
def save_books(books):
    # Save the books into the books JSON file
    save_data(BOOK_FILE, books)

# Function to load member data
def load_members():
  # Load and return the data from the members file
  return load_data(MEMBER_FILE)

# Function to save member data
def save_members(members):
    # Save the members into the members JSON file
    save_data(MEMBER_FILE, members)