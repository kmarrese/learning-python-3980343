# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# hello_func()
# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you doing")
# hello_func("Hey, what's up")

# function that returns a value
# def cube(x):
#   return x ** 3

# result = cube(3)
# print(result)

# function with default value for an parameter
# def hello_func(greeting, name=None):
#   print("hello world!")
#   if name is None:
#     name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you doing", "Joe")
# hello_func("How are you doing")

# function with variable number of parameters
def multi_add(start, *args):
  total = start
  for num in args:
    total += num
  return total

print(multi_add(10,1,2,3))