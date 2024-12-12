# Object oriented Programming  is an input function that has attributes,clsss and subjects.  

## used to work with operators

#(b)
#A class has properties/ attributes
#An object takes on properties of a class
  





class Car:
     def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Create an instance of the Car class
my_car = Car(brand="subaru", color="black")

# Print the attributes of the object
print(f"Car Brand: {my_car.brand}")
print(f"Car Color: {my_car.color}")

#intermediate
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started.")

# Create an instance of the Car class
my_car = Car(brand="subaru", color="black")

# Call the start_engine method
my_car.start_engine()

#Advanced
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
    
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.balance

    def display_account_details(self):
        
        print(f"Account Number: {self.account_number}")


#Object Orientated Programming
#It always has classes and objects
#A class always has properties / attributes
##Methods are items of the class
#Objects come from a class
#An object takes on the properties of a class

#Syntax of OOP
#1.Creating classes
##Cohort class (a class name  and cohort start with a capital letter(upper case))
class Cohort:
    #Name
    #description
    #start_date
    #end_date
    #Within the cohort class,
    #Add a constructure for the cohort class(Read about constructures)
    #Add a method to the class that prints the cohort name and the total number of students 
    #Create a new instance /object of the cohort class