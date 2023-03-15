import math

# Define functions for each operation
def sqrt():
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
    print("Square root of {} = {}".format(num, result))

def fact():
    num = int(input("Enter a number: "))
    result = math.factorial(num)
    print("{}! = {}".format(num, result))

def ln():
    num = float(input("Enter a number: "))
    result = math.log(num)
    print("Natural logarithm of {} = {}".format(num, result))  #function for log

def power():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    result = math.pow(base, exponent)
    print("{} raised to the power of {} = {}".format(base, exponent, result))

# Main program loop
while True:
    print("\nSelect an operation:")
    print("1. Square root")
    print("2. Factorial")
    print("3. Natural logarithm")
    print("4. Power")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        sqrt()
    elif choice == '2':
        fact()
    elif choice == '3':
        ln()
    elif choice == '4':
        power()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
