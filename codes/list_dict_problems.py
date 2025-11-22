# Sum & Average of List
nums = [10, 20, 30, 40, 50]
sum=0
for num in nums:
    sum = sum+num
print(sum)

# length = len(nums)
avg = sum/len(nums)
print(avg)

total=0
count=0
for n in nums:
    total = total + n
    count = count + 1
avg = total/len(nums)
    
print("total:", total)
print("avg:", avg)
print("count: ",count)
    
#Largest & Smallest

nums = [5, 9, 1, 7, 3, 12]
largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("largest: ",largest)
print("smallest: ",smallest)

#Count Positives, Negatives, and Zeros
nums = [0, -1, 5, -3, 8, 0, 2]
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
unique=[]
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)



# Filtering even numbers
nums = [1,2,3,4,5,6]
even_nos=[]
odd_nos=[]
for num in nums:
    if num%2==0:
        even_nos.append(num)
    else:
        odd_nos.append(num)
print(even_nos)
print(odd_nos)


#  Find Second Largest Number (logic level-up)

nums = [10, 5, 20, 8, 15]
largest = nums[0]
second = float('-inf')

for num in nums:
    if num > largest:
        largest = num
        second = largest
    elif num != largest and num > second:
        second  = num
print(largest)
print(second)
        

# Word frequency in sentence
sentence = "this is a test this is only a test"
freq={}
words = sentence.split(" ")
print(words)
for w in words:
    if w in freq:
        freq[w]= freq[w]+1
    else:
        freq[w] = 1
        
print(freq)


#  Reverse a list without slicing
nums = [10, 20, 30, 40]
print(nums[::-1])

rev =[]
for num in nums:
    rev.insert(0,num)
print(rev)