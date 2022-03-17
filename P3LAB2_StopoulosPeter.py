oil = 35
tire  = 19
wash = 7
service = input('Enter desired auto service:')
if service.lower() == 'oil change':
    print('\nYou entered: ' + str(service))
    print('Cost of ' + str(service.lower()) + ': $' + str(oil))
elif service.lower() == 'tire rotation':
    print('\nYou entered: ' + str(service))
    print('Cost of ' + str(service.lower()) + ': $' + str(tire))
elif service.lower() == 'car wash':
    print('\nYou entered: ' + str(service))
    print('Cost of ' + str(service.lower()) + ': $' + str(wash))
else:
    print('\nYou entered: ' + str(service))
    print('Error: Requested service is not recognized')