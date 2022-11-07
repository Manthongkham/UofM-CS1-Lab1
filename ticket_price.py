'''
Lab 3, question 1
Make ticket prices table in relation to customer age for the Sloth Museum.
'''

age = int(input('Enter your age: '))

if 0 <= age <= 7:
    print('Your ticket will be $0, enjoy the Sloth Museum!')
elif 8 <= age <= 17:
    print('Your ticket will be $10, enjoy the Sloth Museum!')
elif 18 <= age <= 64:
    print('Your ticket will be $15, enjoy the Sloth Museum!')
elif 65 <= age <= 122:
    print('Your ticket will be $12, enjoy the Sloth Museum!')
else:
    print('That doesn\'t make any sense! Valid age are 0-122.')
