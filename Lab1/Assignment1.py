import math

# Print Hello World
print("Hello World")


# Functions
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


def calcuate_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    if not float(smaller).is_integer():
        return "Error: Factorial of non-integer"
    smaller = int(smaller)

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


def factorial(num):
    if num < 0:
        return "Error: Factorial of negative number"
    if not num.is_integer():
        return "Error: Factorial of non-integer"
    num = int(num)
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


# User Input
try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit(1)

# Operations
addition_result = addition(x, y)
subtraction_result = subtraction(x, y)
multiplication_result = multiplication(x, y)
division_result = division(x, y)

print(f"The addition of {x} and {y} is {addition_result}")
print(f"The subtraction of {x} and {y} is {subtraction_result}")
print(f"The multiplication of {x} and {y} is {multiplication_result}")
print(f"The division of {x} and {y} is {division_result}")

# Display the largest number
print(f"The largest number is {max(x, y)}")

# LCM & HCF
lcm_result = calculate_lcm(x, y)
hcf_result = calcuate_hcf(x, y)
print(f"The Lowest Common Multiple of {x} and {y} is {lcm_result}")
print(f"The Highest Common Factor of {x} and {y} is {hcf_result}")

# Factorial
try:
    factorial_result1 = factorial(x)
    factorial_result2 = factorial(y)
    print(f"The factorial of {x} is {factorial_result1}")
    print(f"The factorial of {y} is {factorial_result2}")
except ValueError as e:
    print(e)
