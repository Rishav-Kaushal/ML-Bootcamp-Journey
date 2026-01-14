##Day 2 assignments of Lists

#1.
list1=[i for i in range(1,21)]
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(list)
print(list1)

#2.
print(list[0],list[len(list)//2],list[-1])

#3.
print(list[:5])
print(list[15:21])
print(list[5:15])

#4.
sqlist=[i**2 for i in range(1,11)]
print(sqlist)

#5.
evenlist=[i for i in list if i%2==0]
print(evenlist)

#6. 
randomlist=[1,5,8,3,23,5,77,4,6]

randomlist.sort() # becomes asending
randomlist.reverse() # becomes decending
                     #????? HOW TO REMOVE DUPLICATES??
print(randomlist)

#7.
matrix=[]

for i in range(3):
    row=[]
    print("Enter for row", i+1)
    for j in range(3):
        row.append(input("Enter no.:"))
    matrix.append(row)

print(matrix)
print(matrix[1][2])

#8.
students=[
    {"name":"Rishav","age":20},
    {"name":"Sagar","age":17},
    {"name":"Vidya","age":14.5}
]
for stu in students:
    print(stu)
print(students[1]["age"])
#9. 
matrix1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transposemat=[]

for i in range(3):
    row=[]
    for j in range(3):
        row.append(matrix1[j][i])
    transposemat.append(row)
print(transposemat)

#10.

nested=[
    [42,6,365],
    [63,52,35],
    [632,25,52]
]
flat=[]

for i in nested:
    for j in i:
        flat.append(j)

print("Simple nested list:",nested)
print("flattened list:",flat)

#11.
randlist=[i for i in range(1,11)]

randlist.remove(2)
randlist.remove(4)
randlist.remove(6)
print(randlist)
randlist.insert(5,99)
print(randlist)

#12 Zip funcation

lst1=["a","b","x","y"]
lst2=[1,2,9,8]

zipped_lst=[[i,j] for i in lst1 for j in lst2]

print(list(zip(lst1,lst2)))
print(zipped_lst)

#13.
inputlist=[]
for i in range(10):
    inputlist.append(input("Enter nummbers for the list:"))
print(inputlist)

inputlist.reverse()
print(inputlist)

#14.
n=int(input("Enter n :"))

numbers1=[1,6,3,5,34,32]
rotated=[]

rotated=numbers1[-n:]+numbers1[:-n]
print(rotated)

#15.

lst1=[1,2,7,8,4,24,245,665]
lst2=[1,24,7,643]

add=[]

for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i]==lst2[j]:
            add.append(lst1[i])
            break
print(add)

#16. Duplicates remove from list
nums=[1,4,3,2,3,2,3,5,7,7]
unique=[]

for i in nums:
    if i not in unique: #important for duplicates
        unique.append(i)

print(unique)