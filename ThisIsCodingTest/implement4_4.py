N, E, S, W = 0, 1, 2, 3

def game_dev(map_size, coord_dir, map):
    ans = 1
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    r, c = coord_dir[0][0], coord_dir[0][1]
    dir = coord_dir[1]
    whiles = 0
    for i in range(5):
        whiles += 1
        print(whiles)
        #1
        left = (dir+3)%4
        #2
        if map[r + dirs[left][0]][c + dirs[left][1]] == 0:
            dir = left
            map[r][c] = -1
            print(r, c)
            r, c = r + dirs[left][0], c + dirs[left][1]
            ans += 1
        else:
            if map[r+dirs[0][0]][c+dirs[0][1]] != 0 and map[r+dirs[1][0]][c+dirs[1][1]] != 0 and map[r+dirs[2][0]][c+dirs[2][1]] !=0 and map[r+dirs[3][0]][c+dirs[3][1]] != 0:
                back = (dir+2) % 4
                if map[r + dirs[back][0]][c + dirs[back][1]] == 1:
                    print("breaking")
                    break
                elif map[r + dirs[back][0]][c + dirs[back][1]] == -1:
                    r, c = r + dirs[back][0], c + dirs[back][1]
                    continue
                
            else:
                dir = left
                print('turning left')
                continue
    print(ans)





map_size = (4, 4)
coord_dir = [(1, 1), 0]
map = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

game_dev(map_size, coord_dir, map)