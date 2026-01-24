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
    print("Your inc study hour task still in to do list you should focus.")

#print all tasks
print("To do list remaining")
for task in to_do_list:
    print("-",task)

##Ex2. Organizing Student Grades
#create a list to store and calculate average grades for students 

grades=[85,34,90,97,48]


#adding more grades
grades.append(47)

#mathimatical calculations
#average of whole class
avg_grades=sum(grades)/len(grades)
#lowest and highest in whole 
highest=max(grades)
lowest=min(grades)


##Ex3. managing a inventory
#use a list to manage inventory items in a store

inventory=["apple","watermelon","oranges","cherrys","lemon"]

#adding and removing items in inventory
inventory.append("banana")
inventory.remove("watermelon")

#checking something is present or not
item1="oranges"

if item1 in inventory:
    print(f"Yes, {item1} is in stock/present.")
else:
    print(f"No, {item1} is not in stock/present.")
    
#printing everything that is present
print("All Items that is currently is in stock.")
for i in inventory:
    print(f"- {i}")


##Ex4. Collecting user feedback 
feedback=["Great service","good","okay-okay","very bad experience","worst experience","excellent"]

#for adding experince feedback
feedback.append("best")

#counting of +ve feedbaack
posi_words=["great","good","excellent","best","great"]
posi_count=0
for word in feedback:
    for ing in posi_words:
        if ing in word.lower():  ##lower do all alphabets in lower case 
            posi_count+=1
            break  #reduce chance of double count on a same feedback
print("The total positive counts are:",posi_count)
#Showing all feedbacks
print("List of all feedbacks")
for all in feedback:
    print(f"-",all)