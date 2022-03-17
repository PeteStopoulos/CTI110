# P3HW1 Total Purchases
# 11 March 2022
# Peter Stopoulos
def main() :
    # This program take a number grade and outputs a letter grade.

    # system uses 10 point grading scale
    a_score = 90
    # TO DO: define the rest of the scores
    b_score = 80
    c_score = 70
    d_score = 60

    score = input('Enter Grade: ')

    if int(score) >= a_score:
        print('Your grade is: A')
    elif int(score) >= b_score:
        print('Your grade is: B')
    elif int(score) >= c_score:
        print('Your grade is: C')
    elif int(score) >= d_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')


# Program start
main()

