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