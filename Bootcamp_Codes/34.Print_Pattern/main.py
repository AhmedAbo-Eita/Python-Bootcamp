# Print Pattern
# Create a function which takes as parameter integer number (n) 
# and based on this number it prints the following start pattern using nested loop and string formatting. 
# So if n equals 5 the maximum number of stars (*) will be 5 in the pattern.

def print_pattern(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*")
        print("\n")


print_pattern(5)