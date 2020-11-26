"""
===================================================
picking no of elements from a set in different ways
v = c x p ; v = variations without repetitions, c = combinations; p = permutations
===================================================
"""
import itertools

n = int( input( 'No of fruits in basket: ' ) )
fruits = []

for i in range( n ):
    fruit = input( 'enter {} fruit: '.format( str( i + 1 ) ) )
    fruits.append( fruit )

all_fruit = ''.join(fruits)

p = int( input( 'No of fruits you want to pick from basket: ' ) )
fact_n_1 = 1
for i in range( 1, (n - 1) + 1 ):
    fact_n_1 *= i

fact_p = 1
for i in range( 1, p + 1 ):
    fact_p *= i

fact_n_p_1 = 1
for i in range( 1, (n + p - 1) + 1 ):
    fact_n_p_1 *= i

c = int( fact_n_p_1 / (fact_p * fact_n_1) )     # formula: (n-1)!/(p! * (n-1)*)
print( 'No of different combinations of employees: {}'.format( c ) )
print('All combination: {}'.format(list(itertools.combinations_with_replacement(fruits, p))))
