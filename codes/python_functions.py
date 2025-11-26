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

#  Calculator Using Dictionary of Functions (Clean & Professional)

# def calculator(operation):
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
    
#     # user = input("enter operation add,sub: ")
#     if operation == "add":
#         return add
#     elif operation == "sub":
#         return sub
#     else:
#         raise ValueError("wring operation entred , eter add/sub: ")
    
# res = calculator("sub")
# print(res(10,20))

# def calculator():
#     def add(a,b):
#         return a+b
    
#     def sub(a,b): 
#         return a-b
    
#     def mul(a,b): 
#         return a*b
    
#     def div(a,b):
#         if b ==0:
#             return ZeroDivisionError
#         return a/b
    
#     operations = {"add": add, "sub": sub, "mul": mul, "div": div}
    
#     op = input("enter operations add/sub/mul/div: ")
#     a = float(input("enter num1: "))
#     b = float(input("enter num2: "))
    
#     if op not in operations:
#         return "invalid operation name"
    
#     result = operations[op](a,b)
#     print(f"result: {result}")
    
# calculator()    

print("-------------------------------------")
# def calculator():
#     def add(nums):
#         result =0
#         for n in nums:
#             result = result+n
#         return result
    
#     def sub(nums): 
#         result = nums[0]
#         for n in nums[1:]:
#             result = result - n
#         return result
    
#     def mul(nums): 
#         result = nums[0]
#         for n in nums[1:]:
#             result = result * n
#         return result
    
#     def div(nums):
#         result = nums[0]
#         for n in nums[1:]:
#             if n ==0:
#                 return ZeroDivisionError
#             result = result/n
#         return result
    
#     operations = {"add": add, "sub": sub, "mul": mul, "div": div}
    
#     while True:
#         op = input("enter operations add/sub/mul/div: ")
#         # a = float(input("enter num1: "))
#         # b = float(input("enter num2: "))
#         # raw = input("enter numbers separated by space: ")
#         # nums = [float(x) for x in raw.split()]
        
#         if op == "exit":
#             print("bye bye, u have exited ")
#             break
    
#         if op not in operations:
#             print("invalid operation name")
#             continue
        
#         raw = input("enter numbers separated by space: ")
#         nums = [float(x) for x in raw.split()]
        
#         if len(nums) < 2:
#             print("Please enter at least two numbers.")
#             continue
        
    
#         result = operations[op](nums)
#         print(f"result: {result}")
    
# calculator()    


# #GUESS THE NUMBER GAME (Simple & Clean)

# import random
# def guess_number():
    
#     guess_no = random.randint(1,50)
#     print("think a no between 1 - 50")
#     print("ypu have 3 attempts")
    
#     for i in range(1,4):
#         user = int(input("enter a number to guess: "))
#         if user == guess_no:
#             print("congratualtons! you guessed the right number!")
#             print(f"you have guessed in {i} attempts")
#             break
        
#         if user < guess_no:
#             print("no is low")
#         if user > guess_no:
#             print("no too high")
            
#         attempts_left =  3-i
#         if attempts_left > 0:
#             print(f"only attmepts left : {attempts_left}")
            
#     print(f"out of attmepts the correct no was {guess_no}")
    
# guess_number()


# def guessing_number():
    
#     secret_no = random.randint(1,20)
#     print("think of a number to enter: ")
#     print("only 3 attempts: ")
    
#     for i in range(1,4):
#         user_number = int(input("enter a number: "))
#         if user_number == secret_no:
#             print(f"congrats! you have and guess in {i} attmepts")
            
#         if user_number < secret_no:
#             print("no is low")
#         if user_number > secret_no:
#             print("no is high")
            
#         attempts = 3 - i
#         print(f"attempts left : {attempts}")
            
#     print(f"the correct no is {secret_no}")
    
# guessing_number()


# Create a Password Strength Checker

"""Write a function that takes a password string and returns:

"Very Weak","Weak""Medium""Strong""Very Strong"
Based on these rules:

Condition	Points
Length ≥ 8	+1
Contains lowercase	+1
Contains uppercase	+1
Contains digit	+1
Contains special char (!@#$%^&*?)	+1

Score → Strength
1 → Very Weak
2 → Weak
3 → Medium
4 → Strong
5 → Very Strong"""

def password_detector(password):
    points =0
    specials = "!@#$%^&*"
    
    if len(password)>8:
        points +=1
    if any(ch.islower()for ch in password):
        points +=1
    if any(ch.isupper() for ch in password):
        points +=1
    if any(ch.isdigit() for ch in password):
        points+=1
    if any(ch in specials for ch in password):
        points+=1
        
    if points == 1:
        return "very weak"
    elif points ==2:
        return "weak"
    elif points == 3:
        return "Medium"
    elif points == 4:
        return "Strong"
    else:
        return "Very Strong"
    
print(password_detector("12@#$Dei@%^*"))
