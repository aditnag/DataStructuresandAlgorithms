class Solution:
    def factors(self, n):
        lst = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                lst.append(i)
        return lst

    def repeatedSubstringPattern(self, s: str) -> bool:
        # sub_str = ""
        # ss = ""
        # for i in range(len(s) // 2):
        #     sub_str += s[i]
        #     for j in range(len(s) // len(sub_str)):
        #         ss += sub_str
        #     if ss == s:
        #         return True
        #     else:
        #         ss = ""
        factors_lst = self.factors(len(s))  # [1,2,3,4,6]
        sub_str = ""
        flag = False
        for fac in factors_lst:
            mul = len(s) // fac
            sub_str = s[:fac] * mul
            if sub_str == s:
                flag = True
                break
            else:
                flag = False
        return flag


if __name__ == "__main__":
    solution = Solution()
    s = input()
    length = solution.repeatedSubstringPattern(s)
    print(length)
