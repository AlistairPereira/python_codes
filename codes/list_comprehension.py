fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
# numbers_plus_one = []
# for number in numbers:
#     numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
# numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax.
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]
output =[fruit.upper() for fruit in fruits]
print(output)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension 
# syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.title() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
l=[]
vowels =["a","e","i","o","u"]
for s in fruits:
    count=0
    for char in s:
        if char in vowels:
            count +=1
    if(count > 2):
        l.append(s)
print(l)

fruits_with_more_than_two_vowels = [s for s in fruits if sum(1 for char in s if char in vowels) > 2]
print(fruits_with_more_than_two_vowels)


## Exercise 4 - make a variable named fruits_with_only_two_vowels.
# The result should be ['mango', 'kiwi', 'strawberry']
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_only_two_vowels=[]
vowels =["a","e","i","o","u"]
for s in fruits:
    count =0
    for char in s:
        if char in vowels:
            count+=1
    if(count==2):
        fruits_with_only_two_vowels.append(s)
print(fruits_with_only_two_vowels)

# dictionary_comphrehension
cities ={"boston":20,"newyork":60,"LA":45,"heidelberg":70}
d={k:v for k,v in cities.items()}
print(d)
d1={k:v for k,v in cities.items() if v>50}
print(d1)

d2={k: ("cold" if v>50 else "warm") for k,v in cities.items()}
print(d2)

#--------------
def sumofvalue(value):
    return value+value

d3={k:(sumofvalue(v)) for k,v in cities.items()}
print(d3)

 