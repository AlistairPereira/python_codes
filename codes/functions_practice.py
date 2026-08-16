# Even or Odd
# Write a function is_even(n) that
# Returns True if n is even
# Returns False if n is odd
# Then use it in a loop from 1 to 10 and print:

def is_even(n):
    
    if n%2 == 0:
        return True
    else:
        return False

for i in range(1,11):
    if is_even(i):
        print(i,"even")
    else:
        print(i,"odd")
        
        
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
for i in range(1,11):
    if is_even(i):
        print(i,"even")
    else:
        print(i,"ODD")
        
nums = [10, 20, 30, 40, 50]
sum=0
for num in nums:
    sum = sum+num
print(sum)

# length = len(nums)
avg = sum/len(nums)
print(avg)

# def atm(balance):
#     count =0
    
#     while True:
#         amount = int(input("Enter withdrawal amount: "))
#         count +=1
        
#         if amount < balance:
#             balance =  balance - amount
#             print(f"Total withdrawls : {count} , Remaining amount : {balance}")
#         elif amount > balance:
#             return "insufficient funds"
        
        
#         choice = input("Do you want another withdrawal? (yes/no): ")
        
#         if choice == "no":
#             break
        
#     return f"Total withdrawls : {count} , Remaining amount : {balance}"

# res = atm(10000)
# print(res)
    
for i in range(3):
    for j in range(3):
        print(i,j)
        
for i in range(4):
    for j in range(4):
        print(j, end =" ")
    print() #Okay, this row is finished. Move to the next line
    
# Keep stars on the same line
# Use end=" ":

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(1,5):
    # print(i)
    for j in range(5-i):
        print("*", end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end =" ")
    print()
    
    
    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,j)



# Keep asking the user to enter expenses.
# Stop when the user enters 0.
# Calculate:
# Total expenses
# Number of expenses
# Average expense
# Highest expense
# Lowest expense
# Count how many expenses are above average

def expense_tracker():
    
    expenses =[]
    
    while True:
        expense = int(input("enter your expense: "))
        
        if expense == 0:
            break
        
        expenses.append(expense)
        
    total =0
    for expense in expenses: 
        total = total+ expense
    count=len(expenses)
    avg = total/count
        
    max_exp = max(expenses)
    min_exp = min(expenses)
                
    above_avg_count =0
       
    for expense in expenses:
        if expense > avg:
            above_avg_count+=1
            
    return {"total expenses": total, "no of expenses": count, "avg expense": avg, "Highest expense": max_exp,
            "Lowest expense": min_exp, "Above avg expense count": above_avg_count}

res = expense_tracker()
print(res)

print("----------------------------------------------------------")
        
def transaction_analyzer(transactions):
    
    total_credit = 0
    total_debit = 0
    count_debit = 0
    largest = 0
    for transaction in transactions:
        if transaction['type'] == "credit":
            total_credit = total_credit + transaction['amount']
            
        elif transaction['type'] == "debit":
            total_debit = total_debit + transaction['amount']
            count_debit += 1
            
        amount = transaction['amount']
        if largest < amount:
            largest = amount
            
    balance = total_credit - total_debit
    
    # for transaction in transactions['amount']:
    #     if largest > transaction:
    #         largest = largest
    #     else:
    #         largest = transaction
        
            
    return {'total_credit':total_credit, "total_debit":total_debit,"balance" : balance, "largest_transcation": largest, "count_debit":count_debit  }            
    
    
res = transaction_analyzer([
    {"type": "credit", "amount": 5000},
    {"type": "debit", "amount": 1200},
    {"type": "credit", "amount": 3000},
    {"type": "debit", "amount": 700},
    {"type": "debit", "amount": 2000}
])
print(res)

def order_analyzer(orders):
    
    total = 0
    highest = 0
    customer_spending = {}
    for order in orders:
        price = order['price']
        customer = order['customer']
        
        total = total + price
        
        if highest < price:
            highest = price
        
        if customer in customer_spending:
            customer_spending[customer] += price
        else:
            customer_spending[customer] = price
            
        
    return {"total_sales" : total, 'highest_order': highest,  "customer_spending": customer_spending}
    
res = order_analyzer([
    {"customer":"Ali","product":"Laptop","price":800},
    {"customer":"John","product":"Mouse","price":50},
    {"customer":"Ali","product":"Keyboard","price":100},
    {"customer":"Sara","product":"Monitor","price":300},
    {"customer":"John","product":"USB Cable","price":20}
])
print(res)
    
