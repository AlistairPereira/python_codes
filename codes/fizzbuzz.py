# Write a Python function fizz_buzz(n) that prints the numbers from 1 to n. 
# But for multiples of three print "Fizz" instead of the number and for the multiples
# of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

def fizzbuzz(n):
    for num in n:
        if num%3 == 0 and num%5==0:
            print("fizz_buzz")
        elif num%5 ==0:
            print("buzz")
        elif num%3==0:
            print("fizz")
        else:
            print(num)
fizzbuzz([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

#Write a Python function is_armstrong(n)
# that takes an integer n and returns True if it is an Armstrong number, and False otherwise.

num = 153
number = str(num)
power =len(number)   
sum=0
for values in number:
    res=int(values)**power
    sum=sum+res
if sum == num:
    print("is Armstrong")
else:
    print("not armstrong")
    

    







