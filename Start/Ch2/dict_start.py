# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {"one":1,"two":2,3:"three", 4.5:["four","point", "five"]}
print(mydict)

# dictionaries are accessed via keys
print(mydict["one"])  # prints 1
print(mydict["two"])  # prints 2
print(mydict[3])  # prints "three"

# you can also set dictionary data by creating a new key
mydict["newkey"] = "newvalue"
print(mydict)

# Trying to access a nonexistent key will produce an error
# print(mydict["nonexistent"])  # this will cause an error  

# To avoid this, you can use the "in" operator to see if a key exists
print("one" in mydict)  # prints True
print("nonexistent" in mydict)  # prints False

# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())  # prints all keys
print(mydict.values())  # prints all values

# You can also iterate over all the items in a dictionary
for key, value in mydict.items(): 
  print(key, value)
