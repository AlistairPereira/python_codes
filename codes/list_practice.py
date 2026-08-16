print('hello world')

x= 10
y=20
print('Sum:', x+y)


# age = int(input('enter age: '))
# name = input('enter name: ')
# print('my name is', name , 'and age is' , age)

# if age > 18:
#     print('adult')
# elif age >= 15 and age < 18:
#     print('teen')
# else:
#     print('minor')
    
# num1=int(input('enter num1: '))
# num2 = int(input('enter num2: '))
# print('before swap')
# print('num1: ',num1, 'num2: ',num2)
# if num1>5:
#     if num2>10:
#         num1 = num1+num2
#         num2 = num1 -num2
#         num1 = num1- num2
#         print('after swap')
#         print('num1: ',num1, 'num2: ',num2)
#         print('both conditions met')
#     else:
#         print('num2 shud be greater than 10')
# else:
#     if num1 <=5 and num2 <= 10:
#         print('both condition not met')
#     else:
#         print('num1 shud be greater than 5')
        
#largest of 3 nos

# num1=int(input('enter num1: '))
# num2 = int(input('enter num2: '))
# num3 = int(input('enter num3: '))

# if num1 >num2 and num1 > num3:
#     print('num1 is greater')
# elif num2 > num1 and num2 > num3:
#     print('num2 is greater')
# else:
#     print('num3 is greater')

n =[10,20,30,40]
n.append(50)
n.append([60,70])
n.extend([80,90])
n.append('java')
n.append(['python','c++'])
n.extend(['perl'])
n.insert(1,200)
n.remove('perl')
n.pop(1)
n.pop()
print(n.count(80))
print(n.index(20))
print(n)

l =[1,4,5,3,8,6]
l.sort()
print(l)
l.reverse()
print(len(l))
print(l)

numbers =[10,20,30,40]

sum=0
for num in numbers:
    sum = sum + num
    print(sum)

numbers = [10, 50, 30, 20]
print(max(numbers))
  
  
numbers = [10, 25, 30, 5, 40]

count =0
for num in numbers:
    if num > 20:
        count = count+1
print(count)
        
    
filter_list =[]
for num in numbers:
    if num > 20:
        filter_list.append(num)
print(filter_list)

# Suppose sales data:
# sales = [100, 200, 150, 300, 250]
# 🎯 Task:
# Total sales
# Average sales
# Count sales > 200

sales = [100, 200, 150, 300, 250]

total =0
count=0
for num in sales:
    total = total + num
    
    if num > 200:
        count += 1
avg_sales = total/ len(sales)

print(total)
print(avg_sales)
print(count)

numbers = [10, 20, 30, 40,50,60,70,80]
print(numbers[0])
print(numbers[1])

print(numbers[1:])
print(numbers[-1])
print(numbers[::-1])
print(numbers[::2])
print(numbers[1::3])
print(numbers[:5])

fruits = ["apple","banana","cherry"]

for index,value in enumerate(fruits):
    print(index,value)

# Check if number is positive, negative, or zero

number = int(input("enter a number: "))

if number >0:
    print(f"positive number: {number}")
elif number < 0 :
    print(f"negative number: {number}")
else:
    print("zero")


#Count how many numbers are even and odd

l=[1,2,3,4,5]
even_count=0
odd_count=0
for values in l:
    if values%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)

squares = [i*i for i in range(1,11)]
print(squares)

#even nos
nums = [1,2,3,4,5,6,7,8]
even_nos =[num for num in nums if num%2==0]
print(even_nos)

add_1 = [num+1 for num in nums]
print(add_1)

#Create a list of squares ONLY for odd numbers from 1 to 10
odd_list = [i*i for i in range(1,11) if i%2!=0]
print(odd_list)

l=[]
for i in range(1,11):
    if i%2!=0:
        l.append(i*i)
print(l)

even_odd =[("even",i)if i%2==0 else ("odd",i) for i in range(20,30)]
print(even_odd)



words = ["hi", "python", "apple", "ok"]
len_4 = [w for w in words if len(w) > 4]
print(len_4)

#replace 0 with negatives
nums = [-5, 3, -1, 10, -7]
neg = [num if num >0 else 0 for num in nums]
print(neg)

items = ["apple", 50, "banana", 20, 100, "Mango"]
nos= [i for i in items if type(i) == int]
print(nos)

#extract only words starting from a
words = ["apple", "ball", "ant", "dog", "air"]
start_a = [w for w in words if w[0]=="a"]
print(start_a)

a_words = [w for w in words if w.startswith("a")]
print(a_words)

s={1,1,2,4,5,6,8,2}
print(s)
s.add(20)
s.add(80)
s.remove(2)
# s.add(["java", 1])
s.add(("java",1))
s.add
print(s)

# Set only allows immutable (hashable) values

# Type	Allowed in Set?
# int	✅
# string	✅
# tuple	✅
# list	❌
# dict	❌
# List is mutable, so not allowed

# s.add({"name":ali})
#tuple() → makes it immutable
d = {"a": 1, "b": 2}
s.add(tuple(d.items()))

print(s)

        

