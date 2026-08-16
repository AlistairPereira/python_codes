s='mumbai'
print(s[0])
print(s[0:2])
print(s[-1])
print(s[::-1])

x=2
x=x+2
print(x)

fruits = ["apple","banana","cherry"]
print(fruits)
print(fruits[0])
print(fruits[1:])
print(fruits[::-1])
fruits.append("banana")
fruits.insert(1,"mango")
print(fruits)
fruits.extend(["grapes",8])
fruits.append(9)
fruits.append([10,11,12])
fruits.extend([1,2,3])
fruits.pop(-1)
print(fruits)
fruits.remove("grapes")
print(fruits)

fruits[0]="watermelon"
print(fruits)

for fruit in fruits:
    print(fruit)
    
for index,value in enumerate(fruits):
    print(index, value)
    
for index,value in enumerate(fruits[::-1]):
    print("index",index, "value",value)
fruits.append('watermelon')
print(fruits)
print(fruits.count('watermelon'))

print("tuple-------------------------------------------")

t = (1,2,True,"python",4,2,10)
print(t)
print(t.count(2))
print(t[2:5])
print(t[::-1])

print(t.index("python"))
t=(1,2,3,4)
print(sum(t))
for i in range(1,10):
    print(i*2)
    
print("set------------------------------------------------")
    
s={1,2,2,3,3,4}
print(s)
s.add(10)
s.add(20)
print(s)
s.remove(3)
print(s)
s.update([50,60])
s.pop()
s.discard(100)
s.remove(60)
print(s)

a = {1, 2, 3,7}
b = {3, 4, 5,6}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)
print(b^a)

print("Dict------------------------------------------------------------------")
person = {"name":"alistair","age":26,"gender":"male","hobbies":["football","cricket","badminton"]}
print(person)
print(person["name"])
person['name']='ali'
print(person)

person['projects']=['llm','ai','java']
print(person)
print(person['hobbies'][::-1])
print(person['hobbies'][1])

print(person.get('name'))
print(person.setdefault('name'))
print(person.get("region"))
print(person.get("region","alaska"))
print(person.setdefault("salary"))
print(person.setdefault("country",['india','germany']))
print(person)
del person['projects']
print(person)
print(person.setdefault("place","heidelberg"))
print(person)

#reverse a number
# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b
# print(a,b)


# num1 = int(input("enter a num1: "))
# num2 = int(input("enter a num2: "))

# print(num1)
# print(num2)

# if num1 > 10:
#     if num2 > 20:
#         num1 = num1+num2
#         num2 = num1-num2
#         num1 = num1 - num2
#         print("after swap")
#         print(num1)
#         print(num2)
#     else:
#         print("num2 shud be > than 20")
# else:
#     if num1 <= 10 and num2 <= 20:
#         print('both conditions not met')
#     else:
#         print("num1 shud be > than 10")
    
# num = int(input("enter a num: "))
# if num >0:
#     print("positive")
# elif num <0:
#     print("negative")
# else:
#     print("zero")
    
    
# """ Give discount based on purchase amount

# If amount > 5000
# → If customer is “premium”, discount = 20%
# → Else discount = 10%

# Else
# → No discount""

# amount = int(input("enter purchase amount: "))
# customer_type = input("enter customer type Premium/Normal: ")

# if amount > 5000:
#     if customer_type=='premium':
#         discount=0.20
#     else:
#         discount = 0.10
        
# else:
#     if amount < 5000 and customer_type =='premium':
#         discount =0.5
#     elif amount < 5000 and customer_type != 'premium':
#         discount =0
        
# final_price = amount - (amount * discount)
# print(f"Discount: {discount * 100}%")
# print(f"final_price: {final_price}")

# for value in range(10):
#     print(value)
    
l=[10,20,30,40,50,60]
key=40

for index, value in enumerate(l):
    if value == key:
        print("elemnet found at index",index)
        break
    else:
        # print("ciontinung")
        # continue
        pass
        print("passing")
    
else:
    print("element not found")
    
#sum of all the elements in a list

l=[1,2,3,4,5,6]

sum =0
for values in l:
    sum = sum+value
print(sum)

#Count how many numbers are even and odd

l=[1,2,3,4,5]

even_count=0
odd_count=0
for num in l:
    if num%2==0:
        even_count=even_count+1
    else:
        odd_count =odd_count+1
print(f"even_count {even_count}, odd_count {odd_count}")


sum=0
for i in range(1,11):
    sum= sum+i
    if i == 6:
        break
    else:
        continue
print("sum: " ,sum)

# Print all numbers from 1 to N, but skip multiples of 3

for i in range(1,22):
    if i%3 != 0:
        print(i)
        
"""A simple login system
You get 3 attempts to enter the correct password.
After 3 failures → print "Account locked!"""

# password ='12345'
# for i in range(0,3):
#     user_password = input("enter a password: ")
#     if user_password == password:
#         print("password entered correctly")
#         break
#     else:
#         print("wrong password")
#         if i == 0:
#             print('this is ur 2nd attempt')
#         if i == 1:
#             print(" this is ur last attempt")
#         continue
# else:
#     print("account blocked for 24 hrs")
    
