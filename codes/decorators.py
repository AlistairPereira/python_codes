# What is a Decorator? 
# A decorator is a function that takes another function and adds extra behavior to it 
# without changing the original function code.

#--------------------------------------------------------------------------------

# Original function:

# def say_hello():
#     print("Hello")
    
# Before function runs:

# Starting function...
# Hello
# Function finished

# Instead of modifying say_hello(), you wrap it with a decorator.

#------------------------------------------------------------------------
# Real-life example

# Imagine a restaurant:
# Original food: 
# Burger

# Decorator adds:
# Packaging
# Delivery
# Receipt

# The burger did not change.
# The extra features are added around it.

#---------------------------------------------------------------------

# def hello():
#     print("hello world")

# hello()

#without decorator it will print "hello world" only

# def decorator(func):

#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")

#     return wrapper


# def hello():
#     print("hello world")

# hello()

# res = decorator(hello)
# print(res())

#decorator(hello) -> returns a warpper fyunction and we store it in res
# In res we store the wrapper function, 
# and then res() calls the wrapper function, 
# where inside wrapper we call hello()
#------------------------------------------------------------------------

# What does @decorator mean?

# This:

# @decorator
# def hello():
#     print("hello world")

# is exactly the same as:

# def hello():
#     print("hello world")


# hello = decorator(hello)

# Python automatically does the replacement.

# Python converts:
# @decorator
# def hello():

# into:
# hello = decorator(hello)

# @decorator
# def hello():
#     print("hello india")
    
# hello()

def greet():
    print("good morning")
    
greet()
print("----------------------------------------")

def decorator(func):
    
    def wrapper():
        print("hello")
        func()
        print("end")
    
    return wrapper

res = decorator(greet)
res()
print("----------------------------------------")

@decorator
def greet():
    print("good morning")
    
greet()
print("----------------------------------------")

# Before:
# greet ---> original greet()

# After:
# greet = decorator(greet)

# becomes:
# greet ---> wrapper()

# The original greet is not deleted.
# It is stored inside.
# func
# inside the wrapper.

# @decorator
# def add(a,b):
#     print(a+b)
    
# add(5,10)
# TypeError: decorator.<locals>.wrapper() takes 0 positional arguments but 2 were given
# Step 2: Now you call:
# add(5,10)

# But remember:

# add = wrapper

# So Python actually does:

# wrapper(5,10)
# Problem ❌

# Your wrapper is:

# def wrapper():

def add_decorator(func):
    
    def wrapper(*args,**kwrags):
        print("start")
        func(*args,**kwrags)
        print("end")
        
    return wrapper


@add_decorator
def add(a,b):
    print(a+b)
    
add(10,20)

res = add_decorator(add)
print(res(10,5))

"Inside wrapper we call func(), which is the original add(). If we don't pass *args and **kwargs, it gives an error."
"because when res() calls wrapper function, we need wrapper to accept those arguments as weell" 


def timer_decorator(func):
    
    def wrapper(*args, **kwargs):
        print("started")
        result= func(*args, **kwargs)
        print("finished")
        return result
        
    return wrapper

@timer_decorator
def calculate_sum(a,b):
    return a+b
    
res = calculate_sum(10,20)
print(res)  

#-------------------------------------------------------------------------

def login_required(func):
    def wrapper(*args, **kwargs):
        password = input("enter a password: ")
        if password == "1234":
            result = func(*args, **kwargs)
            return result
        else:
            return "access denied"
    
    return wrapper

@login_required
def dashboard(username):
    return f"welcome to dashbaord: {username}"

res = dashboard("alistair")
print(res)

print("---------------------------")

def log_decorator(func):
    
    def wrapper(*args, **kwargs):
        print("Calling function:", func)
        result=func(*args, **kwargs)
        print("Function Completed")
        return result
    return wrapper
        

@log_decorator
def calculate_discount(price, discount):
    return price - (price * discount / 100)

res = calculate_discount(1000,20)
print(res)

print("-------------------------------------")

def log(func):
    def wrapper(*args, **kwargs):
        print("Log start")
        result = func(*args, **kwargs)
        print("Log end")
        return result
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        print("Timer start")
        result = func(*args, **kwargs)
        print("Timer end")
        return result
    return wrapper

@log
@timer
def add(a,b):
    return a+b

res = add(10,22)
print(res)

# The top decorator is always the first one to execute when you call the function. ✅
# This is the only tricky part of multiple decorators bro. Once this clicks, you understand them

# When you CALL the function → it starts from LOG first.
# But when Python applies decorators → TIMER is created first.
# These are two different moments.
# add = log(timer(add))

# First timer happens:
# add = timer(add)

# Inside timer:
# func = original add

# Timer returns:
# timer wrapper

# So now:
# add ---> timer wrapper
# Then log happens:
# add = log(add)

# But remember:
#     Now add is already:
# add ---> timer wrapper

# So when log receives:
# def log(func):

# here:
# func = timer wrapper

# Then log returns:
# log wrapper



def performance(func):
    def wrapper(*args, **kwargs):
        print("started")
        result= func(*args, **kwargs)
        print("finised")
        return result
    return wrapper


@performance
def calculate_total(numbers):
    total=0
    for num in numbers:
        total += num
        
    return total

result = calculate_total([10,20,30,40,50])
print(result)

#---------------------------------------------------

def retry(func):
    
    def wrapper(*args, **kwargs):
        attempts =0
        while attempts < 3:
            try:
                print("started")
                result = func(*args, **kwargs)
                print("stopped")
                return result
            except Exception as e:
                print("Error: ", e)
                attempts +=1
            
        return "failed after 3 attempts"
        
    return wrapper

@retry
def divide(a,b):
    return a/b

res = divide(10,0)
print(res)
