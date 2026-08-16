#Even Squares Generator

# def even_gen():
#     for i in range(1,11):
#         if i%2==0:
#             yield i
    
# g = even_gen()
# print(next(g))
# print(next(g))


# def even_gen(n):
#     for i in range(1,n+1):
#         if i%2 ==0:
#             yield i
            
# g = even_gen(10)
# print(next(g))
# print(next(g))

# def even_squares(n):
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             yield i * i

# g = even_squares(10)
# print(next(g))   
# print(next(g))   
# print(next(g))   
# print(next(g))
# print(next(g))
# # print(next(g))

# def even_2_odd(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i *i
#         else:
#             yield i
# res = even_2_odd(10)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

# def even_2_odd(n):
#     for i in range(1, n+1):
#         if i%2 ==0:
#             yield i*i
#         else:
#             yield i
            
# res = even_2_odd(10)
# print(next(res))
# print(next(res))
# print(next(res))

# when i=2
# Since the yield i*i was the last statement in the if block, Python:

# Exits the if block
# Continues the for loop → next iteration or goes to else only if the if condition was False





# def even_corr(n):
#     print("start corr")
#     while True:
#         i=yield
#         if i %2 ==0:
#             yield i*i 
#         else:
#             yield i

            
            
# res = even_corr(10)
# next(res)
# print(res.send(2))
# print(res.send(3))

def even_corr(n):
    while True:
        i =yield
        if i%2 ==0:
            yield i*i
        else:
            yield i
            
res = even_corr(10)
next(res)
print(res.send(2))
next(res)
print(res.send(3))

# Important:

# After the first yield (4) → the coroutine is paused again at the second yield inside the if/else block
# The next .send() goes back to the previous i = yield line (at the top of the while loop)

# Step by step:

# Coroutine resumes at i = yield → waiting for a new value
# .send(3) → assigns i = 3
# Checks:

'''Key Concept: You cannot “double yield” inside a coroutine like that
When you have both i = yield and another yield in the same loop, you are effectively pausing twice per iteration
The second yield must be resumed with next(), not .send()'''

# You only need one yield per iteration — combine logic like this:

# def even_corr():
#     while True:
#         i = yield           # receive value
#         result = i*i if i % 2 == 0 else i
#         yield result        # send the processed value
        
# res = even_corr()
# next(res)          # prime coroutine
# print(res.send(2))        # prints 4
# print(res.send(3))        # prints 3
# print(res.send(4))        # prints 16


# Question: Running Total Coroutine
# Write a coroutine called running_total() that:
# Starts with a total of 0
# Pauses and waits for a number using .send()
# Adds the number to the total
# Yields the current total after each send

def running_total():
    
    total =0
    while True:
        i = yield 
        total = total + i
        yield total
        
c = running_total()
next(c)
print(c.send(2))
next(c)
print(c.send(3))

def running_total():
    
    total =0
    while True:
        i = yield total  # yield current total first, wait for new number
        total = total + i
        
        
c = running_total()
next(c)
print(c.send(2))
print(c.send(3))