# Python program for simple calculator
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return  a/b

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


operation= int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if operation == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif operation == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif operation == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif operation == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
