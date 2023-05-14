class Rotate_Image:
    def transpose(self, mat, n):
        for i in range(n):
            for j in range(0, i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        return mat

    def row_reverse(self, mat, n):
        for i in range(n):
            mat[i] = mat[i][::-1]
        return mat

    def array_rotation(self, mat, n):
        mat = self.transpose(mat, n)
        mat = self.row_reverse(mat, n)
        return mat

    def main(self, n):
        mat = []
        for i in range(n):
            mat.append([int(j) for j in input().split()])
        self.array_rotation(mat, n)
        for i in range(n):
            for j in range(n):
                print(mat[i][j], end=" ")
            print()


n = int(input("Enter the size of the matrix: "))
obj = Rotate_Image()
obj.main(n)
