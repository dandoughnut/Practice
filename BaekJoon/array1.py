# 10807
import sys
N = int(sys.stdin.readline())
integers = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

ans = 0
for integer in integers:
    if integer == v:
        ans += 1
print(ans)

# 10871
import sys
N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
smalls = []
for a in A:
    if a < X:
        smalls.append(a)
print (' '.join([str(small) for small in smalls]))

# 10818
import sys
N = int(sys.stdin.readline())
ints = list(map(int, sys.stdin.readline().split()))
print(min(ints), max(ints))

# 2562
import sys
idx = 0
maximum = 0
for i in range(9):
    cand = int(sys.stdin.readline())
    if cand > maximum:
        maximum = cand
        idx = i+1
print(maximum)
print(idx)

# 10810
import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for b in range(i, j+1):
        baskets[b-1] = k
for basket in baskets:
    print(basket, end = ' ')

# 10813
import sys
N, M = map(int, sys.stdin.readline().split())
baskets = [str(i+1) for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    i, j = i-1, j-1
    baskets[i], baskets[j] = baskets[j], baskets[i]
print(' '.join(baskets))

# 5597
import sys

students = [str(i+1) for i in range(30)]
while True:
    try:
        hw = int(sys.stdin.readline())
        idx = hw-1
        students[idx] = '0'
    except:
        break

for student in students:
    if student != '0':
        print(student)

# 3052
import sys
rems = []
for _ in range(10):
    n = int(sys.stdin.readline())
    rems.append(n%42)
print(len(set(rems)))

# 10811
import sys
N, M = map(int, sys.stdin.readline().split())

baskets = [str(i+1) for i in range(N)]

for exchange in range(M):
    i, j = map(int, sys.stdin.readline().split())
    save = baskets[i-1:j]
    for idx in range(i-1, j):
        baskets[idx] = save.pop()

print(' '.join(baskets))

# 1546
import statistics
N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
print(statistics.mean(scores) / max_score * 100)

