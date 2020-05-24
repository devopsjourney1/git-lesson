# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
   """This function adds two numbers"""
   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""
   return x - y

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")

choice = input("Enter choice(1/2):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
