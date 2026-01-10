## Day 2 ---------Lists-----------------------------------------

#List

list=["rishav","kaushal",1,2.4,True] #diff data 
print(list)

fruits=["apple","mango","kiwi","pineapple","banana"]

#indexing 
print(fruits[1]) 
print(fruits[-1]) #from end
print(fruits[1:3]) #from 1st index to (3-1)nd index

#modifying
fruits[1]="watermelon" 
print(fruits)

#List methods
fruits.append("Orange") #added orange at last
print(fruits) 
fruits.insert(2,"cherry")  #added cherry at 2nd idx
print(fruits) 
fruits.remove("banana")
print(fruits) 
fruits.pop() #from last remove one
print(fruits) 

print(fruits.index("watermelon")) #index find
print(fruits.count("cherry")) #Number of times

fruits.sort() #sort list in ascending order
fruits.reverse() #reverse the list
print(fruits)

fruits.clear() #clear whole list

#Slicing List
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5]) #idx from 2 to 5
print(numbers[:5]) #idx from 0 to 5
print(numbers[5:]) #idx from 5 to end
print(numbers[::2]) #all but with step 2
print(numbers[::-1]) #all from end step 1
print(numbers[::-2]) #all from end step 1

#Iterating over list

for n in numbers:  #NO bracket
    print(n)
for idx,number in enumerate(numbers):  #enumerate is built fun used to have both same time
    print(idx,number)

#Comprehensive List
#syntax--[output     operation   condition]

list=[]
for n in range(11):
    list.append(n**3)
print("list=", list)

newlist=[n**3 for n in range(11)]  #this is comprehension
print("newlist=", newlist)         

#Comprehension with conditions

square=[num**2 for num in range(20) if num%2==0]
print(square)

#Nested Comprehension

lst1=[1,2,3]
lst2=['a','b','c']

pair=[[i,j] for i in lst1 for j in lst2] #pairing
print(pair)

words=['hello','world','rishav','kaushal']

print([len(k) for k in words])