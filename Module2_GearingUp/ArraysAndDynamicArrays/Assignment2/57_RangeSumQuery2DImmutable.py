# cook your dish here
class RangeSumQuery2DImmutable:
    def main(self):
        n, m = map(int, input().strip().split())

        # matrix input
        mat = []
        for i in range(n):
            mat.append([int(j) for j in input().split()])

        q = int(input())
        qin = []
        for i in range(q):
            qin.append([int(j) for j in input().split()][:4])

        # row sum
        for i in range(n):
            for j in range(1, m):
                mat[i][j] += mat[i][j - 1]

        # col sum
        for i in range(m):
            for j in range(1, n):
                mat[j][i] += mat[j - 1][i]

        for i in range(len(qin)):
            i1 = qin[i][0]
            j1 = qin[i][1]
            i2 = qin[i][2]
            j2 = qin[i][3]
            ans = mat[i2][j2]
            if j1 - 1 >= 0:
                ans -= mat[i2][j1 - 1]
            if i1 - 1 >= 0:
                ans -= mat[i1 - 1][j2]
            if i1 - 1 >= 0 and j1 - 1 >= 0:
                ans += mat[i1 - 1][j1 - 1]

            print(ans)


obj = RangeSumQuery2DImmutable()
obj.main()


