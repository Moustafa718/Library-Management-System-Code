bock={
    "titel":"Red Queen",
    "author":"Victoria",
    "Year":2015,
    "pages":383,
    "is_many":True,
    "rating":4.1 ,

}
print(bock.get("author"))
print(bock["author"])

#if function with dictionary
if bock.get("pages") :
    print("The bock exist")
else:
    print("The Bock dos'nt exist")

#dictionary update item (anfügen)
bock.update({"Writer":"Moustafa"})
print(bock)

#remve item
bock.pop("Writer") # will remove writer
print(bock)

#remve last item
bock.popitem() # will remove rating
print(bock)

#clear dictionary
#bock.clear() # remove all dictionary
#print(bock)
 
#print dictionary keys
keys=bock.keys() 
print(keys)

#print dictionary values
values=bock.values()
print(values)

# dictionary items(keys , values)
items=bock.items() # will do in list (key:values) for each item
print(items)