# My solution to weekly task 4

# Program that asks the user to input any positive integer and outputs the successive values of the following calculation
# Author: Anna Kozakiewicz
# Resource of the code: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

number=int(input('Please enter a positive integer:\n'))

# take the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one

def collatz(number):

# check if the number is odd or even and then calculate

    while number != 1:  
        if number % 2 == 0:     # even   
            number = number // 2
            print(number)

        else:                   # odd
           number =  3 * number + 1
           print(number)    

collatz(number)