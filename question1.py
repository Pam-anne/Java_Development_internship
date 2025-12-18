def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "You cannot divide a number by zero."
    else:
        return a / b


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = input("Enter option (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if option == '1':
    print(f"The answer is: {add(num1, num2)}")
elif option == '2':
    print(f"The answer is: {subtract(num1, num2)}")
elif option == '3':
    print(f"The answer is: {multiply(num1, num2)}")
elif option == '4':
    print(f"The answer is: {divide(num1, num2)}")
else:
    print("Invalid choice! Please enter 1-4.")
