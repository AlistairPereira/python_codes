def greet():
    print("hello how r you")
greet()

# Summary
# print() → just displays something; function returns None
# return → sends the value back; function can be stored or reused

def add(a,b):
    print(a+b)

x=add(3,5)
print(x)

def add(a,b):
    return a+b

y=add(4,5)
print(y)

a=10
c= a+y
print(c)

# a=11
# c=a+x
# print(c)

# 1️⃣ print
# Shows the value on the screen
# Function does not give anything back → automatically returns None
# You cannot use the value elsewhere

# Example:

def add(a, b):
    print(a + b)

x = add(3, 5)  # prints 8
print(x)       # prints None

# Explanation:

# print(a + b) → just displays 8
# x stores nothing → None

# 2️⃣ return
# Function sends the value back
# You can store it in a variable
# You can use it for other calculations

# Example:

def add(a, b):
    return a + b

x = add(4, 5)      # stores 9 in x
y = add(x, 10)     # adds 9 + 10 → 19
print(y)

# Output:

# 19

# Explanation:

# return → gives the value to the variable x
# You can now use x in other calculations

# print → just shows, cannot use it
# return → gives back, you can use it anywhere

#----------------------------------------
# A function can be assigned to a variable

def add(a,b):
    return a+b

sum_func = add # assign the function to a variable
res = sum_func(2,77) #Call the function using the new variable
print(res)

print(add(2, 3))       # 5
print(sum_func(2, 3))  # 5



def square(x):
    return x*x

sq_func = square
res = sq_func(6)
print(res)

print(square(5))

# Rule 2: the function should be returnable from a function
# a function can return another function

def outer():
    print("i am outer function")
    
    def inner():
        print("i am inner function")
        
    return inner

returned_func = outer()
returned_func()


# Key point:
# outer() → runs the outer function and returns inner
# returned_func → stores the inner function
# returned_func() → now you actually call the inner function

# Why is this useful?
# You can create functions dynamically
# You can return specialized functions depending on conditions
# It’s used a lot in decorators and functional programming

def operation(op):
    if op == "add":
        def add(a,b):
            return a+b
        return add
    
    if op == "multiply":
        def multiply(a,b):
            return a*b
        return multiply
    
add_func=operation("add")
print(add_func(9,10))

mul_func = operation("multiply")
print(mul_func(10,9))

# add_func = operation("add")
# Python runs the operation function with op = "add"
# Inside operation, it sees "add" → defines the inner function add(a, b)
# return add → gives the function itself back (does not run it yet!)
# Now add_func stores the add function

# Think:

# add_func → points to add(a,b)
# Then you do:
# print(add_func(9, 10))
# Now Python calls the stored function
# add_func(9, 10) → runs the code inside add → returns 9 + 10 = 19
# print → displays 19

## # Rule 3: the function should be passable into a function

# Examples of objects
# Object type	      Example
# Number	                5
# String	                "hello"
# List	             [1,2,3]
# Dictionary	         {"a":1}
# Function	         def add(a,b): return a+b
# In Python, functions themselves are objects, so you can pass a function into another function.

def add(a,b):
    return a+b

def operate(func, x,y):
    result = func(x,y)
    return result

print(operate(add,3,5))

# Step by step:
# operate(add, 10, 5) → func now points to add
# Inside operate → func(10, 5) → runs add(10, 5) → returns 15
# operate returns 15 → printed

def even_odd(num):
    
    if num%2==0:
        return "even"
    else:
        return "odd"
    
res = even_odd(7)
print(res)

def sum_numbers(l):
    
    sum=0
    for nums in l:
        sum=sum+nums
        
    return sum

res = sum_numbers([1,2,3,4,5])
print(res)

def is_prime(num):
    if num <=1:
        return "not a prime"
    
    for i in range(2,num):
        if num%i==0:
            return 'not prime'
            break

    return 'prime no'
        
res = is_prime(1)
print(res)



def rev_str(s):
    
    return s[::-1]

res = rev_str("python")
print(res)



def vowel_count(s):
    
    vowels =['a','e','i','o','u']
    count=0
    for char in s:
        if char in vowels:
            count +=1
            
    return count

res = vowel_count("alistair")
print(res)

# Question 5: Prime numbers in a range
# Write a function primes_in_range(start, end) that returns all prime numbers between start and end (inclusive).
# Test it with 10, 30 → should return [11, 13, 17, 19, 23, 29].

def is_prime(num):
    if num <=1:
        return "not a prime"
    
    for i in range(2,num):
        if num%i==0:
            return False
            break

    return True
        
res = is_prime(1)
print(res)

def primes_in_range(start,end):
    
    l=[]
    for i in range(start,end+1):
        # if start%i != 0 or end%i != 0:
        if is_prime(i):
            l.append(i)
    return l
        

res = primes_in_range(10,30)
print(res)

