import os

def Clear():
    """Clear the console screen based on the operating system"""
    os.system("cls" if os.name == "nt" else "clear")

# Dictionary to store all books in the library
library = {}

def Menu():
    """Display the main menu options"""
    print("Menu:")
    print("1. Add Book")
    print("2. Check out a Book")
    print("3. Check in a Book")  # Fixed duplicate option
    print("4. List Books")
    print("5. Exit")
    
def add_book():
    """Add a new book to the library catalog"""
    ISBN = input("Enter ISBN: ")
    title = input("Enter Title: ")  # Fixed typo
    author = input("Enter Author: ")
    print(f"Book '{title}' by {author} added to the Catalog with ISBN {ISBN}.")
    
    # Store book details in dictionary
    library[ISBN] = {
        "ISBN": ISBN,
        "title": title,  # Fixed key name
        "author": author,  # Fixed key name (removed colon)
        "available": True,  # Fixed key name
    }

def Add():
    """Prompt user to add multiple books"""
    while True:
        add = input("Do you want to add a new Book (y/n): ").lower()
        if add == "y":
            Clear()
            add_book()
        elif add == "n":
            Clear()
            break
        else:
            print("Invalid Choice! Please choose (y/n)")

def list_book():
    """Display all books in the library catalog"""
    print("Library Catalog:")
    
    if library:
        # Iterate through all books and display their details
        for isbn, details in library.items():
            status = "Available" if details["available"] else "Checked Out"
            print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Status: {status}")
    else:
        print("The library is empty")
    
    # Wait for user to press Enter before returning to menu
    input("Press Enter to return to the menu...")
    Clear()

def check_out():
    """Check out a book from the library"""
    while True:
        ISBN = input("Enter ISBN to check out: ")  # Keep as string
        if ISBN in library:
            if library[ISBN]["available"]:
                print(f"Book '{library[ISBN]['title']}' checked out successfully.")
                library[ISBN]["available"] = False  # Update availability status
            else:
                print("Sorry, the book is currently checked out")
        else:
            print("Book not found in the catalog.")
        
        # Ask if user wants to check out another book
        check_again = input("Do you want to check out another book? (y/n): ").lower()
        if check_again != "y":
            Clear()
            break

def check_in():
    """Check in a book to the library"""
    while True:
        ISBN = input("Enter ISBN to check in: ")  # Keep as string
        if ISBN in library:
            if not library[ISBN]["available"]:
                print(f"Book '{library[ISBN]['title']}' checked in successfully.")
                library[ISBN]["available"] = True  # Update availability status
            else:
                print("This book is already available in the library")
        else:
            print("Book not found in the catalog.")
        
        # Ask if user wants to check in another book
        check_again = input("Do you want to check in another book? (y/n): ").lower()
        if check_again != "y":
            Clear()
            break

# Main program loop
while True:
    Menu()
    try:
        choice = int(input("Enter your choice (1-5): "))
        Clear()
    except ValueError:
        print("Please enter a valid number between 1-5")
        continue

    if choice == 1:
        add_book()
        Add()
    elif choice == 2:
        check_out()
    elif choice == 3:
        check_in()
    elif choice == 4:
        list_book()
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1-5")