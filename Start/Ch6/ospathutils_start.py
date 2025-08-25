#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import time
from datetime import datetime

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("Item exists: " + str(path.exists("textfile.txt")))
print("Item is a file: " + str(path.isfile("textfile.txt")))
print("Item is a directory: " + str(path.isdir("textfile.txt")))

# Work with file paths
print("Item's path: " + str(path.realpath("textfile.txt")))
print("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))

# Get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print("Item's modification time: " + str(t))
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

# Calculate how long ago the item was modified
tdiff = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
print(f"Item was modified {tdiff} ago")
print(f"Item was modified {tdiff.total_seconds()} seconds ago")
