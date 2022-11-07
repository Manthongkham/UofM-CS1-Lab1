'''
Retirement account ballance predictoin, for the purposes of financial planning
however, this program does not considering any kind of employer contributions.
'''

# Gathering nessessary input from the end user. 
current_age             = float(input('Current age:                                     '))
while current_age < 0:
    current_age         = float(input('Cannot be negative, try again:                   '))
current_age = int(current_age)
    
starting_balance        = float(input('Starting balance:                                '))
while starting_balance < 0:
    starting_balance    = float(input('Cannot be negative, try again:                   '))

target_age              = float(input('Target retirement age:                           '))
while target_age < current_age:
    target_age          = float(input('Cannot be less than current age, try again:      '))
target_age = int(target_age)
    
target_balance          = float(input('Target balance at retirement:                    '))
while target_balance < starting_balance:
    target_balance      = float(input('Cannot be less than starting balance, try again: '))
    
annual_contribution     = float(input('Annual contribution amount:                      '))
while annual_contribution < 0:
    annual_contribution = float(input('Cannot be negative, try again:                   '))
    
interest_rate           = float(input('Projected annual growth (percent):               '))
while interest_rate < 0:
    interest_rate       = float(input('Cannot be negative, try again:                   '))
interest_rate /= 100

# Create a variable to save the output for latter
output_growth = '\nProjected Growth:'
output_growth += '\n-----------------'
output_growth += '\nAge        Year Start          Growth           Extra        Year End\n'

year_start = starting_balance
stop_year = target_age

i = 0
for x in range(current_age,target_age):
    year_start2 = year_start

    for y in range(x, target_age):
        # Create the second loop to compoud using given contribution
        growth2 = year_start2 * interest_rate
        year_end2 = year_start2 + growth2

        if year_end2 >= target_balance:
            stop_year = x
        else:
            year_start2 = year_end2

    if x >= stop_year:
        annual_contribution = 0
    else:
        # Keep track when the contribution stop
        i += 1

    # For each year, compute 1) the starting amount, 2) interest earned
    # 3) the ending amount
    growth = year_start * interest_rate
    year_end = year_start + growth + annual_contribution
    output_growth += f'{x}\t${year_start:12.2f}\t${growth:12.2f}\t${annual_contribution:12.2f}\t${year_end:12.2f}\n'
    year_start = year_end

# Print out statements in order as desire.
if(year_end < target_balance):
    print('\nSorry, that target is unreachable :(')
else:
    print(f'\nYay! You can reach that goal by contribution your annual amount for')
    print(f'{i} year(s) until age {current_age + i}, then coasting the rest of the way to {target_age}.')
    print(output_growth)
