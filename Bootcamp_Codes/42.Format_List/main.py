# Format List
#
# Print a given list in the format that is shown below using join method.
#
# custom_list = [1, 2, 3, 4, 5]
# Output
# 1 | 2 | 3 | 4 | 5

#given list
custom_list = [1, 2, 3, 4, 5]
out_list = []

for item in custom_list:
    out_list.append(str(item))

numbers = " | ".join(out_list)
print(numbers)