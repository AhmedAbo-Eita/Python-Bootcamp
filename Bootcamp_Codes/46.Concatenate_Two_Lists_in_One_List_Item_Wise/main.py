# Concatenate Two Lists in One List Item Wise
#
# Implement a function which takes two lists as parameter and return concatenation of these lists item wise.
#
# Example
#
#     list1 = ["Hello ", "take "]
#     list2 = ["Dear", "Sir"]
#     concatenate(list1, list2)
#
# Output
#
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate(p_list1, p_list2):
    final_list = []
    for item1 in p_list1:
        for item2 in list2:
            final_list.append(item1+item2)
    return final_list

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatenate(list1, list2))