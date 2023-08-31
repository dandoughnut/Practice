#
A = int(input())
B = int(input())

print(A*B)

# 1085
x, y, w, h = map(int, input().split())

m = min(x, y, w-x, h-y)
print(m)

# 3009
x_c = []
y_c = []
x = 0
for _ in range(3):
    a, b = map(int, input().split())
    if a not in x_c: 
        x_c.append(a)
        x += a
    else:
        x -= a
    if b not in y_c:
        y_c.append(b)
        y += b
    else:
        y -= b
print(x, y)

# 15894
n = int(input())

print(4 * n)


# 9063
N = int(input())

min_x, max_x, min_y, max_y = 0, 0, 0, 0
for i in range(N):
    a, b = map(int, input().split())
    if i == 0:
        min_x, max_x, min_y, max_y = a, a, b, b
    else:
        min_x, max_x, min_y, max_y = min(a, min_x), max(a, max_x), min(b, min_y), max(b, max_y)

print((max_x-min_x) * (max_y-min_y))


# 10101
angles = []
for _ in range(3):
    angles.append(int(input()))
a, b, c = angles[0], angles[1], angles[2]
if sum(angles) != 180:
    print('Error')
elif a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif a == b or b == c or c == a:
    print('Isosceles')
else:
    print('Scalene')

# 14215
a, b, c = map(int, input().split())

mini = min(a+b, b+c, c+a)
if max(a,b,c) >= mini:
    print(2 * mini - 1)
else:
    print(a+b+c)

# 5073
while True:
    try:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        elif a == 0 or b == 0 or c == 0 or max(a, b, c) >= min(a+b, b+c, c+a):
            print('Invalid')
        elif a == b and b == c and c == a:
            print('Equilateral')
        elif a == b or b== c or c == a:
            print('Isosceles')
        else:
            print('Scalene')
    except:
        break