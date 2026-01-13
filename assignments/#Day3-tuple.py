##Day3------tuple-------------------------------------

#1.
tuple1 = tuple(range(1,11))
print(tuple1)

#2.
print(tuple1[0])
print(tuple1[len(tuple1)//2])
print(tuple1[len(tuple1)-1])

#3.
print(tuple1[:3])
print(tuple1[7:11])
print(tuple1[2:6])

#4.

#5.
tpl1 = (1,2,3)
tpl2 = (4,5,6)
totpl = tpl1+tpl2
print(totpl)

#6.
dup_tpl = (1,2,31,26,3,1,3)
freq = []


#7.
tpl11 = tuple(i for i in range(5))

a,b,c,d,e = tpl11
print(a,b,c,d,e)

#8.
list=[1,2,3,4,5]
tpl=tuple(list)
print(tpl)

#9.
tploftpl=tuple(tuple())