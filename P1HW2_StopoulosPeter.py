# Pizza Calculator
# February 11, 2022
# CTI-110 P1HW2 - Pizza Order
# Peter Stopoulos

print('How many student do you want to order pizza for? ',end='')
students = int(input())
#Algorithm:
#3 x number of students = how many slices are needed.
#number of students / 2 = how many pizzas are needed.
slices = int(students * 3)
pizzas = float(students / 2)
print('----Pizza Order-------')
print('Number of Students: ' + str(students))
print('Pizza Slices Needed: ' + str(slices))
print('Pizzas Needed: ' + str(pizzas))
print('----------------------')
