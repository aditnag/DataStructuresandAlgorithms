# cook your dish here

class PascalTriangle:
    def pascal(self, r):
        mat = [[0 for x in range(r)] for y in range(r+1)]
        for i in range(r):
            for j in range(i + 1):
                if j == 0 or j == i:
                    mat[i][j] = 1
                else:
                    k = i - 1
                    mat[i][j] = mat[k][j - 1] + mat[k][j]
        for i in range(r):
            for j in range(i+1):
                print(mat[i][j], end= " ")
            print(" ")


if __name__ == '__main__':
    numRows = int(input())
    obj = PascalTriangle()
    obj.pascal(numRows)
