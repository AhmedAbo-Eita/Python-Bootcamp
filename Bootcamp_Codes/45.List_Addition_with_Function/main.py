# List Addition with Function
#
# Implement a function which takes two parameters - a list and a value and returns new
# list with value inserted in it without modifying the original list.
#
# Example
#
#     list1 = [1,2,3,4,5]
#     list2 = custom_insert(list1, 6)
#     print(list1)
#     print(list2)
#
# Output
#
#     [1,2,3,4,5]
#     [1,2,3,4,5,6]

def custom_insert(p_list1,number):
    p_list2 = p_list1.copy()
    p_list2.append(number)
    return p_list2

list1 = [1,2,3,4,5]
list2 = custom_insert(list1, 6)
print(list1)
print(list2)
