# cook your dish here
def sq(n):
    l, h = 0, n
    while l <= h:
        m = (l + h) // 2
        if m * m > n:
            h = m - 1
        else:
            if (m + 1) * (m + 1) > n:
                return m
            else:
                l = m + 1


t = int(input())
for _ in range(t):
    n = int(input())
    print(sq(n))
