##Day4-----------File Handing-------------------------------

##File Handling

#Read a whole
with open('example.txt','r') as file:
    for content in file:
        print(content)
#Read line by line
with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) #strip remove new line chara
#writing a file(overwriting)
with open('example.txt','w') as file:
    file.write("It's RK\n")
    file.write('This is a new') #overwrite
#writing a file (without over)
with open('example.txt','a') as file:  #append
    file.write("\nwriting withour overwrite\n")

with open('example.txt','a') as file:
    many=['first line\n','second line\n','third line']
    file.writelines(many)

#Binary bin file
#writing to a bin file #as 'wb'

data=b'Hello this is bin filw'
with open('example.bin','wb') as file:
    file.write(data)
    print(content)

#reading a binary file  #as 'rb'
with open('example.bin','rb') as file:
    content=file.read()
    print(content)

#read the content from the source text file and write to a destination text file

with open('example.txt','r') as source_file:
    content=source_file.read()
with open('destination_file.txt','w') as destination_file:  # auto add this folder
    destination_file.write(content)

#Assignment 
#read a txt file and count the no of lines and words and charaters 

#Writing and then reading a file 
with open('example.txt', "w+") as file: #w+ is for both r and w and if file not present it created if excits its truncated
    file.write("Hello world\n")
    file.write("this is a new line ")
    ##Move the file cursor to the beginning
    file.seek(0) #file cursor to 0, if not this no output 

    ##Read the content 
    content=file.read()
    print(content)

import os
##create a new directory
new_directory="package"
##os.mkdir(new_directory)
print(f"Directory'{new_directory}' created")

#listing files and directories
items=os.listdir('.') #. means current folder
print(items)

##Joining Paths

dir_name="folder"
file_name="file_txt"
full_path=os.path.join(dir_name,file_name)
print(full_path)
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)

#checking for file
path='example.txt'
if os.path.exists(path):
    print(f"The Path '{path}' exists.")
else:
    print(f"The path '{path}' does not exists.")
#checking file aor direc or neither
if os.path.isfile(path):
    print(f"yes '{path}' is a file")
elif os.path.isdir(path):
    print(f"yes '{path}' is a directory.")
else:
    print(f"'{path}' is neither file or directory.")

#getting the absolute path

relative_path='example.txt'
absolute_path=os.path.abspath(relative_path)

print(absolute_path)