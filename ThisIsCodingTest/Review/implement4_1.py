def lrud(n, itin):
    x, y = 1, 1
    poss_move = {
        'L': -1,
        'R': 1,
        'U': -1,
        'D': 1
    }
    for move in itin:
        if (move == 'L' or move == 'R') and (y + poss_move[move] > 0 and y + poss_move[move] <= n):
            y += poss_move[move]
        elif (move == 'U' or move == 'D') and (x + poss_move[move] > 0 and x + poss_move[move] <= n):
            x += poss_move[move]
    print(x, y)

lrud(5, ['R', 'R', 'R', 'U', 'D', 'D'])