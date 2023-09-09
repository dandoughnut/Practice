# 1439
S = input()

zeros = 0
ones = 0
if S[0] == '0':
    zeros += 1
elif S[0] == '1':
    ones += 1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        continue
    elif S[i] == '0':
        zeros += 1
    elif S[i] == '1':
        ones += 1
print(min(zeros, ones))

# 
S = input()
P = input()

count = 0
def count_copy(word, S):
    n = 1
    while word[:n] in S:
        if n == len(P):
            return 1
        n += 1
    return 1 + count_copy(word[n-1:], S)


print(count_copy(P, S))

# 17509
mins = []
penalty = 0
for _ in range(11):
    D, K = map(int, input().split())
    mins.append(D)
    penalty += K * 20
mins.sort()
for i in range(1, len(mins)+1):
    penalty += sum(mins[:i])
print(penalty)


# 4796
i = 0
while True:
    try:
        L, P, V = map(int, input().split())
        if L == 0 and P == 0 and V == 0 :
            break
        days = V // P * L + min(L, V % P)
        i += 1
        print('Case {}: {}'.format(i, days))
    except:
        break


#
import heapq
import sys

N = int(sys.stdin.readline())
decks = []
for _ in range(N):
    deck = int(sys.stdin.readline())
    heapq.heappush(decks, deck)

time = 0
while len(decks) > 1:
    A, B = heapq.heappop(decks), heapq.heappop(decks)
    time += A+B
    heapq.heappush(decks, A+B)
    
print(time)


# 11399
import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort(reverse = True)
time = 0
for i in range(N):
    time += sum(P[i:])
print(time)

# 13904
import sys

N, M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse = True)

cnt = 0
for coin in coins:
    cnt += M // coin
    M %= coin

print(cnt)

# 13904
import sys

# N = int(input())
N = 7
hws = [[] for _ in range(N+1)]

# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     hws[a].append(b)

ins = [(4, 60), (4, 40), (1,20), (2,50), (3,30), (4,10), (6,5)]

for inn in ins:
    hws[inn[0]].append(inn[1])

cnt = 0
for hw in hws:
    if hw:
        print(hw)
        cnt += max(hw)


print(cnt)
    