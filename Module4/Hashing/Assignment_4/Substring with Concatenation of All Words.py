from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordmp = {}
        for word in words:
            if word in wordmp:
                wordmp[word] += 1
            else:
                wordmp[word] = 1
        ans = []
        n = len(words)
        l = len(words[0])
        N = len(s)
        for i in range(N - (n * l) + 1):
            temp = {}
            for j in range(i, i + (n * l), l):
                subword = s[j:j + l]
                if subword in temp:
                    temp[subword] += 1
                else:
                    temp[subword] = 1
            if temp == wordmp:
                ans.append(i)
        return ans
