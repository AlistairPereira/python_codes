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

def math_op():
    def square(n):
        return n*n
    return square

res = math_op()
print(res(2))

def math_operator():
    def sq(n):
        return n*n
    return sq

f= math_operation()
print(f(2))

# Return different functions based on input

def functions(name):
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    
    if name == "square":
        return square
    elif name == "cube":
        return cube
    else:
        raise ValueError(f"unknown func name :{name} use square or cube")
    
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


def add(a,b):
    return a+b

def operate(func,x,y):
    return func(x,y)

print(operate(add,4,5))

#Passing multiple functions

def double(n): return n*2
def triple(n): return n*3
def quad(n): return n*4

def apply(func, value):
    return func(value)

print(apply(double,2))


# Count Even, Odd, Positive, Negative Using One Function

def analyze(nums):
    even=0
    odd=0
    pos=0
    neg=0
    zer =0
    for num in nums:
        if num>0:
            pos +=1
        elif num <0:
            neg +=1
        else:
            zer+=1
            
        if num%2 == 0:
            even+=1
        else:
            odd = odd+1
            
    return { "even": even, "odd":odd, "pos" : pos, "neg": neg, "zeros" : zer}
        
res = analyze([1, -2, 3, 4, -5, 6, 0])
print(res)
print(analyze([1, -2, 3, 4, -5, 6, 0]))


#Square only even numbers using list comprehension inside a function

def square_even(nums):
    x =[num*num for num in nums if num%2==0]
    return x

res = square_even([1,2,3,4,5,6,7,8,9,10])
print(res)

#Word Frequency Using a Function
def word_freq(s):
    freq = {}
    words = s.split()
    print(words)
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

res = word_freq("python is easy and python is powerful")
print(res)

# (Dictionary of squares except multiples of 3)

def dict_sq(nums):
    d ={i:i*i for i in range(1,nums+1) if i%3!=0}
    return d
res = dict_sq(11)
print(res)


# Filter list of dictionaries (marks > 75)
students = [
    {"name": "Alistair", "marks": 80},
    {"name": "Rahul", "marks": 70},
    {"name": "Akash", "marks": 90}
]

for s in students:
    # print(s)
    if s['marks']>75:
        print(s['name'])
        print(s)
        
def filter_students(students):
    return [s for s in students if s['marks']>75]

res = filter_students([
    {"name": "Alistair", "marks": 80},
    {"name": "Rahul", "marks": 70},
    {"name": "Akash", "marks": 90}
])

print(res)

#create  the function that takes a list of dictionaries and returns the sum of people budget
get_budgets = [
            {"name":"rahul","age":24,"budget":23000},
            {"name":"sahil","age":27,"budget":40000},
            {"name":"steve","age":16,"budget":2700}
               ]

sum = 0
for values in get_budgets:
    # print(values["budget"])
    sum = sum+values['budget']
print(sum)

def get_budgets(get_budgets):
    sum = 0
    for values in get_budgets:
    # print(values["budget"])
        sum = sum+values['budget']
    return sum

res = get_budgets([
            {"name":"rahul","age":24,"budget":23000},
            {"name":"sahil","age":27,"budget":40000},
            {"name":"steve","age":16,"budget":2700}
               ])
print(res)


#create a function that takes a list and finds the integer which appears an odd number of times.

def int_odd(l):
    d={}
    for values in l:
        if values in d:
            d[values]+=1
        else:
            d[values]=1
            
    for k,v in d.items():
        if v%2!=0:
            return k
    return None
    
    
res = int_odd([1,1,2,2,10,4,5,5,6,6,4])
print(res)


def integer_odd(l):
    d={}
    for values in l:
        if values in d:
            d[values]+=1
        else:
            d[values]=1
    
    result=[]
    for k,v in d.items():
        if v%2!=0:
            result.append(k)
    return result
res = integer_odd([1,1,2,2,10,4,5,3,5,6,6,4])
print(res)


#In each input list , every number repeats at least once , except for two.
#Write a function that returns the two unique numbers
#eg [1,9,8,8,7,6,1,6] :- [9,7]

def unique(l):
    d={}
    for values in l:
        if values not in d:
            d[values]=1
        else:
            d[values]+=1
    
    result=[]
    for k,v in d.items():
        if v ==1:
            result.append(k)
        
    return result
        
    
res = unique([1,9,8,8,7,6,1,6])
print(res)

