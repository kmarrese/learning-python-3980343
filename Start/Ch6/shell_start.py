#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
# if path.exists("newfile.txt"):
    # get the path to the file in the current directory
    # src = path.realpath("newfile.txt")

    # # let's make a backup copy by appending "bak" to the name
    # dst = src + ".bak"
    # # now use the shell to make a copy of the file
    # shutil.copyfile(src, dst)

    # # rename the original file
    #os.rename("textfile.txt", "newfile.txt")
    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    # with ZipFile("testzip.zip", "w") as newzip:
    #     newzip.write("newfile.txt")
    #     newzip.write("newfile.txt.bak")  

def file_info():
    tot_bytes = 0
    file_list = os.listdir("deps")
    for file in file_list:
        print(f"{file}")
        if file.endswith(".txt") and path.isfile(path.join("deps", file)):
            tot_bytes += os.stat(path.join("deps", file)).st_size
    return tot_bytes

print(file_info())