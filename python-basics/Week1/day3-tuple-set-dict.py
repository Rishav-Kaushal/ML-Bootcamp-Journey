##Day3------tuple & set & dict ----------------------------------------


##Tuple in python-----------------------

tpl1=()
print(type(tuple))
lst=list()
tpl=tuple()
print(type(lst))
print(type(tpl))

num=tuple([1,2,3,4,5,6]) #list to tuple 
print(num) 

mixed_tuple=(1,"str",4.6,True)

#all indexing and slicing same as list
#bracket should be big in this also
num1=num[::-1]
print(num1)

a= num + mixed_tuple*3 #Concatenation with 3 times multiply
print(a)

#num[1]=4  # error TypeError

#Tuple methods
num.count(1) #cont no of times 1 present .
num.index(3) # find which idx(first) has 3 present.

#Packing & Unpacking of tuple 
packed_tpl=1,"hii",4.3  
print(packed_tpl)

a,b,c=packed_tpl #unpacking
print(a)
print(b)
print(c)

num2=(1,2,3,4,5,6)

first,*middle,last=num2 #unpacking with *
print(first)
print(middle) #output is list
print(last)

#Nested Tuple & List
nested_list=[[1,2,3],[4,5,6],(7,"str",4.5)] #possible
nested_tuple=((1,2,3),("a","b","c"),(7,8,9)) #here (1,2,3) is one and at idx 0

nested_list[0] #[1,2,3]
print(nested_list[2][:3])
print(nested_tuple[1])

#iterating in tuple

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")
    print()


##Sets In Python--------------------- 

my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))
empty_set=set()
print(type(empty_set))

set1=set([1,2,2,3,4,55]) #set only take one value here we given as list
print(set1)              #duplicates remove
print(type(empty_set))

#Basics Sets Ops

my_set.add(7) #add 
my_set.remove(1) #remove
print(my_set)
#my_set.remove(10) #give type error
my_set.discard(10) #if not present it didnt give any error
removed=my_set.pop() # first remove
print(removed)
my_set.clear() #clear the set


#Set membershpip test---"in"
my_set={1,2,3,4,5}

print(3 in my_set)
print(10 in my_set)

#Maths ops
set1={1,2,4,8,9,34,56}
set2={2,4,6,3,34,5}

union_set=set1.union(set2)
print(union_set)
inter_set=set1.intersection(set2)
print(inter_set)

diff_set=set1.difference(set2) #uncommon elements of set1 it also have difference_update
print(diff_set)
symmdiff_set=set1.symmetric_difference(set2)  #all elements that is not common
print(symmdiff_set)
set1.intersection_update(set2)  #set1 updated as intersection set1 is intersection 

set1.issubset(set2)    #T & F
set1.issuperset(set2)  #T & F


##Dictionaries in python---------------
#unordered collection,mutable,key-value

#Create dict
#list=[],tuple=(),
empty_dict={}
empty_dict1=dict() #also
print(type(empty_dict))
print(type(empty_dict1))

student={"name":"Rishav","age":20,"grade":98,"name":"Kaushal"}
print(student)  #key should be unique otherwise it take recent 

#accessing
student={"name":"Rishav","age":20,"grade":98,"name":"Kaushal"}

print(student['grade'])
print(student.get('name')) #also if key not present its none
print(student.get("dhhf","Not Present")) #output is Not prsent in case key is missing

#Modifying Dict
student['name']="sagar"
student['age']=17            #update
student['address']="Deoghar" # added

del student['grade'] #this delete that key value
print(student)

#Dictionary Methods
keys=student.keys()  #get all the keys
print(keys) 
values=student.values() #get all the values
print(values) 
items=student.items() #all the key value pair
print(items) #output is list of tuples

student_copy=student 
print(student)
print(student_copy) #same value
student["name"]="Kaushal1"
print(student)
print(student_copy) #here also changed its a problem because we cant make copy of past

#shallow copy
student_copy1=student.copy() #now its a shallow copy here changes in student dont happen

student["name"]="Kaushal2"
print(student)
print(student_copy1) #stays same its shallow copy

#iterating over dict by loops

#over keys

for keys in student.keys(): #here bracket needed
    print(keys)
for items in student.items(): #here bracket needed
    print(items)  #all items that is key value pair
for key,value in student.items(): #same  
    print(key,":",value)

#Nested dictionaries  #sample of mongodb
students={
    "student1":{"name":"Rishav","age":20},
    "student2":{"name":"Sagar","age":17},
}
print(students)
print(students["student2"]["name"]) #access nested value

for student_id,student_info in students.items(): #just via items can take all values
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items(): #as all key value present in info(2nd part)
        print(f"{key}:{value}")

#Dictionary Comprehension with conditions
squares={i:i**2 for i in range(11)   if i%2==0}
print(squares)

#Practical examples
#use a dict to count the freq of elements in list

number=[1,3,3,1,4,5,4,5,3,5,1,2,2]
freq={} 

for num in number: #simple but have to think
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)

dict1={"a":1,"b":2} 
dict2={"c":3,"d":4}

merged_dict={**dict1,**dict2}  #mergeing
print(merged_dict)




