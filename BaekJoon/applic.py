# 2444
n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))


# 10988
s = input()

def check_palindrome(word):
    start, end = 0, len(s)-1
    while True:
        try:
            if start >= end:
                print(1)
                break
            elif word[start] != word[end]:
                print(0)
                break
            else:
                start += 1
                end -= 1
        except:
            break

check_palindrome(s)

# 25083
print('         ,r\'\"7')
print('r`-_   ,\'  ,/')
print(' \. \". L_r\'')
print('   `~\/')
print('      |')
print('      |')

# 3003
chess = list(map(int, input().split()))
right = [1, 1, 2, 2, 2, 8]
for i in range(len(chess)):
    print(right[i] - chess[i], end = ' ')

# 1157
word = input().lower()

d = {}
for i in range(len(word)):
    if word[i] not in d:
        d[word[i]] = 1
    else:
        d[word[i]] += 1

l = sorted(list(d.items()), key=lambda x: x[1], reverse = True)

if len(l) == 1:
    print(l[0][0].upper())
elif l[0][1] == l[1][1]:
    print('?')
else:
    print(l[0][0].upper())
    

#
N = int(input())
words = []
for _ in range(N):
    words.append(input())

group_words = 0

def check_group(word):
    for i in word:
        start, end = word.index(i), word.rindex(i)
        if start == end:
            continue
        else:
            cut = word[start:end+1]
            for j in range(len(cut)):
                if cut[j] != i:
                    return 0
    return 1

for word in words:
    group_words += check_group(word)
print(group_words)

# croatia
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for a in cro:
    if a in word:
        word = word.replace(a, ' ')
        
print(len(word))

# gpa
gpa = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

sum_g = 0
units = 0
for _ in range(20):
    n, u, g = input().split()
    if g != 'P':
        sum_g += gpa[g] * float(u)
        units += float(u)
print(sum_g/units)
