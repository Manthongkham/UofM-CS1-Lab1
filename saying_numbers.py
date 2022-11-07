# Part (a) 
# Create a list for each of the one digit traslation
def one_digit_to_str(n):
	one_digit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	
	# Call the result by using n as an index
	if n < 10: return one_digit[n]


# Part (b)
# Create a list for each of the two digits transtion
def two_digit_to_str(n):
	# Create two differest varible for two digits under twenty
	# and digits representing the peak of each set of 10th number.
	two_digit_under_twenty = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	two_digit = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	
	# Recall the previous related functions
	if n < 10: return one_digit_to_str(n)
	if n < 20: return two_digit_under_twenty[n%10]
	if n < 100:
		# to prevetn the program calling 'zero' when the one digit is 0
		if n % 10 == 0:
			return two_digit[n//10 - 2]
		else:
			return two_digit[n//10 - 2] + ' ' + one_digit_to_str(n%10)


# Part (c)
def three_digit_to_str(n):
	# Recall the previous related functions
	if n < 10: return one_digit_to_str(n)
	if n < 100: return two_digit_to_str(n)

	if n < 1000:
		# to prevetn the program calling 'zero' when the one digit is 0
		if n % 100 == 0:
			return one_digit_to_str(n//100) + ' hundred '
		else:
			return one_digit_to_str(n//100) + ' hundred ' + two_digit_to_str(n%100)


# Part (d)
def int_to_str(n):
	# Recall the previous related functions
	if n < 10: return one_digit_to_str(n)
	if n < 100: return two_digit_to_str(n)
	if n < 1000: return three_digit_to_str(n)

	if n < 1000000:
		a = n // 1000
		b = n % 1000
		if n % 1000 == 0:
			# to prevetn the program calling 'zero' when the one digit is 0
			return three_digit_to_str(a) + ' thousand '
		else:
			return three_digit_to_str(a) + ' thousand ' + three_digit_to_str(b)

	if n < 1000000000:
		c = n//1000000
		d = n%1000000//1000
		e = n%1000
		if n % 1000000 == 0:
			# to prevetn the program calling 'zero' when the one digit is 0
			return three_digit_to_str(c) + ' million '
		if d == 0:
			# to prevetn the program calling 'zero' when the one digit is 0
			return three_digit_to_str(c) + ' million ' + three_digit_to_str(e)
		else:
			return three_digit_to_str(c) + ' million ' + three_digit_to_str(d) + ' thousand ' + three_digit_to_str(e)
	
	else:
		f = n // 1000000000
		g = n % 1000000 // 1000000
		h = n % 1000000 // 1000
		i = n % 1000
		if n % 1000000000 == 0:
			# to prevetn the program calling 'zero' when the one digit is 0
			return three_digit_to_str(n//1000000000) + ' billion '
		if g == 0 and h == 0:
			# to prevetn the program calling 'zero' when the one digit is 0
			return three_digit_to_str(f) + ' billion ' + three_digit_to_str(i)
		elif g == 0:
			# to prevetn the program calling 'zero' when the one digit is 0
			return three_digit_to_str(f) + ' billion ' + three_digit_to_str(h) + ' thousand' + three_digit_to_str(i)
		elif h == 0:
			# to prevetn the program calling 'zero' when the one digit is 0 
			return three_digit_to_str(f) + ' billion ' + three_digit_to_str(g) + ' million ' + three_digit_to_str(i)
		else: 
			return three_digit_to_str(f) + ' billion ' + three_digit_to_str(g) + ' million ', three_digit_to_str(h) + ' thousand' + three_digit_to_str(i)



# Part (e)
# Print out result using only the function form part (d)
user_input = int(input('Enter an integer to pronounce (0-999999999999, anynegative value to exist:\n'))
while user_input >= 0:
	if user_input < 0:
		print('kthxbye!')
		break
	elif user_input > 999999999999:
		user_input = int(input('Cannot be over 999999999999, try again: '))
	else:
		print(int_to_str(user_input))
		print()
		user_input = int(input('Enter an integer to pronounce (0-999999999999, anynegative value to exist:\n'))

if user_input < 0:
	print('kthxbye!')

















