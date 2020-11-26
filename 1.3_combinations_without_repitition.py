# """
# ===================================================
# picking no of elements from a set in different ways
# v = c x p ; v = variations without repetitions, c = combinations; p = permutations
# ===================================================
# """
import random
from collections import Counter
from math import factorial
import itertools

n = int( input( 'No of employees in company: ' ) )

employees = []
for i in range( n ):
    element = input( 'enter {} employee: '.format( str( i + 1 ) ) )
    employees.append( element )

p = int( input( 'No of employees want to pick from company: ' ) )
fact_n = 1
for i in range( 1, n + 1 ):
    fact_n *= i

fact_p = 1
for i in range( 1, p + 1 ):
    fact_p *= i

fact_n_p = 1
for i in range( 1, (n - p) + 1 ):
    fact_n_p *= i

c = int( fact_n / (fact_p * fact_n_p) )  # formula: n!/(p!* (n-p)!)

print( 'No of different combinations of employees: {}'.format( c ) )
print('All combinations: {}'.format(list(itertools.combinations(employees, p))))
