## Day 2-------loops----------------------------------------

# For loop

for i in range(1,10,2): #range is interval range(start,end+1,step)
    print(i)

str="Rishav Kaushal" #can traverse
for i in str:
    print(i)

for i in range(68):
    if i==12:
        continue #continue skip to on next ittration
    elif i==15:
        break #entire for loop stops and came outside
    print(i)
    pass  # it do nothing write or not doesn't matter

# While loop
count=0

while count<=60:   ##while is just control range 
    if count%3==0:
        print(count)
    count+=1

# Nested Loop
for i in range(1,5):
    for j in range(1,4):
        print("i=",i,"and j=",j)

#1. calculate the sum of first N natural number using while
print("Sum of first N natural number")

n=int(input('Enter a no:'))
sum=0
i=0

while i<=n:
    sum+=i
    i+=1
print(f"Sum of first {n} terms {sum}")

#2. Prime number from 1 to n
print("Prime No till 100.")
for num in range(2,101):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                break 
        else:            #else of while/for works only when nothing works inside while/loop
            print(num)
    else:
        print("Number should be in range of 1 to 100")
