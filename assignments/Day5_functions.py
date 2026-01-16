##Day5_Assignment---------------------Functions--------------------------------------------------------------------

#1.1.
def fibonacci(n,memo={}):    #memoization
    """This function calculate nth fibonacci No."""
    if n in memo:
        return memo[n]
    if n ==0:
        return 0
    if n == 1:
        return 1
    memo[n]=fibonacci(n-1,memo) +  fibonacci(n-2,memo) #can do without writing memo just here as in python only it allows default args only once
    return memo[n]
print(fibonacci(44))

#1.2.
from functools import lru_cache #this is least recently used cache same as memoization
@lru_cache(maxsize=None)

def fibo(n):
    """This function calculate nth fibonacci No."""
    if n < 2:
        return n
    return fibo(n-1) +  fibo(n-2)
print(fibo(35))

#2.
def add_to_dict(a, b=dict()):
    if b is None:
        b=dict()
    b[a]=a**2
    return b
    
print(add_to_dict(23,{"rk":20}))

#3.
def var(**kwargs):
    """This function takes keywords args and filter on that pair which value is integer"""
    return {k:v for k,v in kwargs.items() if isinstance(v,int)}

print(var(rk="rki",sk=17,vb=14,skb=47,ab=43))

#4.
fx = lambda x : x**3
def callback(func, lst) :
    c = {func(x) for x in lst}
    return c

print(callback(fx, [1, 5, 2, 9, 7]))
#5.
def upper_fun():   #function that return another function
    def lower_fun(a):
        return a**2
    return lower_fun

square=upper_fun()
print(square(4)) #16

#6.
import time
def timer_decorator(func):
    """This function calculates time taken by any function."""
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrap

@timer_decorator
def complex_calculation(n):
    return sum(x**2 for x in range(n))
print(complex_calculation(10000))

#7.

#8.
def f_x(n):
    """This function do cubic operation."""
    return n**3

def g_x(num1,num2):
    """This function do addition operation."""
    n = num1 + num2
    return f_x(n)
print(g_x(9,12))

def compose(f, g):
    return lambda x : f(g(x))

f = lambda x: x + 1
g = lambda x: x ** 2
h = compose(f, g)
print(h(3))
print(h(8))

#9.
from functools import partial 
"""function by partial"""
multiply_by_2 = partial(lambda x,y: x * y,2)
print(multiply_by_2(3))
print(multiply_by_2(8))

#10.
lst=[]
def average_of_list(nums):
    """This function Returns average of list or None if error occurs"""
    sum,leng=0,0
    if not nums:  #means nums is empty then None
            return None
    for val in nums:
        sum+=val
        leng+=1
    return sum/leng
print(average_of_list(lst))

def avg(num):
    try:
        if not num:
            return None
        return sum(num) / len(num)
    except (TypeError, ZeroDivisionError):
        return None
print(avg(lst))

#11.
def fibonacci_series(n):
    """This function print the Fibonacci sequence """
    if n <= 0:
        return None
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fibonacci_series(38))

#12.  # Revisit to understand
def fx(x):
    def fy(y):
        def fz(z):
            return x*y*z
        return fz
    return fy

print(fx(39)(45)(180))

#13.
def write_to_file(lst, filename):
    """Thhis function works as context manager."""
    try:
        with open(filename, 'a') as f:
            for num in lst:
                f.write(f"{num}\n")
    except IOError as e:
        print(f"An error occurred : {e}")

write_to_file([1,2,3,4,5], 'sample.txt')

#14.
def mixed_list(mix):
    """This functions segregate different data types."""
    li = list()
    lf = list()
    ls = list()

    for i in mix:
        if isinstance(i,int):  #checking but if i is 'True' it go in so """if in int and not in bool"""
            li.append(i)
        elif isinstance(i,float):
            lf.append(i)
        else:
            ls.append(i)
    return li,lf,ls

n=[1,2,5,5.4,"dd",322,34.45]
print(mixed_list(n))

#15.
def call_count(counter = {'count' : 0}):
    """This functions counts no of times this fun called"""
    counter['count'] += 1
    return counter['count']

print(call_count())
print(call_count())
print(call_count())
print(call_count())
print(call_count())

        
        





