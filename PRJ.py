import os
 
def Clear():
    os.system("cls" if os.name == "nt" else "clear")

library = {}

def Menu():
    print("Menu:")
    print("1. Add Book")
    print("2. Check out a Book")
    print("3. Check in a Book")  # Fixed duplicate option
    print("4. List Books")
    print("5. Exit")
    
def add_book():
    ISBN = input("Enter ISBN: ")
    title = input("Enter Title: ")  # Fixed typo
    author = input("Enter Author: ")
    print(f"Book '{title}' by {author} added to the Catalog with ISBN {ISBN}.")
    library[ISBN] = {
        "ISBN": ISBN,
        "title": title,
        "author": author,  # Fixed key name
        "available": True,  # Fixed key name
    }

def Add():
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
    print("Library Catalog:")
    if library:
        for isbn, details in library.items():
            status = "Available" if details["available"] else "Checked Out"
            print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Status: {status}")
    else:
        print("The library is empty")
    
    while True:
        back_menu = input("Do you want to go back to Menu (y/n): ").lower()
        if back_menu == 'y' or back_menu == 'n':
            Clear()
            break
        else:
            print("Please enter 'y' or 'n'")

def check_out():
    while True:
        ISBN = input("Enter ISBN to check out: ")  # Keep as string
        if ISBN in library:
            if library[ISBN]["available"]:
                print(f"Book '{library[ISBN]['title']}' checked out successfully.")
                library[ISBN]["available"] = False
            else:
                print("Sorry, the book is currently checked out")
        else:
            print("Book not found in the catalog.")
        
        again = input("Do you want to check out another book? (y/n): ").lower()
        if again != 'y':
            Clear()
            break

def check_in():
    while True:
        ISBN = input("Enter ISBN to check in: ")  # Keep as string
        if ISBN in library:
            if not library[ISBN]["available"]:
                print(f"Book '{library[ISBN]['title']}' checked in successfully.")
                library[ISBN]["available"] = True
            else:
                print("This book is already available in the library")
        else:
            print("Book not found in the catalog.")
        
        again = input("Do you want to check in another book? (y/n): ").lower()
        if again != 'y':
            Clear()
            break

while True:
    Menu()
    try:
        choice = int(input("Enter your choice (1-5): "))
        Clear()
    except ValueError:
        print("Please enter a valid number")
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
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter (1-5)")