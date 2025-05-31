#Task 1: Calculate Factorial Using a Function


def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
NUMBER=5
fact = factorial(NUMBER)
print(f"THE FOCTORIAL OF {NUMBER} is: {fact}")


#Task 2: Using the Math Module for Calculations

import math

number = float(input("ENTER YOUR NUMBER: "))

sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)

print("THE SQUARE ROOT OF: ", sqrt_result)
print("THE LOGORITHM OF: ", log_result)
print("THE SINE OF THE NUMBER (in Radiane): ", sine_result)