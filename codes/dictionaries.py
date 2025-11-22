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