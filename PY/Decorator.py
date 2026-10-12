'''

A decorator is a function that takes another function as input, adds some functionality to it, 
and returns the modified function, all without changing the source code of the original function.

Think of it like gift wrapping:

The gift = original function
The wrapping paper + ribbon = decorator
The result = decorated gift (same gift, but with added style/functionality)

'''

# 1. Define the decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Executes the original function
        print("Something is happening after the function is called.")
    return wrapper  # Returns the modified function

# 2. Apply the decorator using the @ symbol
@my_decorator
def say_hello():
    print("Hello!")

# 3. Call the function
say_hello()
