# Dummy Python Script
# Author: Your Name
# Purpose: Demonstrate basic Python syntax

def greet_user(name):
    print(f"Hello, {name}! Welcome to the dummy program.")
def add_numbers(a, b):
    return a + b

def main():
    # Greeting
    greet_user("Alice")

    # Add two numbers
    result = add_numbers(5, 10)
    print(f"The result of addition is: {result}")

    # Dummy loop
    for i in range(3):
        print(f"Loop iteration {i + 1}")

    # Dummy condition
    if result > 10:
        print("That's a big number!")
    else:
        print("That's a small number!")

# Entry point
if __name__ == "__main__":
    main()
