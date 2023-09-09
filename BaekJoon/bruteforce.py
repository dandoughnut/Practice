n, m = map(int, input().split())
cards = list(map(int, input().split()))


def black_jack(cards):
    l = len(cards)
    bingo = 0
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if cards[i]+cards[j]+cards[k] == m:
                    return m
                elif cards[i]+cards[j]+cards[k] < m and cards[i]+cards[j]+cards[k] > bingo:
                    bingo = cards[i]+cards[j]+cards[k]
    return bingo

print(black_jack(cards))

#
# 2231
N = int(input())

def find_M(N):
    ans = 0
    for i in range(1, N):
        s = str(i)
        cand = i
        for ch in s:
            cand += int(ch)
        if cand == N:
            ans = i
            break
    print(ans)

find_M(N)