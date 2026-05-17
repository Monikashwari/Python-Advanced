import os
print("Current working directory:", os.getcwd()) 
print(os.path.abspath(__file__)) # get absolute path of the current file
print(os.path.dirname(os.path.abspath(__file__))) # get directory name of the current file
print(os.listdir()) # list all files and directories in the current directory
print (os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_main.py")) # join directory name with test_main.py to get full path of the test file

for i in os.listdir():
    if os.path.isfile(i):
        print(f"{i} is a file.")
    elif os.path.isdir(i):
        print(f"{i} is a directory.")

last_load = '2026-01-14'
# Here we manipulate the path using OS Module to find the date of the latest Load.
for i in os.listdir((os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data"))):
    if i.split('.')[0] > last_load:
        print(f"Processing {i} new File .")
