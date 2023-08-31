# 27866
S = input()
i = int(input())
print(S[i-1])

# 2743
print(len(input()))

# 9086
T = int(input())
for _ in range(T):
    S = str(input())
    print(S[0] + S[-1])

# 11654
s = str(input())
print(ord(s))

# 11720
N = int(input())
s = str(input())
ans = 0
for i in range(N):
    ans += int(s[i])
print(ans)

# 10809
# solve again

# 2675
T = int(input())

for _ in range(T):
    P = ''
    R, S = input().split()
    R_int = int(R)
    for i in range(len(S)):
        P += R_int * S[i]
    print(P)

# 1152
s = input()
words = s.split()
print(len(words))

# 2908
A, B = input().split()
A, B = int(A[::-1]), int(B[::-1])
print(max(A, B))


# 5622
time = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '']

S = input()
min_time = 0
for ch in S:
    for i in range(len(time)):
        if ch in time[i]:
            min_time += i

print(min_time)

# 11718
while True:
    try: 
        print(input())
    except:
        break