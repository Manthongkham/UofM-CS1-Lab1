'''
Sloth Machine is intended to help people win some money!
'''
import random

print('Welcome to TWENTY SLOTHS, good luck!')

# Get all the variables needed 
game = 1
exist = True
total_bet = 0
total_winning = 0

# Creating a while loop that will let player bet more even if the lost. 
while exist == True:
    # Keep tract of what game are they on
    print(f'\nGAME {game}')
    print('------')

    # Making an input validation to prevent player betting the wrong ammount
    bet_amt = int(input('Enter amount to bet: '))
    while bet_amt < 10:
        bet_amt = int(input('Bet must be at least $10, try again: '))

    # Create options for the player
    winning = bet_amt    
    num_sloth = 1
    while num_sloth < 20:
        print(f'\ncurrent sloths: {num_sloth}')
        print('1. Get 1-8 more sloths')
        print('2. Get 4-7 more sloths')
        print('3. Hold')
        
        # Create a mechenism for each options    
        user_input = int(input('\nEnter your choice (1, 2, or 3): '))
        if user_input == 1:
            add_me = random.randint(1, 8)
            print(f'\nAdding {add_me}...')
            num_sloth += add_me
        elif user_input == 2:
            add_me = random.randint(4, 7)
            print(f'\nAdding {add_me}...')
            num_sloth += add_me
        elif user_input == 3:
            print(f'\nHolding at {num_sloth}...')
            break
        else:
            print('\nInvalid choice. Let\'s try that again...')
    
    # Categorize the pizzes and print to the screen          
    if num_sloth <= 14:
        winning *= 0.00
        print(f'You won ${winning:.2f}. Congrats, you lost money :(')
    elif num_sloth == 15:
        winning *= 0.25
        print(f'You won ${winning:.2f}. Congrats, you lost money :(')
    elif num_sloth == 16:
        winning *= 0.50
        print(f'You won ${winning:.2f}. Congrats, you lost money :(')
    elif num_sloth == 17:
        winning *= 1.00
        print(f'You won ${winning:.2f}. Congrats, you break even!')
    elif num_sloth == 18:
        winning *= 1.25
        print(f'You won ${winning:.2f}. Amazing, you gained money!')
    elif num_sloth == 19:
        winning *= 1.50
        print(f'You won ${winning:.2f}. Amazing, you gained money!')
    elif num_sloth == 20:
        winning *= 2.00
        print(f'Amazing, you\'re at exactly {num_sloth} sloths!')
        print(f'You won ${winning:.2f}. Amazing, you gained money!')
    else:
        winning *= 0.00
        print(f'Oh no, you\'re at {num_sloth} sloths!')
        print(f'You won ${winning:.2f}. Congrats, you lost money :(')

    # Create a gran total for the winning at the end of all games
    total_winning += winning
    total_bet += bet_amt

    # Print the grant total of all game so far
    print(f'\nTotal games played: {game}')
    print(f'Net gain/loss: ${(total_winning - total_bet):.2f}')
    
    # Create an option for player to bet again
    x = input('\nEnter 1 to play again, anything else to exit: ')
    if x == '1':
        game += 1
    else:
        exist = False

# Have a final statement for the final game
print('\nThanks for playing! Hope you came out ahead...')
