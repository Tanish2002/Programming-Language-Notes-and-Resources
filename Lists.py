'''

LISTS

Python elements that are ordered , mutable and allow duplicate elements.

'''

# Simple List 

mylist = ['Adit','Parth','Sahil']       #NAMES OF MY FRIENDS, LOL 
print(mylist)


# Printing an item from a specific index in a list 

item = mylist[-2]
print(item)


# Iterating through list 

for i in mylist :
    print ("Happy birthday to " + i) 


# Checking for items in a list

if "Adit" in mylist :
    print("He is in your list")
else:
    print ("He is not in your list")
    
    
# Checking no. of items in a list 

print(len(mylist))


#Adding a value to the end of a list

mylist.append("Dummy_Boi")
print(mylist)


# Adding a value to a given index in a list

mylist.insert(3,'Pranit')
print (mylist)


# Printing the last item in a list BUT ALSO REMOVING IT  at the same time

mylist.pop()
print(mylist)

    
# Removing a specific item in a list

'''
I am first adding a dummy name to the list and will remove it later coz it will be pretty biased to remove one of my friends, locals

'''

mylist.append("Dummy_Boi")
print(mylist)

mylist.remove("Dummy_Boi")
print(mylist)


# Remove all items in a list 

mylist.clear()
print(mylist)


#LOL, Let's get the list back again

mylist = ['Adit','Parth','Sahil','Pranit']
print(mylist)


# Reversing a list ( Why would you wanna do that ? )

mylist.reverse()
print(mylist)

# Sort your list 

# Example 1 (Alphabets)

test_list = ["adit", "Adit", "parth", "Parth"]
test_list.sort()
print(test_list)
    
'''
Hence, we conclude that python , when sorting a list, 
sorts the words with their first letter capital 
before the words whose first letter is small 
    
'''

#Example 2 (numbers)

test_list2=[1,4,65,789,0,-303,-1,-0.5]
test_list2.sort()
print(test_list2)


# Creating a list with multiple same elements in it

test_list3 = [2] * 12
print(test_list3)


# Creating a list with other lists inside it

new_list = test_list2 + test_list3
print(new_list)

# Slicing (taking only a part of the list)

slice1 = mylist[1:3]
print(slice1)

'''
(When we do not specify a start index, then it starts from index 0 )
(When we do not specify a stop index, then it goes till the last item in the list.)

'''


# Slicing with step index
a=test_list2[::2]
print(a)

'''

(Every second item in the list is printed)

'''

# List_Comprehensions

some_list=[1,2,3,4,5,6,7]

# If we want to add 2 to every item in the list,

b= [i + 2 for i in some_list]
print(b)
 
'''
 
 This is an advanced and shorter method to do things in python

'''



















    
    
    
