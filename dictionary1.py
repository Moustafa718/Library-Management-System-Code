book={
    "titel":"Red queen",
    "auther":"Victoria avyared",
    "copies ":123,


    }
book["titel"]="Mousta" # titel wird updated auf (Moustafa)
print(book)

#################
techers={

}
techers["name"]="Moustafa" # append name:Moustafa
techers["last name "]="Alsheikh"

print(techers)

techers={} # techers 

#__________________________________

students={
    1:"Moustafa",
    2:"Ahmad",
    3:"Omar",
    4:"Ayham",
}
#loop for dictionary(loop print just keys)
for key  in students:
    print(f"student ID:" )
    print(key)
    print("Student Name:")
    print(students[key]) # print value of key[1]= Moustafa
    print("-"*30)


info={}
name=input("What is your name? ")
country=input("where are you from? ")
old=int(input("How old are you? "))

info["name"]=name
info["country"]=country
info["age"]= old
print(info)