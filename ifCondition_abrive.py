guess=int(input("Enter a number: "))

if guess ==3:
    print("good choice")
else:
    print("bad choice ")

print("Good choice")if guess==3 else print("bad choice") # abrivation for if condition

import os
def clear():
    if os.name=="nt": # if os windos 
        os.system("cls")
    else:
        os.system("clear")

def clear_screen():
    os.system( "cls"  if os.name=="nt"  else "clear" ) # abriviation for clear function