# import random
# secret_number = random.randint(1,50)

# for i in range(1,4):
#     guess = int(input("Enter a number between 1 and 50: "))

#     if guess == secret_number:
#         print("correct guess")
#         break
#     elif guess < secret_number:
#         print("number is low")
#     else:
#         print("number is high")
        
#     if i==2:
#         print('next attempt is ur last')
        
# else:
#     print("game over ")
    
# secret_number = random.randint(1,50)
# while True:
#     guess = int(input("Enter a number between 1 and 50: "))

#     if guess == secret_number:
#         print("correct guess")
#         break
#     elif guess < secret_number:
#         print("number is low")
#     else:
#         print("number is high")
    

for i in range(1,11):
    print(i, ":", i*i)
    
squares=[i*i for i in range(1,11)]
print(squares)

l=[1,2,3,4,5]
even_nos=[]
for num in l:
    if num%2==0:
        even_nos.append(num)
print(even_nos)

#Create a list of squares ONLY for odd numbers from 1 to 10

odd_squares =[i*i for i in range(1,11) if i%2!=0]
print(odd_squares)

# From this list, extract only strings
items = [1, "apple", 3, "banana", True, "cat"]

x=[item for item in items if type(item)==str]
print(x)

#Make a list of squares from 1–10 but skip multiples of 3
x=[i*i for i in range(1,11) if i%3!=0]
print(x)

#extract only words starting from a
words = ["apple", "ball", "ant", "dog", "air"]
x=[word for word in words if word[0] == "a"]
print(x)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# # Hint: You'll need a way to check if something is a vowel.

fruits = ['mango', 'kiw', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
l=[]
vowels =["a","e","i","o","u"]
for fruit in fruits:
    count=0
    for char in fruit:
        if char in vowels:
            count = count+1
    if count >=2:
        l.append(fruit)
print(l)
    
    
cities ={"boston":20,"newyork":60,"LA":45,"heidelberg":70}
d={k:v*2 for k,v in cities.items()}
print(d)

d={k:v for k,v in cities.items() if v>50}
print(d)

d={k:("cold" if v>50 else "hot")  for k,v in cities.items()}
print(d)

#replace 0 with negatives
nums = [-5, 3, -1, 10, -7]
l=[0 if num<0 else num for num in nums ]
print(l)

sum=0
for i in range(1,11):
    sum = sum+i
    if i ==6:
        break
    else:
        continue
print(sum)

# Sum & Average of List
nums = [10, 20, 30, 40, 50]
sum =0
count=0
for num in nums:
    sum += num
    count += 1
print(sum)
print(count)

avg = sum/len(nums)
print(avg)

# #Largest & Smallest
nums = [5, 9, 1, 7, 3, 12]
largest = nums[0]
smallest= nums[0]

for num in nums:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print(f"largest : {largest} , smallest: {smallest}")


#Count Positives, Negatives, and Zeros
# nums = [0, -1, 5, -3, 8, 0, 2]

pos=0
neg=0
zeros=0
for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zeros += 1
print(
    {"pos":pos,
     "neg": neg,
     "zeros":zeros}
)
pos=0
neg=0
zer=0
for num in nums:
    if num > 0:
        pos+=1
    elif num <0:
        neg+=1
    else:
        zer+=1
        
print({
    "pos": pos,
    "neg": neg,
    "zeros": zer
})

# Removing duplicates
nums = [1,2,2,3,4,4,4,5,6,6]
l=[]
for num in nums:
    if num not in l:
        l.append(num)
print(l)

# (frequency counter)
nums = [1,2,2,3,3,3,4,4,4,4]

d={}
for num in nums:
    if num in d:
        d[num] += 1
    elif num not in d:
        d[num] =1 
print(d)

# (character count)
word = "banana"
d={}
for w in word:
    if w in d:
        d[w]+=1
    else:
        d[w] =1
print(d)

number = 7

if number > 1:
    for i in range(2,number):
        if number%i==0:
            print("not a prime no")
            break
    else:
        print("prime no")
        
#Guess Number with multiple guesses and count the no of guesses
# by printing 'u have taken 6 attempts to guess the number'
        
import random
secret_number = random.randint(1,50)

count = 0
while True:
    user_input = int(input("enter a number"))
    count = count+1
    
    if user_input == secret_number:
        print(f"{secret_number} is the number , u won!")
        print(f"u have taken {count} attempts to guess the number")
        break
        
    elif user_input < secret_number:
        print("number is low")
        
    else:
        print("number is high")
        
    if user_input > 50:
        print("u have entered a number > 50 , pls enter number < than 50")
        # break
        continue

l=[1,2,3,4,5,6,7,8]
l1=[]
for num in l:
    if num%2!=0:
        l1.append(num*num)
print(l1)


l=[1,1,3,4,5,1,3,4]
d={}
for num in l:
    if num in d:
        d[num] +=1
    else:
        d[num]=1
   
print(d)     


