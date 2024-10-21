# Count Characters in a Word
#
# Implement a function that takes a String as a parameter and returns a dictionary
# with characters as keys from the String and values are the occurrence of characters in the String.
# Basically we are counting the occurrence of characters in a given string and returning it as output in Dictionary.
#
# Example
#     count_character("BABACDAS")
# Output
#     {
#      'B': 2,
#      'A': 3,
#      'C': 1,
#      'D': 1,
#      'S': 1
#     }

def string_dict(User_String):
    out_dict = {}
    for letter in User_String:
        if letter not in out_dict:
            out_dict[letter] = 1
        else:
            out_dict[letter] = out_dict[letter] + 1

    return out_dict

print(string_dict("BABACDAS"))
