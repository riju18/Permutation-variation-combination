x = int( input( 'Input the number to find out all ways:  ' ) )
f = 1
count = 0
temp = ''
all_ways = []
for i in range( 1, x + 1 ):
    f *= i

print('all possible ways: {}'.format(f))

