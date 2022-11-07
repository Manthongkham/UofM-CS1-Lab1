'''
Lab 3, question 2
wrtite a program to check if ISBN is valid using the ISBN system fomular 
'''

isbn_number = input('Enthe 10-digit ISBN: ')

# Converting input into integer with the exception of the last digit
if len(isbn_number) == 10:
    x1 = int(isbn_number[0]) 
    x2 = int(isbn_number[1])
    x3 = int(isbn_number[2])
    x4 = int(isbn_number[3])
    x5 = int(isbn_number[4])
    x6 = int(isbn_number[5])
    x7 = int(isbn_number[6])
    x8 = int(isbn_number[7])
    x9 = int(isbn_number[8])
    x10 = isbn_number[9]

# Converting the last digit (10x) into integer
    if x10 == 'X':
        x10 = 10
    elif x10 == 'x':
        x10 = 10
    else:
        x10 = int(isbn_number[9])

# Check if ISBN is valid by using the input and the ISBN system formula
    valid_cal = ((x1*10)+(x2*9)+(x3*8)+(x4*7)+(x5*6)+(x6*5)+(x7*4)+(x8*3)+(x9*2)+(x10*1)) % 11
        
    if valid_cal == 0:
        print('Number is valid!')
    else:
        print('Number is invalid!')

# Let the end-user knows that the input is invalid
else:
    print('Error - number is not 10 digits')
