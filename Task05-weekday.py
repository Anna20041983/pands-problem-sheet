# My solution to weekly task 5

# Program that outputs whether or not today is a weekday
# Author: Anna Kozakiewicz
# Resource of the code: https://www.pythonprogramming.in/how-to-find-current-day-is-weekday-or-weekends-in-python.html

# The code is based on the weekday() function 
# And checks if it's > 5 then it is a weekend or if it's < 5 then it is a weekday
# Then print the correct asnwer depending on the day of the week

import datetime
 
d = datetime.datetime.today().weekday()
if d > 5: # 5 Sat, 6 Sun
    print('It is the weekend, yay!')
else:  
    print('Yes, unfortunately today is a weekday')