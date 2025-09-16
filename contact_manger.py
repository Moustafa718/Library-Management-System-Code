import os # os (operating system)
import time

# function for clear screen
def clear():
    if os.name=="nt": # if os windos 
        os.system("cls")
    else:
        os.system("clear")

contacts={}

while True: # work until i break
    print("contact Management\n")
    print("1- Add a contact")
    print("2- View a contact")
    print("2- View a contact")
    print("4- Exit\n")
    #input a chooice 1-4
    number=int(input("Pleace choose an number from 1-4: "))

    #add contact
    if number ==1:
        
        id=input("Enter the contact ID: ")
        name=input("Pleace type a name: ")
        phone=input("Pleace type a phone number: ")
        print(f"{name} was added successfully...\n")
        # add input in dictionary
        contacts[id]={"Name":name, "phone":phone}

        time.sleep(3) # wait 3 seconde dann clear
        clear()

    # view contact 
    elif number==2:
        if contacts: # if items contact 
            print(contacts)
        else:
            print("your have no contacts")

        time.sleep(3)
        clear()

    # edit contact
    elif number ==3:
        id_to_edit=input("Enter An ID to Edit: ")
        if id_to_edit in contacts:
            
            name_to_edit=input("Entet a new name: ")
            phone_to_edit=input("Enter a new number: ")

            contacts[id_to_edit]={"name":name_to_edit,"phone":phone_to_edit,}
            
            print("success...\n")
            
            time.sleep(3)
            clear()
        else:
            print(f"Sorry, {id_to_edit} was not found...")
        #cheange contact
        

    # exit and break
    elif number==4:
        print("Exiting....")
        break

    else:
        print("Invalid choice. Pleace type 1-4\n")