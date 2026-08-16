# # An function is treated as a first class citizen in a language
# # Rule 1: the function can be assigned to a variable
# # Rule 2: the function should be returnable from a function
# # Rule 3: the function should be passable into a function

# def some_function(value):
#     #print(value)
#     return value
    
# res=some_function("srh")
# print(res)

# def some_function():
#     print("some function")
#     return "srh"

# res = some_function
# res()

# def outer_function():
#     print("this is outer")
#     def inner_function():
#         print("inner function called")
#         return "srh"

#     return inner_function

# result = outer_function()
# print(result())
# print("------------------")

# def outer_function(value):
#     a=value()
#     print(a)
#     print("outerrrrr")
#     def inner_function():
#         print("inner called")
#         return "srh"
#     return inner_function
    
# def passable_fucntion():
#     print("passable caleed")
#     return "something"

# res = outer_function(passable_fucntion)
# print(res())

#DECORATORS

# def outer_function(func):
#     print("this is outer function")
#     def inner_function(*args,**kwargs):
#         print("inside inner function")
#         var= func(*args,**kwargs)
#         upper_case=var.upper()    
#         return upper_case
    
#     return inner_function
    
# @outer_function
# def string_function():
#     print("inside string function")
#     return "srh university heidelberg"

# result= string_function()
# print(result)

#GENERATORS

def generator_func(value):
    print("generator function")
    count=0
    
    while count < value:
        print("inside generator function")
        yield count
        print("after yield")
        count+=1
        
res = generator_func(3)
print(res.__next__())
print(res.__next__())
print(res.__next__())
# print(res.__next__())

print("---------------------")


def begin_coroutine(func):
    def inner_function():
        result= func()
        result.__next__()
        return result
    return inner_function


@begin_coroutine
def my_gen():
    print("gen called")
    input=yield 1
    print(f"got {input}")
    print("called 2nd time")
    input=yield 2
    print(f"got {input}")
    yield 3
    
res= my_gen()
res.send(1000)
res.send(2000)
    
