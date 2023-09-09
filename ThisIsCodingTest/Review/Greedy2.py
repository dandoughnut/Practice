n, m, k = map(int, input.split())

data = list(map(int, input().split()))

data = reversed(sorted(data))

turns, rem = m // k , m % k
return turns * (k * data[0] + data[1]) + rem * data[0]
