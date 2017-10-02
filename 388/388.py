'''

 How many numbers of 7 or less digits whose last 3 (digits) are multiples of 388?


'''

print (len([ x for x in \
             map(lambda n: n[-3:], \
                 map(str, \
                     [y * 388 for y in range(1, int(10000000/388))])) \
             if '388' in x ]))

'''
You can print all the numbers of this solution:

print '\n'.join( [ x for x in map(str, [y * 388 for y in range(1, int(10000000/388))]) if x[-3:] == '388' ])

'''
