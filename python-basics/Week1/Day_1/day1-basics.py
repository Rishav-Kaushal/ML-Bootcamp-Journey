##This is a Small Part of ML Udemy Course That is Basics

##Day 1-------Python Basics--------------------------------

#Variables and Data Types------

age=20
name="Rishav"
height=5.11
is_student=True
print("age=",age,type(age))
print("Name=",name,type(name))
print("height=",height,type(height))
print("is_student=",is_student,type(is_student))

#Type Conversion
age=2
age_str=str(age)
print("age_str=",age_str,type(age_str))
str="3.14"
float_str=float(str)
print("float_str=",float_str,type(float_str))
 
#Basic Input and Output
print("Now Basic Input Ouput")
num=input("Enter a no:")
print(num,type(num))

#Simple calculator
print("Simple Calc")
num1=int(input("Enter 1st no:"))
num2=int(input("Enter 2nd no:"))
sum=num1+num2
diff=num1-num2
prod=num1*num2 
divison=num1/num2
print("Sum=",sum)
print("Difference=",diff)
print("Product=",prod)
print("Division=",divison)

#Operators in Python------

#Arithmetic Operators
a=10 
b=3 #sum diff prod div is done above
print(num1, "to the power", num2, ":", num1**num2)
print(num1, "floor division", num2, ":", num1//num2)
print(num1, "mod", num2, ":", num1%num2)

#Comparison Operators(==, !=, >, <, >=, <=)--outputs boolean 
#Logical Operators(and, or, not)
x=True
y=False
print("x or y:", x or y)

#Conditional Statements

# if, elif, else
#here we use colons after condition
print("Traffic light basic ques")
color="y"
if color=="g":
    print(color, "is green so go")
elif color=="r":
    print(color, "is red do stop")
else:
    print(color, "is yellow so get ready")

#nested if
print("Nested if")
num=int(input("Enter a no:"))
if num<=0:
    if num==0:
        print("Number is zero:")
    else:
        print("Number is negative")
else:
    print("Number is positive")
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")
#Practice Problems

#1. Determine if a year is a leap year or not.
print("Leap Year")
year=int(input("Enter a year:"))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#2. Simple calc making to all add diff multi div
print("Simple Calculator")
num1=int(input("Enter 1st no:"))
num2=int(input("Enter 2nd no:"))

op=int(input("Enter numbers as: Addition-1,Subtration-2,Multiplication-3,Division-4:"))

if op in [1,2,3,4]:
    if(op==1):
        print("Sum of num1 & num2",num1+num2)
    elif(op==2):
        print("substration of num1 & num2",num1-num2)
    elif(op==3):
        print("multiplication of num1 & num2",num1*num2)
    elif(op==4):
        if(num2!=0):
            print("division of num1 & num2",num1/num2)
        else:
            print("Can't divide by zero")
else:
    print("Ínvalid Operator")

