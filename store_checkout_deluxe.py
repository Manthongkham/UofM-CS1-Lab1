'''
write a program that simulates checkout from an online store with any number of items.
'''

# Get user input for how many types of items they're buying
num_type = int(input('How many types of items are you buying today? '))
print()

# assisn initial shopping variables necessary 
num_item = 0
subtotal = 0

# Create a while loop that collect informations for each type of purcase
i = 1
while i <= num_type:
    a = input(f'Description for item {i}: ')
    b = input(f'Unit Price of {a}: ')
    c = input(f'Quantity of {a}: ')
    b = float(b)
    c = int(c)
    num_item += c
    subtotal += (b * c)
    print(f'{c}x {a} will cost ${(b * c):.2f}')
    print(f'({num_item} item(s) bought so far, costing ${subtotal:.2f})')
    i += 1
    print()

# Calculate expressions needed for purchase purposes
tax = subtotal * .0925
shipping = subtotal * .10
total = subtotal + tax + shipping

# Show the summary of the purcase
print(f'Subtotal: ${subtotal :9.2f}')
print(f'Tax:      ${tax      :9.2f}')
print(f'Shipping: ${shipping :9.2f}')
print(f'Total:    ${total    :9.2f}')
