class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = j = 0
        ans = 1
        freq = [0] * 256
        freq[ord(s[0])] = 1
        while j < len(s) - 1:
            if freq[ord(s[j + 1])] == 0:
                j += 1
                freq[ord(s[j])] += 1
            else:
                freq[ord(s[i])] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
