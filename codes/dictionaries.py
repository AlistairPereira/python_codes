student = {
    "name": "Alistair",
    "age": 24,
    "course": "Data Science"
}
student['age'] =25
student['city']= "Heidelberg"
del student['course']
print(student.setdefault("salary"))
print(student.setdefault("hobbies","football"))
print(student.setdefault("courses",["it","german","Python"]))
print(student)


# (frequency counter)
nums = [1,2,2,3,3,3,4,4,4,4]

freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

# (character count)
word = "banana"
freq={}
for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)


# (merge dictionaries)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result={}
for key,values in d1.items():
    result[key]=values
print(result)
for key,values in d2.items():
    if key in result:
        result[key] += values
    else:
        result[key] = values
print(result)


#spli, join, strip

text = "I love python"
res = text.split()
print(res)

data = "apple,banana,mango"
print(data.split(","))
print(data.split("-"))

words = ['I', 'love', 'python']
s = " ".join(words)
print(s)
s="-".join(words)
print(s)
s="&".join(words)
print(s)

name = "   Alistair   "
print(name.strip())
name = "###Alistair###"
print(name.strip("#"))
print(name.lstrip("#"))



squares = {x: x*x for x in range(1,6)}
print(squares)

# Using items() — Copy a dictionary
d = {"a":1, "b":2, "c":3}
copy_d = {k:v for k,v in d.items()}
print(copy_d)

#Convert all values to uppercase
fruits = {"a": "apple", "b": "banana", "c": "cherry"}
x ={k:v.upper() for k,v in fruits.items() }
print(x)

# Keep only items where value > 2
nums = {"a":1, "b":5, "c":2, "d":7}
x= {k:v for k,v in nums.items() if v > 2}
print(x)

#Swapping Keys and Values (VERY useful)
d = {"a":1, "b":2, "c":3}
res ={v:k for k,v in d.items()}
print(res)

# Frequency Count Using Dict Comprehension + set()
# We can compress it using comprehension:

sentence = "this is a test this is only a test"
words = sentence.split()
# print(words)
d={}
for w in words:
    if w in d:
        d[w] +=1
    else:
        d[w] =1
print(d)
    
    
res = {x: ("even" if x % 2 == 0 else "odd") for x in range(1,11)}
print(res)

res = {x: ("even" if x%2==0 else "odd") for x in range(1,11)}
print(res)

sentence = "this is a test this is only a test"
words = sentence.split()
freq = {w: words.count(w) for w in set(words)}
print(freq)