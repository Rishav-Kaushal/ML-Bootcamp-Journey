##Day4_Assignment------------------------File_Handling--------------------------------------------------------------

#1.
with open('sample.txt','r') as f:
    for line in f:
        print(line.strip())

#2.
def write_file(lines,filename):
    with open(filename,'w') as file:
        for line in lines:
            file.write(line + '\n')

write_file(["Hello"],'output.txt')
#method 2
with open('output.txt','w') as f:
    for i in range(4):
        f.write("\n")
        f.write(input("Enter string:"))
with open('output.txt','r') as f:
    content = f.read()
    print(content)

#3.
with open('source.txt','r') as f:
    content=f.read()
with open('destination.txt','w') as f:
    f.write(content)
print(f)

#4.
with open('source.txt','a') as f:
    f.write(input("Enter any string:"))
with open('source.txt','r') as f:
    co=f.read()
    print(co)

#5.
with open('sample.txt','r') as f:
    content = f.read()

char = len(content.split()) #auto read all words 
print("Total charaters:",char)

#6.
def find_and_replace(filename, old_word, new_word):
    with open(filename, 'r') as file:
        text = file.read()
    new_text = text.replace(old_word, new_word) #replace func
    with open(filename, 'w') as file:
        file.write(new_text)

find_and_replace('sample.txt', 'old', 'new')

#7.
def read_reverse(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines): #reversed()
        print(line.strip())

read_reverse('source.txt')

#8.
with open('source.txt','r') as f:
    content = f.read()
    c=0
    for i in content:
        if i == '\n':
            c += 1
    print("Total char:",len(content))
    print("Total words:",len(content.split()))
    print("Total lines",c+1) #len(f.readlines())

#9.
with open('source.txt','r') as f:
    content1 = f.read()
with open('output.txt','r') as f:
    content2 = f.read()

with open('op.txt','w') as f:
    f.writelines(content1)
    f.writelines(content2)
with open('op.txt','r') as f:
    fol=f.read()
    print(fol)

#10.  ## reread to understand
def split_file(filename, lines_per_file):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i in range(0, len(lines), lines_per_file):
        with open(f'{filename}_part{i//lines_per_file + 1}.txt', 'w') as part_file:
            part_file.writelines(lines[i:i + lines_per_file])
            
split_file('sample.txt', 100)

#11. to write a log file & write log mess with timestamps
import datetime

def log_message(message, filename='activity.log'):
    ts = datetime.datetime.now().isoformat()
    with open(filename, 'a') as file:
        file.write(f"[{ts}] {message}\n")
        print(file)
log_message('This a log message.')
#12.
with open('image.bin','r') as b:
    content = b.read()
with open('copy_image.bin','w') as b:
    b.write(content)
with open('copy_image.bin','r') as b:
    content = b.read()
print(content)

#13.
dict={}
with open('data.csv','r') as c:
    for line in c:
        a,b = line.strip().split(',') #strip remove new line char
        dict[a] = b
print(dict)
'''
#14.
import json

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

print(read_json('data.json'))
'''
#15.
def read_protected_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except PermissionError as e:
        print(f"Permission error: {e}")

read_protected_file('source.txt')

