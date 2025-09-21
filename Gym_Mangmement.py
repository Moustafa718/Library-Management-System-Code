import time 
import os
#clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Global list to store all member objects
membership_list = []

class Member:
    """
    Represents a gym member with personal details and membership status.
    """
    def __init__(self, first_name, last_name, membership_ID, status):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_ID = membership_ID
        self.status = status

    def output(self):
        """
        Displays all information about the member.
        """
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Membership ID: {self.membership_ID}")
        print(f"Status: {self.status}")
        print("_" * 20)  # Visual separator
    

def user_input():
    """
     Collects information from the user to create a new member.
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    membership_ID = input("Enter your membership ID: ")
    status = input("Enter your membership status, or press enter: ")
    
    # Default to inactive if not explicitly set to active
    if status.lower() != "active":
        status = "inactive"
    
    return Member(first_name, last_name, membership_ID, status)


def display_menu():
    """
    Shows the main menu options for the gym management system.
    """
    clear()
    print("Welcome to Gym Membership Management\n")
    print("Choose an Action:\n")
    print("1. Add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit\n")


def search_member(membership_list):
    """
    Allows searching for members based on different criteria.
    """
    clear()
    print("Search by\n")
    print("1. Membership ID")
    print("2. First Name")
    print("3. Membership status\n")
    
    found_members = []  # Store matching members

    search_choice = input("Enter your choice: ")
    
    # Search by membership ID (exact match)
    if search_choice == "1":
        search_id = input("Enter the membership ID to search: ") 
        for member in membership_list:
            if member.membership_ID == search_id:
                found_members.append(member)
                break  # Assuming IDs are unique

    # Search by first name 
    elif search_choice == "2":
        first_name = input("Enter the first name to search: ")
        for member in membership_list:
            if member.first_name.lower() == first_name.lower():
                found_members.append(member)

    # Search by status 
    elif search_choice == "3":
        membership_status = input("Enter the membership status to search (active/inactive): ")
        for member in membership_list:
            if member.status.lower() == membership_status.lower():
                found_members.append(member)

    # Display search results
    if found_members:
        clear()
        print("Member(s) found:\n")
        for member in found_members:
            member.output()
    else:
        print("No members found matching your criteria!")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")
    
    # Add a new member
    if choice == "1":
        membership_list.append(user_input())
        print("Member added successfully!")
        time.sleep(2)  # Pause 2 second

    # Display all members
    elif choice == "2":
        print("Displaying all members...\n")
        time.sleep(2)  # pause 
        
        if membership_list:
            for member in membership_list:
                member.output()
                time.sleep(1)  # Pause between members
        else:
            print("Member list is empty")
            time.sleep(2)
    
    # Search for a member
    elif choice == "3":
        if membership_list:
            search_member(membership_list)
            input("\nPress Enter to continue...")  # Wait for user to view results
        else:
            print("No members to search")
            time.sleep(2)
        
    # Exit the program
    elif choice == "4":
        print("Exiting program...")
        break
    
    # Handle invalid menu choices
    else:
        print("Invalid choice! Please enter a number between 1-4")
        time.sleep(2)
        clear()











    