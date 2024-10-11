# Print Pattern
# Create a function which takes as parameter integer number (n) 
# and based on this number it prints the following start pattern using nested loop and string formatting. 
# So if n equals 5 the maximum number of stars (*) will be 5 in the pattern.

def print_pattern(n):
    counter = 1
    for i in range(0,n):
        for j in range(0,counter):
            print("*", end=" " )
        counter +=1
        print(" ")
    counter -=1
    for i in range(0,n):
        for j in range(1,counter):
            print("*", end=" " )
        counter -=1
        print(" ")


print_pattern(10)