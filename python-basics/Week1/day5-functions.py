##Day5---------------------------Functions--------------------------------------------------------------------------

#Functions
def evenodd(num):
    """This Function finds even or odd"""
    if num%2 == 0:
        print(f"The Number {num} is even.")
    else:
        print(f"the Number {num} is odd.")

evenodd(234)

def  add(a,b): #with multiple parameters
    """This function add two given numbers"""
    c=a+b
    return c #or return a+b directly

print(add(3,6))

#Default Para
def greet(name="Guest"): #default is guest if no local para
    print(f"hello, {name} Welcome here!")

greet()

#Variable length argument
#positional arguments
def print_numbers(*args): #this is for multiple arguments
    for num in args:
        print(num)

print_numbers(1,2,5,3,7,4,0,"ok")
#keywords arguments
def print_details(**kwargs): # all arguments in key value pair
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="Rishav",age="20",state="jharkhand")

def print_all_details(*args,**kwargs):
    for val in args:
        print(f"Positional arguments:",val)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    
print_all_details(1,2,5,3,7,4,0,"ok",name="Rishav",age="20",state="jharkhand")

#return statements
def multiply(a,b):
    return a*b,a #can return multiple values
multiply(2,3)

#Examples--------------------------------------------------------------

#1. Temp Conv111
def temp_conv(temp,unit):
    """This function converts temperature between celsius and farenhit"""
    if unit == 'C':
        return temp * 9/5 + 32
    elif unit == 'F':
        return (temp-32)*5/9
    else:
        return None
print(temp_conv(25,'C'))

#2. Pass Strength Checker
def is_strong_pass(password):
    """This function will check if any password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password): #any is builtin 
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_-+=' for char in password):
        return False
    return True  #if no false then only this work
    
print(is_strong_pass("We23akP@wd"))

#3. Caln total cost of items in a shopping cart

def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item['price']*item['quantity']
    return total_cost

cart=[
    {'name':'apple','price':1,'quantity':20},
    {'name':'banana','price':1.5,'quantity':10},
    {'name':'cherry','price':2,'quantity':8},
]
print(calculate_total_cost(cart))

#4. check if a string is palindrome
def is_palindrome(str):
    str=str.lower().replace(" ","") #removing spaces
    return str==str[::-1]

print(is_palindrome("a man a plan a canal panama"))
print(is_palindrome("rishsire"))

#5.
def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

print(fact(5))

##very very important
#6. a func to read a file and count the freq

def count_word_freq(file_path):
    word_count = {}
    with open(file_path,'r') as f:
        for line in f:
            words = line.split() # split by spaces
            for word in words:
                word = word.lower().strip('.,!?:;"\'/')
                word_count[word]=word_count.get(word,0)+1  #get means if find the "word" if not then 0
    return word_count

file_path='destination_file.txt'
print(count_word_freq(file_path))

#7. Validate email address



##Lambda Functions----------------------------------------------------
#small anonymous func, any no of args but only 1 expression , required lambda func
# a func without a name

#syntax
lambda arguments: expression 

even = lambda n : n%2 == 0
print(even(13))

add = lambda a,b,c : a+b+c
print(add(2,6,33))

##Map function--------------------------------------------------------
#it applies a func to all items in a list
#syntax   map(any function,iteriables)


#map with lambda func
num = [1,2,3,4,5,6,7,8,9]
list1 = list(map(lambda x:x**2,num)) #convert to list must
print(list1)

#adding both
num1=[1,2,3]
num2=[4,5,6]

added_num=list(map(lambda x,y:x+y,num1,num2))
print(added_num)

#map() to convert a list of str to int
str_num=['1','2','3','4']
int_num=list(map(int, str_num))
print(int_num)


words=['apple','banana','cherry']
upper_word=list(map(str.upper,words))
print(upper_word)


def get_name(person):
    return person['name']

people=[
    {'name':'Rishav','age':21},
    {'name':'Kaushal','age':20}
]
list12=list(map(get_name,people))
print(list12)


##Filter function -----------------------------------------------------------
#it constructs an iiterator from elements of an interable for which a function returns true 
#used to filter out it's from a list(any iterable) based upon condition

def even(num):
    if num%2 == 0 :
        return True
lst11=[1,2,3,4,5,6,7,8,9,10,11,12,13]
up_list=list(filter(even,lst11))
print(up_list)

great_lst=list(filter(lambda x:x>5,lst11))
print(great_lst)

#filter with lambda and multiple conditions
num11=[1,2,3,4,5,6,7,8,9,10,11,12,13]
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0, num11))
print(even_and_greater_than_five)

#filter with dict
people=[
    {'name':'Rishav','age':21},
    {'name':'Kaushal','age':17},
    {'name':'Sagar','age':21}
]
def age_greater_than_18(person):
    return person['age']>18
abc=list(filter(age_greater_than_18,people))
print(abc)

#it is a powerful tool for creating iterators that filter items outt of an iterable based on a func, used for data cleaning, filtering objects, removing unwanted elements from list