# Student Grades
#
# Implement a function which takes a dictionary as a parameter in which student scores are stored
# and converts their scores to grades and return it as new dictionary.
#
# This is the scoring criteria:
#
#     Scores 85 - 100: Grade = "Outstanding"
#     Scores 65 - 84: Grade = "Good"
#     Scores 50 - 64: Grade = "Acceptable"
#     Scores 50 lower: Grade = "Fail"
#
# Example
#
#     student_scores = {
#       "John": 90,
#       "Edy": 68,
#       "Marry": 88,
#       "Ewan": 79,
#       "Park": 62,
#     }
#     convert_grade(student_scores)
#
# Output
#
#     {
#      'John': 'Outstanding',
#      'Edy': 'Good',
#      'Marry': 'Outstanding',
#      'Ewan': 'Good',
#      'Park': 'Acceptable'
#     }

#given student scores dictionary
student_scores = {
    "John": 90,
    "Edy": 68,
    "Marry": 88,
    "Ewan": 79,
    "Park": 62,
}

# function take the score and convert it to a grade
def convert_grade(dict):
    p_dict = {}
    for key in dict:
        if dict[key]>= 85:
            p_dict[key] = "Outstanding"
        elif dict[key]>= 65:
            p_dict[key] = "Good"
        elif dict[key] >= 50:
            p_dict[key] = "Acceptable"
        else:
            p_dict[key] = "Fail"
    return p_dict

#calling the function and pass the student_scores dictionary to it
print(convert_grade(student_scores))
