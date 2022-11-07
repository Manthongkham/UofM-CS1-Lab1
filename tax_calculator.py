'''
Lab 3, question 3(b)
This tax calculator will calculate the total tax owed and tax rate for a given gross salary
by using the 2021 income tax bracket table as a refference 
'''

# Asking end user for gross salary input to calculate the desire income tax information
gross_salary = int(input('What was your 2021 income? '))

# create fomula of 2021 income taxes bracket for refference
bracket1 = (9950)*.10
bracket2 = (40525 - 9950)*.12
bracket3 = (86375 - 40525)*.22
bracket4 = (164925 - 86375)*.24
bracket5 = (209425 - 164925)*.32
bracket6 = (523600 - 209425)*.35
bracket7 = (gross_salary - 523600)*.37

# Create each condition for each tax bracket 
if gross_salary <= 9950:
    bracket1 = (gross_salary) *.10        
    total_tax = bracket1
    tax_rate = (total_tax / gross_salary)*100
    print(f'    First $  9950:       ${bracket1:9.2f}')
    print()
    print(f'Total tax Owed:          ${total_tax:9.2f}')
    print(f'Effective tax rate:      {tax_rate:9.1f}%')
    
elif gross_salary <= 40525:
    bracket2 = (gross_salary - 9950)*.12
    total_tax = bracket1 + bracket2
    tax_rate = (total_tax / gross_salary)*100
    print(f'    First $  9950:       ${bracket1:9.2f}')
    print(f'$  9950 - $ 40525:       ${bracket2:9.2f}')
    print()
    print(f'Total tax Owed:          ${total_tax:9.2f}')
    print(f'Effective tax rate:      {tax_rate:9.1f}%')

elif gross_salary <= 86375:
    bracket3 = (gross_salary - 40525)*.22
    total_tax = bracket1 + bracket2 + bracket3
    tax_rate = (total_tax / gross_salary)*100
    print(f'    First $  9950:       ${bracket1:9.2f}')
    print(f'$  9950 - $ 40525:       ${bracket2:9.2f}')
    print(f'$ 40525 - $ 86375:       ${bracket3:9.2f}')
    print()
    print(f'Total tax Owed:          ${total_tax:9.2f}')
    print(f'Effective tax rate:      {tax_rate:9.1f}%')

elif gross_salary <= 164925:
    bracket4 = (gross_salary - 86375)*.24
    total_tax = bracket1 + bracket2 + bracket3 + bracket4
    tax_rate = (total_tax / gross_salary)*100
    print(f'    First $  9950:       ${bracket1:9.2f}')
    print(f'$  9950 - $ 40525:       ${bracket2:9.2f}')
    print(f'$ 40525 - $ 86375:       ${bracket3:9.2f}')
    print(f'$ 86375 - $164925:       ${bracket4:9.2f}')
    print()
    print(f'Total tax Owed:          ${total_tax:9.2f}')
    print(f'Effective tax rate:      {tax_rate:9.1f}%')
    
elif gross_salary <= 209425:
    bracket5 = (gross_salary - 164925)*.32
    total_tax = bracket1 + bracket2 + bracket3 + bracket4 + bracket5
    tax_rate = (total_tax / gross_salary)*100
    print(f'    First $  9950:       ${bracket1:9.2f}')
    print(f'$  9950 - $ 40525:       ${bracket2:9.2f}')
    print(f'$ 40525 - $ 86375:       ${bracket3:9.2f}')
    print(f'$ 86375 - $164925:       ${bracket4:9.2f}')
    print(f'$164925 - $209425:       ${bracket5:9.2f}')
    print()
    print(f'Total tax Owed:          ${total_tax:9.2f}')
    print(f'Effective tax rate:      {tax_rate:9.1f}%')

elif gross_salary <= 523600:
    bracket6 = (gross_salary - 209425)*.35
    total_tax = bracket1 + bracket2 + bracket3 + bracket4 + bracket5 + bracket6
    tax_rate = (total_tax / gross_salary)*100
    print(f'    First $  9950:       ${bracket1:9.2f}')
    print(f'$  9950 - $ 40525:       ${bracket2:9.2f}')
    print(f'$ 40525 - $ 86375:       ${bracket3:9.2f}')
    print(f'$ 86375 - $164925:       ${bracket4:9.2f}')
    print(f'$164925 - $209425:       ${bracket5:9.2f}')
    print(f'$209425 - $523600:       ${bracket6:9.2f}')
    print()
    print(f'Total tax Owed:          ${total_tax:9.2f}')
    print(f'Effective tax rate:      {tax_rate:9.1f}%')

else:
    total_tax = bracket1 + bracket2 + bracket3 + bracket4 + bracket5 + bracket6 + bracket7
    tax_rate = (total_tax / gross_salary)*100
    print(f'    First $  9950:       ${bracket1:9.2f}')
    print(f'$  9950 - $ 40525:       ${bracket2:9.2f}')
    print(f'$ 40525 - $ 86375:       ${bracket3:9.2f}')
    print(f'$ 86375 - $164925:       ${bracket4:9.2f}')
    print(f'$164925 - $209425:       ${bracket5:9.2f}')
    print(f'$209425 - $523600:       ${bracket6:9.2f}')
    print(f'    After $523600:       ${bracket7:9.2f}')
    print()
    print(f'Total tax Owed:          ${total_tax:9.2f}')
    print(f'Effective tax rate:      {tax_rate:9.1f}%')
