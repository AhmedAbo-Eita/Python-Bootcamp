# Implement a function that takes two strings as parameters and returns their concatenation.
#
# Example:
# concatenate("face", "book")
# output:
# facebook

def concatenate(text1,text2):
    final_text = text1+text2
    return final_text

out = concatenate("face","book")
print(out)