class Solution:
    def isSafe(self, i, j, mat):
        x = i - 1
        while x >= 0:
            if mat[x][j] == 1:
                return False
            x -= 1

        x, y = i - 1, j - 1
        while x >= 0 and y >= 0:
            if mat[x][y] == 1:
                return False
            x -= 1
            y -= 1

        x, y = i - 1, j + 1
        while x >= 0 and y < len(mat[0]):
            if mat[x][y] == 1:
                return False
            x -= 1
            y += 1
        return True

    def nqueen(self, r, mat):
        if r == len(mat):
            return 1
        count = 0
        for c in range(len(mat[0])):
            if self.isSafe(r, c, mat):
                mat[r][c] = 1
                count += self.nqueen(r + 1, mat)
                mat[r][c] = 0
        return count

    def totalNQueens(self, n: int) -> int:
        row = col = 0
        chess = [[0 for _ in range(n)] for _ in range(n)]
        return self.nqueen(row, chess)
