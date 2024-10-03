# Implement a function which takes a List as a parameter and returns the sum of the scores which are above average.
#
# Example
# student_scores = [80, 60, 50, 65, 75, 55]
# sum_score_above_average(student_scores) # 220

# Hint : DO NOT use any built in function such as sum() and len() !



#given list
student_scores = [80, 60, 50, 65, 75, 55]

def sum_score_above_average(p_student_scores):
    # get a variable sum and give it an initial value 0
    sum = 0
    sum_above_averge=0
    count = 0
    for score in student_scores:
        sum += score
        count += 1
    average = sum/count

    for score in student_scores:
        if score>average:
            sum_above_averge += score
    return sum_above_averge

print(sum_score_above_average(student_scores))