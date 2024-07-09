import numpy as np


def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Create two NumPy arrays
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

# Matrix of Addition
try:
    addition_result = np.add(x, y)
    print("Addition Result:\n", addition_result)
except Exception as e:
    print("Error in addition:", e)

# Matrix of Subtraction
try:
    subtraction_result = np.subtract(x, y)
    print("Subtraction Result:\n", subtraction_result)
except Exception as e:
    print("Error in subtraction:", e)

# Matrix of Multiplication
try:
    multiplication_result = np.multiply(x, y)
    print("Multiplication Result:\n", multiplication_result)
except Exception as e:
    print("Error in multiplication:", e)

# Matrix of Division
try:
    division_result = np.divide(x, y)
    print("Division Result:\n", division_result)
except Exception as e:
    print("Error in division:", e)

# Create List
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Creating a dictionary
student = {"name": "John Doe", "age": 20, "major": "Computer Science"}
print(student["name"])
print(student["age"])
print(student["major"])

target_element = 5
# Linear Search
result_linear_index = linear_search(my_list, target_element)
if result_linear_index != -1:
    print(f"Element {target_element} found at index {result_linear_index}.")
else:
    print(f"Element {target_element} not found in the list.")

# Binary Search
result_binary_index = binary_search(my_list, target_element)

if result_binary_index != -1:
    print(f"Element {target_element} found at index {result_binary_index}.")
else:
    print(f"Element {target_element} not found in the list.")
