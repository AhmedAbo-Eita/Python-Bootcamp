# Create a function that takes two digits number from console and returns sum of digits. e.g.
# if the input was 45, then the output should be 4 + 5 = 9
#
# Example Input
# sum_of_two_digits()
# Enter two digit number: 45
# Output
#
# 4 + 5  = 9
#
# 9

def sum_of_two_digits():
    num = input("Enter two digit number: ")
    result = int(num[0])+int(num[1])
    return result

print(sum_of_two_digits())