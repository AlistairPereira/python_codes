class Account:
    
    count =0 # if we define any variable outside the other class methods then it is called class variable.
                #everytime we create a object the account value shud increment.
                
    #class method: if u want to work with all your object variables then we can define a class method
    #here we use class method to increase the value of count
    
    @classmethod
    def incr_count(cls): #here first argument is "cls"
        cls.count += 1
        
    @classmethod #to get the current value of count
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def print_Val():
        print("static method in Account class")
        
    #here first parameter is "self" for instance/object method
    def __init__(self, cust_id, name, initial_bal=0):
        self.__id = cust_id
        self.__name = name
        self.__balance = initial_bal
         # self.__id = cust_id
        # self.__name = name
        # self.__balance = initial_bal
        
        #how to access the class variable
        # Account.count += 1 #without classmethod
        Account.incr_count() #with classmethod
        
    def get_balance(self):
        return self.__balance
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return 'insufficient amount'
        else:
            self.__balance = self.__balance - amount
            return f"amount withdrawn : {amount} , balance: {self.__balance}"
        
class Savings_Account(Account):
    def __init__(self,id,name,initial_bal=0):
        #if we want to call existing method(variables) from parent class use super.
        super().__init__(id,name,initial_bal)
        self.limit = 50000 #create one more variable
        
        #for withdrawal check the limit shud be 50000 perday
#so if we want to add a new functionality in child class, we can ovverride the method of parent class
        
    def withdraw(self,amount):  #method overriding
        if amount < self.limit:
            new_bal= super().withdraw(amount) #here we call the same withdraw method of parent class (so use super())
            self.limit = self.limit - amount
            return new_bal
        else:
            print("daily limit reached")

#object/instance of class,  of class Account
customer1 = Account("101","abc")
# Account(customer1,"101","abc") # 
# print(customer1)

customer2 = Account("102","xyz")
# print(customer2)
print(customer2.get_balance())
customer3 = Account("103","pqr")
# print(customer3)
customer4 = Account("104","ali")
#in the background when we create a object python gives a call to function called  __init__
# print(customer1.id, customer1.name, customer1.balance)
print(customer1.get_balance())
print(customer1.deposit(50000))
print(customer1.get_balance())
print(customer1.withdraw(20000))
print(customer1.withdraw(50000))



print(customer2.deposit(8000))
print(customer3.deposit(10000))
print(customer4.deposit(70000))

print(Account.count)
print(customer1.count)
print(customer2.count)
print("---------------")
# Account.count += 5
print(Account.count)
print(customer1.count)
print(customer2.count)
print("------------------------")
customer1.count =100
print(customer1.count)
print(customer2.count)
#if we modify the value of class variable , using class name it will update values accrooss all objects
#but if modify the value of class variable , using object, then it will update the value only for that object 

print(Account.get_count())

# Account.get_balance(customer1)
# No. customer1.get_balance() does NOT call __init__ again.
# __init__ runs only when the object is created.

#now we want to check for all customers whos balance is less tahn 10000
# l =[customer1,customer2,customer3,customer4]

# for obj in l:
#     if obj.balance < 10000:
#         print(obj.id, obj.name)
        
        #okay here are using the varaibles that are defined in class ,  outside the class
        #if we want to restrct it then we need to make the vraiables private  by using "__"
        # self.__id = cust_id
        # self.__name = name
        # self.__balance = initial_bal
        
        # so now once everythings private how dow e still get balance use getter and setter method
        
l =[customer1,customer2,customer3,customer4]

for obj in l:
    if obj.get_balance() < 10000:
        print(obj.get_id(), obj.get_name())
        
print(customer1._Account__id) #to access private varibale outside class
print(customer1._Account__name)
print(customer1.__dict__)
print(Account.get_count())
print(Account.print_Val())

# everytime we create a object , it will give call to __init__ method
# how will python identify for which object i am passing this values(101, "abc")
# so in the background it passess something like this
# Account(customer1,"101","abc")
#looks like we pass2 vlaues 101 and "anc" but we pass 3 , so first value is instance of class and we write an extra agruemnet (Self) def __init__(self)
# self = object instance

#everytime we create objects, we need variables (instance variabkes)


#for (objects) we have instance method (def __init__) and instance variables  (self = object instance)
#for class variables we have classmethod  (cls = class instance)
#statiscmethod -> independent (not accessing class and instance variables)

#Inheritance: in oops we use it to reuse the existing code
#Accounts Class , i want to further bifurcate into savings accoungs and current accounts
# so i want to reuse some code of Accounts class (withdraw , deposit methodt etc..), plus i want to add some new functinality.
# class Savings_Account(Account) : in parenthesis enter class from which u want to inherit

cust1 = Savings_Account(101, "ABC") # so here it will give call to def_init__of savings account then it will go to super().
# and call existing methods from parnet class and also add extra variaboe lmit
print(cust1)
print(cust1.__dict__)
# help(cust1)

print(cust1.deposit(80000)) #first it will check if deposit is there in child class, if not then it will serach in parent, if its there then it will execute
print(cust1.withdraw(40000))
print(cust1.withdraw(9999))

# Method resolution order:
#  |      Savings_Account
#  |      Account
#  |      builtins.object

#it will first search for method in saving_accounts , if not there then it will serach in parent class(Account),
# if not then it will serach in builtins, if not thn it will throw an error

# (suppose we want to set a minium withdraw shud be not more thn 50000 daily)
#say if we want to add a new feature or variable in child class then use def_init__

