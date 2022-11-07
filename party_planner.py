# This program purpose is to calculate the ammount of drinks we need to buy 
# To get ready for a party for a cirtain amount of people.

# This function is to calculate the amount of extra cans left over 
# After the party.
def plan_party(f, c, p):
	people = f + 1                     # The amount of people including yourself
	can_need = people * c              # The minimum amount of cans need 
	
	actual_pack = 1                    
	actual_can = p
	while actual_can < can_need:       # Create a loop to calculate the lowest amount of packs need 
		actual_pack += 1               # for the party by adding 1 pack at a time until the total amount of cans
		actual_can += p                # match or greater than the minimum amount of can needed

	print(f'\n{actual_pack} {p}-pack(s) needed')    # Print the result of the total packs you need to buy
	print(f'{actual_can - can_need} extra can(s)')  # Print the left over can you will have after the party

# This function is to calculate a similar calculation as plan_party() 
# But only output the result of the number of packs needed.
def plan_party2(f, c, p):
	people = f + 1
	can_need = people * c
	actual_pack = 1
	actual_can = p

	while actual_can < can_need:
		actual_pack += 1
		actual_can += p	
	return actual_pack                 # Instead of printing the result. We only return a value 


# Practice calling the first function: plan_party()
# The result will print without a value because the print() was build within the function
print('(A)')
plan_party(9, 14, 6)
plan_party(4, 6, 3)
plan_party(4, 6, 4)
print('------------------------------------------------------------')


# To print the second function, we need to use print() outside the function
# The function only return a value of the result.
print('(B)')

# We can also store the return result inside a variable for latter use.
x = plan_party2(9, 14, 6)
y = plan_party2(4, 6, 3)
z = plan_party2(4, 6, 4)

print(x)
print(y)
print(z)
print('------------------------------------------------------------')


# We can use input() function to get a values for any parameters.
# By assigning it to a variables and use it as a parameter when call for function.
print('(C)')
num_friend = int(input('How many friends are you throwing this party for? '))
num_can_per_person = int(input('How many cans will each person drink? '))
num_can_in_pack = int(input('How many cans are in each pack? '))
a = plan_party2(num_friend, num_can_per_person, num_can_in_pack)

plan_party(num_friend, num_can_per_person, num_can_in_pack)
print(f'Return value from plan_party2: {a}')
print('------------------------------------------------------------')
