# oops -> object oriented programming


# 1. Encapsulation

class BankAccount():
    def __init__(self, balance):
        self.__balance = balance  # --> private variable
    
    def __deposit(self, amount):  # --> private method
        if amount > 0:
            self.__balance += amount
    
    def add_money(self, amount):
        temp = self.__deposit(amount)
        return temp
        
    def get_balance(self):
        return self.__balance


# account = BankAccount(20000)
# print(f"current balance before deposit - {account.get_balance()}")
# account.add_money(30000)
# print(f"current balance after deposit - {account.get_balance()}")

# print(account.balance)

# 2. Inheritance

# 1. parent class (base class)
# 2. child class (derived class)

class Animal():  # --> parent class
    animal_var = "I'm a global variable inside class Animal"
    def speak(self):
        return "This animal makes a sound"

class Dog(Animal): # --> child class
    def speak(self):
        return "Dog barks - makes woof!"
    
    def get_details(self):
        return "My name is Chintu and I'm a Dog"

class Cat(Animal): # --> child class
    def speak(self):
        return "Cat makes meow's!"
    
    def get_details(self):
        return "My name is Rita and I'm a Cat"
    
# Chintu = Dog()
# print(Chintu.speak())
# print(Chintu.get_details())
# print(Chintu.animal_var)

# Rita = Cat()
# print(Rita.speak())
# print(Rita.get_details())

# multiple inheritence
class FatherParent():
    pass

class MotherParent():
    pass

class Child(FatherParent, MotherParent):
    pass

# Multi-level Inheritance

class GrandParent():
    pass

class FatherParent(GrandParent):
    pass

class Child(FatherParent):
    pass



class GooglePay():
    def make_payment(self, amount):
        return f"Paid {amount} to user via GPay"

class PhonePey():
    def make_payment(self, amount):
        return f"Paid {amount} to user via PhonePey"
    
class AmazonPay():
    def make_payment(self, amount):
        return f"Paid {amount} to user via AmazonPay"

instances = [GooglePay(), PhonePey(), AmazonPay()]

for instance in instances:
    print(instance.make_payment(1000))
    
