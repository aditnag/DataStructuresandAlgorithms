# Edge Cases:
# 1. if total_count("(") == total_count(")")
#   i.  string is completed ---> do not do anything
#   ii. string is not completed, eg: (())__ ---> add "("
# 2. if total_count("(") > total_count(")")
#   i.  if total_count("(") == n ---> meaning all "(" is over ---> add ")"
#   ii. if total_count("(") < n ---> meaning all "(" is not over ---> 2 choices, either "(" or ")"

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp = []
        l = r = idx = 0
        # return self.parenthesis(temp, idx, n, l, r)
        # return list(self.parenthesis(temp, idx, n, l, r))
        result = []
        print(self.parenthesis(temp, n, l, r,result))

    def parenthesis(self, temp, n, l, r,result):
        if l + r == 2 * n:
            return result.append("".join(temp))
            # return result
        if l == r:
            temp.append("(")
            self.parenthesis(temp, n, l + 1, r,result)
            temp.pop()
        if l > r and l == n:
            temp.append(")")
            self.parenthesis(temp, n, l, r + 1,result)
            temp.pop()
        if r < l < n:
            temp.append("(")
            self.parenthesis(temp, n, l + 1, r,result)
            temp.pop()
            temp.append(")")
            self.parenthesis(temp, n, l, r + 1,result)
            temp.pop()

        return result


n = int(input())
obj = Solution()
obj.generateParenthesis(n)
