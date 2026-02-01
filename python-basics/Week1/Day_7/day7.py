#Exceptions are events that disruprt the normal flow of a prograam they occur when a error is encountered
#To handle Exceptions 

try:
    a = b
except NameError as ex:
    print(ex) #it print exactly what get on error 

try:
    r=1/0
except ZeroDivisionError as zr: #zr is just a alias 
    print(zr)
    print("Please dont divide by zero")

try:
    r=1/2
    a=b  # this is not handled so except block no sense
except ZeroDivisionError as zr: #zr is just a alias 
    print(zr)
    print("Please dont divide by zero")

try:
    a=b+c
except Exception as ee: # this is top class it handle each and every exception
    print(ee)           # this classs should be at the last befor all zero name etc
    print("main exception caught here.")

##try, except,else block
try:
    num=int(input("Enter a num:"))
    result = 10/num
except ValueError:
    print("this is not a valid no.")
except ZeroDivisionError:
    print("You cant divide by 0")
except Exception:
    print(Exception)
else: #this will run only when there is no exception if there is exception handled then it is no run 
    print("Hey, The result is ",result)
finally: ##this will run always always always #to close the program
    print("Program completed!!")

###File Handling and Exception handling

try:
    file = open('example.txt','r')
    content = file.read()
    print(content)
    a=b
except FileNotFoundError:
    print("File does not found")
except Exception as ex:
    print(ex)
finally:
    if 'file' in locals() and not file.closed():
        file.close()
        print('file close')







