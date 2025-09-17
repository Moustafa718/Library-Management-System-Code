import os
import time

def clear_screen():
     os.system("cls"if os.name=="nt" else "clear")

class User:
    def __init__(self,first_name, last_name, email, password, status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status


    def display_user(self):
         print(f"First name: {self.first_name}")
         print(f"Last name: {self.last_name}")
         print(f"E-Mail: {self.email}")
         print(f"Status: {self.status}")
         print("_"*20)
    

def creat_user():
        first_name=input("Enter your first name: ")
        last_name=input("Enter your last name:")
        email=input("Enter your E-Mail: ")
        password=input("Enter your password: ")
        return User(first_name, last_name,email,password)
    
     
def Welcome():
    print("Welcome to user mangement \n")
    print("Choose an Action:\n")
    print("1. Add new user ")
    print("2. Display all users")
    print("3. Exit\n")


    

new_users=[]
while True:
     Welcome()
     choice=input("Enter your choise: ")

     if choice=="1":
          new_users.append(creat_user())
          print("User added successfully!")
          time.sleep(2)
          
     elif choice=="2":
        
        if new_users:
            clear_screen()
            print("Displing all new user")
            time.sleep(1)
            for user in new_users:
                user.display_user()
                time.sleep(3)
        else:
            print("Sorry,didn't find any user to display! ")
            time.sleep(2)
            
               
     
     elif choice=="3":
          print("Exiting...")
          break
     else:
          print("Invalid choice! please try again. ")

