# cook your dish here
from math import sqrt


def findDivisors(n):
    if n < 2:
        return 0
    ans = 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                ans += i
            else:
                ans += i
                ans += n // i

    return ans + 1


t = int(input())
for _ in range(t):
    n = int(input())
    print(findDivisors(n))
