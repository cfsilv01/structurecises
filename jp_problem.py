'''
    Josephus problem
    
    1 to N numbered players, are sitting in a circle.
    Starting at person 1, after M passes, the person at Mth
    pass is eliminated, the circle is reduced, and the game 
    continues with the person next to the eliminated person. 
    The last remaining person wins.

    Variables
        - N - number of players
        - M - number of passes
        - start - initial player position/player next to eliminated player
        - table - array of players
'''

N=5
M=0
start = 0
table = [i+1 for i in range(N)]

def play_josephus(table, start):

    if len(table) == 1:
        print('Winner is ',table[0])
    else:
        # Index of next elimination
        elim_player = (start + M) % len(table)
        print('Player {} eliminated'.format(table[elim_player]))

        # Remove eliminated players value at index
        del table[elim_player]

        # Recurse with updated array and index of next player
        play_josephus(table, elim_player) 

if __name__ == '__main__':
    play_josephus(table, start)