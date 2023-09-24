# cook your dish here

def findDivisors(n):
    ans = [1]
    if n < 2:
        return []
    if n > 1:
        ans.append(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                ans.append(i)
            else:
                ans.append(i)
                ans.append(n // i)

    return ans


def commanDivisiors(a, b):
    divisors_a = findDivisors(a)
    divisors_b = findDivisors(b)
    common_divisors = [div for div in divisors_a if div in divisors_b]
    return len(common_divisors)


t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    print(commanDivisiors(a, b))
