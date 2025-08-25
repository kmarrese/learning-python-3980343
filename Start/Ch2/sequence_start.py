# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
print("Lists...")
mylist = [1, "two", 3, 4, False]
print("length of mylist: " + str(len(mylist)))

# to access a member of a sequence type, use []
# print(mylist[1])  # prints "two"
# print(mylist[-1])  # prints False
# mylist[3] = True  # lists are mutable, so you can change them
# print(mylist)

# add a list to another list
print("append to list...")
another_list = [5, 6, 7]
mylist = mylist + another_list  
print(mylist)

# use slices to get parts of a sequence
print("slicing lists...")
print(mylist[2:5])  # prints from index 2 to index 4
print(mylist[:3])  # prints from the beginning to index 2
print(mylist[3:])  # prints from index 3 to the end
print(mylist[::2])  # prints every 2nd element

# you can use slices to reverse a sequence
print("reversing lists...")
print(mylist[::-1])  # prints the list in reverse order

# Tuples are like lists, but they are immutable
print("tuples...")
mytuple = (1, "two", 3, 4, False)
print(mytuple)
print(mytuple[1])  # prints "two"

# Sets are also sequences, but they contain unique values
print("sets...")
myset = {1, 2, 3, 4, 2, 4, 5}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print("membership test...")
print(1 in mylist)          # prints True
print("hello" in mytuple)   # prints False
print(3 in myset)           # prints True