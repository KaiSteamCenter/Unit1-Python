"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

class person:
    def __init__(self, name, age):
        self.name = name  # Set the "name" attribute of the instance.
        self.age = age    # Set the "age" attribute of the instance.

    def intro(self): # Method to introduce the person, printing their name and age. 
         print(f"Hi, my name is {self.name} and I am {self.age} years old.")

mekhi = person("Mekhi", 17) # Creates instance

mekhi.intro() # Calls intro method



"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class Animal: # Define a class called "Animal"
    def __init__(self, name):
        self.name = name # Set the "name" attribute of the instance.
    def speak(self): # Filler stuff
        pass
    
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof") # Returns value of Dog (animal), and prints them saying woof
    
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow") # Returns value of Cat (animal), and prints them saying meow

dog = Dog("Oscar") # Creates instance w/ name of dog
cat = Cat("Grouch") # Creates instance w/ name of cat

dog.speak()  # Calls dog.speak method
cat.speak()  # Calls cat.speak method

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class BankAccount: #Define BankAccount class
    def __init__(self, balance, owner):
        self.balance = balance # Initilize balance
        self.owner = owner # Initilize owner
    
    def balances(self):
        print(f"{self.owner}'s Bank Account Balance: {self.balance}") # Shows balance to begin w/

    def withdraw(self, takeaway):
        self.balance = self.balance - takeaway  # Math function to subtract amount from og balance
        print(f"Your new balance is {self.balance}")
    def deposit(self, depo):
        self.balance = self.balance + depo  # Math function to add amount to newbalance
        print(f"Your new balance is {self.balance}")
  


mekhiAccount = BankAccount(1000, "Mekhi") # Creates Instant



mekhiAccount.balances() # Calls function of balance
mekhiAccount.withdraw(100) # Calls function of withdraw
mekhiAccount.deposit(200) # Calls function of deposit