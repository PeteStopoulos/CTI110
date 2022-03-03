# CTI-110
# P2HW2 - Score Avg
# Peter Stopoulos
# 25 February 2022

score1 = float(input('Enter score #1 : '))
score2 = float(input('Enter score #2 : '))
score3 = float(input('Enter score #3 : '))
score4 = float(input('Enter score #4 : '))
score5 = float(input('Enter score #5 : '))
score6 = float(input('Enter score #6 : '))
score7 = float(input('Enter score #7 : '))

grades = [score1, score2, score3, score4, score5, score6, score7]  # Compiles all scores to a list
lowest_score = min(grades)  # Calculates the lowest score
grades.remove(min(grades))  # Removes lowest score
average_grade = sum(grades) / len(grades)  # Calculates the average by taking the sum divided by amount of scores
print('-----Results------')
print(f'Lowest Score: {lowest_score:.1f}')
print(f'Modified List: {grades}')
print(f'Scores Average: {average_grade:.1f}')
print('-------------------')

