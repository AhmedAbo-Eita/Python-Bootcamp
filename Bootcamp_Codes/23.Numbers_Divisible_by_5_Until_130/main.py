# Implement a function which takes a given ordered list as a parameter and displays numbers divisible by 5 and if a number is greater than 130 display STOP in the console.
#
# Example
#     list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
#     numbers_divisible_byfive(list1)
# Output
#     15
#     40
#     75
#     STOP

def numbers_divisible_byfive(p_list):
    for num in p_list:
        if num % 5 == 0 and num < 130:
            print(num)
        elif num % 5 == 0 and num > 130:
            print("STOP")
            break

list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
numbers_divisible_byfive(list1)