# #Question: Count Positives, Negatives, and Zeros
# Write a function count_pos_neg_zeros(lst) that takes a list of numbers as input.
# The function should return a dictionary with:
# 'pos' → number of positive numbers
# 'neg' → number of negative numbers
# 'zeros' → number of zeros
# {'pos': 3, 'neg': 2, 'zeros': 2}

def count_pos_neg_zeros(lst):
    
    pos_count=0
    neg_count=0
    zer_count=0
    for nums in lst:
        if nums > 0:
            pos_count+=1  
        elif nums <0:
            neg_count+=1  
        else:
            zer_count+=1
    return {"pos":pos_count, "neg":neg_count, "zeros":zer_count}
            
res=count_pos_neg_zeros([0, -1, 5, -3, 8, 0, 2])
print(res)
    
def sum_nums(*n):
    
    sum=0
    for num in n:
        sum=sum+num
    return sum

res = sum_nums(1,2,3,4)
print(res)



# *args collects all arguments into a tuple args = (1,2,3) or (4,5,6,7,8)
# You can loop through them, sum them, multiply them, etc.
# ✅ Key: *args → any number of positional arguments

# Double asterisk **kwargs
# **kwargs allows a function to accept any number of keyword arguments (arguments with names).
# Inside the function, kwargs becomes a dictionary containing all the extra keyword arguments.

def user_info(**info):
    
    for k,v in info.items():
        return (f"{k}: {v}")
    
res = user_info(name ="alis",age=26, surname="Alex", city="Berlin", email="alex@example.com")
print(res)

# 1️⃣ return stops the function immediately
# Once Python sees a return, it exits the function and sends the value back.
# That’s why in your loop, only the first item was returned.

def user_info(**info):
    
    result =""
    for k,v in info.items():
        result += f"{k}: {v}\n"
    return result
    
res = user_info(name ="alis",age=26, surname="Alex", city="Berlin", email="alex@example.com")
print(res)

def user_info(**info):
    result = []
    for k, v in info.items():
        result.append(f"{k}: {v}")
    return result  # return after the loop

res = user_info(name="Alis", age=26, city="Berlin")
print(res)


# ✅ Rule of thumb:
# return sends one object back (it could be a number, string, list, dict, tuple, etc.)
# If you want multiple things, put them in a list, tuple, or dict and return that

# Question 1: Calculator function
# Write a function calculator(a, b, operation) that can add, subtract, multiply, or divide two numbers based on the operation argument 
# ("add", "subtract", "multiply", "divide").
# Example:
# calculator(10, 5, "multiply")  # Output: 50

def calculator(operation):
    
    if operation == "add":
        def add(a,b):
            return a+b
        return add
        
    if operation == "subtract":
        def subtract(a,b):
            return a-b
        return subtract
        
    if operation == "multiply":
        def multiply(a,b):
            return a*b
        return multiply
        
    if operation == "divide":
        def divide(a,b):
            return a/b
        return divide
        

res = calculator("multiply")
print(res(10,5))


def calc(operation):
    a= int(input("enter num1:"))
    b= int(input("enter num2: "))

    if operation == "add":
        return a+b
    elif operation == "multiply":
        return a*b
    elif operation == "divide":
        return a/b
    elif operation == "subtract":
        return a-b
    else:
        return "invalid operation"

op = input("Enter operation (add/multiply/divide/subtract): ").lower()
res = calc(op)
print(res)  
 
# Next line outside any function is executed
# op = input("Enter operation (add/multiply/divide/subtract): ").lower()
# Python goes inside the calc function
# operation parameter gets the value of op (whatever the user typed)     


def calculate(operation , *args):
    
    if operation == "add":
        result= sum(args)
    elif operation == "multiply":
        result = 1
        for nums in args:
            result= result * nums
    elif operation == "subtract":
        result = args[0]
        for nums in args[1:]:
            result = result - nums
    elif operation == "divide":
        result = args[0]
        for nums in args[1:]:
            if nums ==0:
                return ZeroDivisionError
            result = result/nums
            
    else:
        return 'invalid operations'
    
    return result
                
res = calculate("add",2,3,4,5)
print(res)                

res = calculate("multiply",2,3,4,5)
print(res)   

# Question 2: Count vowels, consonants, digits, special characters
# Write a function char_summary(s) that takes a string s and returns a dictionary:
# 'vowels' → number of vowels (a, e, i, o, u)
# 'consonants' → number of consonants
# 'digits' → number of digits
# 'special' → everything else
# Test:
# char_summary("Hello123!")  # Output: {'vowels': 2, 'consonants': 3, 'digits': 3, 'special': 1}



def count_chars(x):
    vowels =['a','e','i','o','u']
    special =['!',"@","#","$","%"]
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    
    count_vowels =0
    count_special=0
    count_digits=0
    count_consonants =0
    for char in x:
        if char in vowels:
            count_vowels +=1
        if char in special:
            count_special +=1
        if char in digits:
            count_digits +=1
        if char not in vowels and char not in special and char not in digits:
            count_consonants +=1
    return {"vowels": count_vowels, "special": count_special, "dgits": count_digits,"consonants": count_consonants}

