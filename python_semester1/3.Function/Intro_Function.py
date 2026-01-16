#INTRO to Function in Python

# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create / Define function


# Function with Return values

a = 2
b = 32

def calculator():
    result = a + b
    return result

print(calculator())

#Function with Parameter(INPUT)

def multiply(a: int| float,b: int| float):
    result = a*b
    return result

print(multiply(3,9))

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
