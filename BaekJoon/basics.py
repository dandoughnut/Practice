# 10869
A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)


# 10926
s = input()

print(s+'??!')


#18108
y = int(input())

add = 2541 - 1998

print(y - add)


# 10430
A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


# 2588
A = int(input())
B = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))


# 11382
A, B, C = map(int, input().split())

print(A+B+C)


# 10171
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
# typing \\ to get \


# 10172
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")


# 1330
A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')


# 9498
A = int(input())

if A >= 90 and A <= 100:
    print('A')
elif A >= 80 and A < 90:
    print('B')
elif A >= 70 and A < 80:
    print('C')
elif A >= 60 and A < 70:
    print('D')
else:
    print('F')


# 2753
x = int(input())

if (x % 4 == 0 and x % 100 != 0) or (x % 4 == 0 and x % 400 == 0):
    print(1)
else:
    print(0)


# 14681
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

# 2884
H, M = map(int, input().split())

if M - 45 >= 0:
    print(H, M-45)
else:
    print((H-1+24)%24, M+15)

# 2525
A, B = map(int, input().split())
C = int(input())

H, M = C // 60, C % 60

if M + B < 60:
    print((A+H)%24, M+B)
else:
    print((A+H+1)%24, M+B-60)


# 2480
A, B, C = map(int, input().split())

if A==B and B==C:
    print(10000+A*1000)
elif A==B or B==C or A==C:
    if A==B:
        print(1000+A*100)
    elif B==C:
        print(1000+B*100)
    else:
        print(1000+C*100)
else:
    print(max(A,B,C)*100)

# 15439
N = int(input())
print(N* (N-1))