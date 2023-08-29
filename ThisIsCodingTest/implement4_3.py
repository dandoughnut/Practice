# ord

def knight_moves(s):
    c, r = int(ord(s[0])) - int(ord('a')) + 1, int(s[1]) 
    moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
    ans = 0
    for move in moves:
        c_to, r_to = c+move[0], r+move[1]
        if c_to >= 1 and c_to <= 8 and r_to >= 1 and r_to <= 8:
            ans += 1
    print(ans)

knight_moves('a1')