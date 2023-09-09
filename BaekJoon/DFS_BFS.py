# 1260

import sys
from collections import deque

N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]
visited_d = [False for _ in range (N+1)]
visited_b = [False for _ in range (N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

for node in nodes:
    node.sort()

def dfs(nodes, visited_d, v):
    if not visited_d[v]:
        print(v, end = ' ')
        visited_d[v] = True
        for item in nodes[v]:
            dfs(nodes, visited_d, item)

def bfs(nodes, visited_b, v):
    search = deque([])
    if not visited_b[v]:
        search.append(v)
    while search:
        popp = search.popleft()
        visited_b[popp] = True
        print(popp, end = ' ')
        for item in nodes[popp]:            
            if not visited_b[item] and item not in search:
                search.append(item)

dfs(nodes, visited_d, V)
print()
bfs(nodes, visited_b, V)