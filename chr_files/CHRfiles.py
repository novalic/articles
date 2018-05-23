# Outputs results

line = 'c033 73f7 f7f7 3241 3fcc be49 4949 ffbe'.replace(' ', '')

result = \
[ x + 2*y for x, y in \
        zip(\
            [int(x) for x in list(bin(int(line[:16], 16))[2:].zfill(64))],\
            [int(x) for x in list(bin(int(line[16:], 16))[2:].zfill(64))]\
        )\
]

# Matrix representation:
matrix = \
[ result[index:index + 8] for index in range(0, len(result), 8) ]

print(*matrix, sep='\n')



# Result in binary (two digits)

print(*[ [ bin(entry)[2:].zfill(2) for entry in result ][index:index + 8] \
          for index in range(0, len(result), 8) ], \
      sep='\n'\
    )


# Output is:

# [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 3, 3, 2, 2, 3, 1, 1, 3, 1, 1, 2, 1, 1, 3, 1, 3, 1, 1, 2, 1, 1, 3, 1, 3, 1, 1, 2, 1, 1, 3, 2, 2, 3, 3, 2, 2, 3, 2, 2, 1, 2, 2, 2, 2, 2, 1]

# Organized in a two dimension array:

# [1, 1, 2, 2, 2, 2, 2, 2]
# [2, 2, 1, 1, 2, 2, 1, 1]
# [2, 1, 3, 3, 2, 2, 3, 1]
# [1, 3, 1, 1, 2, 1, 1, 3]
# [1, 3, 1, 1, 2, 1, 1, 3]
# [1, 3, 1, 1, 2, 1, 1, 3]
# [2, 2, 3, 3, 2, 2, 3, 2]
# [2, 1, 2, 2, 2, 2, 2, 1]


# In binary:

# ['01', '01', '10', '10', '10', '10', '10', '10']
# ['10', '10', '01', '01', '10', '10', '01', '01']
# ['10', '01', '11', '11', '10', '10', '11', '01']
# ['01', '11', '01', '01', '10', '01', '01', '11']
# ['01', '11', '01', '01', '10', '01', '01', '11']
# ['01', '11', '01', '01', '10', '01', '01', '11']
# ['10', '10', '11', '11', '10', '10', '11', '10']
# ['10', '01', '10', '10', '10', '10', '10', '01']



# Print each tile:

tiles = ['0000 0000 0000 0000 0000 0000 0000 0000', \
          '0000 0000 0000 0000 0000 0000 0000 0000', \
          '070f 3f7f ffff ff7f 0007 0f37 7f7f 6f1f', \
          '3f3f 1e1c 1c30 70fc 1e1c 0d0b 030f 2f73', \
          '60f0 f8f8 feff ffff 0060 f0e0 f8e0 8000', \
          'c033 73f7 f7f7 3241 3fcc be49 4949 ffbe', \
          '0000 0000 f0e0 d0f0 0000 0000 0000 0000', \
          'e040 8080 80c0 6070 0080 0000 0000 80a0' 
        ]

for tile in tiles:
  line = tile.replace(' ', '')
  result = \
    [ x + 2*y for x, y in \
        zip(\
          [int(x) for x in list(bin(int(line[:16], 16))[2:].zfill(64))], \
          [int(x) for x in list(bin(int(line[16:], 16))[2:].zfill(64))]\
        )\
    ]
  matrix = \
    [ result[index:index + 8] for index in range(0, len(result), 8) ]
  print(*matrix, sep='\n')
  print('\n')



# # For dummies!

# # Create two strings with each line of hexadecimal values and removing whitespaces
# l1 = 'c033 73f7 f7f7 3241'.replace(' ', '')
# l2 = '3fcc be49 4949 ffbe'.replace(' ', '')

# # Define a function that given a string representation of a hexadecimal number
# # returns a binary string of that number, removing the first two characters that
# # are '0b' for binary. Fills with zeros to complete 4 digits.
# def to_bin(hexa_num):
#   to_int = int(hexa_num, 16)
#   return bin(to_int)[2:].zfill(4)

# # The function to calculate the color
# def calculate(num1, num2):
#   return num1 + (2 * num2)
  
# # Creating a string of binary digits
# # for each line of hexadecimal numbers
# bin_string1 = ''
# bin_string2 = ''

# for index in range(0, 16):
#   bin_string1 += (to_bin(l1[index]))
#   bin_string2 += (to_bin(l2[index]))

# # Turns the strings to lists, then for each entry of the list, converts to 
# # integer and apply the function to calculate the resulting color.
# list1 = list(bin_string1)
# list2 = list(bin_string2)
# res = list()

# for index in range(0,64):
#   num1 = int(list1[index])
#   num2 = int(list2[index])
#   res.append(calculate(num1, num2))