import sys

input = sys.stdin.readline
n = int(input().rstrip())
cards = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
tests = list(map(int, input().rstrip().split()))

counts = {}

for card in cards:
    if card in counts:
        counts[card] += 1
    else:
        counts[card] = 1

for test in tests:
    if test in counts:
        print(counts[test], end = ' ')
    else:
        print(0, end = ' ')

# example
# n = 10
# cards = '6 3 2 10 10 10 -10 -10 7 3'
# cards = cards = list(map(int, cards.split()))
# m = 8
# counts = '10 9 -5 2 3 4 5 -10'
# counts = list(map(int, counts.split()))

