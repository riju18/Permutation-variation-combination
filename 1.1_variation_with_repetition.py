"""
Ex: Suppose a locker has 2 input contains 3 elements like: a, b, c. How many variation are there?
like : aa, ab, ac etc
"""

import random
import itertools

n = int( input( 'No of elements (ex: a, b, c) to unlock: ' ) )
elements = []

for i in range( n ):
    element = input( 'enter {} element: '.format( str( i + 1 ) ) )
    elements.append( element )

all_elements = ''.join(elements)
print(all_elements)

p = int( input( 'No of available space: ' ) )

v = n ** p  # formula: (n to the power of p)

print( 'No of available variation to unlock: {}'.format( v ) )

all_ways = []
count = 0
for i in range( 1, v + 1 ):
    count += 1
    m_n = []
    for j in range( p ):
        m_n.append( random.choice( elements ) )
    mn = ', '.join( m_n )
    while mn in all_ways:
        m_n = []
        for j in range( p ):
            m_n.append( random.choice( elements ) )
        mn = ', '.join( m_n )
    all_ways.append( mn )
    print( 'count:{}, variation:{}'.format( count, mn ) )

# builtin fn
# ============
print('All variation: {}'.format(list(itertools.product(all_elements, repeat=p))))
