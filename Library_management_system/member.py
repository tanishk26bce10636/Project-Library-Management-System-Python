# Import functions to load and save member data
from database import load_members, save_members

# Function to add a new member
def add_member():

    print("\n--- Add Member ---")
   # Load all existing members
    members = load_members()

 # Ask the user to enter a Member ID
    member_id = input("Enter Member ID: ")

# Search through all existing members
    for member in members:

# Check if the entered Member ID already exists
        if member["id"] == member_id:
           # Display an error message
            print("Member ID already exists")
         # Stop the function
            return

# Ask the user to enter member details
    name = input("Enter Member Name: ")
    phone = input("Enter Phone Number: ")

# Create a dictionary containing the member details
    member = {
        "id": member_id,
        "name": name,
        "phone": phone
    }

 # Add the new member to the members list
    members.append(member)
  # Save the updated members list
    save_members(members)

# Display success message
    print("Member added successfully")

# Function to display all members
def view_members():

    print("\n--- All Members ---")
   # Load all members from the database
    members = load_members()

# Check if there are no members
    if len(members) == 0:
      # Display message if the list is empty
        print("No members available.")
      # Stop the function
        return

# Go through each member in the list
    for member in members:

        print("----------------------------")
# Display the Member ID
        print("Member ID :", member["id"])
        print("Name      :", member["name"])
        print("Phone     :", member["phone"])
