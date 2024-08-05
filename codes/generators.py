def generator_func(value):
    print("inside generator function")
    count = 0
    
    while count < value:
        print("waiting befire yield statement")
        yield count
        print("yield statement executed")
        count +=1
        
# for values in generator_func(3):
#     print(values)
    
generator=generator_func(3)
print(generator)
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())

print("----------------------")

def begin_coroutine(func):
    def inner_function():
        result = func()
        result.__next__()
        return result
    return inner_function

@begin_coroutine     # output = begin_coroutine(my_generator)  -> return output()
def my_generator():
    print("generator called")
    input = yield 1  # freeze # assign value to yield (and "send" automatically unfrezes it)
    print(f'got value {input}')
    print("i am unfrozen")
    input= yield 2 # freeze
    print(f'got value 2nd time  {input}')
    print("i am unfrozen 2nd time")
    yield 3
    
    
started_coroutine = my_generator()  
# print(result)
# first = result.__next__()
started_coroutine.send(100)
started_coroutine.send(200)

# print(first)
# second = result.__next__()
# print(second)
# third = result.__next__()
print("program completed")



# open the file
# line by line in the file
# seach_word()
# write_to_db()
