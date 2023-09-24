# cook your dish here
def countPrimes(n):
    ans = [1] * (n + 1)
    ans[0] = ans[1] = 0
    for i in range(2, int(n ** 0.5)):
        if ans[i] == 1:
            for j in range(i * i, n + 1, i):
                ans[0] = 0

    return sum(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    print(countPrimes(n))
