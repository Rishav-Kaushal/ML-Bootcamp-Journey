##Day3-----Real_World_Examples_list-----------


##Ex1. Manage a To Do List
#to create a to do list to keep track of tasks

to_do_list=["Make Notes","Inc study hour","reduce distration"]

#adding and removing
to_do_list.append("Search for GSoC")
to_do_list.append("Go for A Run")
to_do_list.remove("Make Notes")

#reminder
if "Inc study hour" in to_do_list:
    print("Inc your study hour pls")

#print all tasks
print("To do list remaining")
for task in to_do_list:
    print("-",task)
'''
##Ex2. Organizing Student Grades
#create a list to store and calculate average grades for students 

grades=[85,34,90,97,48]

grades.append(47)

avg_grades=sum(grades)/len(grades)
highest=max(grades)
lowest=min(grades)

##Ex3. managing a inventory
#use a list to manage inventory items in a store

inventory=["apple","banana",'oranges']

append remove 

if present or now by item="oranges" if else

print all stockjs present 

##Ex4. Collecting user feedback 
feedback=["Great service",""]

append 
#count +ve feed {sum(1 for comment in ffedback if "great in comment.lower()" )}

print all  feedback


'''