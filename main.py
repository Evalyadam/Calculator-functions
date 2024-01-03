def calculate(operation):
    number_1 = input(f'Enter first number: ')
    number_2 = input(f'Enter second number: ')
    
    if operation == 'add':
        total = int(number_1) + int(number_2)
    elif operation == 'divide':
        total = int(number_1) / int(number_2)
    elif operation == 'multiply':
        total = int(number_1) * int(number_2)
    elif operation == 'subtract':
        total = int(number_1) - int(number_2)
    else:
        print('Invalid operation')
        return

    print(f'Total: {total}')


#Calcualtes 2 numbers based of the parameters.
#Made in 15:46 PM 3/10/2024 Hebron GMT time.
#These functions can be used throughout all projects.(As long as you have it downloaded xD.).
#ADMR Calculater. (add devide multiply remove).
#Free To Use!!!
