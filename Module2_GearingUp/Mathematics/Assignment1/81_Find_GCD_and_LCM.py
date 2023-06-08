# cook your dish here

class HCFandLCM:
    def find_hcf_lcm(self, a, b):
        minm = min(a, b)
        maxm = max(a, b)
        while maxm % minm != 0:
            temp = maxm
            maxm = minm
            minm = temp % minm
        gcd = minm
        lcm = (a*b)//gcd
        print(f"{gcd} {lcm}")


if __name__ == '__main__':
    a, b = map(int, input().strip().split())
    obj = HCFandLCM()
    obj.find_hcf_lcm(a, b)
