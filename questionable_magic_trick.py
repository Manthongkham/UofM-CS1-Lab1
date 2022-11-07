'''
The following program is to show magic trick that nu matter the input number is, the final result
will always be 7.
'''


print('''You stand in the presence of the magnigicent Magic Mademoiselle Millicent.
Prepare to be ammazed!''')

user_number = int(input('Enter an integer: '))
new_user_number = user_number

print('\nOK, watch this...')

new_user_number *= 5
print(f'We\'ll multiply by 5 and get {new_user_number}')

new_user_number += 35
print(f'Then we\'ll add 35 and get {new_user_number}')

new_user_number //= 5
print(f'Then we\'ll divide by 5 and get {new_user_number}') 

new_user_number -= user_number 
print(f'Then we\'ll subtract the original number and get... {new_user_number}. Amazing!!!')
