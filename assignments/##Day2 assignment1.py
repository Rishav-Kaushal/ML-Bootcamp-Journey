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
nestedlist=[[i,j] for i in range(1,4) for j in range(1,4)]
print(nestedlist)