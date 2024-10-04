# Implement a function which takes two parameters as start and end of range and returns sum of even numbers within given range.
#
# Example
# add_even_numbers(1,100)
#
# Output
# 2550

def add_even_numbers(start, end):
    result = 0
    if start % 2 == 0:
        end += 1
        for num in range(start,end,2):
            result += num
        return result
    else:
        start += 1
        end += 1
        for num in range(start,end,2):
            result += num
        return result

print(add_even_numbers(1,100))