res = count_chars("Hello123!")
print(res)

def count_chars(x):
    vowels = ['a','e','i','o','u']
    special = ['!', "@", "#", "$", "%"]
    digits = ["0","1","2","3","4","5","6","7","8","9"]

    count_vowels = 0
    count_special = 0
    count_digits = 0
    count_consonants = 0

    for char in x:
        c = char.lower()
        if c in vowels:
            count_vowels += 1
        elif char in special:
            count_special += 1
        elif char in digits:
            count_digits += 1
        elif c.isalpha():  # any other alphabet character → consonant
            count_consonants += 1

    return {"vowels": count_vowels, "special": count_special, "digits": count_digits, "consonants": count_consonants}

res = count_chars("Hello123!")
print(res)
        

l=[1,1,3,4,5,1,3,4]
d={}
for num in l:
    if num in d:
        d[num] +=1
    else:
        d[num]=1
   
print(d)  


def is_palindrome(s):
    
    if s == s[::-1]:
        return True
    else:
        return False

res = is_palindrome("nitin")
print(res)

# Question 2: Word Frequency Counter
# Write a function word_frequency(sentence) that:
# Takes a string sentence as input
# Returns a dictionary where:
# Keys = words in the sentence
# Values = number of times each word appears
# Example:
# sentence = "hello world hello python"
# word_frequency(sentence)

# Expected output:

# {'hello': 2, 'world': 1, 'python': 1}

def word_frequency(sentence):
    
    sentence = sentence.split()
    
    d={}
    for char in sentence:
        if char in d:
            d[char]+=1
        else:
            d[char]=1
            
    return d
            
res = word_frequency("hello world hello python")
print(res)

s="hello world hello python"
print(s)
print(s.split(" "))
print("".join(s))

# Question 3: Text Analyzer

# Write a function text_analyzer(text) that:

# Takes a string text as input
# Returns a dictionary with the following statistics:
# 'words' → total number of words
# 'unique_words' → number of unique words
# 'letters' → total number of alphabetic characters
# 'digits' → total number of digits
# 'special_chars' → total number of special characters (anything not a letter or digit)
# sentence = "Hello World! 123 Python."
# text_analyzer(sentence)

# Expected output:

# {
#   'words': 4,
#   'unique_words': 4,
#   'letters': 17,
#   'digits': 3,
#   'special_chars': 3
# }

def text_analyzer(sentence):
    
    special =['!',"@","#","$","%"," "]
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    
    digit_count =0
    special_count =0
    letters =0
    
    words_list = sentence.split()
    words = len(words_list)
    unique_words = len(set(words_list))
        
    for char in sentence:
        if char in digits:
            digit_count+=1
        if char in special:
            special_count+=1
        if char.isalpha():
            letters+=1
        
    
    return {"digits":digit_count, "special": special_count,"letters":letters,"unique": unique_words,"words":words}


res = text_analyzer("Hello World! 123 Python Hello.")   
print(res)         


# Question 3: Max Occurring Character
# Write a function max_char(s) that returns the character that appears the most times in a string s.
# Test with "programming" → Output: 'g'
    
    
def max_char(s):
    
    d={}
    for char in s:
        if char in d:
            d[char]+=1
        else:
            d[char]=1

    max_count=0
    max_char=''
    for k,v in d.items():
        if v > max_count:
            max_count = v
            max_char =k
        
    return max_char
        
    

res = max_char("programmingg")
print(res)

# Question: Count Word Lengths
# Write a function word_lengths(sentence) that:
# Takes a string sentence as input
# Returns a dictionary where:
# Keys = words
# Values = length of each word
# Example:
# sentence = "Python is fun"
# word_lengths(sentence)

# Expected output:

# {'Python': 6, 'is': 2, 'fun': 3}

def word_lengths(s):
    
    s= s.split()
    result={}
    for words in s:
        result[words] = len(words)
    return result
        

res = word_lengths("Python is fun")
print(res)

s= "Python is fun"
s=s.split()
for words in s:
    print(words,":", len(words))

# Question: Price Analyzer
# Write a function price_analyzer(prices) that:
# Takes a list of prices (numbers) as input, e.g., [100, 250, 50, 400]
# Returns a dictionary with:
# 'max_price' → highest price
# 'min_price' → lowest price
# 'average_price' → average price
# 'total_price' → sum of all prices
# Example:
# prices = [100, 250, 50, 400]
# price_analyzer(prices)
l=[1,2,3,4,5]
print(len(l))
        
def prize_analyzer(l):
    

    total = sum(l)
    max_num = max(l)
    min_num = min(l)
    avg = total/len(l)
        
    return {"total": total, "avg": avg,"max":max_num, "min":min_num}

res = prize_analyzer([1,2,3,4,5])
print(res)
    
l=[1,2,3,4,5]
print(len(l))