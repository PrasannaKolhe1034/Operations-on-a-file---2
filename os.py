new_file=open('New_File.txt','x')
new_file.close()

import os
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file doesn't exist")    

my_file=open("my_file.txt", "w")
my_file.write("hi!")
my_file.close()

os.remove("Codingal.txt")
os.rmdir('Folder')