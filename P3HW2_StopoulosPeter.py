# CTI-110
# P3HW2 - Pizza Order
# Peter Stopoulos
# 11 March 2022

def pizza():
    pizzas = 0  # Depends on number of students
    price = 0   # Depends on number of pizzas
    num_students = int(input('How many students do you want to order pizza for? '))
    people_pizza = float(input('Enter number of people per pizza (1.5, 2, or 3): '))
    if people_pizza == 1.5 or 2:
        pizzas = int(people_pizza * num_students)
        price = float(pizzas * 5 * 1.06)
        print('-----Pizza Order---------')
        print('Number of Students: ' + str(num_students))
        print('Pizzas Needed: ' + str(pizzas))
        print('Price: ' + str(price))
        print('-------------------------')
    elif people_pizza == 3:
        pizzas = int(people_pizza * num_students)
        price = float(pizzas * 5 * 1.06)
        print('-----Pizza Order---------')
        print('Number of Students: ' + str(num_students))
        print('Pizzas Needed: ' + str(pizzas))
        print('Price: $' + str(price))
        print('-------------------------')

    else:
        print('INVALID ENTRY!!!')
        print('Should have entered 1.5, 2, or 3')


pizza()