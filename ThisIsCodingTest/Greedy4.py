
def until_one(n, k):
    result = 0
    while n != 1:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        result += 1

    print(result)

until_one(25, 2)