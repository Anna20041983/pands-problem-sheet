# My solution to weekly task 2

# How to calculate BMI
# Author: Anna Kozakiewicz

# We must calculate bmi by dividing weight by height

weight = int(input("Please enter your weight in kg: "))
height = int(input("Please enter your height in cm: "))

# With both inputs BMI is calculated by the formula below 
# Height is divided by 100 to convert the centimetres into metres
# Resource of the formula: https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g

BMI = weight/(height/100)**2

# The last step is to print the calculated BMI

print(f"Your BMI is {BMI} kg/m²")