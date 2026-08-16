"""A generator is a special type of function that produces values ONE at a time
instead of returning everything at once.

It uses the keyword yield instead of return."""

"""WHY DO WE NEED GENERATORS?
Because normal functions:
compute everything
store everything in memory
return all values at once
This is a problem when the output is huge (like 10 million numbers).

Generators:
compute only when needed
do not store everything
save memory and speed
This is called lazy evaluation.

Save memory
Fast
Useful for big data, streaming, reading huge files
    """
    
def normal_func():
    return [1,2,3]
res = normal_func()
print(res)
print("---------------------")

def gen():
    yield 1
    yield 2
    yield 3
    
g = gen()
print(next(g))
print(next(g))
print(next(g))

"""HOW yield WORKS (very simple)
Think of yield as a pause button:
The function runs
Hits a yield → outputs a value
Function freezes
Next time you call next() → it continues from where it stopped"""
print("---------------------")


def demo():
    print("step 1")
    yield 10
    print("step 2")
    yield 20
    
d = demo()
print(next(d))
print(next(d))

#Save memory

print("---------------------")

def func():
    return [i for i in range(1,100)] #uses huge memory

res = func()
print(res)

def gen_func():
    for i in range(1,100):
        yield i
        
g = gen_func()
print(next(g))
print(next(g))

print("---------------------")

#Reading files
def read_files():
    with open("big.txt") as f:
        for lines in f:
            yield lines
g = read_files()
print(next(g))
print(next(g))

# Generator Expressions
# Just like list comprehensions, but generators:
print("---------------------")

g= (x*x for x in range(10))
print(g)
print(next(g))
print(next(g))

print("---------------------")

def infinite_count():
    n=1
    while True:
        print("before yield")
        yield n
        print("after yield")
        n = n+1
        print("end of loop")
        
g = infinite_count()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("-----------------------------------")

print("---------------------")


def generator_func(value):
    print("inside a generator")
    count =0
    while count < value:
        print("before yield")
        yield count
        print("after yield")
        count += 1
        print("loop completed")
        
gen = generator_func(3)
print(next(gen))
print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
print("---------------------")


    


def generator_func(value):
    print("inside a generator")
    count =0
    while count < value:
        print("before yield")
        yield count
        print("after yield")
        count += 1
        print("loop completed")
        
gen = generator_func(3)

print(gen.__next__())
print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

# 1️⃣ What is a coroutine?

# A coroutine is like a generator, but you can send data into it while it’s paused.

# Generators: only yield values out → you call next() to get the next value
# Coroutines: you can pause, yield, and also receive values using .send()

# Think of it like a conversation:

# Generator: “I give you numbers one by one.”
# Coroutine: “I give you numbers, but you can also tell me something back before I continue.”

""" Generator = You ask the generator for data
next(gen) → generator gives output

Coroutine = Coroutine asks YOU for data
cor.send(value) → coroutine receives input"""

"""Generators:
You pull values from them
→ using next()

Coroutines:
You push values into them
→ using send()

This is the MAIN difference."""

# Feature	       Generator	  Coroutine
# Purpose	    produce values	  receive values
# Uses yield	    YES	          YES
# next()	     get value	      start coroutine
# send()	   rarely used	      main method
# Communication	one-way	      two-way
# Async support	no	          yes (conceptually)

"""
✅ In a generator, you can ONLY pull values using next().
❌ You cannot send input into the generator with next().
✅ In a coroutine, you can push values into the function using .send().

This is the MAIN difference. 
"""
# def coro():
#     print("coroutine started")
#     x = yield
#     print("received: ",x)
    
# # c = coro()
# # next(c) #here (coroutine started and returns None

# c = coro()
# next(c) # here (coroutine started) and coroutine pauses at x= yield
# c.send(10)    # x = 10 and received : 10


"""Why can't next() send a value?
Because next() always sends None."""


def cour():
    print("corotine started")
    while True:
        x = yield #assgn yield to a variable that is how coroutine works
        print("received: ",x)
        
cr = cour()
next(cr)
cr.send(10)
cr.send(20)

def my_coro():
    print("started my_corr")
    a = yield #corotine freezez here  then mc.send 100 -> then unfreeze a=yield and a =100 so cortine receives data
    print("A: ",a)
    b = yield #corottine ferezes again
    print("B: ",b) #when mc.send 200, cortine unfreezes and prints b= 200
    c = yield
#so baiscaly send unfrezes it and prints b =200 then again at next yield it pauses 
# just like next() startes from where it paused , and corotine
# unfezes where it freezed (yield)
mc = my_coro()
next(mc) # corotine starts and stops (freezes) till yield.
mc.send(100)
mc.send(200)


def gen_func(value):
    print("generator started")
    count =0
    while count < value:
        print("1st time yield")
        yield count

        print("after yield")
        count = count+1
        print("done")
        
res = gen_func(5)
print(next(res))
print(next(res))
print(next(res))


def mine_corr():
    print("start corr")
    a = yield
    print("A: ",a)
    b = yield
    print("B: ",b)
    c = yield
cor = mine_corr()
next(cor)
cor.send(11)
cor.send(22)
# cor.send(33)


