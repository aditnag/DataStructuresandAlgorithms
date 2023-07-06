# Edge Cases:
# 1. if total_count("(") == total_count(")")
#   i.  string is completed ---> do not do anything
#   ii. string is not completed, eg: (())__ ---> add "("
# 2. if total_count("(") > total_count(")")
#   i.  if total_count("(") == n ---> meaning all "(" is over ---> add ")"
#   ii. if total_count("(") < n ---> meaning all "(" is not over ---> 2 choices, either "(" or ")"

class Parenthesis:
    def balanced_parenthesis(self, n, l, r, s, idx):
        if l + r == 2 * n:
            print("".join(s))
            return
        if l == r:
            s.append("(")
            self.balanced_parenthesis(n, l + 1, r, s, idx + 1)
            s.pop()
        elif l > r and l == n:
            s.append(")")
            self.balanced_parenthesis(n, l, r + 1, s, idx + 1)
            s.pop()
        else:
            s.append("(")
            self.balanced_parenthesis(n, l + 1, r, s, idx + 1)
            s.pop()
            s.append(")")
            self.balanced_parenthesis(n, l, r + 1, s, idx + 1)
            s.pop()

    def main(self):
        n = int(input())
        s = []
        l = r = idx = 0  # l and r are count of left and right braces
        self.balanced_parenthesis(n, l, r, s, idx)


obj = Parenthesis()
obj.main()
