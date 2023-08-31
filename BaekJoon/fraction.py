# 5086
while True:
    try:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        elif A > B and A % B == 0:
            print('multiple')
        elif A < B and B % A == 0:
            print('factor')
        else:
            print('neither')
    except:
        break

# 2501
N, K = map(int, input().split())

fracs = []
for i in range(1, N+1):
    if N % i == 0:
        fracs.append(i)
    if len(fracs) == K:
        print(fracs[-1])
        break
if len(fracs) < K:
    print(0)

# 9506
while True:
    try:
        frac = [1]
        n = int(input())
        if n == -1:
            break
        for i in range(2, n):
            if n % i == 0:
                frac.append(i)
        if sum(frac) == n:
            print('{} = 1'.format(n), end = ' ')
            for num in frac[1:]:
                print('+ {}'.format(num), end = ' ')
        else:
            print('{} is NOT perfect.'.format(n))
    except:
        break
    
# 1978
N = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    if num < 2:
        continue
    else:
        for i in range(num+1):
            if i < 2:
                continue
            if i == num:
                ans += 1
                break
            elif num % i == 0:
                break
            
print(ans)


# 2581
M = int(input())
N = int(input())

primes = []
for i in range(M, N+1):
    for j in range(2, i+1):
        if i != j and i % j == 0:
            break
        else:
            if j == i:
                primes.append(i)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))


# 11653
N = int(input())
for i in range(1, N+1):
    if i != 1 and N % i == 0:
        while N % i == 0:
            print(i)
            N /= i

# Really good solution
def is_prime(n):
    if n < 2:
        return False
    prime = [True] * (n+1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False
    return prime[n]
def factorization(n):
    i = 2
    while i*i <= n:
        
        if n % i == 0:
            
            if is_prime(i):
                print(i)
            
            else:
                factorization(i)
            n //= i
        else:
            i += 1
    
    if n != 1:
        print(n)
n = int(input())
if n != 1:
    factorization(n)