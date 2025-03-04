price = 1000000
buyer_credit = 'bad'

if buyer_credit == 'good':
    value = 0.1 * price
    print(f'The down payment is ${value}')
else:
    value = 0.2 * price
    print(f'The down payment is ${value}')