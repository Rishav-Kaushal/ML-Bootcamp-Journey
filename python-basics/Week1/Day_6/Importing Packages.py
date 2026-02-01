#Day6---------Importing_Modules & Packages------------------------------------------

import math
# mathmatically calcu package
print(math.sqrt(40))

from math  import sqrt,pi
#from <package name> import <inside the package>
print(sqrt(16))
print(pi)

from math import *
#import everything import from math

import numpy as np
#np is alias means short name for using multiple type
n = np.array([1,2,3,4])
print(n)

#custom packages made
from package.maths import adds 

print(adds(2,5))

from package import maths
print(maths.adds(2,7))

##can create subpackages in the packages folder also in subpackages their should be __init__.py
#intersting that how to take packages
from package.subpackages.multiply import multi

print(multi(3,7))

"""Standard Library Overview"""
import math 

import array
arr = array.array('i',[1,2,3,4])
print(arr)

import random
print(random.randint(1,10)) # random int from given
print(random.choice(['a','b','c']))

import os #for file amd directory access
print(os.getcwd())
#os.mkdir('test_dir') #it make a folder that name given 

#high level operation of=n files or collection of files
import shutil
#shutil.copyfile('destination_file.txt','destination_file1.txt')

import json #data serialization
data = {'name':'Rishav','age':20}

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

json_past = json.loads(json_str)
print(json_past)
print(type(json_past))

import csv #comma sep values
with open('example.csv',mode = 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['RIshav',20])
with open('example.csv', mode = 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#datetime
from datetime import datetime,timedelta

now = datetime.now()
print(now)
yesterday = now-timedelta(days=1) #timedelta one para is days 
print(yesterday)

import time
print(time.time())
time.sleep(2) # sleep for 2 sec
print(time.time())

#re library is built in used mostly for pattern matching ie email match bany pattern
import re # regular expression
pattern = r'\d+'  #d means here digits 
text = 'There is some 5 pips'
match = re.search(pattern,text)
print(match.group()) # output is 5

##python lib is extensive and provides tools for almost any task you can think of from file handling to web services from data to exceution 