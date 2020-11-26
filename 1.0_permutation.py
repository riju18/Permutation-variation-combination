elements = []

x = int( input( 'Input the number to find out all ways:  ' ) )
for i in range( x ):
    element = input( 'enter {} element: '.format( str( i + 1 ) ) )
    elements.append( element )

f = 1
count = 0
temp = ''
all_ways = []
for i in range( 1, x + 1 ):
    f *= i

print('all possible ways: {}'.format(f))

