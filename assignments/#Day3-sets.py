##Day3 assignment----------set------------------------------

#1.
my_set = set(i for i in range(1,11))  #here inside range its comma
print(my_set)

#2.
my_set.add(11)
my_set.remove(1)
print(my_set)

#3.
set1 = set(i for i in range(1,6))
set2 = set(i*2 for i in range(1,6))

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
diff_set = set1.difference(set2)
symmdiff_set = set1.symmetric_difference(set2)
print(union_set)
print(intersection_set)
print(diff_set)
print(symmdiff_set)

#4.
squ_set=set(i**2 for i in range(1,11))
print(squ_set)

#5.
filtered_set=set(item for item in my_set  if item%2==0)
print(filtered_set)

#6.
new_set={1,2,3,4,2,5,6,4,5,3}
print(new_set)

#7.
sets1=set(i for i in range(1,6))
sets2=set(i for i in range(1,4))

bool1=sets2.issubset(sets1)
print(bool1)
bool2=sets1.issuperset(sets2)
print(bool2)

#8.
frozen_set=frozenset(i for i in range(1,6)) ##frozenset is set which is immutable
print(frozen_set)

#9.
conv_set=set(i for i in range(1,6))
list=list(conv_set)                 #set into list
list.append(6)

re_set=set(list)     #list into set
print(re_set)

#10.


#11.
set={1,2,3,4,5,6,7,8,9}

for i in set:
    print(i)

#12.
set_new={1,3,456,3,2454,32}
print(set_new)

for i in range(len(set_new)):
    set_new.pop()
    print(set_new)

#13.
sset1={1,4,2,36,3,643,343}
sset2={4,1,62,643,3234,24}

sset1.symmetric_difference_update(sset2)
print(sset1)

#14.
setss={1,3,353,543,23467,33,354,32,22,2}

bools=5 in setss
print(bools)

#15.
set_t={1,6,2,456,(1,7),(3,4)}
print(set_t)

