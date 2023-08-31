# 2745
N, B = input().split()
B = int(B)
ans = 0
rev = N[::-1]
for i in range(len(rev)):
    if rev[i].isdigit():
        ans += B**i * int(rev[i])
    else:
        ans += B**i * (ord(rev[i]) - ord('A') + 10)

print(ans)


# 11005
N, B = map(int, input().split())
pwr = 1
while True:
    try:
        if B ** pwr > N:
            break
        else:
            pwr += 1
    except:
        break
ans = ''
for i in reversed(range(pwr)):
    dig = N // B ** i 
    # turn into str and add to ans
    if dig < 10:
        ans += str(dig)
    else:
        ans += chr(dig-10+ord('A'))
    N = N % (B ** i)
print(ans)


# 2720
T = int(input())
for _ in range(T):
    C = int(input())
    coins = [25, 10, 5, 1]
    for coin in coins:
        print(C // coin, end = ' ')
        C = C % coin


# 2903
N = int(input())
vx = [2]
for i in range(N):
    vx.append(vx[-1]*2 - 1)
print(vx[-1] ** 2)


# 2292
N = int(input())
hive = [1]
i = 1
while True:
    try:
        if N > hive[-1]:
            hive.append(hive[-1] + i * 6)
            i += 1
        else:
            break
    except:
        break
print(len(hive))

# 1193
N = int(input())
fracs = [1]
if N == 1:
    print('1/1')
else:        
    while True:
        try:     
            fracs.append(fracs[-1]+len(fracs)+1)
            if N <= fracs[-1]:
                break    
        except:
            break
    dif = abs(fracs[-1] - N)
    if len(fracs) % 2 == 0:
        print('{}/{}'.format(len(fracs)-dif, 1+dif))
    else:
        print('{}/{}'.format((1+dif), len(fracs)-dif))

# 2869
import math

A, B, V = map(int, input().split())

print(1 + math.ceil((V-A) / (A-B)))
