#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
# print("today's date is", today)

# print out the date's individual components
# print("Date components:", today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("Today's weekday # is:", today.weekday())
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("Today is:", days[today.weekday()])

## DATETIME OBJECTS
# Get today's date from the datetime class
now = datetime.now()
print("The current date and time is:", now)

# Get the current time
print("The current time is:", datetime.now().time())
