import itertools

teams = []

total_team = int( input( 'Input the number of team:  ' ) )
matches = int( input( 'Input the number of matches each team will play:  ' ) )

for t in range( total_team ):
    team = input( 'enter {} team: '.format( str( t + 1 ) ) )
    teams.append( team )

total_matches = int( (total_team * matches) / 2 )
print( 'all number of matches: {}'.format( total_matches ) )
print( list( itertools.permutations( teams, 2 ) ) )
