# cook your dish here

class HardestProblemEver:
    def Divisors(self, subsequence):
        if not subsequence:  # Check if the list is empty
            return 0
        count = [0] * (max(subsequence) + 1)
        for i in range(len(subsequence)):
            number = subsequence[i]
            for j in range(2, number + 1):
                if number % j == 0:
                    count[j] += 1
                    if count[j] == len(subsequence):
                        return 0
        return 1

    def solve(self, ar):
        n = len(ar)
        subsequence = []
        result = 0
        if n == 1:
            return 0
        for i in range(n):
            for j in range(i + 1):
                subsequence = ar[j:i + 1]
                result |= self.Divisors(subsequence)
        return result

    # def solve(self, ar):
    #     result = 0
    #     n = len(ar)
    #     for i in range(n):
    #         subsequence = [ar[i]]
    #         result |= self.Divisors(subsequence)
    #         for j in range(i + 1, n):
    #             subsequence.append(ar[j])
    #             result |= self.Divisors(subsequence)
    #     return result


if __name__ == '__main__':
    obj = HardestProblemEver()
    t = int(input())
    while t:
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        print(obj.solve(ar))
        t -= 1