def employee_analyzer(employees):
    
    total = 0
    highest = 0
    department_salary={}
    highest_employee = ""
    
    for employee in employees:
        salary = employee['salary']
        department = employee['department']
        
        total = total+ salary

        if salary > highest:
            highest = salary
            highest_employee = employee['name']
        
        if department in department_salary:
            department_salary[department] += salary
        else:
            department_salary[department] = salary
            
    avg_salary = total/len(employees)
        
    return {"total_salary": total, "highest salary": highest, "average salary": avg_salary, "department_salary":department_salary,
            "highest_paid_employee": highest_employee }
    
res = employee_analyzer([
    {"name":"Ali", "department":"IT", "salary":60000},
    {"name":"John", "department":"HR", "salary":45000},
    {"name":"Sara", "department":"IT", "salary":70000},
    {"name":"Mike", "department":"Finance", "salary":55000},
    {"name":"Emma", "department":"HR", "salary":50000}
])
print(res)


def password_checker(password):
    
    length = len(password)
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    special = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase= True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            special = True
            
    score = 0
    
    if length >= 8:
        score +=1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score+=1
    if has_digit:
        score += 1
    if special :
        score +=1
        
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {"length": length,
            " has_uppercase": has_uppercase,
            "has_lowercase": has_lowercase,
            "has_digit": has_digit,
            "special": special,
            "strength": strength,
            "score":score}
    
res = password_checker("Ali@1234")
print(res)


def sentence_analyzer(sentence):
    
    s= sentence.split()
    total_words = len(s)
    
    unique_words = set(s)
    unique_words = len(unique_words)
    
    word_freq={}
    
    for char in s:
        if char in word_freq:
            word_freq[char] += 1
        else:
            word_freq[char] = 1
            
    max_count=0
    k= ''
    for k,v in word_freq.items():
        if v > max_count:
            max_count = v
            common_word = k
            
    
    return {"total_words":total_words, "unique_words": unique_words, "most common word": common_word, "word frequency": word_freq }

res = sentence_analyzer("Python is easy and Python is powerful")
print(res)

# s = "Python is easy and Python is is powerful"
# s= s.split()
# d={}
# for char in s:
#     print(char)
#     if char in d:
#         d[char]+=1
#     else:
#         d[char]=1
# print(d)

# max_count=0
# k= ''
# for k,v in d.items():
#     if v > max_count:
#         max_count = v
#         print(k, ":",max_count)
        
    


# word_freq={}
# for char in s:
#     if char in word_freq:
#         word_freq[char] +=1
#     else:
#         word_freq = 1


def cart_analyzer(cart):
    
    total = 0
    total_quantity =0
    highest =0
    exp_item =''
    
    total_elec =0
    total_furn= 0
    
    for values in cart:
        total = total + values['price']
        total_quantity = total_quantity + values['quantity']
        
        price = values['price']
        
        if highest < price:
            highest = price
            exp_item = values['item']
        
    for values in cart:
        if values['category'] == "Electronics":
            total_elec = total_elec + values['price']
        if values['category'] == "Furniture":
            total_furn = total_furn + values['price']
          
    d={}
    for values in cart:
        # print(values['item'])
        if values['item'] in d:
            d[values['item']]+=1
        else:
            d[values['item']] =1

    more_than_1 =[]
    for k,v in d.items():
        if v > 1:
            more_than_1.append(k)
    
    return {
        "total_costs": total, "total_quantity": total_quantity, "most expensive item": exp_item,
            "category_summary": [total_elec, total_furn],
            "items_bought_more_than_one": more_than_1
            }
        

res = cart_analyzer(cart = [
    {"item": "Laptop", "category": "Electronics", "price": 800, "quantity": 1},
    {"item": "Mouse", "category": "Electronics", "price": 20, "quantity": 3},
    {"item": "Chair", "category": "Furniture", "price": 150, "quantity": 2},
    {"item": "Mouse", "category": "Electronics", "price": 50, "quantity": 1}
])

print(res)

l=[
    {"item": "Laptop", "category": "Electronics", "price": 800, "quantity": 1},
    {"item": "Mouse", "category": "Electronics", "price": 20, "quantity": 3},
    {"item": "Chair", "category": "Furniture", "price": 150, "quantity": 2},
    {"item": "Mouse", "category": "Electronics", "price": 50, "quantity": 1}
]
d={}
for values in l:
    # print(values['item'])
    if values['item'] in d:
        d[values['item']]+=1
    else:
        d[values['item']] =1
print(d)

