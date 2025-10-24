score1 = 85
score2 = 78
score3 = 92
# Define a function calculate_average(score1, score2, score3) that returns the average of three scores
def calculate_average(score1, score2, score3):
    average_score= sum((score1, score2, score3))/3
    return average_score

print(calculate_average(45, 50, 25))
# Define a function drop_lowest(score1, score2, score3) that returns the average of the two highest scores
def finding_average_of_two_highest(score1, score2, score3):
    sum_of_scores = sum((score1, score2, score3))
    minimal_num=min(score1, score2, score3)
    average_of_two_highest= (sum_of_scores-minimal_num)/2
    return average_of_two_highest

print(finding_average_of_two_highest(45, 50, 25))
    # find sum
    # subtract min
    # divide by 2
# Define a function calculate_weighted(assignments, midterm, final) that calculates weighted average:
def calculate_weighted(assignments, midterm, final):
    total_gpa= (assignments*0.3)+(midterm*0.3)+(final*0.4)
    return round(total_gpa, 2)
print(calculate_weighted(87,87,90))

# Assignments: 30%
# Midterm: 30%
# Final: 40%
# Define a function determine_grade(average) that returns letter grade:
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
avg = finding_average_of_two_highest(score1, score2, score3)
def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >=80:
        return 'B'
    elif average >=70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
print(determine_grade(avg))

def needs_improvement(current_avg, target_grade):
    if target_grade=='A':
        target_score=90
    elif target_grade=='B':
        target_score=80
    elif target_grade=='C':
        target_score=70
    if target_grade=='D':
        target_score=60

    how_much_needed= target_score-current_avg
    return how_much_needed
print(needs_improvement(65, 'B'))

def current_average(score1, score2, score3):
    current_average=((finding_average_of_two_highest(score1, score2, score3)<calculate_average(score1, score2, score3))+(finding_average_of_two_highest(score1, score2, score3)>calculate_average(score1, score2, score3)))
    return current_average

# STUDENT GRADE CALCULATOR
# ========================================
# Assignment Scores: 85, 78, 92
# Midterm Score: 88
# Final Score: 82
# ----------------------------------------
# Regular Assignment Average: 85.00
# Average with Lowest Dropped: 88.50
# Using Better Average: 88.50

# Weighted Course Average: 85.95
# Letter Grade: B

# Needs improvement for an 'A': Yes
# Points needed: 4.05
# Already meets or exceeds 'B' grade requirement

def score_calculator(score1, score2, score3, target_grade, midterm, final):
    assignments=finding_average_of_two_highest(score1, score2, score3)
    regular_avg=calculate_average(score1, score2, score3)
    avg_with_lowest_dropped=finding_average_of_two_highest(score1, score2, score3)
    weighted_course_average=calculate_weighted(assignments, midterm, final)
    letter_grade=determine_grade(avg)
    current_average=((finding_average_of_two_highest(score1, score2, score3)<calculate_average(score1, score2, score3))+(finding_average_of_two_highest(score1, score2, score3)>calculate_average(score1, score2, score3)))
    needed_points=needs_improvement(avg_with_lowest_dropped, target_grade)

    print('STUDENT GRADE CALCULATOR')
    print('='*20)
    print(f'Assignment scores: {score1}, {score2}, {score3}')
    print(f'Midterm score: {midterm}')
    print(f'Final score: {final}')
    print('-'*20)
    print(f'Regular Assignment Average: {regular_avg}')
    print(f'Average with Lowest Dropped: {avg_with_lowest_dropped}')
    print(f'Using Better Average: {avg_with_lowest_dropped}\n')
    print(f'Weighted Course Average: {weighted_course_average}')
    print(f'Letter Grade: {letter_grade}\n')
    print(f'Needs improvement for an "{target_grade}": {current_average}')
    print(f'Points needed: {needed_points}')
    print(f"Already meets or exceeds '{letter_grade}' grade requirement")
    
print(score_calculator(65, 90, 70, 'A', 75, 80))




