'''
Write a program named sequences.py that prints the following sequences of numbers on the 
sreen, one number per line. Also number your lists starting from 1. Start by writing a loop
that runs the desired number of iteratinos, then think about what each iteration should do.

Print a blank line and a label for each part before showing the sequence.
'''

# The first 107 terms are incrementing by 10.
print('Part (a)')
i = 1
x = 707
while i < 108:
    print(f'{i}. {x}')
    x += 10
    i += 1

# The first 49 terms are incrementing by 7% 
print()
print('Part (b)')
i = 1
x = 1000.0
while i < 50:
    print(f'{i}. {x}')
    x *= 1.07
    i += 1

# The first 30 terms are decrementing by the product of n and 2. 
print()
print('Part (c)')
i = 1
x = 1969
subtract_me = 2
while i < 31:
    print(f'{i}. {x}')
    x -= subtract_me
    subtract_me *= 2
    i += 1

# For the first 42 terms. Each term is computed by adding the two previous terms.
print()
print('Part (d)')
i = 1
x = 11
add_me = -3
a = 0
while i < 43:
    print(f'{i}. {x}')
    a = x
    x += add_me
    add_me = a
    i += 1

# For the first 100 terms. Each term is evauate as even or odd, which has its own equation.
print()
print('Part (e)')
i = 1
x = 111
while i < 101:
    print(f'{i}. {x}')
    if x % 2 == 0:
        x //= 2
    else:
        x = (3 * x) + 1
    i += 1
