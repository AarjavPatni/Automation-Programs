from tabulate import tabulate
from random import randint
from time import time

# Define the major system mapping
major_system = {
    0: ('s', 'z'),
    1: ('t', 'd', 'th'),
    2: ('n',),
    3: ('m',),
    4: ('r',),
    5: ('l',),
    6: ('j', 'ch', 'sh', 'soft g'),
    7: ('k', 'hard c', 'hard g'),
    8: ('f', 'v'),
    9: ('p', 'b')
}

# Function to convert a number to its mnemonic


def number_to_mnemonic(num):
    mnemonic = ""
    for digit in str(num):
        # mnemonic_options = major_system[int(digit)]
        mnemonic += ', '.join(major_system[int(digit)])
    return mnemonic


# Generate a table of numbers and mnemonics
table_data = []
for num in range(10):
    mnemonic = number_to_mnemonic(num)
    table_data.append([num, mnemonic])

# Print the table
print(tabulate(table_data, headers=[
      'Number', 'Mnemonic'], tablefmt='grid'), end='\n\n')

# Ask user to choose between encoding and decoding
# choice = int(input('Enter 1 to encode or 2 to decode: '))

while True:
    print(randint(11, 100))
    start_time = time()
    input('Mnemonic: ')
    end_time = time()
    print(f'{round(end_time - start_time, 1)}s', end='\n\n')