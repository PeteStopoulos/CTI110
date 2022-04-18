# CTI-110
# 15 April 2022
# CTI-110 P5HW1 - Score List
# Peter Stopoulos
def collect_scores(num_scores): # Collects the amount of score entered in the input when function was called.
    is_valid = True
    num = 1
    scores = []
    for score in range(num_scores):
        score = int(input(f'Enter Score #{num}: '))
        if score < 0 or score > 100:
            is_valid = False
        while is_valid is False:
            print('Score Entry invalid, please re-enter a score between 0 and 100: ')
            score = int(input(f'Enter score #{num}: '))
            if score > -1 and score < 101:
                is_valid = True
        scores.append(score)
        num += 1
    return scores
def evaluate_scores(score_list):    # Function Evaluating scores entered 
    grade = ''
    lowest_score = min(score_list)  # Calculates the lowest score
    score_list.remove(min(score_list))  # Removes lowest score
    average_score = sum(score_list) / len(score_list)  # Calculates the average by taking the sum divided by amount of scores
    if 90 <= average_score:
        grade = 'A'
    elif 80 <= average_score:
        grade = 'B'
    elif 70 <= average_score:
        grade = 'C'
    elif 60 <= average_score:
        grade = 'D'
    elif 59 >= average_score:
        grade = 'F'
    return lowest_score, score_list, average_score, grade

def results(lowest_score, score_list, average_score, grade):     # Function displaying results of the scores evaluated

    is_viewing = True
    while is_viewing is True:
        print('-----Results------')
        print(f'Lowest Score  : {lowest_score:.1f}')
        print(f'Modified List : {score_list}')
        print(f'Scores Average: {average_score:.1f}')
        print(f'Grade         : {grade}')
        print('-------------------')
        return_menu = input('press enter to return to the menu! ')
        if return_menu != 1:
            is_viewing = False

def main():     # Main Menu function. Calls other functions when the user needs them.
    is_running = True
    scores = []
    while is_running is True:
        choice = input(f'\n-----------MENU-------------\n'
                '1) Create Score List\n'
                '2) Display Results\n'
                '3) Exit\n'
                '---------------------------\n')
        if choice == '1':
            scores = collect_scores(int(input('How many scores would you like to enter? ')))
        elif choice == '2':
            if scores == []:
                print('Must create score list first!')
            elif scores != []: 
                a, b, c,d = evaluate_scores(scores)
                results(a, b, c, d)
        elif choice == '3':
            print('Goodbye!')
            is_running = False
        else:
            print('Invalid Input!')

main()