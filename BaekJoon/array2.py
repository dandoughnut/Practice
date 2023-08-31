# 2738

N, M = map(int, input().split())

A = []
B = []
U = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)
for i in range(N):
    for j in range(M):
        a, b = A[i][j], B[i][j]
        print(a+b, end = ' ')
    print()

# 2566
maximum = 0
r, c = 0, 0
for i in range(9):
    row = list(map(int, input().split()))
    cand = max(row)
    if cand >= maximum:
        maximum = cand
        r, c = i+1, row.index(cand)+1
print(maximum)
print(r, c)


# 10798
lines = []
ans = ''
max_len = 0
for _ in range(5):
    line = input()
    lines.append(line)
    if len(line) > max_len:
        max_len = len(line)

for i in range(max_len):
    for j in range(5):
        if i < len(lines[j]):
            ans += lines[j][i]
print(ans)


# 2563
paper = [[0] * 100 for i in range(100)]

N = int(input())
for _ in range(N):
    left, down = map(int, input().split())
    for l in range(left, left+10):
        for d in range(down, down+10):
            paper[d][l] = 1

total = 0
for line in paper:
    total += sum(line)
print(total)




