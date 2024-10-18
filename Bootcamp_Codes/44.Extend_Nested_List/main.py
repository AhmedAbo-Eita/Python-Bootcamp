# Extend Nested List
# Given a nested list and update the list with sub list ["h", "i", "j"] in such a way that it will look like the following list.

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# Output
# ist1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

#given list
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
#the sub list
list2 = ["h", "i", "j"]
#add the sub list to the main list
for item in list2:
    list1[2][1][2].append(item)
#print the result
print(list1)