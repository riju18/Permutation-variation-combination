import random
from collections import Counter

n = int( input( 'No of sportsman you want to select: ' ) )
sportsman = []

for i in range( n ):
    element = input( 'enter {} sportsman: '.format( str( i + 1 ) ) )
    sportsman.append( element )

p = int( input( 'No of place in the sport: ' ) )

fact_n = 1
for i in range( 1, n + 1 ):
    fact_n *= i

fact_n_p = 1
for i in range( 1, (n - p) + 1 ):
    fact_n_p *= 1

v = int(fact_n / fact_n_p)  # formula: n!/(n-p)!

print( 'No of available variation: {}'.format( v ) )

all_ways = []
count = 0

for i in range( 1, v + 1 ):
    count += 1
    all_sportsman = []
        
    while True:
        for j in range( p ):
            all_sportsman.append( random.choice( sportsman ) )
            
        no_of_sportsman = Counter( all_sportsman )
        total_sportsman = [no_of_sportsman[s] for s in no_of_sportsman]
        if any(y > 1 for y in total_sportsman):
            all_sportsman = []
        else:
            break
    
    unique_sportsman = ', '.join(all_sportsman)
    while unique_sportsman in all_ways:
        all_sportsman = []
        while True:
            for j in range( p ):
                all_sportsman.append( random.choice( sportsman ) )
    
            no_of_sportsman = Counter( all_sportsman )
            total_sportsman = [no_of_sportsman[s] for s in no_of_sportsman]
            if any(y > 1 for y in total_sportsman):
                all_sportsman = []
            else:
                break
        unique_sportsman = ', '.join( all_sportsman )
    all_ways.append( unique_sportsman )
    print( 'count:{}, way:{}'.format( count, unique_sportsman ) )


