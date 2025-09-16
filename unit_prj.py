import os
# Cleat screen
def Clear():
    os.system("cls" if os.name=="nt" else "clear")
# Dictionary to store all books in the library
library={}
# Menu
def Menu():
    print("Menu:")
    print("1. Add Book")
    print("2. Check out a Book")
    print("3. Check in a Book")  
    print("4. list Book")
    print("5. Exit")

# Add book to library
def add_book():
    while True:
        Clear()
        isbn=input("Enter ISBN: ")
        title=input("Enter Titel: ")
        author=input("Enter Author: ")

        library[isbn]={
            "titel": title,             # Fixed key names
            "author": author,  
            "available": True,  
            }
        print(f"Book {title} by {author} added to the Catalog with ISBN {isbn}. ") 

        choice=input("Do you add a new Book (y/n): ")
        # Add a new book and break
        if choice.lower() != "y":
            break

# Book Check out 
def check_out():
    while True:
        Clear()
        isbn=input("Enter ISBN to check out: ")  
        if isbn in library:
            if library[isbn]["available"]:  
                library[isbn]["available"]=False  # Change book availability
                print(f"Book {library[isbn]['titel']} Check out successfully. ")  
            else:
                print("Sorry, the book is currently checked out ")
        else:
            print("The Book is not in catalog. ")
        choice=input("Do you want to check out another book? (y/n): ")  
        if choice.lower() != "y":
            break

# Book Check in  
def check_in():
    while True:
        Clear()
        isbn=input("Enter ISBN: ") 
        if isbn in library:

            if not library[isbn]["available"]:  
                library[isbn]["available"]=True  # Change book availability
                print(f"Book {library[isbn]['titel']} checked in successfully ")  
            else:
                print("this book already available in the library")

        else:
            print("book not found in the catalog. ")
            
        choice=input("Do you want to check in another book? (y/n): ")
        if choice.lower() !="y":
            break
            
# list book display
def list_book():
    while True:
        Clear()
        print("\nlibrary catalog: ")

        # print book list
        for isbn in library:
            book_info = library[isbn]
            print(f"ISBN: {isbn}, Title: {book_info['titel']}, Author: {book_info['author']}, Available: {book_info['available']}")  

        choice=input("Do you want to go back to main Menu? (y/n): ")  
        if choice.lower() == "y":
            break
        # if library empty
        if not library:
            print("library is empty ")
        input("press Enter to go to main menu. ")
        break

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
    elif choice==2:
        check_out()
    elif choice==3:
        check_in()
    elif choice==4:
        list_book()
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. pleace enter (1-5)")
