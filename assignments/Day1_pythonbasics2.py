##Day1_Assignment----------------------Conditional--------------------------------------------------------------

#1. simple if elif else

num=float(input("Enter a number:"))

if num>0:
    print(f"The number {num} is a +ve no.")
elif num<0:
    print(f"the number {num} is a -ve no.")
else:
    print("Its a zero")

#2. nested if ques


num=int(input("Enter a no.:"))

if num>0:
    if num%2==0:
        print(f"The number {num} is +ve and even no.")
    else:
        print(f"The number {num} is +ve and odd no.")
elif num<0:
    print(f"the number {num} is a -ve no.")
else:
    print("Its a zero")



#LOOPS

#3.for Loops

for i in range(1,11):
    print(i)

#4.While Loop
i=1
while i<=10:
    print(i)
    i+=1

#5. Nested Loop

for i in range(5):
    for j in range(5):
        print("*",end="")
    print("")

#6. pass-empty continue-skip break-stop

#7.
num=int(input("Enter a no.:"))

for i in range(1,num+1):
    if i%2==0:
        print(i)

#8. factorial Calculaton

n=int(input("Enter a no.:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(f'The factorial of {n} is {fact}.')


#9. Sum of digits

num=int(input("Enter a no>:"))

sum=0
while num>0:
    re=num%10
    sum+=re
    num=num//10
print(sum)

#10. 

num=int(input("enter a no.:"))
 
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("no")
            break
        else:
            print("Yes it is a prime no")


#11. Fibonacci sequence

num=int(input("Enter a no.:"))

# 1 2 3 5 8 13 21