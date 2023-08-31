# 2739
n = int(input())

for i in range(1, 10):
    print(n, '*', i, '=', n*i)


# 10950
T = int(input())
test_cases = []
for i in range(T):
    test_cases.append(list(map(int, input().split())))

for test_case in test_cases:
    print(test_case[0]+test_case[1])
    

# 8393
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)


# 25304
X = int(input())
N = int(input())
receipt = []
for _ in range(N):
    receipt.append(list(map(int, input().split())))

total = 0
for item in receipt:
    total += item[0] * item[1]
if total == X:
    print('Yes')
else:
    print('No')

# 25314
N = int(input())

x = N // 4

longs = ''
for i in range(x):
    longs += 'long '
print (longs + 'int')

# 15552
# sys.stdin.readline.rstrip()
import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
    
# 11021
import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #{}:'.format(i+1), A+B)

# 11022
import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(i+1, A, B, A+B))

# 2438
import sys
N = int(sys.stdin.readline())
for i in range(N):
    print('*' * (i+1))

# 2439
import sys
N = int(sys.stdin.readline())
for i in range(N):
    print(' ' * (N-(i+1)) + '*' * (i+1))

# 10952
import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    print(A+B)

# 10951 : try, except-break
import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break

