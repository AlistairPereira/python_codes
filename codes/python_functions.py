def add(a,b):
    print(a+b)
    
x = add(3,4)
print(x)

def add(a,b):
    return a+b

y = add(3,5)
print(y)


z=y+6
print(z)

# a=x+6
# print(a)

# Python First-Class Functions:
# Rule 1: A function can be assigned to a variable

def add(a,b):
    sum = a+b
    print(sum)
    
x = add
print(x(15,4))

def add(a,b):
    sum = a+b
    return sum
    
x = add
print(x(15,4))

def add(a,b):
    sum = a+b
    return sum
    
x = add
print(x(b=12,a=13))

#Assign multiple functions

def square(x):
    return x*x

def cube(y):
    return y*y*y
    
f1 = square
f2 = cube
print(f1(3))
print(f2(3))

#Store functions in a list

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

functs =[add,sub,mul]
for f in functs:
    print(f(3,6))
    
    
# Store functions in a dictionary (VERY common)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
ops = {
    "add":add,
    "sub":sub,
    "mul":mul
}

print(ops["add"](2,3))
print(ops["sub"](10,5))
print(ops["mul"](3,3))


# Rule 2: the function should be returnable from a function
# Rule 2: A function can be RETURNED from another function

def outer():
    print("this is outer")
    def inner():
        print("i am inner func")
        
    return inner

x = outer()
x()
# print(x())

def math_operation():
    def square(n):
        return n*n
    return square

f = math_operation()
print(f(5))

# Return different functions based on input

def functions(name):
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    
    if name == "sqaure":
        return square
    else:
        return cube
    
res = functions("cube")
print(res(4))

# Function that returns another function with parameters

def power(x):
    def calc(n):
        return n **x
    return calc

sqaure = power(2)
print(sqaure(3))

cube = power(3)
print(cube(3))

#A function can be PASSED as an argument to another function

def greet():
    print("hello")
    
def call_me(func):
    func()
    
call_me(greet)

#You are NOT passing greet()
# You are passing greet (a function reference)
# You are NOT passing greet()
# You are passing greet (the function) as an argument.

def add(a,b):
    return a+b

def operate(func, x,y):
    return func(x,y)

res = operate(add,3,6)
print(res)

#Passing multiple functions

def double(n): return n*2
def triple(n): return n*3
def quad(n): return n*4

def apply(func, value):
    return func(value)

print(apply(double,2))