#STILL IN PROGRESS

'''

Tuple: ordered, immutable , allow duplicate elements 

'''

# Creating a Tuple

mytuple = ("Sahil","Adit","Parth")
print(mytuple)


# Parenthesis are optional

mytuple = "Sahil","Adit","Parth"
print(mytuple)


# Ading only 1 item in a Tuple

'''

When we add only 1 item in a tuple , we have put a comma after it.
This is because ("Adit") is considered a variable.

'''

one_item_tuple=("Adit",)
print(one_item_tuple)


#Creating Tuple from list

a=["this","is","a","list"]
a.remove("list")   #just changing the word list to tuple
a.append("tuple")
b=tuple(a)  #actual work happening here
print(b)


# finding items from index in tuple

item = mytuple[1]
print(item)


# Iterating tuple

for some_boi in mytuple :
    print(" This boi's name is",some_boi)


# Checking for items in a tuple

if "Adit" in mytuple:
    print("Yeahhhhh")
else:
    print("Nope")


#finding out number of items in tuple

print(len(mytuple))


# Finding out number of items in a tuple

num_tuple=(1,1,1,1,1,2,3,4,5,4,3,2,23,4,56,7,8,9,90,7,6,6,6,6,5,3,3,4,5,6,7,8,8,9,7,5,45,4)
print(num_tuple.count(6))


# Finding out index of an item in tuple

'''

NOTE : If item is repeated in tuple , the index of the first appearence of item will be returned.

'''

print(num_tuple.index(4))
