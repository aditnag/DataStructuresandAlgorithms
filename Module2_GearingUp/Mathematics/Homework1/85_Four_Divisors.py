# cook your dish here

class FourDivisors:
    def find_factors_sum(self, n):
        count = 0
        fact_sum = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if i * i == n:
                    count += 1
                else:
                    count += 2
        if count == 4:
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    if i * i == n:
                        fact_sum += i
                    else:
                        fact_sum += i + n / i
        return int(fact_sum)

    def find_sum(self, ar):
        total_sum = 0
        for i in range(len(ar)):
            total_sum += self.find_factors_sum(ar[i])
        print(total_sum)


if __name__ == '__main__':
    obj = FourDivisors()
    t = int(input())
    while t:
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        obj.find_sum(ar)
        t -= 1
