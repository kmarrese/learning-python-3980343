#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
# print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
# print("Today is: " + str(now))

# print today's date one year from now
# print("One year from now it will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
# print(timedelta(weeks=1, days=2, hours=3, minutes=4))

# calculate the date 1 week ago, formatted as a string
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d, %Y")
# print("One week ago it was: ", s)

### How many days until April Fools' Day?
today = datetime.today()
afd = datetime(today.year, 4, 1)
if afd < today:
    print("April Fools' Day already went by %d days ago" % ((today - afd).days))
    afd = afd.replace(year=today.year + 1)

time_to_afd = afd - today
print("It's just", time_to_afd.days, "days until April Fools' Day!")