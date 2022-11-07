current_age             = int(input('Current age:                                     '))
while current_age < 0:
    current_age         = int(input('Cannot be negative, try again:                   '))
    
starting_balance        = int(input('Starting balance:                                '))
while starting_balance < 0:
    starting_balance    = int(input('Cannot be negative, try again:                   '))

target_age              = int(input('Target retirement age:                           '))
while target_age < current_age:
    target_age          = int(input('Cannot be less than current age, try again:      '))
    
target_balance          = int(input('Target balance at retirement:                    '))
while target_balance < starting_balance:
    target_balance      = int(input('Cannot be less than starting balance, try again: '))
    
annual_contribution     = int(input('Annual contribution amount:                      '))
while annual_contribution < 0:
    annual_contribution = int(input('Cannot be negative, try again:                   '))
    
interest_rate           = int(input('Projected annual growth (percent):               '))
while interest_rate < 0:
    interest_rate       = int(input('Cannot be negative, try again:                   '))
interest_rate /= 100

output_growth  = ''
output_growth += '\nProjected Growth:'
output_growth += '\n-----------------'
output_growth += '\nAge      Year Start          Growth           Extra        Year End\n'

year_start = starting_balance
stop_year = target_age

i = 0
for x in range(current_age,target_age):
    year_start2 = year_start

    for y in range(x, target_age):
        growth2 = year_start2 * interest_rate
        year_end2 = year_start2 + growth2
        
        if year_end2 >= target_balance:
            stop_year = x
        else:
            year_start2 = year_end2

    if x >= stop_year:
        annual_contribution = 0
    else:
        i += 1

    growth = year_start * interest_rate
    year_end = year_start + growth + annual_contribution
    output_growth += f'{x}\t${year_start:10.2f}\t${growth:10.2f}\t${annual_contribution:10.2f}\t${year_end:10.2f}\n'
    year_start = year_end


if(year_end < target_balance):
    print("\nSorry, that target is unreachable :(")
else:
    print(f'\nYay! You can reach that goal by contribution your annual amount for')
    print(f'{i} year(s) until age {current_age + i}, then coasting the rest of the way to {target_age}.')
    print(output_growth)
