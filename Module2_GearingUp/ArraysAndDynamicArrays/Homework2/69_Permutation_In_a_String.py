# cook your dish here

class PermutationInaString:

    def isPermutation(self, a, b):
        la = len(a)
        lb = len(b)
        if la > lb:
            return False
        ha = {i: 0 for i in range(26)}
        hb = {i: 0 for i in range(26)}
        # storing the frequencies of characters in dictionary ha that are present in string a
        for i in range(la):
            ha[ord(a[i]) - ord('a')] += 1
        # storing the frequencies of character's of window size la in dictionary hb that are present in string b
        for i in range(la):
            hb[ord(b[i]) - ord('a')] += 1

        # checking 1st window in B
        if ha == hb:
            return True
        else:
            for j in range(la, lb):
                # checking 1st window in B
                if ha == hb:
                    return True
                hb[ord(b[j - la]) - ord('a')] -= 1
                hb[ord(b[j]) - ord('a')] += 1
                if ha == hb:
                    break

        if ha == hb:
            return True
        else:
            return False

    def main(self):
        t = int(input())
        while t:
            s1 = input()
            s2 = input()
            print(self.isPermutation(s1, s2))
            t -= 1


obj = PermutationInaString()
obj.main()



