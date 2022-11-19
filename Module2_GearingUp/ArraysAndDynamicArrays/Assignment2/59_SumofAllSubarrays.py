# cook your dish here
class SumofAllSubarrays:
    def main(self):
        n = int(input())
        arr = list(map(int, input().strip().split()))[:n]

        ans = 0
        for i in range(n):
            ans += arr[i] * (i + 1) * (n - i)

        print(ans % (10 ** 9 + 7))


obj = SumofAllSubarrays()
obj.main()
