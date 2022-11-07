'''
Write a program that asks the user to enter a password. The program should show as access granted
or denied message depending on whether the password was correct. Use loop to allow the user a 
maximum of 4 incorrect entries before ending the program. For each incorrect entry, the program
should also display how many attempts are remaining
'''

# Create the correct password and ask for user input. 
password = 'sloth'
user_input = input('Enter password: ')

# Create a loop that will check the user input
i = 1
while i < 5:
    # For in correct user input, the loop will go through the earror process.
    if password != user_input:
        if i < 4:
            # display the denied message and ask for more user input.
            print(f'Incorrect password. You have {4-i} attempt(s) remaining.')
            user_input = input('Enter password: ')
        else:
            # Display message once the maximum of 4 incorrect user input have reached.
            print('Your account has been locked for 24 hours')
    else:
        # The loop will automatically stop as soon as the user input match the password.
        print('Access granted.')
        break
    i +=1