more_than_1 =[]
for k,v in d.items():
    if v > 1:
        more_than_1.append(k)
print(more_than_1)


def movie_analyzer(movies):
    
    total_movies = len(movies)
    total_rating =0
    highest = 0
    highest_rate_movie =''
    
    for movie in movies:
        total_rating = total_rating + movie['rating']
        
        rating = movie['rating']
        if highest < rating:
            highest = rating
            highest_rate_movie = movie['title']
            
    
    scifi_total =0
    scifi_count=0
    romance_total =0
    romance_count=0
    for movie in movies:
        if movie['genre'] == "Sci-Fi":
            scifi_total = scifi_total + movie['rating']
            scifi_count += 1
        elif movie['genre'] == "Romance":
            romance_total = romance_total + movie['rating']
            romance_count +=1
        
    
    avg_scifi = scifi_total/scifi_count
    avg_romance = romance_total/romance_count
    
    popular_movies=[]
    for movie in movies:
        if movie['votes']> 2000:
            popular_movies.append(movie['title'])    
        
    avg_rating = total_rating/total_movies
        

    return {"total_movies": total_movies, 
            "total_rating": total_rating, 
            "avg_rating": avg_rating,
            "highest_rated_movie": highest_rate_movie,
            "genre_average_rating": {"Scifi": avg_scifi,"Romance":avg_romance},
            "popular movies":popular_movies }
res = movie_analyzer([
    {"title":"Inception", "genre":"Sci-Fi", "rating":8.8, "votes":2000},
    {"title":"Interstellar", "genre":"Sci-Fi", "rating":8.6, "votes":2500},
    {"title":"Titanic", "genre":"Romance", "rating":7.9, "votes":1800},
    {"title":"The Notebook", "genre":"Romance", "rating":7.8, "votes":1200},
    {"title":"Avatar", "genre":"Sci-Fi", "rating":7.6, "votes":3000}
])
print(res)

#find dupilcates numbers [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]

def find_duplicates(numbers):
    
    d={}
    for num in numbers:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    # return d
    
    dup =[]
    for k,v in d.items():
        if v > 1:
            dup.append(k)
    return dup

res = find_duplicates([1, 2, 3, 2, 4, 5, 1, 6, 7, 3])
print(res)

#Fid the 2nd Largest number
def second_largest(numbers):
    largest = numbers[0]
    second_largest = float('-inf') #(a number smaller than every possible number)
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
            
        elif num > second_largest and num != largest:
            second_largest = num
            
    return [second_largest, largest]

res = second_largest( [10, 5, 8, 20, 15])
print(res)

#Question: find the first unique character 
# if aabbcdde , output = c 
def first_unique_char(s):
    
    d={}
    for char in s:
        if char in d:
            d[char] +=1
        else:
            d[char]=1
    # return d
    
    result=[]
    for k,v in d.items():
        if v ==1:
            result.append(k)
    return result[0]

res = first_unique_char("gaabbcddeg")
print(res)

#Question: Check if Two Strings are Anagrams

def is_anagram(s1,s2):
    
    d1={}
    for char in s1:
        if char in d1:
            d1[char]+=1
        else:
            d1[char] =1
            
    d2={}
    for char in s2:
        if char in d2:
            d2[char]+=1
        else:
            d2[char] =1
    
    # return {"d1":d1, "d2": d2}
    
    if d1 == d2:
        return True
    else:
        return False

res = is_anagram("listen","silent") 
print(res)

# Question: Move All Zeros to End

def move_zeros(numbers):
    count_zero =0
    result=[]
    
    for num in numbers:
        if num ==0:
            count_zero+=1
        else:
            result.append(num)
            
    while count_zero > 0:
        result.append(0)
        count_zero = count_zero - 1
    return result
    
    # greater_zero=[]
    # zeros=[]
    # for num in numbers:
    #     if num > 0:
    #         greater_zero.append(num)
            
    #     if num == 0:
    #         zeros.append(num)   
    
    # return [greater_zero  , zeros]          
    

res = move_zeros([0,1,0,3,12])
print(res)

def remove_duplicates(numbers):
    result=[]
    for num in numbers:
        if num not in result:
            result.append(num)
    
    return result    

res = remove_duplicates([6,1,1,2,2,3,4,4,5])
print(res)

def find_missing(numbers):
    for i in range(len(numbers)-1):
        if numbers[i]+1 != numbers[i+1]:
            return numbers[i] +1
  
        

res = find_missing([1,2,3,5,6])
print(res)
