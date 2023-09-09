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

# 2164
from collections import deque

N = int(input())
queue = deque([])
for i in range(N):
    queue.append(i+1)
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[-1])


# 28279
import sys
from collections import deque

n=int(input())
deck = deque()
for i in range(n):
    o=list(map(int, sys.stdin.readline().strip().split()))
    c=o[0]
    l=len(deck)
    if c==1:
        deck.appendleft(o[1])
    elif c==2:
        deck.append(o[1])
    elif c==3:
        print(deck.popleft() if l else -1)
    elif c==4:
        print(deck.pop() if l else -1)
    elif c==5:
        print(len(deck))
    elif c==6:
        print(0 if l else 1)
    elif c==7:
        print(deck[0] if l else -1)
    elif c==8:
        print(deck[-1] if l else -1)