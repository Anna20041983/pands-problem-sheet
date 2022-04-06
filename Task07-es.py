# My solution to weekly task 7

# Program that reads in a text file and outputs the number of e's it contains
# Author: Anna Kozakiewicz
# Resource of the code: https://www.sanfoundry.com/python-program-read-file-counts-number/
# Resource of the Moby Dick text: https://www.gutenberg.org/ebooks/2701 & http://www.literaturepage.com/read/mobydick-599.html

filename ="moby-dick.txt "
l=input("Please enter a letter to be searched: ")
k = 0

# open the file in read mode
 
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1

# call the function and display the count of letter 'e' in text

print("The number of", l, "'s it contains:")
print(k)       
