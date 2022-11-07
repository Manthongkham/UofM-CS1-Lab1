'''
This program outlike the information about a given loan for personal financial decision.
'''

print('Please enter the following information:     ')

principle_loan = int(input('Initial amount of loan:       '))
rate = float(input('Annual interest reate (in %): ')) / 100 / 12
n_term = int(input('Number of years:              ')) * 12

monthly_payment = principle_loan * ((rate * ((1 + rate)**n_term))/(((1 + rate)**n_term) - 1))
total_loan = monthly_payment * n_term
total_interest = total_loan - principle_loan

print(f'\nMonthly payment: ${monthly_payment:.2f}')
print(f'Total paid:      ${total_loan:.2f}')
print(f'Interest paid:   ${total_interest:.2f}')
