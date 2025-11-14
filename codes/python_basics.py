s="mumbai"
print(s[0])
print(s[-1])
print(s[1:4])
print(s[::-1])
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