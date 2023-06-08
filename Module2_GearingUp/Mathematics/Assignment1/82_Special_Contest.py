# cook your dish here

class SpecialContest:
    def gcd(self, a, b):
        minm = min(a, b)
        maxm = max(a, b)
        while maxm % minm != 0:
            temp = maxm
            maxm = minm
            minm = temp % minm
        return minm

    def win(self, n, a, b, k):
        solved_bob = n // a
        solved_alice = n // b
        lcm = (a * b) // self.gcd(a, b)
        solved_by_both = n // lcm
        if solved_bob + solved_alice - 2 * solved_by_both >= k:
            print("Win")
        else:
            print("Lose")


if __name__ == '__main__':
    obj = SpecialContest()
    t = int(input())
    while t:
        n, a, b, k = map(int, input().strip().split())
        obj.win(n, a, b, k)
        t -= 1
