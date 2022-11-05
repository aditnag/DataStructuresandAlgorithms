# cook your dish here
class ArrayRotation:
    def main(self):
        n, k = map(int, input().strip().split())
        ar = list(map(int, input().strip().split()))[:n]

        if k > n:
            k = k % n

        # Reversing the first part ,ie, 0 to n-k-1
        for i in range(0, (n - k) // 2):
            temp = ar[i]
            ar[i] = ar[n - k - 1 - i]
            ar[n - k - 1 - i] = temp

        # Reversing the second part ,ie, n-k to n-1
        a = 1
        for i in range(n - k, n - k + (k // 2)):
            temp = ar[i]
            ar[i] = ar[n - a]
            ar[n - a] = temp
            a += 1

        # Reversing the whole array
        for i in range(n // 2):
            temp = ar[i]
            ar[i] = ar[n - 1 - i]
            ar[n - 1 - i] = temp

        for ele in ar:
            print(ele, end=" ")


obj = ArrayRotation()
obj.main()
