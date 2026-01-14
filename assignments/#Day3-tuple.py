##Day3------tuple-------------------------------------

#1.
tuple1 = tuple(range(1,11))
print(tuple1)

#2.
print(tuple1[0])
print(tuple1[len(tuple1)//2])
print(tuple1[len(tuple1)-1]) #tuple1[-1]

#3.
print(tuple1[:3])
print(tuple1[7:11]) #tuple1[-3:]
print(tuple1[2:6])

#4.
matrix=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print(matrix)
for row in matrix:
    print(row)
print(matrix[1][2]) #2nd row 3rd column

#5.
tpl1 = (1,2,3)
tpl2 = (4,5,6)
totpl = tpl1+tpl2
print("concatationof two tuple : ",totpl)

#6.
dup_tpl = (1,2,31,26,3,1,3)
add=[]
for i in range(0,len(dup_tpl)):
    if dup_tpl[i] not in add:
        print(f"The occurence of {dup_tpl[i]}: {dup_tpl.count(dup_tpl[i])}")
        print(f"Index of first occurence of {dup_tpl[i]}:{dup_tpl.index(dup_tpl[i])}")
        add.append(dup_tpl[i])
#7.
tpl11 = tuple(i for i in range(5))

a,b,c,d,e = tpl11
print(a,b,c,d,e)

#8.
list1=[1,2,3,4,5]
tpl = tuple(list1)
print("list to tuple",tpl)

#9.
tploftpl=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print("Tuple of tuple:",tploftpl)

#10.
t = tuple(x for x in range(1,6))
l = list(t)
l.append(6)
tu = tuple(l)
print("Resulting tuple:",tu)

#11.
tup = ("rk","sk","vb")
str = ""
for i in tup:
    str += i
print(str)
print(type(str))

#12.
dict = {
    (1,2):3,
    (4,5):65,
    (6,7):46
}
print(dict)


#13.
nested_tpl = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
for sub in nested_tpl:
    for item in sub:
        print(item,end = " ")
print()

#14.
tuple11 = (1,2,3,6,3,5,2,8,5,6)
set = set(tuple11)
tuple12 = tuple(set)
print(tuple11)

print(tuple12)

#15.
lst1 = list()
for i in range(6):
    lst1.append(float(input("Ënter the numbers:"))) #append use not index
print("the tuple by user input:",tuple(lst1))
