# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# while x < 5:
#   print(x)
#   x += 1

# answer = input("Should I stop? ")
# while answer.lower() != "yes":
#   print(answer)
#   answer = input("Should I stop? ")

# define a for loop
# for i in range(5):
#   print(i)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# for d in days:
#   print(d)

# use a for loop over a collection


# use the break and continue statements
# for d in days:
#   if (d == "Wednesday"):
#     break
#   print(d)

# for d in days:
#   if (d == "Thursday"):
#     continue
#   print(d)

# using the enumerate() function to get an index and an item
for i, d in enumerate(days):
  print(i, d)