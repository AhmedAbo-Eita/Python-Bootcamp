# Instructions

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Grade	Score
# A	>= 0.9
# B	>= 0.8
# C	>= 0.7
# D	>= 0.6
# F	< 0.6
# Example

# Enter score: perfect
# > Bad score
# Enter score: 10.0
# > Bad score
# Enter score: 0.75
# > C
# Enter score: 0.5
# > F

try:
    score = float(input("Enter Score: "))
except:
    print("Bad score")
    quit()

if score>1:
    print("Bad score")
elif score>=.9:
    print("Score is A")
elif score>=.8:
    print("Score is B")
elif score>=.7:
    print("Score is C")
elif score>=.6:
    print("Score is D")
else:
    print("Score is F")
