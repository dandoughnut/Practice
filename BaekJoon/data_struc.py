# 28278
import sys

N = int(sys.stdin.readline())

stk = []
for _ in range(N):
    o = sys.stdin.readline().split()
    if o[0] == '1':
        stk.append(o[1])
    elif o[0] == '2':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif o[0] == '3':
        print(len(stk))
    elif o[0] == '4':
        if stk:
            print(0)
        else:
            print(1)
    elif o[0] == '5':
        if stk:
            print(stk[-1])
        else:
            print(-1)

# 10773
import sys

fin = []
K = int(sys.stdin.readline())
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        fin.pop()
    else:
        fin.append(n)
print(sum(fin))


# 4949
def balanced(s):
    stack = []
    for ch in s:
        if ch == '[' or ch == '(':
            stack.append(ch)
        elif ch ==']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif ch == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')


while True:
    try:
        s = input()
        if s == '.':
            break
        balanced(s)
    except:
        break
    
        
# 18258
from collections import deque
import sys

N = int(sys.stdin.readline())

def command(N):
    queue = deque([])
    for _ in range(N):
        o = sys.stdin.readline().split()
        if o[0] == 'push':
            queue.append(int(o[1]))
        elif o[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif o[0] == 'size':
            print(len(queue))
        elif o[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif o[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif o[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
command(N)
