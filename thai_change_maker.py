'''
This program determines a combination of Thai baht that adds up to some amount
And convert it into US dollar
'''


user_number = int(input('Enter number of baht: '))

thousand_bill = user_number // 1000
five_hun_bill = user_number % 1000 // 500
one_hun_bill = user_number % 1000 % 500 // 100
five_ten_bill = user_number % 1000 % 500 % 100 // 50
two_ten_bill = user_number % 1000 % 500 % 100 % 50 // 20
one_ten_coin = user_number % 1000 % 500 % 100 % 50 % 20 // 10
five_unit_coin = user_number % 1000 % 500 % 100 % 50 % 20 % 10 // 5
two_unit_coin = user_number % 1000 % 500 % 100 % 50 % 20 % 10 % 5 // 2
one_unit_coin = user_number % 1000 % 500 % 100 % 50 % 20 % 10 % 5 % 2 // 1

print(f'\n1000 baht bills: {thousand_bill}')
print(f'500 baht bills: {five_hun_bill}')
print(f'100 baht bills: {one_hun_bill}')
print(f'50 baht bills: {five_ten_bill}')
print(f'20 baht bills: {two_ten_bill}')
print(f'10 baht coins: {one_ten_coin}')
print(f'5 baht coins: {five_unit_coin}')
print(f'2 baht coins: {two_unit_coin}')
print(f'1 baht coins: {one_unit_coin}')

print(f'\nIn USD, that\'s ${user_number * 0.027:.3f} ')
