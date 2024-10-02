# Highest Score
# A List of scores of students are given, implement a program that calculates the
# highest score from the given list.

# Example
# student_scores = [80, 60, 50, 65, 75, 55]
# # The highest score in the class is: 80

# Hint: DO NOT use any built in function such as max() and sum() !

student_scores = [80, 60, 50, 65, 75, 55]
def max_two_numbers(num1,num2):
    if num1>num2:
        return num1
    return num2
max = 0
for score in student_scores:
    max = max_two_numbers(score,max)

print (f"The highest score in the class is: {max}")