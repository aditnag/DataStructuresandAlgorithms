# cook your dish here

class MatrixBlockSum:
    def row_col_sum(self, mat, m, n):
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        for i in range(n):
            for j in range(1, m):
                mat[j][i] += mat[j - 1][i]

        return mat

    def find_sum(self, mat, r, c, k):
        ans = [[0 for x in range(n)] for y in range(m)]
        rcs = self.row_col_sum(mat, m, n)
        for i in range(r):
            r1 = max(0, i - k)
            r2 = min(r - 1, i + k)
            for j in range(c):
                c1 = max(0, j - k)
                c2 = min(c - 1, j + k)
                if r1 == c1 == 0:
                    ans[i][j] = rcs[r2][c2]
                elif r1 == 0:
                    ans[i][j] =rcs[r2][c2] - rcs[r2][c1 - 1]
                elif c1 == 0:
                    ans[i][j] = rcs[r2][c2] - rcs[r1 - 1][c2]
                else:
                    ans[i][j] = rcs[r2][c2] - rcs[r2][c1 - 1] - rcs[r1 - 1][c2] + rcs[r1 - 1][c1 - 1]

        for i in range(m):
            for j in range(n):
                print(ans[i][j], end=" ")
            print()


m, n, k = map(int, input().strip().split())
mat = []
for i in range(m):
    mat.append([int(j) for j in input().split()])

obj = MatrixBlockSum()
obj.find_sum(mat, m, n, k)
