#create a function that takes a list and finds the integer which appears an odd number of times.

def unique(*l):
    d={}
    for values in l:
        if values in d:
            d[values]+=1
        else:
            d[values]=1
            
    for k,v in d.items():
        if v%2!=0:
            return k
    return None

res = unique(1,1,2,3,4,5,5,6,6,4)
print(res)

#write a function that takes a list of numbers and returns a list with 2 elemnts
#1. first elemet :- sum of all even numbers
#2. second element:- sum of all odd numbers
def even_odd(*l):
    sum_even =0
    sum_odd=0
    l=[1,2,3,4,5]
    for values in l:
        if values%2==0:
            sum_even = sum_even +values
        else:
            sum_odd = sum_odd + values
    return f"sum_even : {sum_even} , sum_odd : {sum_odd}"

res = even_odd(1,2,3,4,5)
print(res)

#create  the function that takes a list of dictionaries and returns the sum of people budget

# get_budgets = [
#             {"name":"rahul","age":24,"budget":23000},
#             {"name":"sahil","age":27,"budget":40000},
#             {"name":"steve","age":16,"budget":2700}
#                ]

#print(get_budgets[0]['budget'])

def budget(get_budgets):
    sum=0
    for values in get_budgets:
        sum = sum+values['budget']
    return sum
res = budget([
            {"name":"rahul","age":24,"budget":23000},
            {"name":"sahil","age":27,"budget":40000},
            {"name":"steve","age":16,"budget":2700}
               ])
print(res)
        
        
#In each input list , every number repeats at least once , except for two.
#Write a function that returns the two unique numbers
#eg [1,9,8,8,7,6,1,6] :- [9,7]

def unique(l):
    d={}
    for values in l:
        if values not in d:
            d[values]=1
        else:
            d[values]+=1
            
    l=[]
    for k,v in d.items():
        if v==1:
            l.append(k)
    return l
res = unique([1,9,8,8,7,6,1,6])
print(res)
    
