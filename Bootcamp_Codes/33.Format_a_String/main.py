# Format a String
# Use find and string slicing to extract the portion of the string after the colon character and 
# then use the float function to convert the extracted string into a floating point number.

# custom_string = 'X-MAPDS-Confidence:0.8475'
# Output
# 0.8475

custom_string = 'X-MAPDS-Confidence:0.8475' 
#finding the : in the string 
index = custom_string.find(":")
#convert the number after : to float
num = float(custom_string[index+1:])
# print the result
print(num)