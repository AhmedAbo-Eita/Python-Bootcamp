# mplement a function that calculates the sum of all odd numbers from 1 to 100 by using range() function inside loop.
#
# Example
# 1+3+5+...+97+99 = 2500

def add_odd_numbers():
    sum = 0
    for num in range(1,101,2):
        sum += num
    return sum

print(add_odd_numbers())