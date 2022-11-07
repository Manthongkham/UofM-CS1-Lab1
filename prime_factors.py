'''
Creating a prime factors machine to output all the prime factor of a number.
'''

# Provide input validation in order to prevent any invalid input.
n = int(input('Enter a positive interger 2 or greater: '))
while n < 2:
	n = int(input('Must be at least 2, try again: '))

print(f'Prime factors of {n}:')

# Creating am algorithm that will the number by 2 and itself and every number 
# inbetween in order to figure out the prime factors.
i = 2
while i <= n:       
    if n % i == 0:
    	# Output each prime factors
        print(i)
        n //= i
        continue
    # Increasing each incrematon by 1.
    i += 1
    