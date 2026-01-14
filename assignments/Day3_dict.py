##Day3_Assignment----------------------Dictionary---------------------------------------------------------------------

#1.
dic = {i:i**2 for i in range(1,11)}
print(dic)

#2.
print(dic[5])
print(dic.keys())

#3.
dic[11] = 121
dic.pop(1)  # i forgottten
print(dic)
#4.
for key,value in dic.items():
    print(f"pair-{key}:{value}")

#5.
dict_sq = {i:i**3 for i in range(1,11)}
print(dict_sq)

#6.
dict1 = {i:i**2 for i in range(1,6)}
dict2 = {i:i**2 for i in range(6,11)}

merged_dict = {**dict1,**dict2}
print(merged_dict)

#7.
dict11 = {
    "student1":{
        "name":"Rishav",
        "age":20,
        "grades":{
            "math":98,
            "science":90,
            "english":89
        }
    }
}
print(dict11)
for sub,subs in dict11.items():
    for key,value in subs.items():
        print(key,":",value)

#8.
d = {i:[i*j for j in range(1,6)] for i in range(1,6)}
print(d)

#9.
dictt = {i:(i,i**2) for i in range(1,6)}
print(dictt)

#10.
dict_list = {i:i**2 for i in range(1,6)}
lst = list()
for key,value in dict_list.items():
    tpl = (key,value)
    lst.append(tpl)
print(lst)

#11.
dict_filter = {i:i**2 for i in range(1,11)}
dict_filtered = {}
for i,j in dict_filter.items():
    if i%2 == 0:
        dict_filtered[i] = j
print(dict_filter)
print(dict_filtered)

#12.
dictt11 = {i:i**2 for i in range(1,6)}
dict_swap = {}
for i,j in dictt11.items():
    dict_swap[j] = i

print(dict_swap)

#13.
from collections import defaultdict

default_dict = defaultdict(list)
default_dict['a'].append(1)
default_dict['a'].append(2)
default_dict['b'].append(3)
print(default_dict)

#14.
dicttt = {}
for i in range(5):
    str=input("enter string:")
    dicttt[str] = len(str)
print(dicttt)

#15.
import json
book = {
    "title" : "a shameful",
    "since" : 2005,
    "baddi" : "build"
}
book_json=json.dumps(book)
print(book_json)