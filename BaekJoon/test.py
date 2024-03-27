from sys import stdin

input = stdin.readline

N = input()
nums = sorted(list(map(int, input().split())))
M = input()
tests = list(map(int, input().split()))

def bin_search(tst, nums, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if tst == nums[mid]:
        return 1
    elif tst < nums[mid]:
        return bin_search(tst, nums, start, mid-1)
    else:
        return bin_search(tst,nums, mid+1, end)
    

for tst in tests:
    start = 0
    end = len(nums) - 1
    print(bin_search(tst, nums, start, end))