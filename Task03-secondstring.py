# My solution to weekly task 3

# Program creating a string and outputting every second letter in reverse order
# Author: Anna Kozakiewicz

# First we need an input

inputString = input('Please enter a sentence:')

# The sentence for input is: The quick brown fox jumps over the lazy dog.

# Then we want to show every second letter in reverse orded from our input
# Resource to help understand the code: https://stackoverflow.com/questions/766141/understanding-string-reversal-via-slicing

reversed = inputString[::-2]

# The last step is to print our output

print(reversed)
