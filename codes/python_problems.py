#Swap a number (num > 10 and num2 >20)
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))

# if num1 > 10:
#     if num2 > 20:
#         num1 = num1 + num2
#         num2 = num1 - num2
#         num1 = num1 - num2
#         print("after swaping")
#         print("num1",num1)
#         print("num2",num2)
#     else:
#         print("num2 should be greate than 20")
# else:
#     if num1 <=10 and num2<=20:
#         print("both conditions not met")
#     else:
#         print("num1 should be greater than 10")



# #Write a program that checks if a number is odd or even.
# num = 2
# if num%2==0:
#     print("even")
# else:
#     print("odd")
    
# #Write a program to compute the factorial of a number using a loop.
# number= int(input("enter a number: "))
# result=1
# for i in range(1,number+1):
#     result=i*result
# print("factorial of ", number, "is : ", result) 

#Prime number

number = 23
result = "Number is prime"
if number > 1: 
    for i in range(2,number):
        if number%i == 0:
            result = "Number is not prime"
            break        
else:
    print("invalid input")
    
print(result)

number = 23
if number > 1: 
    for i in range(2,number):
        if number%i == 0:
            print(number, "is not prime")
            break 
    else:
        print(number ,"is prime")       
else:
    print("invalid input")         
        
# Check if a given string is a palindrome (reads the same forwards and backwards).
def palindrome(s):
    s=s.replace(" ","")
    if s == s[::-1]:
        print(s,"is palindrome")
    else:
        print(s,"not a palindrome")
        
palindrome("nitin ")

#random number

import random
def guess_number():
    for i in range(1,4):
        number = int(input("enter a number between 1 - 10: "))
        random_number = random.randint(1,10)
        
        if random_number == number:
            print("congrats! correct guess")
            break
        else:
            if i==1:
                print("wrong guess, more 2 chnaces left")
            elif i==2:
                print("wrong guess, more 1 chance left")
            else:
                print("wrong guess, all 3 chnaces over")

guess_number()

#Write a Python program that generates and prints the multiplication table for a given number.
# count = 1

# while count <= 5:
#     print(count)
#     count += 1
r = int(input("enter a range: "))
table= int(input("enter the table number : "))
for i in range(1,r+1):
    print(table,"*",i,"=",table * i)
    
#Problem: Write a Python program that removes duplicate elements from a list.

l=[1,2,3,4,4,4,5,5,6,7]
l= list(set(l))
print(l)

l=["a","b","c","d"]
for i in l:
    if i=="b":
        print(l.index(i))








    

