# 1️⃣ What is a generator?

# A generator is a special kind of function in Python that:

# Yields values one at a time instead of returning all at once
# Is memory-efficient, especially for large datasets
# Uses the yield keyword instead of return

# Think of it like a water tap:

# You don’t store the whole bucket in memory
# You get one drop at a time when you turn the tap

def normal_func():
    return [1,2,3]

res = normal_func()
print(res)

def gen():
    yield 1
    yield 2
    yield 3
    
g = gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) - stop iteration error

"""HOW yield WORKS (very simple)
Think of yield as a pause button:
The function runs
Hits a yield → outputs a value
Function freezes
Next time you call next() → it continues from where it stopped"""

def demo():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    
d = demo()
print(next(d))
print(next(d))

#Save memory

def func():
    return [i for i in range(1,100)] #uses huge memory

res = func()
print(res)


def func():
    for i in range(1,100):
        yield i
res =func()
print(next(res))
print(next(res))

#reading files


def read_files():
    with open("big.txt") as f:
        for lines in f:
            yield lines
g= read_files()
print(next(g))
print(next(g))

# Generator Expressions
# Just like list comprehensions, but generators:
print("---------------------")

g =(x*x for x in range(10))
print(g)
print(next(g))
print(next(g))


def infinite_count():
    
    n=1
    while True:
        print("befire yield")
        yield n
        print("after yield")
        n=n+1
        print("end loop")

g = infinite_count()
print(next(g))
print(next(g))

def generator_func(value):
    
    count =0
    while count < value:
        print("before yield")
        yield count 
        print( "aftr yield")
        count += 1
        print("ending")

g = generator_func(3)
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) stop iteration error

def generator_func(value):
    print("inside a generator")
    count =0
    while count < value:
        print("before yield")
        yield count
        print("after yield")
        count += 1
        print("loop completed")
        
g = generator_func(3)

print(g.__next__())
print(g.__next__())


#Coroutines

# def simple_coroutine():
#     print("couroutine started")
#     x=yield
#     print("received", x)
    
# co = simple_coroutine()
# next(co) #here corotuine started and returns None, # Start the coroutine, runs until the first yield
# co.send(10)

# next(co) → starts coroutine, runs until yield, pauses
# co.send(10) → resumes from yield (resumes the coroutine:), assigns x = 10 → prints Received: 10
# Important: you must call next() once before .send(), otherwise Python will raise an error.

# Why StopIteration happens
# next(co) → starts the coroutine, runs until the first yield, pauses there. ✅ This is correct.

# co.send(10) → resumes the coroutine:

# x = yield
# yield receives 10 → assigns x = 10
# Prints "received 10" ✅
# Then the function reaches the end → coroutine is finished → Python raises StopIteration
# Important concept:
# Once a coroutine (or generator) reaches the end of the function, it stops permanently
# The first .send() works, but the next .send() would raise StopIteration if there are no more yields

# How to make a coroutine reusable

# You need a loop so the coroutine can keep running and receiving values:

def simple_coroutine():
    print("coroutine started")
    while True:
        x = yield
        print("received", x)
c = simple_coroutine()
next(c)
c.send(10)
c.send(20)
        
# Step 1: next(c)
# Python enters the coroutine and executes:
# print("coroutine started")
# while True:
#     x = yield
# yield is hit → coroutine pauses here
# The variable x is not yet assigned
# next(c) returns None (because yield has no value)
# ✅ The coroutine is now paused at x = yield, waiting for a .send()
# Step 2: c.send(10)
# Python resumes exactly where it left off, right at the yield line:
# x = yield
# 10 is sent → assigned to x
# Next line executes:
# print("received", x)
# Output:
# received 10
# Then the coroutine goes back to the top of the while True loop, hits x = yield again → pauses and waits for next .send()

# ✅ Important: it does not start over at the top of the function — it resumes exactly after the last yield

# Step 3: c.send(20)
# Coroutine resumes from the paused yield line again
# x = yield
# 20 is sent → assigned to x
# Next line executes:
# print("received", x)
# Output:
# received 20
# Loop continues → pauses again at x = yield → ready for the next .send()
# Step 4: Key Concept — “Pause and Resume”
# Each yield pauses the coroutine and remembers its state
# .send(value) → resumes from exactly where it paused
# Local variables (like x) and loop state are preserved
# while True keeps it alive so you can keep sending values indefinitely

def my_coro():
    while True:
        print("corotine start")
        a=yield
        print("A", a)
        b = yield
        print("B", b)
        c=yield
        
    
c = my_coro()
next(c)
c.send(100)
c.send(200)
c.send(300)

# Step 5: What’s happening internally
# Step	  Coroutine state	                     Output
# mc = my_coro()	                      Coroutine created, not started	—
# next(mc)	      Runs till first yield	"started my_corr"
# mc.send(100)	     Resumes after first yield, a=100	"A: 100"
# mc.send(200)	       Resumes after second yield, b=200	"B: 200"
# Next mc.send(x)	 Pauses at c = yield