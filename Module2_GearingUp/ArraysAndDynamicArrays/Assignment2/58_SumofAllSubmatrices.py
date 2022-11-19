# cook your dish here
class SumofAllSubmatrices:
    def main(self):
        n, m = map(int, input().strip().split())

        mat = []
        for i in range(n):
            mat.append([int(j) for j in input().split()])

        ans = 0
        for i in range(n):
            for j in range(m):
                ans += mat[i][j] * (i + 1) * (j + 1) * (n - i) * (m - j)

        print(ans % (10 ** 9 + 7))


obj = SumofAllSubmatrices()
obj.main()
