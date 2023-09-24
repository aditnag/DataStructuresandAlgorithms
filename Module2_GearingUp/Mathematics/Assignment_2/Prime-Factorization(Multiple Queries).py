# cook your dish here
def findprime(n):
    if n <= 2:
        print(0)
    primes = []
    for i in range(2, n + 1):
        while n % i == 0:
            primes.append(i)
            continue
    mp = {}
    for num in primes:
        if num in mp:
            mp[num] += 1
        else:
            mp[num] = 1
    for k, v in mp.items():
        print(f"{k} {v}")


T = int(input())
for _ in range(T):
    N = int(input().strip())
    findprime(N)