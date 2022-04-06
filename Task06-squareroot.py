# My solution to weekly task 6

# Function to return square root of a number using Newtons Method
# Author: Anna Kozakiewicz
# Resource of the code: https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method

def NewtonMethod (number, number_items=100):
    num = float (number)
    for i in range (number_items):
        number = 0.5 * (number + num / number)
    return number

#  The input of our code is to put a positive number

num = float(input ("Please enter a positive number : "))

# Then the output is calculated and printed

print ("Square root of", num, "is approx : ", NewtonMethod (num))