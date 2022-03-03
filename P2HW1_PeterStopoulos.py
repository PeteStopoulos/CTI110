# P2HW1 Total Purchases
# 25 February 2022
# CTI-110 P2HW1 - Total Purchases
# Peter Stopoulos
item1 = float((input('Enter the price of item #1: ')))
item2 = float((input('Enter the price of item #2: ')))
item3 = float((input('Enter the price of item #3: ')))
item4 = float((input('Enter the price of item #4: ')))
item5 = float((input('Enter the price of item #5: ')))
subtotal = float(item1 + item2 + item3 + item4 + item5)
sales_tax = float(subtotal * 0.07)
total = float(subtotal + sales_tax)
# Program calculates sum of all items prices entered.
# Program calculates sales tac of the sum of all items enter * 0.07 (7%)
# Program calculated the total by adding the sum of all items entered to the sales tax
print('-----Results-----')
print(f'Subtotal: {subtotal:.2f}')
print(f'Sales Tax: {sales_tax:.2f}')
print(f'Total: {total:.2f}')
