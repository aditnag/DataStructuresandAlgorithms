# cook your dish here

class SpiralMatrix:
    def findSpiralMatrix(self, mat, m, n):
        sr = 0  # starting row index
        sc = 0  # starting column index
        while sr < m and sc < n:

            # Print the first row from
            # the remaining rows
            for i in range(sc, n):
                print(mat[sr][i], end=" ")
            sr += 1

            # Print the last column from
            # the remaining columns
            for i in range(sr, m):
                print(mat[i][n - 1], end=" ")
            n -= 1

            # Print the last row from
            # the remaining rows
            if sr < m:
                for i in range(n - 1, sc - 1, -1):
                    print(mat[m - 1][i], end=" ")
                m -= 1

            # Print the first column from
            # the remaining columns
            if sc < n:
                for i in range(m - 1, sr - 1, -1):
                    print(mat[i][sc], end=" ")
                sc += 1


if __name__ == '__main__':
    obj = SpiralMatrix()
    m, n = map(int, input().strip().split())
    mat = []
    for i in range(m):
        mat.append([int(j) for j in input().split()])
    obj.findSpiralMatrix(mat, m, n)
