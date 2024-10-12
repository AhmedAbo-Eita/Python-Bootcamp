# First and Last Characters

# Implement a function which takes the string type list as a parameter and returns the count of the number of strings
# where the string length is 2 or more and the first and the last characters are same.

# Example
#list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
#count_words(list1)
# Output
# 3


#given list
list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']

#implementation of the function
def count_words(p_list):
    counter = 0
    for word in p_list:
        if len(word) >= 2 and word[0] == word[-1]:
            counter += 1
    return counter

counts = count_words(list1)
print(counts)