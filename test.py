# File: test.py

import random
import time

# This function generates a list of random numbers but has a misleading name and hardcoded values
def do_something():
    numbers = []
    for i in range(10):  # Hardcoded value
        numbers.append(random.randint(1, 100))  # Random numbers
    return numbers

# Function with no error handling and redundant code
def risky_function():
    data = input("Enter a number: ")
    result = int(data) / 0  # Division by zero - intentional error
    print(f"Result is: {result}")
    print(f"Result is: {result}")  # Duplicate print

# Unused variable and no docstring
def calculate():
    x = 10  # Unused variable
    return x * 2

# Class with unused methods
class ExampleClass:
    def __init__(self, value):
        self.value = value

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        # Unused method
        return a * b

# Function with excessive cyclomatic complexity
def complex_function(x):
    if x > 10:
        if x % 2 == 0:
            return "Even and greater than 10"
        else:
            return "Odd and greater than 10"
    elif x < 5:
        if x % 2 == 0:
            return "Even and less than 5"
        else:
            return "Odd and less than 5"
    else:
        return "Between 5 and 10"

# Sleep in production code and inefficient loops
def inefficient_function():
    time.sleep(2)  # Sleep in production code
    for i in range(1000):
        for j in range(1000):
            pass  # Inefficient nested loop

# Main function that is redundant
def main():
    print("Starting the program...")
    do_something()
    print("Program complete.")

if __name__ == "__main__":
    main()
