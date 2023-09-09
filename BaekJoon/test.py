import sys
from collections import deque

input = sys.stdin.readline


def printer(m, queue):
    cnt = 0
    while queue:
        max_pri = max(queue, key = lambda x: x[1])[1]
        front = queue.popleft()
        if front[1] == max_pri:
            cnt += 1
            if front[0] == m:
                break
        else:
            queue.append(front)
    return cnt

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    queue = deque([(i, docs[i]) for i in range(len(docs))])
    print(printer(m, queue))
