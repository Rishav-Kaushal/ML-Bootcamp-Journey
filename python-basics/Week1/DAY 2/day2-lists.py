## Day 2 ---------Lists-----------------------------------------

#List

list1=["rishav","kaushal",1,2.4,True] #diff data 
print(list1)

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

# Iterating over list

for n in numbers:  # NO bracket
    print(n)
for idx,number in enumerate(numbers):  # enumerate is built fun used to have both same time
    print(idx,number)

# Comprehensive List
# syntax--[output     operation   condition]

listtss=[]
for n in range(11):
    listtss.append(n**3)
print("list=", listtss)

newlist=[n**3 for n in range(11)]  #this is comprehension
print("newlist=", newlist)         

# Comprehension with conditions

square=[num**2 for num in range(20) if num%2==0]
print(square)

# Nested Comprehension

lst1=[1,2,3]
lst2=['a','b','c']

pair=[[i,j] for i in lst1 for j in lst2] #pairing
print(pair)

words=['hello','world','rishav','kaushal']

print([len(k) for k in words])

#Q. Duplicates remove from list
nums=[1,4,3,2,3,2,3,5,7,7]
unique=[]

for i in nums:
    if i not in unique: #important for duplicates
        unique.append(i)
print(unique)


#For import random
import random

random_numbers = [random.randint(1, 20) for _ in range(15)]
print(f"Original list: {random_numbers}")

sorted_numbers = sorted(random_numbers)
print(f"Sorted in ascending order: {sorted_numbers}")

sorted_numbers_desc = sorted(random_numbers, reverse=True)
print(f"Sorted in descending order: {sorted_numbers_desc}")

unique_numbers = list(set(random_numbers))
print(f"List with duplicates removed: {unique_numbers}")

#Zipping of two lists
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = list(zip(list1, list2))
print(zipped)