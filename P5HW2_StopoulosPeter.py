# Math Quiz
# 15 April 2022
# CTI-110 P5HW2 - Math Quiz
# Peter Stopoulos
import random

def quiz_adding():  # Function creating a simple addition quiz
    continue_adding = True
    while continue_adding is True:  # Loop to keep playing if user decides
        a = random.randint(1,200)   # Random number to be added
        b = random.randint(1,200)   # Random number to be added
        c = a + b
        guesses = 0
        answer_is_correct = False
        while not answer_is_correct:
            print(f'  {a}\n'
                  f'+ {b}')
            answer = int(input())
            guesses += 1
            if answer > c:
                print("Sorry, that answer is too high.")
            elif answer < c:
                print('Sorry, that answer is too low.')
            elif answer == c:
                print("Congratulations! That is correct.")
                print(f'Number of guesses: {guesses}')
                answer_is_correct = True
        choice = input('Press 0 to return to the menu or anything else to add again! ')
        if choice == '0':
            continue_adding = False
def quiz_subtracting(): # Function Creating a simple subtraction Quiz
    continue_subtracting = True
    while continue_subtracting is True: # Loop to keep playing if user decides
        a = random.randint(1,200)
        b = random.randint(1,a) # Random number 'b' is between 1 and 'a' so the answer is not negative
        c = a - b
        guesses = 0
        answer_is_correct = False
        while not answer_is_correct:
            print(f'  {a}\n'
                  f'- {b}')
            answer = int(input())
            guesses += 1
            if answer > c:
                print("Sorry, that answer is too high.")
            elif answer < c:
                print('Sorry, that answer is too low.')
            elif answer == c:
                print("Congratulations! That is correct.")
                print(f'Number of guesses: {guesses}')
                answer_is_correct = True
        choice = input('Press 0 to return to the menu or anything else to subtract again! ')
        if choice == '0':
            continue_subtracting = False
def main_menu():    # Main Menu, call other functions from here
    menu = True
    while menu is True:
        print('MAIN MENU\n'
              '-----------------------------\n'
              '1. Adding random numbers\n'
              '2. Subtracting random numbers\n'
              '3. Exit\n'
              '------------------------------')
        choice = input()
        if choice == '1':
            quiz_adding()
        elif choice == '2':
            quiz_subtracting()
        elif choice == '3':
            print('Goodbye!')
            menu = False
        else:
            print('Invalid Selection!')

main_menu() # Runs Main Menu