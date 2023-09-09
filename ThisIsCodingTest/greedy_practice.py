# Q01 adventurer guild
N = int(input())
adv = list(map(int, input().split()))

adv.sort()
gone = []
start = 0
for i in range(len(adv)):
    print(adv, i, gone)
    if len(adv[start:i+1]) >= adv[i]:
        gone.append(adv[start:i+1])
        start = i+1
j = len(gone)
print(j)

# Q02 * or +
s = input()

ans = 0
for i in range(len(s)):
    ans = max(ans + int(s[i]), ans * int(s[i]))
print(ans)

# 만들수없는 동전 리뷰 (이코데 314, 511)


# 볼링공
N, M = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(len(nums)):
    count += len(nums[i:]) - nums[i:].count(nums[i])
print(count)



