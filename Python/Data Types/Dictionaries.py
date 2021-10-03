'''

Dictionary : Key Value Pairs, Unordered, Mutable

'''

# Creating a dictionary

mydict = {
    "name": "Adit",
    "age" : 14,
    "city": "Delhi",
}

print(mydict)


# Getting a value from dictionary

value = mydict["name"]
print(value)


# Entering a new item in our dictionary

value = mydict["email"] = "name@xyz.com"
print(mydict)


# Deleting an item from the dictioary

del mydict["city"]
print(mydict)

'''Let's add the city back again lol'''

value=mydict["city"] = "Delhi"
print(mydict)


# Alternate mehod for deleting an item

mydict.pop("city")

'''

Wait, did I add the city just to remove it again ??????

Np, Let's add it one last time

'''

value=mydict["city"]="Delhi"


# Removing the last item added in a dictionary  (Guess city is gone agin !)

mydict.popitem()
print(mydict)

'''

NOTE : THIS FEATURE ONLY WORKS WITH PYTHON 3.7  OR VERSIONS AFTER 3.7

'''































