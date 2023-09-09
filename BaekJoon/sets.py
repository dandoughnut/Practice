# 1269
a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A ^ B))

# 10815
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))
A.sort()

def binary_search(A, b):
    start, end = 0, len(A)-1
    mid = (start + end) // 2
    while True:
        try:
            if b == A[mid]:
                print(1, end = ' ')
                break
            elif start >= end:
                print(0, end = ' ')
                break
            elif b < A[mid]:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        except:
            break
    return

for b in B:
    binary_search(A, b)
