# File: problematic_code.py

import os
import logging
import hashlib

# Configure logging with unnecessary global scope
logging.basicConfig(level=logging.DEBUG)

# Function with insecure practices (e.g., storing passwords insecurely)
def save_user_credentials(username, password):
    with open("user_credentials.txt", "a") as file:
        file.write(f"{username}:{password}\n")  # Plaintext password storage

# Function with poorly handled exceptions
def divide_numbers(a, b):
    try:
        return a / b
    except Exception as e:  # Catch-all exception handling
        print("An error occurred:", e)

# Function with excessive logging
def process_data(data):
    logging.info("Processing data...")
    for item in data:
        logging.debug(f"Processing item: {item}")
        logging.warning("This is a dummy warning!")  # Unnecessary warnings
    logging.info("Data processed.")

# Function with hardcoded sensitive information
def connect_to_service():
    api_key = "12345-ABCDE"  # Hardcoded API key
    logging.info(f"Connecting to service with API key: {api_key}")  # Exposing sensitive data in logs

# Recursive function with no termination condition
def infinite_recursion(x):
    return infinite_recursion(x + 1)

# Unused imports and functions
import math  # Unused import

def unused_function():
    return math.sqrt(16)

# Function with missing input validation
def get_user_input():
    age = input("Enter your age: ")  # No validation
    if int(age) < 18:
        print("You are not eligible.")
    else:
        print("Welcome!")

# Main function with improper structure
def main():
    logging.info("Starting the program...")
    save_user_credentials("user1", "password123")
    result = divide_numbers(10, 0)
    print("Result of division:", result)
    process_data(["item1", "item2", "item3"])
    infinite_recursion(0)  # Intentional infinite recursion

if __name__ == "__main__":
    main()
