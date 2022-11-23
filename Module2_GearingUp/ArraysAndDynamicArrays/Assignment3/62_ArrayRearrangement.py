# cook your dish here
class ArrayRearrangement:
    def main(self):
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        for i in range(n):
            if ar[i] >= 0:
                index = ar[i]
                value = i
                while index != i:
                    temp = ar[index]
                    ar[index] = -(value + 1)
                    value = index
                    index = temp
                ar[index] = -(value + 1)

        for i in range(n):
            ar[i] = ar[i] * -1 - 1

        for ele in ar:
            print(ele, end=" ")


obj = ArrayRearrangement()
obj.main()
