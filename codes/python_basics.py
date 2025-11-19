s="mumbai"
print(s[0])
print(s[0])
print(s[-1])
print(s[1:4])
print(s[::-1])
print(s[1:4])
x=[1,2,3,"java",True,10]
for i in x:
    print(i)
for i in s:
    print(i)
    
x=2
x=x+2
print(x)

# user_input = int(input("enter a number: "))
# x=10
# x=user_input+x
# print(f"the user input was {user_input} and output = {x}")

#------------------------------------------------------lists (mutable, ordered, duplicates, can contain data of any data_types)--------------------------------------------------------
fruits = ["apple","banana","cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[0:])
fruits.append("banana")
fruits.insert(1,"mango")
fruits.extend(["test"])
fruits.append([1,2,"watermelon"])
print(fruits[-1])
fruits.extend([10])
print(fruits)
fruits.pop(2) # remove any element on 2nd index position
print(fruits)
fruits.remove("test")
print(fruits)

fruits[0]="aaples"
print(fruits)

for fruit in fruits:
    print(fruit)
for index,value in enumerate(fruits):
    print(index,value)
for index,value in enumerate(fruits[::-1]):
    print(index,value)
    
    
#----------------------------------------tuple (immutable, orederd,contain dupliactes, can contain data of any data_types)-----------------------------------

t = (1,2,True,"python",4,2,10)
print(t)
print(t.count(2))
print(t[2])
print(t[1:])
print(type(t))
t = (1,2,4,2,10)
print(sum(t))
print(t.index(4))
print("-----------------------")
for i in range(1,10):
    print(i)
    
#----------------------Set (mutable, unordered, no duplicates, can contain data of any data_types) --------------------------------------------------------

s={1,2,2,3,3,4}
print(s)
s.add(10)
print(s)
s.add(20)
print(s)
s.remove(3)
print(s)
# You cannot access via index (No s[0])
# This gives error:
#s[0]
print(s)
# Because sets are unordered.
s.update([50,60])
print(s)
s.pop()
print(s)
s.discard(22)
print(s)

s.remove(2)   # removes 2 → error if not found
s.discard(7)  # no error even if 7 not in set
s.pop()       # removes a random item

print("----------------------------------")
a = {1, 2, 3}
b = {3, 4, 5}

print(a|b) #union
print(a&b) #intersection (only common)
print(a-b) #differnce
print(b-a) #difference
print(a^b)   #symmetric difference
print(b^a)
for i in s:
    print(i)

#---------------Dictionaries(key:value) Ordered, Mutable, keys : Unique, Values: duplicates (and of any data type)-------------------------

person = {"name":"alistair","age":26,"gender":"male","hobbies":["football","cricket","badminton"]}
print(person)
print(person["name"])
person['name']="ali bhai"
print(person)
person['language']="english"
print(person)
person['projects']=["llm","DE","Power bi"]
print(person)
print(person['projects'][1])
person['name']="alistair"
print(person)
print(person.get('name'))
print(person.get("age"))
print(person.get("salary"))
print(person)
print(person.get("salary",400000))
print(person.setdefault("name"))
print(person.setdefault("salary"))
print(person)
print(person.setdefault("wages","89000"))
print(person)
person['salary']=50000
print(person)
print("--------------------------")
print(person["name"])
person['name']="amroy"
person['hobbies']=["reading","listening music"]
print(person)
print(person.get('name'))
print(person.get("country"))
print(person.get("region","alaska"))
print(person.setdefault("name"))
print(person.setdefault("networth",90000000))
print(person.setdefault("name","alistair"))
print(person)

#Reverse a number
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)

#swap numbers
num1 = int(input("enter a num1: "))
num2 = int(input("enter a num2: "))
print(f"num1 = {num1} , num2 = {num2}")

if num1>10:
    if num2 > 20:
        num1 = num1+num2
        num2 = num1-num2
        num1 = num1-num2
        print("after swapping")
        print(f"num1: {num1} , num2: {num2}")
    else:
        print("num2 should be greater than 20")
else:
    if num1 <= 10 and num2 <= 20:
        print("both conditions not met")
    else:
        print("num1 should be greater than 10")
        
        
#Check if number is positive, negative, or zero

number = int(input("enter a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# # Check if a number is divisible by 5 and 11

number = int(input("enter a number and check if its divisble by 5 and 11: "))
if number%5 ==0 and number%11==0:
    print("divisible by 5 and 11")
else:
    print("not divisible")
    
    
""" Give discount based on purchase amount

If amount > 5000
→ If customer is “premium”, discount = 20%
→ Else discount = 10%

Else
→ No discount"""


purchase_amount=int(input("enter purchase amount: "))
customer= input("enter customer type 'premium/normal': ")

if purchase_amount >= 5000:
    if customer == "premium":
        discount=0.20
    else:
        discount=0.10
else:
    if purchase_amount < 5000 and customer == "premium":
        discount = 0.05
    elif purchase_amount < 5000 and customer != "premium":
        discount =0

final_price = purchase_amount - (purchase_amount * discount)
print(f"Discount: {discount * 100}%")
print(f"final_price: {final_price}")


""" Electricity Bill Calculator

Input: units

If units ≤ 100 → ₹5 per unit

If 101–200 → ₹7 per unit
If  200 → then First 200 units → 7
Remaining → 10

Use nested-if for the >200 case."""
# units = int(input("enter units: "))

# if units <= 100:
#     price = units * 5
# elif units > 100 and units <= 200:
#     price = units * 7
# else:
#     if units > 200:
#         if units > 200 and units <=400:
#             price = units * 7
#         else:
#             price = units *10
# print(f"units : {units} , price : {price} ")


units = int(input("enter units: "))

if units <= 100:
    price = units * 5
elif units > 100 and units <= 200:
    price = units * 7
else:
    # first_100 = 100 * 5
    first_200 = 200 * 7
    remaining = (units - 200) * 10
    price = first_200 + remaining
    
    
print(f"units : {units} , price : {price} ")

"""Nested if: Shop Discount System

Inputs: amount, membership (yes/no)
Logic:

If amount > 8000:

If membership == yes → 30%

Else → 20%

Else if amount > 5000:

membership yes → 15%

membership no → 10%

Else → 0%"""

amount = int(input("enter a amt: "))
membership = input("Are you a member : yes/no ")

if amount > 8000:
    if membership == "yes":
        discount = 0.30
    else:
        discount = 0.20
elif amount > 5000:
    if membership == "yes":
        discount = 0.15
    else:
        discount = 0.10
else:
    discount = 0
final_price = amount - (amount * discount)
print(f"Discount: {discount * 100}%")
print(f"final_price: {final_price}")

    
